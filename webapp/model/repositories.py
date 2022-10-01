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
            output = []
            for element in query_users:
                user_data = User(email=element.email,
                        hashed_password=element.hashed_password,
                        is_active=element.is_active,
                        day_of_birth=element.day_of_birth,
                        month_of_birth=element.month_of_birth,
                        year_of_birth=element.year_of_birth,
                        city_of_birth=element.city_of_birth)
                output.append(user_data)
            return output

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
    def __init__(self, session_factory: Callable[..., AbstractContextManager[Session]]) -> None:
        self.session_factory = session_factory

    def create_admin(self,
                     admin_input: AdminInput) -> User:
        with self.session_factory() as session:
            admin_user = UserAdmin(user_id=admin_input.user_id, is_admin=admin_input.is_admin)
            session.add(admin_user)
            session.commit()
            session.refresh(admin_user)
            return admin_user

    def get_admin_users(self) -> Iterator[UserAdmin]:
        with self.session_factory() as session:
            output = []
            query_admin_users = session.query(UserAdmin).all()
            for element in query_admin_users:
                user_admin_data = UserAdmin(user_id=element.user_id, is_admin=element.is_admin)
                output.append(user_admin_data)
            return output


class NotFoundError(Exception):
    entity_name: str

    def __init__(self, entity_id):
        super().__init__(f"{self.entity_name} not found, id: {entity_id}")


class UserNotFoundError(NotFoundError):
    entity_name: str = "User"
