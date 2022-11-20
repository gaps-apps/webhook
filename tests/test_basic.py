import pytest

from app import create_app


@pytest.fixture
def app():
    return create_app()


@pytest.mark.asyncio
async def test_basic_asgi_client(app):
    _, response = await app.asgi_client.post("/gh")

    assert response.status == 200
