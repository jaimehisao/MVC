"""Application module."""

from fastapi import FastAPI
from containers import Container

from characters import router as characters_router
from episodes import router as episodes_router
from locations import router as locations_router


def create_app() -> FastAPI:
    container = Container()

    app = FastAPI()
    app.container = container
    app.include_router(characters_router)
    app.include_router(episodes_router)
    app.include_router(locations_router)
    return app


app = create_app()
