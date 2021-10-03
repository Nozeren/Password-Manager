import os
from sqlalchemy import inspect, Column, ForeignKey, Integer, String, or_, and_, Boolean, DateTime, create_engine, MetaData
from sqlalchemy.orm import sessionmaker, relationship, backref
from ..db import base
from ..db import password_table


file = os.path.join(os.getcwd(), os.listdir(os.getcwd())[0])
file = os.path.dirname(file)

engine = create_engine(
    "sqlite:///"+file+"\lib\db\database.db?charset=utf8",convert_unicode=True,echo=False)

base.Base.metadata.create_all(engine, checkfirst=True)
Session = sessionmaker(bind=engine)
session = Session()


inspect = inspect(engine)
password= password_table.Password()
