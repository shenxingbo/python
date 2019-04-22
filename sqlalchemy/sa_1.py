#encoding:utf-8
# sqlalchemy的单表操作

from sqlalchemy.engine import create_engine
url = "mysql://root:root@10.202.38.46:3306/blog"
engine =create_engine(url, encoding='utf-8', echo=True)


from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base(engine)

from sqlalchemy import Column
from sqlalchemy.types import Integer, Date, DateTime, Float, Text, String


def create_all_table(Base):
    Base.metadata.create_all()


def drop_all_table(Base):
    Base.metadata.drop_all()


class User(Base):

    __tablename__ = 't_user'

    id = Column(Integer, primary_key=True, autoincrement=True)
    account = Column(String(length=8), unique=True)
    pwd = Column(String(length=3))
    birth = Column(Date)
    score = Column(Float(decimal_return_scale=2))


class Address(Base):
    __tablename__ = 't_addr'

    id = Column(Integer, primary_key=True, autoincrement=True)
    aname = Column(String(30), unique=True)

