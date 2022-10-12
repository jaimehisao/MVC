"""Characters endpoints module."""

from fastapi import APIRouter, Depends
from dependency_injector.wiring import inject, Provide

from containers import Container
from services import CharacterService

router = APIRouter()


### Episodes Endpoints ###
@router.get("/characters")
@inject
def get_characters(
        characters_service: CharacterService = Depends(Provide[Container.character_service]),
):
    return characters_service.get_all()
