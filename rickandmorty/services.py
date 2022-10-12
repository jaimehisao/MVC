"""Services module."""

import sys
sys.path.append("")
import rickandmorty.repositories as repositories
import rickandmorty.location as location_dto
import rickandmorty.episode as episode_dto
import rickandmorty.character as character_dto


class EpisodesService:
    """Episodes service."""

    def __init__(self, episodes_repository: repositories.EpisodeRepository) -> None:
        self.episodes_repository = episodes_repository

    def get_all(self):
        return self.episodes_repository.get_all()

    def get_by_id(self, episode_id: int):
        return self.episodes_repository.get_by_id(episode_id)

    def add(self, episode_input: episode_dto.Episode):
        return self.episodes_repository.add(episode_input)


class LocationsService:
    """Locations service."""

    def __init__(self, locations_repository: repositories.LocationRepository) -> None:
        self.locations_repository = locations_repository

    def get_all(self):
        return self.locations_repository.get_all()

    def get_by_id(self, location_id: int):
        return self.locations_repository.get_by_id(location_id)

    def add(self, location_input: location_dto.Location):
        return self.locations_repository.add(location_input)


class CharacterService:
    """Character service."""

    def __init__(self, character_repository: repositories.CharacterRepository) -> None:
        self.character_repository = character_repository

    def get_all(self):
        return self.character_repository.get_all()

    def get_by_id(self, character_id: int):
        return self.character_repository.get_by_id(character_id)

    def add(self, character_input: character_dto.Character):
        return self.character_repository.add(character_input)
