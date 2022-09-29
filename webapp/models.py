"""Models module."""

from sqlalchemy import Column, String, Boolean, Integer

from .database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    # nuevos campos
    day_of_birth = Column(Integer)
    month_of_birth = Column(Integer)
    year_of_birth = Column(Integer)
    city_of_birth = Column(String)

    def __repr__(self):
        return f"<User(id={self.id}, " \
               f"email=\"{self.email}\", " \
               f"hashed_password=\"{self.hashed_password}\", " \
               f"day_of_birth=\"{self.day_of_birth}\", " \
               f"month_of_birth=\"{self.month_of_birth}\", " \
               f"year_of_birth=\"{self.year_of_birth}\", " \
               f"city_of_birth=\"{self.city_of_birth}\", " \
               f"is_active={self.is_active})>"


class UserAdmin(Base):
    __tablename__ = "user_admins"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    is_admin = Column(Boolean, default=True)

    def __repr__(self):
        return f"<UserAdmin(id={self.id}, " \
               f"user_id=\"{self.user_id}\", " \
               f"is_admin=\"{self.is_admin}\")>"
