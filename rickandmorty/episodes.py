"""Episodes endpoints module."""

from fastapi import APIRouter, Depends
from dependency_injector.wiring import inject, Provide

import rickandmorty.containers as containers
import rickandmorty.services as services

router = APIRouter()


### Episodes Endpoints ###
@router.get("/episodes")
@inject
def get_episodes(
        episodes_service: services.EpisodesService = Depends(Provide[containers.EpisodesService]),
):
    return episodes_service.get_all()
