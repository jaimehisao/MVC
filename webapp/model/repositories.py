"""Repositories module."""

from contextlib import AbstractContextManager
from typing import Callable, Iterator

from sqlalchemy.orm import Session

from models import User, UserAdmin
from ..dto.input import AdminInput, UserInput

class UserRepository:

    def __init__(self, session_factory: Callable[..., AbstractContextManager[Session]]) -> None:
        self.session_factory = session_factory

    def get_all(self) -> Iterator[User]:
        with self.session_factory() as session:
            query_users = session.query(User).all()
            return query_users

    def get_by_id(self, user_id: int) -> User:
        with self.session_factory() as session:
            user = session.query(User).filter(User.id == user_id).first()
            if not user:
                raise UserNotFoundError(user_id)
            return user

    def add(self,
            user_input: UserInput) -> User:
        with self.session_factory() as session:
            user = User(email=user_input.email,
                        hashed_password=user_input.hashed_password,
                        is_active=user_input.is_active,
                        day_of_birth=user_input.day_of_birth,
                        month_of_birth=user_input.month_of_birth,
                        year_of_birth=user_input.year_of_birth,
                        city_of_birth=user_input.city_of_birth)
            session.add(user)
            session.commit()
            session.refresh(user)
            return user

    def delete_by_id(self, user_id: int) -> None:
        with self.session_factory() as session:
            entity: User = session.query(User).filter(User.id == user_id).first()
            if not entity:
                raise UserNotFoundError(user_id)
            session.delete(entity)
            session.commit()


class UserAdminRepository:
    def __init__(self, user_admin_repository: UserAdminRepository) -> None:
        self._repository: UserAdminRepository = user_admin_repository

    def get_admin_users(self) -> Iterator[UserAdmin]:
        return self._repository.get_all()

    def creatre_admin_user(self, admin_input: AdminInput) -> UserAdmin:
        return self._repository.add(admin_input)



class NotFoundError(Exception):
    entity_name: str

    def __init__(self, entity_id):
        super().__init__(f"{self.entity_name} not found, id: {entity_id}")


class UserNotFoundError(NotFoundError):

    entity_name: str = "User"
