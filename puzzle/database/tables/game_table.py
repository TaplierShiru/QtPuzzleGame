from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from .base import Base


class Game(Base):
    __tablename__ = 'games'
    id = Column(Integer, primary_key=True)
    diff = Column(String(10), ForeignKey("difficulty_params.diff"))
    id_img = Column(Integer, ForeignKey("images.id"))
    config_path = Column(String(50))

    parent_images = relationship("Image", back_populates="children_games")
    parent_diffs = relationship("DifficultyParams", back_populates="children_games")

    def __init__(self, diff, id_img, config_path):
        self.diff = diff
        self.id_img = id_img
        self.config_path = config_path

    def __repr__(self):
        return "<Game('%s', '%s', '%s')>" % (self.diff, self.id_img, self.config_path)

