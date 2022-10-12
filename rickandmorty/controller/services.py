"""Services module."""

from typing import Iterator

from mvc.webapp.model.repositories import UserRepository, UserAdminRepository
from ..model.models import User, UserAdmin
from mvc.webapp.dto.input import UserInput, AdminInput


class EpisodesService:
    """Episodes service."""

    def __init__(self, episodes_repository: EpisodesRepository) -> None:
        self.episodes_repository = episodes_repository

    def get_all(self) -> Iterator[Episodes]:
        return self.episodes_repository.get_all()

    def get_by_id(self, episode_id: int) -> Episodes:
        return self.episodes_repository.get_by_id(episode_id)

    def add(self, episode_input: EpisodeInput) -> Episodes:
        return self.episodes_repository.add(episode_input)

    def delete_by_id(self, episode_id: int) -> None:
        self.episodes_repository.delete_by_id(episode_id)


class UserService:

    def __init__(self, user_repository: UserRepository) -> None:
        self._repository: UserRepository = user_repository

    def get_users(self) -> Iterator[User]:
        return self._repository.get_all()

    def get_user_by_id(self, user_id: int) -> User:
        return self._repository.get_by_id(user_id)

    def create_user(self, user_input: UserInput) -> User:
        return self._repository.add(email=f"{user_input.user_name}@email.com",
                                    password=user_input.hashed_password,
                                    is_active=user_input.is_active,
                                    day_of_birth=user_input.day_of_birth,
                                    month_of_birth=user_input.month_of_birth,
                                    year_of_birth=user_input.year_of_birth,
                                    city_of_birth=user_input.city_of_birth)

    def delete_user_by_id(self, user_id: int) -> None:
        return self._repository.delete_by_id(user_id)


