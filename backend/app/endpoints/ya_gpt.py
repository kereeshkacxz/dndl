
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status
from pydantic import BaseModel

from app.db.connection import getSession
from app.utils.ya_gpt import gptProcessor

apiRouter = APIRouter(prefix='/gpt', tags=["Ya Gpt"])

class MessageRequest(BaseModel):
    text: str
    instruction: str = None
    temperature: float = 0.1
    max_tokens: int = 1000

@apiRouter.post(
    "/test",
    status_code=status.HTTP_200_OK,
)
async def send_message_to_model(request: MessageRequest):
    try:
        response = await gptProcessor.sendRequest(
            text=request.text,
            instruction=request.instruction,
            temperature=request.temperature,
            maxTokens=request.max_tokens
        )
        return {"answer_alternatives": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@apiRouter.post(
    "/test/image",
    status_code=status.HTTP_200_OK,
)
async def send_message_to_art_model(
    request: str,
    session: AsyncSession = Depends(getSession),
):
    try:
        response = await gptProcessor.sendRequestForImage(
            prompt=request,
            session=session
        )
        return {'image_id': response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
