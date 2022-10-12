"""Characters endpoints module."""

from fastapi import APIRouter, Depends, Response, status
from dependency_injector.wiring import inject, Provide

from ..containers import Container
from ..controller.services import CharacterService
from ..model.repositories import NotFoundError

router = APIRouter()


### Episodes Endpoints ###
@router.get("/characters")
@inject
def get_characters(
        characters_service: CharacterService = Depends(Provide[Container.characters_service]),
):
    return characters_service.get_all()
