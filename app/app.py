import asyncio
import hashlib
import hmac
import os

import aio_pika
import orjson
from sanic import Sanic
from sanic.exceptions import SanicException
from sanic.log import logger
from sanic.response import text


async def publish_event(data: dict):

    connection = await aio_pika.connect_robust(
        "amqp://fuzz:Y2cx51ngSRRCoLhb@rabbitmq/", loop=asyncio.get_event_loop()
    )

    routing_key = "github_push_events"

    channel = await connection.channel()

    await channel.default_exchange.publish(
        aio_pika.Message(body=orjson.dumps(data)), routing_key=routing_key
    )

    await connection.close()


def create_app():
    app = Sanic("webhook")

    GH_WH_SECRET = os.getenv("GH_WH_SECRET", "")

    @app.post("/gh")
    async def from_github(request):
        try:
            header = request.headers["x-hub-signature-256"]
            logger.info(header)
            signature = hmac.new(
                bytes(GH_WH_SECRET, "utf-8"), request.body, digestmod=hashlib.sha256
            )
            token = f"sha256={signature.hexdigest()}"
            logger.info(token)

            if token == header:
                event = request.json()
                await publish_event(
                    {"repo": event["repository"]["full_name"], "refs": event["refs"]}
                )
                return text("ok")
        except:
            SanicException(status_code=400)

    return app
