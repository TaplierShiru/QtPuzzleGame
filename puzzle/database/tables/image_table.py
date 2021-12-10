from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from .base import Base


class Image(Base):
    __tablename__ = 'images'
    id = Column(Integer, primary_key=True)
    image_path = Column(String(50), unique=True)

    children_games = relationship("Game", back_populates='parent_images', cascade="all, delete-orphan")
    children_saved_games = relationship('SavedGame', back_populates='parent_images', cascade="all, delete-orphan")

    def __init__(self, image_path):
        self.image_path = image_path

    def __repr__(self):
        return "<Image('%s')>" % (self.image_path)

    def get_img_name(self) -> str:
        return self.image_path.split('/')[-1].split('\\')[-1].split('.')[0]

