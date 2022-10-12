class Location:
    name: str
    _type: str
    dimension: int
    number_of_residents: int

    def __init__(self, name, _type, dimension, number_of_residents):
        self.name = name
        self._type = _type
        self.dimension = dimension
        self.number_of_residents = number_of_residents
