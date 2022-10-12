from pydantic import BaseModel


class Episode(BaseModel):
    name: str
    air_date: str
    episode_number: str
    number_of_characters: int
