from sanic import Sanic
from sanic.response import text


def create_app():
    app = Sanic("webhook")

    @app.post("/gh")
    async def from_github(request):
        return text("ok")

    return app
