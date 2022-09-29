"""Endpoints module."""

from fastapi import APIRouter, Depends, Response, status
from dependency_injector.wiring import inject, Provide

from .containers import Container
from .services import UserService, UserAdminService, UserInput
from .repositories import NotFoundError

router = APIRouter()


### User endpoints ###
@router.get("/users")
@inject
def get_list(
        user_service: UserService = Depends(Provide[Container.user_service]),
):
    return user_service.get_users()


@router.get("/users/{user_id}")
@inject
def get_by_id(
        user_id: int,
        user_service: UserService = Depends(Provide[Container.user_service]),
):
    try:
        return user_service.get_user_by_id(user_id)
    except NotFoundError:
        return Response(status_code=status.HTTP_404_NOT_FOUND)


@router.post("/users", status_code=status.HTTP_201_CREATED)
@inject
def add(
        user_input: UserInput,
        user_service: UserService = Depends(Provide[Container.user_service])
):
    return user_service.create_user(user_input)


@router.delete("/users/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
@inject
def remove(
        user_id: int,
        user_service: UserService = Depends(Provide[Container.user_service]),
):
    try:
        user_service.delete_user_by_id(user_id)
    except NotFoundError:
        return Response(status_code=status.HTTP_404_NOT_FOUND)
    else:
        return Response(status_code=status.HTTP_204_NO_CONTENT)


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

@router.get("/status")
def get_status():
    return {"status": "OK"}
