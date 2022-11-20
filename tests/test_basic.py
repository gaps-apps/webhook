import pytest

from app import create_app


@pytest.fixture
def app():
    return create_app()


@pytest.mark.asyncio
async def test_basic_asgi_client(app):
    request, response = await app.asgi_client.get("/")

    assert request.method.lower() == "get"
    assert response.body == b"Hello, world."
    assert response.status == 200
