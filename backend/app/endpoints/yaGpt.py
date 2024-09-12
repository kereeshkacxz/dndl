from fastapi import APIRouter, Depends
from starlette import status

from app.utils.questionGen import knowledge_check_gen
from app.utils.auth import getCurrentUser
from app.utils.yaGpt import gptProcessor
from app.models import Question, YaGpt


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

@apiRouter.post(
    "/questions",
    status_code=status.HTTP_200_OK
)
async def generate_question(
    question: Question,
):
    return await knowledge_check_gen(question)
