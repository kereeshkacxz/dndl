import pytest
from starlette import status


class TestRegistration:
    @staticmethod
    def get_reg_url() -> str:
        return "/user/register"

    @staticmethod
    def get_auth_url() -> str:
        return "/user/token"

    @staticmethod
    def get_me_url() -> str:
        return "/user/me"

    @pytest.mark.asyncio
    @pytest.mark.parametrize(
        "data, expected_status",
        [
            ({"username": "123", "password": "short_name"}, status.HTTP_422_UNPROCESSABLE_ENTITY),
            ({"username": "short_password", "password": "123"}, status.HTTP_422_UNPROCESSABLE_ENTITY),
            ({"username": "good_name", "password": "good_password"}, status.HTTP_201_CREATED),
        ],
    )
    async def test_registration(self, client, data, expected_status):
        response = await client.post(url=self.get_reg_url(), json=data)
        assert response.status_code == expected_status

    @pytest.mark.asyncio
    async def test_get_me(self, client):
        data = {
            "username": "testgetme",
            "password": "testgetme",
        }
        response = await client.post(url=self.get_reg_url(), json=data)
        assert response.status_code == status.HTTP_201_CREATED

        response = await client.post(url=self.get_auth_url(), data=data)
        assert response.status_code == status.HTTP_200_OK

        access_token = response.json()["access_token"]
        headers = {"Authorization": f"Bearer {access_token}"}
        response = await client.get(url=self.get_me_url(), headers=headers)
        assert response.status_code == status.HTTP_200_OK

        user_data = response.json()
        assert user_data["username"] == "testgetme"

    @pytest.mark.asyncio
    async def test_invalid_get_me(self, client):
        access_token = "wrong_token"
        headers = {"Authorization": f"Bearer {access_token}"}
        response = await client.get(url=self.get_me_url(), headers=headers)
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    @pytest.mark.asyncio
    @pytest.mark.parametrize(
        "data_reg, data_auth, expected_status",
        [
            (
                {"username": "testauth", "password": "testauth"},
                {"username": "testauth", "password": "testauth"},
                status.HTTP_200_OK,
            ),
            (
                {"username": "testauth", "password": "testauth"},
                {"username": "badname", "password": "badpassword"},
                status.HTTP_401_UNAUTHORIZED,
            ),
        ],
    )
    async def test_authentication(self, client, data_reg, data_auth, expected_status):
        response = await client.post(url=self.get_reg_url(), json=data_reg)
        response = await client.post(url=self.get_auth_url(), data=data_auth)
        assert response.status_code == expected_status
