# coding=utf-8

from sqlalchemy import Column, String, Integer, Date
from base import Base

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    author_id = Column(Integer)
    created = Column(Date)
    title = Column(String)
    body = Column(String)
