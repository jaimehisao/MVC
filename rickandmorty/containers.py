"""Containers module."""

from dependency_injector import containers, providers

from rickandmorty.services import EpisodesService, LocationsService, CharacterService
from rickandmorty.repositories import EpisodeRepository, LocationRepository, CharacterRepository


class Container(containers.DeclarativeContainer):

    wiring_config = containers.WiringConfiguration(modules=[".view"])

    episode_repository = providers.Factory(
        EpisodeRepository,
    )

    location_repository = providers.Factory(
        LocationRepository,
    )

    character_repository = providers.Factory(
        CharacterRepository,
    )

    episode_service = providers.Factory(
        EpisodesService,
    )

    location_service = providers.Factory(
        LocationsService,
    )

    character_service = providers.Factory(
        CharacterService,
    )
