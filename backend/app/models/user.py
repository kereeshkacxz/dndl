import uuid

from pydantic import field_validator
from sqlmodel import Field, SQLModel

from app.config import getSettings

class EditForm(SQLModel):
    old_password: str = Field(min_length=8)
    new_password: str | None = Field(default=None, min_length=8, nullable=True)

    username: str | None = Field(default=None, nullable=True, min_length=5)
    gender: str | None = Field(default=None, nullable=True)
    email: str | None = Field(default=None, nullable=True)

    @field_validator("new_password")
    def hashPassword(cls, new_password):
        new_password = getSettings().PWD_CONTEXT.hash(new_password)
        return new_password

class LoginForm(SQLModel):
    username: str = Field(min_length=5)
    password: str = Field(min_length=8)

class RegistrationForm(SQLModel):
    username: str = Field(min_length=5)
    password: str = Field(min_length=8)

    @field_validator("password")
    def hashPassword(cls, password):
        password = getSettings().PWD_CONTEXT.hash(password)
        return password

class UserTable(SQLModel, table=True):
    id: uuid.UUID | None = Field(default_factory=uuid.uuid4, primary_key=True)
    type: str | None = Field(default="user", nullable=False)

    username: str = Field(nullable=False, unique=True, index=True)
    password: str = Field(nullable=False)

    gender: str | None = Field(nullable=True)
    email: str | None = Field(nullable=True)

    avatar_id: uuid.UUID | None = Field(nullable=True)


class UserSchema(SQLModel):
    username: str
    type: str

    gender: str | None 
    email: str | None 

    avatar_id: uuid.UUID | None 
