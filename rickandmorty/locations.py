"""Locations endpoints module."""

from fastapi import APIRouter, Depends
from dependency_injector.wiring import inject, Provide

from containers import Container
from services import LocationsService

router = APIRouter()


### Episodes Endpoints ###
@router.get("/locations")
@inject
def get_locations(
        locations_service: LocationsService = Depends(Provide[Container.location_service]),
):
    return locations_service.get_all()
