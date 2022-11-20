from sanic import Sanic
from sanic.response import text


def create_app():
    app = Sanic("MyHelloWorldApp")

    @app.get("/")
    async def hello_world(request):
        return text("Hello, world.")

    return app
