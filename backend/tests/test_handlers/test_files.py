import pytest
from starlette import status

from app.utils.files import fileProcessor


fileProcessor.fileDir = "test/file/"


class TestFile:
    @staticmethod
    def get_file_url() -> str:
        return "/file"

    @pytest.mark.asyncio
    @pytest.mark.parametrize(
        "file_path, expected_status",
        [
            ("tests/test_handlers/data/video.mp4", status.HTTP_201_CREATED),
            ("tests/test_handlers/data/file.txt", status.HTTP_201_CREATED),
        ],
    )
    async def test_load_file(self, client, active_user_token, file_path, expected_status):
        with open(file_path, "rb") as file:
            response = await client.post(
                self.get_file_url(), files={"file": (file_path, file)}, headers=active_user_token
            )
            assert response.status_code == expected_status

    @pytest.mark.asyncio
    @pytest.mark.parametrize(
        "file_path, expected_status",
        [
            ("tests/test_handlers/data/file.txt", status.HTTP_201_CREATED),
        ],
    )
    async def test_get_file_url(self, client, active_user_token, file_path, expected_status):
        with open(file_path, "rb") as file:
            response = await client.post(
                self.get_file_url(), files={"file": (file_path, file)}, headers=active_user_token
            )
            assert response.status_code == expected_status
        download_url = response.json()["downloadUrl"]
        fileName = download_url.split("=")[-1]
        response = await client.get(self.get_file_url(), params={"codeForS3": fileName}, headers=active_user_token)
        assert response.status_code == status.HTTP_307_TEMPORARY_REDIRECT

    @pytest.mark.asyncio
    @pytest.mark.parametrize(
        "file_path, expected_status",
        [
            ("tests/test_handlers/data/file.txt", status.HTTP_201_CREATED),
        ],
    )
    async def test_delete_file(self, client, active_user_token, file_path, expected_status):
        with open(file_path, "rb") as file:
            response = await client.post(
                self.get_file_url(), files={"file": (file_path, file)}, headers=active_user_token
            )
            assert response.status_code == expected_status
        download_url = response.json()["downloadUrl"]
        fileName = download_url.split("=")[-1]
        await client.delete(self.get_file_url(), params={"codeForS3": fileName}, headers=active_user_token)
