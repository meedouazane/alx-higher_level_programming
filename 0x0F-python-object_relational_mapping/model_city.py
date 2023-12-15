#!/usr/bin/python3
''' contains the class definition of a State '''
from sqlalchemy import Column, Integer, String, MetaData, ForeignKey 
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


mymetadata = MetaData()
Base = declarative_base(metadata=mymetadata)


class City(Base):
    ''' inherits from Base '''
    __tablename__ = 'City'
    id = Column(
            Integer, autoincrement=True, nullable=False,
            unique=True, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'))
    states = relationship('States', backref='City')

