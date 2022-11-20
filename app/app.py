from sanic import Sanic
from sanic.response import text
from sanic.log import logger
import os
import hmac
import hashlib


def create_app():
    app = Sanic("webhook")

    GH_WH_SECRET = os.getenv("GH_WH_SECRET", "")

    @app.post("/gh")
    async def from_github(request):
        logger.info(request.headers["x-hub-signature-256"])
        signature = hmac.new(
            bytes(GH_WH_SECRET, "utf-8"), request.body, digestmod=hashlib.sha256
        )
        logger.info(f"sha256={signature}")
        return text("ok")

    return app
