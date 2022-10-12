from pydantic import BaseModel


class Location(BaseModel):
    name: str
    _type: str
    dimension: int
    number_of_residents: int
