class Episode:
    name: str
    air_date: str
    episode_number: int
    number_of_characters: int

    def __init__(self, name, air_date, episode_number, number_of_characters):
        self.name = name
        self.air_date = air_date
        self.episode_number = episode_number
        self.number_of_characters = number_of_characters
