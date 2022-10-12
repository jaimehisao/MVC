"""Repositories module."""

from typing import Iterator


import rickandmorty.location as location_dto
import rickandmorty.episode as episode_dto
import rickandmorty.character as character_dto


class EpisodeRepository:
    def __init__(self) -> None:
        # self.session_factory = session_factory
        self.episode_dict = {}

    def get_all(self) -> Iterator[episode_dto.Episode]:
        return self.episode_dict

    def get_by_id(self, episode_id: int) -> episode_dto.Episode:
        return self.episode_dict[episode_id]

    def add(self, episode: episode_dto.Episode):
        self.episode_dict[episode.episode_number] = episode


class LocationRepository:
    def __init__(self) -> None:
        # self.session_factory = session_factory
        self.location_dict = {}

    def get_all(self) -> Iterator[location_dto.Location]:
        return self.location_dict

    def get_by_id(self, location_id: int) -> location_dto.Location:
        return self.location_dict[location_id]

    def add(self, location: location_dto.Location):
        self.location_dict[location.name] = location


class CharacterRepository:
    def __init__(self) -> None:
        # self.session_factory = session_factory
        self.character_dict = {}

    def get_all(self) -> Iterator[character_dto.Character]:
        return self.character_dict

    def get_by_id(self, character_id: int) -> character_dto.Character:
        return self.character_dict[character_id]

    def add(self, character: character_dto.Character):
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

