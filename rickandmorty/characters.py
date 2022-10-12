"""Characters endpoints module."""

from fastapi import APIRouter, Depends
from dependency_injector.wiring import inject, Provide

import rickandmorty.containers as containers
import rickandmorty.services as services

router = APIRouter()


### Episodes Endpoints ###
@router.get("/characters")
@inject
def get_characters(
        characters_service: services.CharacterService = Depends(Provide[containers.CharacterService]),
):
    return characters_service.get_all()
