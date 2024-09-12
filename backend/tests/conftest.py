# pylint: disable=redefined-outer-name
# pylint: disable=unused-argument

from os import environ
from types import SimpleNamespace
from uuid import uuid4

import boto3
import pytest
from alembic.command import upgrade
from alembic.config import Config
from httpx import ASGITransport, AsyncClient
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import create_database, database_exists, drop_database

from app.__main__ import getApp
from app.config.utils import getSettings
from app.db.connection import SessionManager
from app.utils.yaS3 import s3Client
from tests.utils import make_alembic_config


@pytest.fixture(scope="session")
async def postgres() -> str:
    """
    Создает временную БД для запуска теста.
    """
    settings = getSettings()

    tmp_name = ".".join([uuid4().hex, "pytest"])
    settings.POSTGRES_DB = tmp_name
    environ["POSTGRES_DB"] = tmp_name

    tmp_url = settings.databaseUriSync
    if not database_exists(tmp_url):
        create_database(tmp_url)
    try:
        yield settings.databaseUri
    finally:
        drop_database(tmp_url)
        delete_s3_folder()


def delete_s3_folder():
    settings = getSettings()
    session = boto3.session.Session(
        aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
    )
    s3 = session.client(service_name="s3", endpoint_url="https://storage.yandexcloud.net")
    response = s3.list_objects(Bucket=s3Client.bucketName, Prefix="test/")
    if "Contents" in response:
        objects_to_delete = [{"Key": obj["Key"]} for obj in response["Contents"]]
        s3.delete_objects(Bucket=s3Client.bucketName, Delete={"Objects": objects_to_delete})


def run_upgrade(connection, cfg):
    cfg.attributes["connection"] = connection
    upgrade(cfg, "head")


async def run_async_upgrade(config: Config, database_uri: str):
    async_engine = create_async_engine(database_uri, echo=True)
    async with async_engine.begin() as conn:
        await conn.run_sync(run_upgrade, config)


@pytest.fixture
def alembic_config(postgres) -> Config:
    """
    Создает файл конфигурации для alembic.
    """
    cmd_options = SimpleNamespace(config="app/db/", name="alembic", pg_url=postgres, raiseerr=False, x=None)
    return make_alembic_config(cmd_options)


@pytest.fixture
def alembic_engine():
    """
    Override this fixture to provide pytest-alembic powered tests with a database handle.
    """
    settings = getSettings()
    return create_async_engine(settings.databaseUri, echo=True)


@pytest.fixture
async def migrated_postgres(postgres, alembic_config: Config):
    """
    Проводит миграции.
    """
    await run_async_upgrade(alembic_config, postgres)


@pytest.fixture
async def client(migrated_postgres, manager: SessionManager = SessionManager()) -> AsyncClient:
    """
    Returns a client that can be used to interact with the application.
    """
    app = getApp()
    manager.refresh()
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test/api/v1") as client:
        yield client


@pytest.fixture
async def engine_async(postgres) -> AsyncEngine:
    engine = create_async_engine(postgres, future=True)
    yield engine
    await engine.dispose()


@pytest.fixture
def session_factory_async(engine_async) -> sessionmaker:
    return sessionmaker(engine_async, class_=AsyncSession, expire_on_commit=False)


@pytest.fixture
async def session(session_factory_async) -> AsyncSession:
    async with session_factory_async() as session:
        yield session


@pytest.fixture
async def active_user_token(client: AsyncClient):
    data = {
        "username": "activeuser",
        "password": "activeuser",
    }
    await client.post(url="/user/register", json=data)
    response = await client.post(url="/user/token", data=data)
    token = response.json()["access_token"]
    return {"Authorization": f"Bearer {token}"}
