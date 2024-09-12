import pytest
from starlette import status


class TestHealthCheckHandler:
    @staticmethod
    def get_ping_application_url() -> str:
        return "/health_check/ping"

    @pytest.mark.asyncio
    async def test_ping_application(self, client):
        response = await client.get(url=self.get_ping_application_url())
        assert response.status_code == status.HTTP_200_OK
