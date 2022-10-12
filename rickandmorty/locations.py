"""Locations endpoints module."""

from fastapi import APIRouter, Depends
from dependency_injector.wiring import inject, Provide

import rickandmorty.containers as containers
import rickandmorty.services as services

router = APIRouter()


### Episodes Endpoints ###
@router.get("/locations")
@inject
def get_locations(
        locations_service: services.LocationsService = Depends(Provide[containers.LocationsService]),
):
    return locations_service.get_all()
