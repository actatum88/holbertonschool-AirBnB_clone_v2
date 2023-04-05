#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv

STO_TYP = getenv("HBNB_TYPE_STORAGE")


class State(BaseModel, Base):
    """ State class """
    if STO_TYP == 'db':
        __tablename__ = "states"
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state", cascade="delete")
    else:
        name = ''

    @property
    def cities(self):
        """
        Return the list of City objects from storage linked to the current State
        """
        from models import storage
        from models.city import City
        cities = []
        for city in storage.all(City).values():
            if city.state_id == self.id:
                cities.append(city)
        return cities

