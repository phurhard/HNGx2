#!/usr/bin/env python3
""" Users model
"""
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Create a SQLite database engine
engine = create_engine('sqlite:///HNGxTWO.db')

# Create a base class for declarative models
Base = declarative_base()
# Create the database tables
Base.metadata.create_all(engine)

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()
# Define your User model
class User(Base):
    __tablename__ = 'users'
    
    id = Column(String, primary_key=True, autoincrement=False)
    name = Column(String, nullable=False)
    
    def __init__(self):
        '''Initialization'''
        pass
    def strValidation(self, x: str = None) -> str:
        '''Validate input'''
        if x is None or type(x) is not str:
            return None
        else:
            return x
    
    def new(self, obj):
        '''Adds a new obj to the db'''
        self.session.add(obj)
    def save(self):
        '''Saves the current session'''
        self.session.commit()

    def get(self, user_id):
        '''Returns a user based on its id'''
        All = self.session.query(User).all()
        for user in All:
            if user.id == user_id:
                return user

    def to_json(self):
        '''serializes the instance'''
        serial = self.__dict__().copy()
        return serial
    def delete(self, user=None):
        '''Deletes an instance feom the DB'''
        if user is not None:
            self.session.delete(user)
"""


import sqlite3

class User():
    '''User model for person instance'''

    #setting up sqlite3 database

    def __init__(self, id: str, name: str = ""):
        '''initialization for users model'''
        self.id = random.randint(); # find a way to make it incremental by it self
        self.name = name

    # class methods needed, [ save, remove, 
    def save():
        '''Saves the current processes'''
#        session.storage.save()

    def to_json(self):
        '''Serialize the user instance'''
        serialized = self.__dict__.copy()
        return serialized
    def remove():
        '''Deletes the instance from DB'''
"""     
