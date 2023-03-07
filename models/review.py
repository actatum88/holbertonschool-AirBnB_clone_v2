#!/usr/bin/python3
""" Clase Review """
from sqlalchemy import Column, String, Table, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base


class Review(BaseModel, Base):
    """Review class to store reviews"""
    __tablename__ = "reviews"
    text = Column(String(1024), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
