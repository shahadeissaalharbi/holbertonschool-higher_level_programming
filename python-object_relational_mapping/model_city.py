#!/usr/bin/python3
"""
Module that defines the City class, mapping to the 'cities' table
in MySQL, linked to the 'states' table via a foreign key.
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base


class City(Base):
    """Represents a city, linked to the MySQL table 'cities'."""

    __tablename__ = "cities"

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
