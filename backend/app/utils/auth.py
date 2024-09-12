from datetime import datetime, timedelta, timezone
from typing import Annotated

import jwt
from fastapi import Depends, HTTPException, status
from jwt.exceptions import InvalidTokenError
from sqlalchemy import exc, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.config import DefaultSettings, getSettings
from app.db.connection import getSession
from app.models import RegistrationForm, TokenData, UserTable


def verifyPassword(plain_password: str, hashed_password: str) -> bool:
    return getSettings().PWD_CONTEXT.verify(plain_password, hashed_password)


async def getUser(session: AsyncSession, username: str) -> UserTable | None:
    query = select(UserTable).where(UserTable.username == username)
    return await session.scalar(query)


async def registerUser(session: AsyncSession, user_data: RegistrationForm) -> bool:
    user = UserTable(**user_data.model_dump(exclude_unset=True))
    session.add(user)
    try:
        await session.commit()
    except exc.IntegrityError:
        return False
    return True


async def authenticateUser(session: AsyncSession, username: str, password: str):
    user = await getUser(session, username)
    if not user:
        return False
    if not verifyPassword(password, user.password):
        return False
    return user


def createAccessToken(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=7 * 24 * 60)
    settings = getSettings()
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt


async def getCurrentUser(
    token: Annotated[str, Depends(getSettings().OAUTH2_SCHEME)],
    session: Annotated[AsyncSession, Depends(getSession)],
    settings: Annotated[DefaultSettings, Depends(getSettings)],
) -> UserTable:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except InvalidTokenError:
        raise credentials_exception
    user = await getUser(session, username=token_data.username)
    if user is None:
        raise credentials_exception
    return user
