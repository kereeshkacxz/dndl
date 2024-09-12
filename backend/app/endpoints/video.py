from typing import Annotated

from fastapi import APIRouter, Depends, File, HTTPException, Query, UploadFile, status
from fastapi.responses import RedirectResponse
from sqlmodel.ext.asyncio.session import AsyncSession

from app.config import DefaultSettings, getSettings
from app.db.connection import getSession
from app.models import VideoUrl
from app.utils.auth import getCurrentUser
from app.utils.files import videoProcessor


apiRouter = APIRouter(
    prefix="/video",
    tags=["Video"],
    dependencies=[Depends(getCurrentUser)],
)


@apiRouter.post("", status_code=status.HTTP_201_CREATED)
async def upload_video(
    file: Annotated[UploadFile, File()],
    session: Annotated[AsyncSession, Depends(getSession)],
    settings: Annotated[DefaultSettings, Depends(getSettings)],
) -> VideoUrl:
    if "video" not in file.content_type:
        raise HTTPException(
            status_code=400,
            detail="Uploaded file is not a video",
        )
    codeForS3 = await videoProcessor.saveFile(file, session)
    downloadUrl = f"{settings.PATH_PREFIX}/video/?codeForS3={codeForS3}"
    return VideoUrl(downloadUrl=downloadUrl)


@apiRouter.get("", status_code=status.HTTP_307_TEMPORARY_REDIRECT)
async def get_video_url(
    codeForS3: Annotated[str, Query()],
    session: Annotated[AsyncSession, Depends(getSession)],
) -> RedirectResponse:
    fileUrl = await videoProcessor.getFileUrl(codeForS3, session)
    return RedirectResponse(fileUrl)


@apiRouter.delete("", status_code=status.HTTP_204_NO_CONTENT)
async def delete_video(
    codeForS3: Annotated[str, Query()],
    session: Annotated[AsyncSession, Depends(getSession)],
):
    await videoProcessor.deleteFile(codeForS3, session)
