#!/usr/bin/env python3
""" Users model
"""
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


# Create a base class for declarative models
Base = declarative_base()

# Define your User model
class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    
    def __init__(self):
        '''Initialization'''
        engine = create_engine("sqlite:///HNGxTWO.db")
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def strValidation(self, x: str = None) -> str:
        '''Validate input'''
        if x is None or type(x) is not str:
            return None
        else:
            return x
    
    def new(self):
        '''Adds a new obj to the db'''
        self.session.add(self)
    def save(self):
        '''Saves the current session'''
        print('before save')
        self.session.commit()
        print('saved')

    def get(self, user_id):
        '''Returns a user based on its id'''
        print(type(self.session))
        All = self.session.query(User).all()
        for user in All:
            if user.id == user_id:
                return user
        return All

    def to_json(self):
        '''serializes the instance'''
        serial = {}
        for k, v in self.__dict__.items():
            if k.startswith('ses') or k.startswith('_'):
                pass
            else:
                serial[k] = v
        print(serial)
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
