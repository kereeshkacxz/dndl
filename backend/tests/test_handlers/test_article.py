from uuid import uuid4

import pytest
from starlette import status

from tests.test_handlers.data.article_data import all_types, bad_article, one_type


class TestArticle:
    @staticmethod
    def get_article_url() -> str:
        return "/article"

    @pytest.mark.asyncio
    @pytest.mark.parametrize(
        "data, expected_status",
        [
            (all_types, status.HTTP_201_CREATED),
            (one_type, status.HTTP_201_CREATED),
            (bad_article, status.HTTP_422_UNPROCESSABLE_ENTITY),
        ],
    )
    async def test_create_article(self, client, active_user_token, data, expected_status):
        response = await client.post(self.get_article_url(), json=data, headers=active_user_token)
        assert response.status_code == expected_status

    @pytest.mark.asyncio
    @pytest.mark.parametrize(
        "data, expected_status",
        [
            (one_type, status.HTTP_200_OK),
        ],
    )
    async def test_get_article(self, client, active_user_token, data, expected_status):
        response = await client.post(self.get_article_url(), json=data, headers=active_user_token)
        article_id = response.json()["articleId"]
        response = await client.get(self.get_article_url() + "/" + article_id, headers=active_user_token)
        assert response.status_code == expected_status
        assert response.json() == data

    @pytest.mark.asyncio
    @pytest.mark.parametrize(
        "data, article_id, expected_status",
        [
            (one_type, None, status.HTTP_200_OK),
            (one_type, "123", status.HTTP_422_UNPROCESSABLE_ENTITY),
            (one_type, str(uuid4()), status.HTTP_404_NOT_FOUND),
        ],
    )
    async def test_get_article(self, client, active_user_token, data, article_id, expected_status):
        response = await client.post(self.get_article_url(), json=data, headers=active_user_token)
        if article_id is None:
            article_id = response.json()["articleId"]
        response = await client.get(self.get_article_url() + "/" + article_id, headers=active_user_token)
        assert response.status_code == expected_status
        if expected_status == status.HTTP_200_OK:
            assert response.json() == data

    @pytest.mark.asyncio
    @pytest.mark.parametrize(
        "data, article_id, expected_status",
        [
            (one_type, None, status.HTTP_204_NO_CONTENT),
            (all_types, None, status.HTTP_204_NO_CONTENT),
            (one_type, "123", status.HTTP_422_UNPROCESSABLE_ENTITY),
            (one_type, str(uuid4()), status.HTTP_404_NOT_FOUND),
        ],
    )
    async def test_delete_article(self, client, active_user_token, data, article_id, expected_status):
        response = await client.post(self.get_article_url(), json=data, headers=active_user_token)
        if article_id is None:
            article_id = response.json()["articleId"]
        response = await client.delete(self.get_article_url() + "/" + article_id, headers=active_user_token)
        assert response.status_code == expected_status

    @pytest.mark.asyncio
    @pytest.mark.parametrize(
        "data, article_id, article_data, expected_status",
        [
            (one_type, None, None, status.HTTP_200_OK),
            (one_type, "123", None, status.HTTP_422_UNPROCESSABLE_ENTITY),
            (one_type, str(uuid4()), None, status.HTTP_200_OK),
            (all_types, None, all_types, status.HTTP_200_OK),
        ],
    )
    async def test_update_article(
        self,
        client,
        active_user_token,
        data,
        article_id,
        article_data,
        expected_status,
    ):
        response = await client.post(self.get_article_url(), json=data, headers=active_user_token)
        if article_id is None:
            article_id = response.json()["articleId"]
        if article_data is None:
            article_data = {"title": "string", "content": []}
        response = await client.put(
            self.get_article_url() + "/" + article_id, headers=active_user_token, json=article_data
        )
        assert response.status_code == expected_status
