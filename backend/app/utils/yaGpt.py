import json
from datetime import datetime, timedelta, timezone

import httpx
import requests

from app.config import getSettings


class YaGPT:
    def __init__(self):
        self.iamToken = ""
        self.iamTokenExpirationTimestamp = datetime.now(timezone.utc)
        self.folderId = getSettings().FOLDER_ID

    async def tokenUpdate(self):
        url = "https://iam.api.cloud.yandex.net/iam/v1/tokens"
        headers = {"Content-Type": "application/json"}
        data = {"yandexPassportOauthToken": getSettings().OAUTH_YANDEX_TOKEN}

        iamTokenData = {}
        with httpx.Client() as client:
            response = client.post(url, headers=headers, data=json.dumps(data))

            if response.status_code != 200:
                raise Exception(f"Error: {response.status_code}, {response.text}")

            iamTokenData = response.json()

        self.iamToken = iamTokenData["iamToken"]

        date_string = iamTokenData["expiresAt"].replace("Z", "+00:00")
        dt_object = datetime.fromisoformat(date_string[:26] + date_string[29:])

        self.iamTokenExpirationTimestamp = dt_object

    async def sendRequest(self, text, instruction=None, temperature=0.1, maxTokens=1000):
        if datetime.now(timezone.utc) > self.iamTokenExpirationTimestamp:
            await self.tokenUpdate()

        url = "https://llm.api.cloud.yandex.net/foundationModels/v1/completion"

        data = {
            "modelUri": f"gpt://{self.folderId}/yandexgpt-lite",
            "completionOptions": {
                "stream": False,
                "temperature": temperature,
                "maxTokens": f"{maxTokens}",
            },
            "messages": [{"role": "user", "text": f"{text}"}],
        }

        if instruction is not None:
            data["messages"].append({"role": "assistant", "text": f"{instruction}"})

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.iamToken}",
            "x-folder-id": self.folderId,
        }

        response = requests.post(url, headers=headers, json=data)

        if response.status_code != 200:
            raise Exception(f"Error: {response.status_code}, {response.text}")

        data = response.json()

        return data["result"]["alternatives"][0]["message"]["text"]


gptProcessor = YaGPT()