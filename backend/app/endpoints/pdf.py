from fastapi import APIRouter, Body
from typing import Annotated
from fastapi.responses import StreamingResponse

from starlette import status

from app.models import Character
from app.utils.pdf_creater import create_pdf

apiRouter = APIRouter(prefix="/pdf", tags=["PDF"])

@apiRouter.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    responses={
        status.HTTP_400_BAD_REQUEST: {
            "description": "Username already exists",
        },
    }
)
async def generate_pdf(character: Annotated[Character, Body()],):
    character_data = character.dict()
    # try:
    pdf_buffer = create_pdf(json_data={'character': character_data})
    return StreamingResponse(pdf_buffer, media_type="application/pdf", headers={"Content-Disposition": "attachment; filename=character_sheet.pdf"})
    # except Exception as e:
    #     raise HTTPException(status_code=500, detail=str(e))