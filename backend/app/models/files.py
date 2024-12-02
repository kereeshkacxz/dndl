import uuid

from pydantic import field_validator
from sqlmodel import Field, SQLModel

from app.config import getSettings

class FilesTable(SQLModel, table = True):
    id: uuid.UUID | None = Field(default_factory=uuid.uuid4, primary_key=True)

    filename: str
    filepath: str

