from fastapi import APIRouter, Depends
from starlette import status

from app.utils.auth import getCurrentUser
from app.utils.yaGpt import gptProcessor
from app.models import YaGpt


apiRouter = APIRouter(tags=["Yandex GPT"], dependencies=[Depends(getCurrentUser)])


@apiRouter.post(
    "/text_gen",
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(getCurrentUser)],
)
async def gpt_test(
    data: YaGpt
):
    return await gptProcessor.sendRequest(data.text)

