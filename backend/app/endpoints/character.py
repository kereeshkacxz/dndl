from typing import Annotated
import json

from fastapi import APIRouter, Body, Depends, HTTPException, UploadFile, File
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from starlette import status

from app.config import DefaultSettings, getSettings
from app.db.connection import getSession
from app.models import Character, CharacterTable, UserTable, CharacterUpdate
from app.utils.auth import getCurrentUser

apiRouter = APIRouter(prefix="/character", tags=["Character"])

@apiRouter.post(
    "/",
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
    "/{character_id}",
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

@apiRouter.get(
    "/",
    status_code=status.HTTP_200_OK,
    responses={
        status.HTTP_404_NOT_FOUND: {
            "description": "You don't have characters",
        },
    }
)
async def get_users_characters(
    current_user: Annotated[UserTable, Depends(getCurrentUser)],
    session: AsyncSession = Depends(getSession),
) -> dict:  
    statement = await session.execute(select(CharacterTable).where(CharacterTable.owner_id == current_user.id))
    characters = statement.scalars().all()
    if not characters:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="You don't have characters")
    
    data = []
    for character in characters:
        character_data = json.loads(character.data)
        shortly_data = {
            "character_id": character.id,
            "name": character_data["name"],
            "player": character_data["player"],
            "class_name": character_data["class_name"],
            "level": character_data["level"],
            "race": character_data["race"]
        }
        data.append(shortly_data)

    return {
        "data": data
    }

@apiRouter.patch(
    "/{character_id}",
    status_code=status.HTTP_200_OK,
    responses={
        status.HTTP_404_NOT_FOUND: {
            "description": "Character not found",
        },
        status.HTTP_400_BAD_REQUEST: {
            "description": "Invalid data provided",
        },
        status.HTTP_403_FORBIDDEN: {
            "description": "You don't have permisson for this character"
        }
    }
)
async def update_character(
    character_id: str,
    updated_character: Annotated[CharacterUpdate, Body()],
    current_user: Annotated[UserTable, Depends(getCurrentUser)],
    session: AsyncSession = Depends(getSession),
) -> dict:
    character = await session.scalar(select(CharacterTable).where(CharacterTable.id == character_id, CharacterTable.owner_id == current_user.id))
    
    if character is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Character not found")

    if current_user.id != character.owner_id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="You don't have permisson for this character")

    character_data = json.loads(character.data)
    updated_data = updated_character.dict(exclude_unset=True)

    character_data.update(updated_data)
    character.data = json.dumps(character_data)

    await session.commit()
    await session.refresh(character)

    return {
        "id": character.id,
        "data": json.loads(character.data)
    }

@apiRouter.delete(
    "/{character_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    responses={
        status.HTTP_404_NOT_FOUND: {
            "description": "Character not found",
        },
        status.HTTP_403_FORBIDDEN: {
            "description": "You do not have permission to delete this character",
        },
    }
)
async def delete_character(
    character_id: str,
    current_user: Annotated[UserTable, Depends(getCurrentUser)],
    session: AsyncSession = Depends(getSession),
) -> None:
    character = await session.scalar(select(CharacterTable).where(CharacterTable.id == character_id, CharacterTable.owner_id == current_user.id))
    
    if character is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Character not found")

    if current_user.id != character.owner_id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="You don't have permisson for this character")

    await session.delete(character)
    await session.commit()

    return None