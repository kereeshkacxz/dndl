import requests
import base64
import time

from yandex_cloud_ml_sdk import YCloudML
from app.config import getSettings
from app.utils.files import save_img_file

class YaGPT:
    def __init__(self):
        self.sdk = YCloudML(
            folder_id=getSettings().FOLDER_ID,
            auth=getSettings().YANDEX_SECRET_KEY
        )
        self.model = self.sdk.models.completions('yandex-art')
        
    async def sendRequest(self, text, instruction=None, temperature=0.1, maxTokens=1000):
        self.model = self.model.configure(
            temperature=temperature,
            max_tokens=maxTokens
        )
        
        messages = [{"role": "user", "text": text}]
        if instruction:
            messages.append({"role": "assistant", "text": instruction})

        result = self.model.run(messages)

        return result

        # return [result[i].text for i in range(len(result))]

    async def sendRequestForImage(self, prompt, session, seed=2):
        prompt = {
            "modelUri": f"art://{getSettings().FOLDER_ID}/yandex-art/latest",
            "generationOptions": {
            "seed": seed,
            "aspectRatio": {
                "widthRatio": "1",
                "heightRatio": "1"
            }
            },
            "messages": [
                {
                    "weight": "1",
                    "text": prompt
                }
            ]
        }
        
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Api-key {getSettings().YANDEX_SECRET_KEY}"
        }
        
        create_request = requests.post('https://llm.api.cloud.yandex.net/foundationModels/v1/imageGenerationAsync', headers=headers, json=prompt)

        for _ in range(20):
            time.sleep(5)
            done_request = requests.get(f'https://llm.api.cloud.yandex.net:443/operations/{create_request.json()["id"]}', headers=headers)
            if done_request.json()['done'] == True:
                file_data = await save_img_file(
                    file=done_request.json()['response']['image'],
                    path='static/images/',
                    session=session
                )        
                return file_data.id
        
        return {"detal": "Generate error"}


gptProcessor = YaGPT()
