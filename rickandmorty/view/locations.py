"""Locations endpoints module."""

from fastapi import APIRouter, Depends, Response, status
from dependency_injector.wiring import inject, Provide

from ..containers import Container
from ..controller.services import EpisodesService, LocationsService, CharacterService
from ..model.repositories import NotFoundError

router = APIRouter()


### Episodes Endpoints ###
@router.get("/locations")
@inject
def get_locations(
        locations_service: LocationsService = Depends(Provide[Container.locations_service]),
):
    return locations_service.get_all()
