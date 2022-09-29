"""Status endpoints module."""

from fastapi import APIRouter, Depends, Response, status
from dependency_injector.wiring import inject, Provide

from .containers import Container
from .services import UserService, UserAdminService, UserInput
from .repositories import NotFoundError

router = APIRouter()


@router.get("/status")
def get_status():
    return {"status": "OK"}
