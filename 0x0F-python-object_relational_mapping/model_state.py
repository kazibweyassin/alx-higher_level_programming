#!/usr/bin/python3
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker
Base = declarative_base():

class State(Base):
    """State class"""
    __table__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, unique=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    
    #create engine and bind it to MQSL server
engine = create_engine('mysql+mysqldb://username:password@localhost:3306/database_name')

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
