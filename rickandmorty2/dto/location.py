from pydantic import BaseModel


class Location(BaseModel):
    name: str
    _type: str
    dimension: str
    number_of_residents: int
