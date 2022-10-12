from fastapi import APIRouter, Depends

import sys
sys.path.append('../')
from dto.character import Character
from dto.location import Location
from dto.episode import Episode

from model.db import episode_dict, locations, characters

router = APIRouter()


@router.get("/episodes", response_model=list[Episode])
def get_episodes() -> list[Episode]:
    return episode_dict


@router.get("/locations", response_model=list[Location])
def get_locations():
    return locations


@router.get("/characters", response_model=list[Character])
def get_characters():
    return characters
