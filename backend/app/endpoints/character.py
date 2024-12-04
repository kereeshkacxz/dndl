from typing import Annotated
import json

from fastapi import APIRouter, Body, Depends, HTTPException, UploadFile, File
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from starlette import status

from app.config import DefaultSettings, getSettings
from app.db.connection import getSession
from app.models import Character, CharacterTable, UserTable
from app.utils.auth import getCurrentUser

apiRouter = APIRouter(prefix="/character", tags=["Character"])

@apiRouter.post(
    "/create",
    status_code=status.HTTP_201_CREATED,
    responses={
        status.HTTP_400_BAD_REQUEST: {
            "description": "Username already exists",
        },
    }
)
async def create_character(
    current_user: Annotated[UserTable, Depends(getCurrentUser)],
    character: Annotated[Character, Body()],
    session: AsyncSession = Depends(getSession),
) -> dict:  
    
    data = character.json()
    character_obj = CharacterTable(
        data=data,
        owner_id=current_user.id
    ) 

    session.add(character_obj)
    await session.commit()
    await session.refresh(character_obj)

    return {"id": character_obj.id}

@apiRouter.get(
    "/get_character_data",
    status_code=status.HTTP_200_OK,
    responses={
        status.HTTP_404_NOT_FOUND: {
            "description": "Character not found",
        },
    }
)
async def get_character_data(
    character_id: str,
    session: AsyncSession = Depends(getSession),
) -> dict:  
    character = await session.scalar(select(CharacterTable).where(CharacterTable.id == character_id))
    if character is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Character not found")

    return {
        "data": json.loads(character.data)
    }

