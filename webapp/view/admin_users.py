"""Admin Users endpoints module."""

from fastapi import APIRouter, Depends, Response, status
from dependency_injector.wiring import inject, Provide

from .containers import Container
from .services import UserService, UserAdminService, UserInput
from .repositories import NotFoundError

router = APIRouter()


### Admin Endpoints ###
@router.get("/admin/users")
@inject
def get_admin_users(
        user_admin_service: UserAdminService = Depends(Provide[Container.user_admin_service]),
):
    return user_admin_service.get_admin_users()


@router.post("/admin/users")
@inject
def add_admin_user(
        admin_input: UserAdminInput,
        user_admin_service: UserAdminService = Depends(Provide[Container.user_admin_service]),
):
    return user_admin_service.create_admin(UserAdminInput)
