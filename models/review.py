#!/usr/bin/python3
"""The script for the review class"""
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey, Float


class Review(BaseModel, Base):
    """Review class inherits BaseModels, Base
    Attributes:
        place_id: attr place_id
        user_id: attr user_id
        text: the review txt
    """
    __tablename__ = "reviews"
    text = Column(String(1024), nullable=False)
    place_id = Column(String(60), ForeignKey("places.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
