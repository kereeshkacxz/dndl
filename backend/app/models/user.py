import uuid

from sqlmodel import Field, SQLModel


class UserTable(SQLModel, table=True):
    id: uuid.UUID | None = Field(default_factory=uuid.uuid4, primary_key=True)
    username: str = Field(nullable=False, unique=True, index=True)
    password: str = Field(nullable=False)


class UserSchema(SQLModel):
    username: str
