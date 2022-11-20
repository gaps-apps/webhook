import hashlib
import hmac
import os

from sanic import Sanic
from sanic.log import logger
from sanic.response import text


def create_app():
    app = Sanic("webhook")

    GH_WH_SECRET = os.getenv("GH_WH_SECRET", "")

    @app.post("/gh")
    async def from_github(request):
        logger.info(request.headers["x-hub-signature-256"])
        signature = hmac.new(
            bytes(GH_WH_SECRET, "utf-8"), request.body, digestmod=hashlib.sha256
        )
        logger.info(f"sha256={signature.hexdigest()}")
        return text("ok")

    return app
