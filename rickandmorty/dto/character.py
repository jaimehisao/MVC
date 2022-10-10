class Character:
    name: str
    species: str
    gender: str
    number_of_episodes: int

    def __init__(self, name, species, gender, number_of_episodes):
        self.name = name
        self.species = species
        self.gender = gender
        self.number_of_episodes = number_of_episodes
