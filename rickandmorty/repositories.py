"""Repositories module."""

from typing import Iterator

from dto.episode import Episode
from dto.location import Location
from dto.character import Character

from models import EpisodeModel, LocationModel, CharacterModel

class EpisodeRepository:
    def __init__(self) -> None:
        # self.session_factory = session_factory
        self.episode_dict = {}

    def get_all(self) -> Iterator[EpisodeModel]:
        return self.episode_dict

    def get_by_id(self, episode_id: int) -> EpisodeModel:
        return self.episode_dict[episode_id]

    def add(self, episode: Episode):
        self.episode_dict[episode.episode_number] = episode


class LocationRepository:
    def __init__(self) -> None:
        # self.session_factory = session_factory
        self.location_dict = {}

    def get_all(self) -> Iterator[LocationModel]:
        return self.location_dict

    def get_by_id(self, location_id: int) -> LocationModel:
        return self.location_dict[location_id]

    def add(self, location: Location):
        self.location_dict[location.name] = location


class CharacterRepository:
    def __init__(self) -> None:
        # self.session_factory = session_factory
        self.character_dict = {}

    def get_all(self) -> Iterator[CharacterModel]:
        return self.character_dict

    def get_by_id(self, character_id: int) -> CharacterModel:
        return self.character_dict[character_id]

    def add(self, character: Character):
        self.character_dict[character.name] = character


class NotFoundError(Exception):
    entity_name: str

    def __init__(self, entity_id):
        super().__init__(f"{self.entity_name} not found, id: {entity_id}")


class EpisodeNotFoundError(NotFoundError):
    entity_name: str = "Episode"


class LocationNotFoundError(NotFoundError):
    entity_name: str = "Location"


class CharacterNotFoundError(NotFoundError):
    entity_name: str = "Character"

