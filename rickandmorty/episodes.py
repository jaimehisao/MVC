"""Episodes endpoints module."""

from fastapi import APIRouter, Depends
from dependency_injector.wiring import inject, Provide

from containers import Container
from services import EpisodesService

router = APIRouter()


### Episodes Endpoints ###
@router.get("/episodes")
@inject
def get_episodes(
        episodes_service: EpisodesService = Depends(Provide[Container.episode_service]),
):
    return episodes_service.get_all()
