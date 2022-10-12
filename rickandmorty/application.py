"""Application module."""

from fastapi import FastAPI
from containers import Container

def create_app() -> FastAPI:
    container = Container()

    db = container.db()
    db.create_database()

    app = FastAPI()
    app.container = container
    app.include_router(admin_users_router)
    app.include_router(status_router)
    app.include_router(users_router)
    return app


app = create_app()
