"""Episodes endpoints module."""

from fastapi import APIRouter, Depends, Response, status
from dependency_injector.wiring import inject, Provide

from ..containers import Container
from ..controller.services import EpisodesService, LocationsService, CharacterService
from ..model.repositories import NotFoundError

router = APIRouter()


### Episodes Endpoints ###
@router.get("/episodes")
@inject
def get_episodes(
        episodes_service: EpisodesService = Depends(Provide[Container.episodes_service]),
):
    return episodes_service.get_all()
