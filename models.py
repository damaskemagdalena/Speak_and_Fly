from datetime import datetime
from sqlalchemy import Integer, Column, String, DateTime, ForeignKey, Text, Table
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Language(Base):
    __tablename__ = "languages"

    id = Column(Integer, primary_key = True)
    name = Column(String(20), nullable = False, unique = True)

    def __repr__(self):
        return f'Language ({self.name})'


class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False, unique=True)

    def __repr__(self):
        return f'Category ({self.name})'


class Level(Base):
    __tablename__ = "levels"

    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False, unique=True)
    description = Column(Text, nullable=False)

    def __repr__(self):
        return f'Level ({self.name})'

