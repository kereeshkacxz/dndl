from datetime import timedelta
from typing import Annotated

from fastapi import APIRouter, Body, Depends, HTTPException, UploadFile, File
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from app.config import DefaultSettings, getSettings
from app.db.connection import getSession
from app.models import RegistrationForm, Token, UserSchema, UserTable, LoginForm, EditForm
from app.utils.auth import authenticateUser, createAccessToken, getCurrentUser, registerUser
from app.utils.files import save_file, delete_file, get_file

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
    settings: Annotated[DefaultSettings, Depends(getSettings)],
    session: AsyncSession = Depends(getSession),
) -> Token:
    is_success = await registerUser(session, registration_form)
    if not is_success:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already exists",
        )

    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = createAccessToken(data={"sub": registration_form.username}, expires_delta=access_token_expires)
    return {"access_token": access_token, "token_type": "bearer"}

# Эта ручка только для норм работы сваггера, потом удалить
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
        )
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = createAccessToken(data={"sub": user.username}, expires_delta=access_token_expires)
    return Token(access_token=access_token, token_type="bearer")

@apiRouter.post(
    "/login",
    responses={
        status.HTTP_401_UNAUTHORIZED: {
            "description": "Incorrect username or password",
        },
    },
)
async def login_for_access_token(
    form_data: Annotated[LoginForm, Body()],
    settings: Annotated[DefaultSettings, Depends(getSettings)],
    session: AsyncSession = Depends(getSession),
) -> Token:
    user = await authenticateUser(session, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
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

@apiRouter.post(
    "/edit_user_info",
    responses={
        status.HTTP_401_UNAUTHORIZED: {
            "description": "Incorrect old password",
        },
    },
)
async def edit_user_info(
    form_data: Annotated[EditForm, Body()],
    current_user: Annotated[UserTable, Depends(getCurrentUser)],
    session: AsyncSession = Depends(getSession),
) -> UserSchema:
    user = await authenticateUser(session, current_user.username, form_data.old_password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect old password",
        )
    data = form_data.dict(exclude_unset=True)
    if form_data.new_password:
        data["password"] = form_data.new_password
        data.pop("new_password")

    data.pop("old_password")

    for key, value in data.items():
        if hasattr(current_user, key):
            setattr(current_user, key, value)

    session.add(current_user)
    await session.commit()

    return current_user

@apiRouter.post(
    "/avatar_update",
    responses={
        status.HTTP_401_UNAUTHORIZED: {
            "description": "Incorrect username or password",
        },
        status.HTTP_400_BAD_REQUEST: {
            "description": "Invalid file type",
        },
    },
    summary="Upload user avatar",
)
async def avatar_upload(
    file: Annotated[UploadFile, File()],
    current_user: Annotated[UserTable, Depends(getCurrentUser)],
    session: AsyncSession = Depends(getSession),
) -> UserSchema:
    allowed_types = {"image/jpeg", "image/png", "image/gif"}
    if file.content_type not in allowed_types:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid file type. Allowed types are: JPEG, PNG, GIF.",
        )

    if current_user.avatar_id:
        await delete_file(current_user.avatar_id, session)

    file_data = await save_file(file, "static/avatars/", session)
    current_user.avatar_id = file_data.id

    session.add(current_user)
    await session.commit()

    return current_user