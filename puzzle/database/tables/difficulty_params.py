from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from .base import Base


class DifficultyParams(Base):
    __tablename__ = 'difficulty_params'
    diff = Column(String(10), primary_key=True)
    frag_h = Column(Integer)
    frag_v = Column(Integer)
    type_build = Column(String(14))
    type_puzzle = Column(String(20))

    children_saved_games = relationship('SavedGame', back_populates='parent_diffs', cascade="all, delete-orphan")
    children_games = relationship('Game', back_populates='parent_diffs', cascade="all, delete-orphan")

    def __init__(self, diff, frag_h, frag_v, type_build, type_puzzle):
        self.diff = diff
        self.frag_h = frag_h
        self.frag_v = frag_v
        self.type_build = type_build
        self.type_puzzle = type_puzzle

    def __repr__(self):
        return "<DifficultyParams('%s', '%s', '%s', '%s', '%s')>" % (
            self.diff, self.frag_h, self.frag_v, self.type_build, self.type_puzzle
        )

