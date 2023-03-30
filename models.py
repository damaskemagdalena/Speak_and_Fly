from sqlalchemy import Integer, Column, String, ForeignKey, Text, Date, Float
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

class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True)
    lessons = Column(Integer, nullable=False)
    description = Column(Text, nullable=False)
    language_id = Column(Integer, ForeignKey("languages.id"))
    category_id = Column(Integer, ForeignKey("categories.id"))
    level_id = Column(Integer, ForeignKey("levels.id"))
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    price = Column(Float, nullable=False)
