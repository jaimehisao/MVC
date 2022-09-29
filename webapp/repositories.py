"""Repositories module."""

from contextlib import AbstractContextManager
from numbers import Integral
from typing import Callable, Iterator

from sqlalchemy.orm import Session

from model.models import User


class UserRepository:

    def __init__(self, session_factory: Callable[..., AbstractContextManager[Session]]) -> None:
        self.session_factory = session_factory

    def get_all(self) -> Iterator[User]:
        with self.session_factory() as session:
            query_users = session.query(User).all()
            output_user = {}
            for user in query_users:
                output_user[user.id] = user
            return output_user

    def get_by_id(self, user_id: int) -> User:
        with self.session_factory() as session:
            user = session.query(User).filter(User.id == user_id).first()
            if not user:
                raise UserNotFoundError(user_id)
            return user

    def add(self,
            email: str,
            password: str,
            day_of_birth: int,
            month_of_birth: int,
            year_of_birth: int,
            city_of_birth: str,
            is_active: bool = True) -> User:
        with self.session_factory() as session:
            user = User(email=email,
                        hashed_password=password,
                        is_active=is_active,
                        day_of_birth=day_of_birth,
                        month_of_birth=month_of_birth,
                        year_of_birth=year_of_birth,
                        city_of_birth=city_of_birth)
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



class NotFoundError(Exception):
    entity_name: str

    def __init__(self, entity_id):
        super().__init__(f"{self.entity_name} not found, id: {entity_id}")


class UserNotFoundError(NotFoundError):

    entity_name: str = "User"
