#!/usr/bin/python3
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String

""" Module for the class definition of a state"""

Base = declarative_base()

class State(Base):
    """Represent a state for Mysql database.
    __tablename__ (str): The name of the MySQL table to store States.
    id (sqlalchemy.Integer): The state's id.
    name (sqlalchemy.String): The state's name.
    """
    __tablename__ = "states"
    id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
