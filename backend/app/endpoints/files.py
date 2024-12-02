from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import RedirectResponse

from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from app.db.connection import getSession
from app.utils.files import get_file

apiRouter = APIRouter(prefix="", tags=["Files"])


@apiRouter.get(
    "/get_file",
    status_code=status.HTTP_200_OK,
    responses={
        status.HTTP_404_NOT_FOUND: {
            "description": "File not found",
        },
    }
)
async def get_file_by_id(
    id: str,
    session: AsyncSession = Depends(getSession),
) -> RedirectResponse:
    file = await get_file(id, session)
    if not file:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="File not found",
        )
    
    # Сдась может быть логика проверки прав доступа

    fileUrl = file.filepath +  file.filename
    return RedirectResponse(fileUrl)