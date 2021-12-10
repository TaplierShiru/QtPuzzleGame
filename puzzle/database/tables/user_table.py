from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from .base import Base


class User(Base):
    __tablename__ = 'users'
    login = Column(String(8), primary_key=True)
    password = Column(String(12))
    role = Column(String(20))

    children_logins_saved_game = relationship("SavedGame", back_populates="parent_logins", cascade="all, delete-orphan")
    children_logins_record = relationship("Record", back_populates="parent_logins", cascade="all, delete-orphan")

    def __init__(self, login, password, role):
        self.login = login
        self.password = password
        self.role = role

    def __repr__(self):
        return "<User('%s', '%s', '%s')>" % (self.fullname, self.password, self.role)

