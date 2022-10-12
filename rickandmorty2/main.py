from fastapi import FastAPI, Depends

from callers import get_all_characters, get_all_episodes, get_all_locations
from dto.episode import Episode
from dto.character import Character
from dto.location import Location


app = FastAPI()

locations = get_all_locations()
episode_dict = get_all_episodes()
characters = get_all_characters()


@app.get("/episodes", response_model=list[Episode])
def get_episodes() -> list[Episode]:
    return episode_dict


@app.get("/locations", response_model=list[Location])
def get_locations():
    return locations


@app.get("/characters", response_model=list[Character])
def get_characters():
    return characters
