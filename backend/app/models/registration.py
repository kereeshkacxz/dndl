from pydantic import field_validator
from sqlmodel import Field, SQLModel

from app.config import getSettings


class RegistrationForm(SQLModel):
    username: str = Field(min_length=5)
    password: str = Field(min_length=8)

    @field_validator("password")
    def hashPassword(cls, password):
        password = getSettings().PWD_CONTEXT.hash(password)
        return password


class RegistrationSuccess(SQLModel):
    message: str
