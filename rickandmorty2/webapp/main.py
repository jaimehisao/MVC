from fastapi import FastAPI

from .callers import get_all_characters, get_all_episodes, get_all_locations

app = FastAPI()

locations = get_all_locations()
episodes = get_all_episodes()
characters = get_all_characters()


@app.get("/episodes")
def get_episodes():
    return episodes


@app.get("/locations")
def get_locations():
    return locations


@app.get("/characters")
def get_characters():
    return characters
