"""Models module."""

from sqlalchemy import Column, String, Boolean, Integer
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class EpisodeModel(Base):
    __tablename__ = "episodes"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    air_date = Column(String)
    episode = Column(String)
    characters = Column(String)
    url = Column(String)
    created = Column(String)

    def __repr__(self):
        return f"<Character(id={self.id}, " \
               f"name=\"{self.name}\", " \
               f"status=\"{self.status}\", "\
               f"species=\"{self.species}\", " \
               f"type={self.type})>"


class LocationModel(Base):
    __tablename__ = "locations"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    type = Column(String)
    dimension = Column(String)
    residents = Column(String)
    url = Column(String)
    created = Column(String)

    def __repr__(self):
        return f"<Character(id={self.id}, " \
               f"name=\"{self.name}\", " \
               f"status=\"{self.status}\", "\
               f"species=\"{self.species}\", " \
               f"type={self.type})>"


class CharacterModel(Base):
    __tablename__ = "characters"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    status = Column(String)
    species = Column(String)
    type = Column(String)

    def __repr__(self):
        return f"<Character(id={self.id}, " \
               f"name=\"{self.name}\", " \
               f"status=\"{self.status}\", "\
               f"species=\"{self.species}\", " \
               f"type={self.type})>"
