#!/usr/bin/python3
from sqalchemy import Column, ForeignKey, Integer, String
from model_state import Base
"""
"""
Base = declarative_base()

if __name__ == "__main__"

class City(Base):
    """Base city class"""
    __tablename__ = "cities"
    id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
