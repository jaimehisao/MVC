from pydantic import BaseModel


class Episode(BaseModel):
    name: str
    air_date: str
    episode_number: int
    number_of_characters: int
