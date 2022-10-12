from pydantic import BaseModel


class Character(BaseModel):
    name: str
    species: str
    gender: str
    number_of_episodes: int
