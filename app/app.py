from sanic import Sanic
from sanic.response import text
from sanic.log import logger

def create_app():
    app = Sanic("webhook")

    @app.post("/gh")
    async def from_github(request):
        logger.info(request.body)
        return text("ok")

    return app
