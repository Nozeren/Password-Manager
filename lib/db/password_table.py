import datetime
from sqlalchemy import *
from sqlalchemy.orm import relationship
from ..db.base import Base
import math
from random import choice
import random
import string


class Password (Base):
    __tablename__ = "passwords"
    id = Column(Integer, autoincrement=True, primary_key=True)
    site= Column(String)
    password=Column(String)

    def __repr__(self):
        return f'{self.site,self.password}'

    @classmethod
    def new_password(cls,session):
        LENGTH=16
        lower = string.ascii_lowercase
        upper = string.ascii_uppercase
        num = string.digits
        symbols = string.punctuation

        all = string.ascii_letters + string.digits + string.punctuation
        password = "".join(random.sample(all,LENGTH))

        return password

    @classmethod
    def save_pass(cls,session,site,passw):
        new_pass=cls(site=site,password=passw)
        session.add(new_pass)
        session.commit()
        print("created")

    @classmethod
    def search(cls,session,site):
        sear=session.query(cls).filter(cls.site==site).first()
        return sear

    @classmethod
    def list_site(cls,session):
        return session.query(cls).all()

    @classmethod
    def delete_pass(cls,session,site):
        site=session.query(cls).filter(cls.site==site).delete()
        session.commit()
