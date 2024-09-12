from datetime import timedelta
from typing import Annotated

from fastapi import APIRouter, Body, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from app.config import DefaultSettings, getSettings
from app.db.connection import getSession
from app.models import RegistrationForm, RegistrationSuccess, Token, UserSchema, UserTable
from app.utils.auth import authenticateUser, createAccessToken, getCurrentUser, registerUser


apiRouter = APIRouter(prefix="/user", tags=["User"])


@apiRouter.post(
    "/register",
    status_code=status.HTTP_201_CREATED,
    responses={
        status.HTTP_400_BAD_REQUEST: {
            "description": "Username already exists",
        },
    },
)
async def registration(
    registration_form: Annotated[RegistrationForm, Body()],
    session: AsyncSession = Depends(getSession),
) -> RegistrationSuccess:
    is_success = await registerUser(session, registration_form)
    if is_success:
        return {"message": "Registered!"}
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail="Username already exists",
    )


@apiRouter.post(
    "/token",
    responses={
        status.HTTP_401_UNAUTHORIZED: {
            "description": "Incorrect username or password",
        },
    },
)
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    session: Annotated[AsyncSession, Depends(getSession)],
    settings: Annotated[DefaultSettings, Depends(getSettings)],
) -> Token:
    user = await authenticateUser(session, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = createAccessToken(data={"sub": user.username}, expires_delta=access_token_expires)
    return Token(access_token=access_token, token_type="bearer")


@apiRouter.get(
    "/me",
    responses={
        status.HTTP_401_UNAUTHORIZED: {
            "description": "Incorrect username or password",
        },
    },
    summary="Get active user information",
)
async def read_users_me(
    current_user: Annotated[UserTable, Depends(getCurrentUser)],
) -> UserSchema:
    return current_user
