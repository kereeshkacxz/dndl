import os
import uuid
from typing import Annotated
from fastapi import Depends, UploadFile
from sqlalchemy.ext.asyncio import AsyncSession
from datetime import datetime
from sqlalchemy import select

from app.db.connection import getSession
from app.models import FilesTable


async def save_file(
    file: UploadFile,
    path: str, 
    session: Annotated[AsyncSession, Depends(getSession)],
) -> FilesTable | None:

    if not os.path.exists(path):
        return None

    filename = datetime.now().strftime('%Y-%m-%d_%H-%M-%S') + '_' + str(uuid.uuid4()) + '.' + file.filename.split('.')[-1]

    file_data = FilesTable(filename=filename, filepath=path)
    session.add(file_data)
    await session.commit()
    await session.refresh(file_data)

    with open(path + '/' + filename, 'wb') as f:
        f.write(await file.read())

    return file_data

async def get_file(
    id: str, 
    session: Annotated[AsyncSession, Depends(getSession)]
) -> FilesTable | None:
    query = select(FilesTable).where(FilesTable.id == id)
    return await session.scalar(query)
    

async def delete_file(
    id: str, 
    session: Annotated[AsyncSession, Depends(getSession)]
) -> bool:
    query = select(FilesTable).where(FilesTable.id == id)
    file = await session.scalar(query)

    if not file:
        return False
    
    if os.path.exists(file.filepath + file.filename):
        os.remove(file.filepath + file.filename)

    session.delete(file)
    await session.commit()
    return True

