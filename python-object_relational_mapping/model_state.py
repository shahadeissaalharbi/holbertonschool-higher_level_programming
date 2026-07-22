#!/usr/bin/python3
"""
Module that defines the State class and the SQLAlchemy Base,
mapping to the 'states' table in MySQL.
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String


# Base is the declarative base all our ORM models inherit from
Base = declarative_base()


class State(Base):
    """Represents a state, linked to the MySQL table 'states'."""

    __tablename__ = "states"

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
