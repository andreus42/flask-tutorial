from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, String, Integer, Boolean, ForeignKey, Date

engine = create_engine('sqlite:///instance/flaskr.sqlite')
Session = sessionmaker(bind=engine)
Base = declarative_base()
