from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from .base import Base


class SavedGame(Base):
    __tablename__ = 'saved_games'
    id = Column(Integer, primary_key=True)
    login = Column(String(8), ForeignKey("users.login"))
    diff = Column(String(10), ForeignKey("difficulty_params.diff"))
    score_type = Column(String(14))
    id_img = Column(Integer, ForeignKey("images.id"))
    config_path = Column(String(50))

    parent_images = relationship("Image", back_populates="children_saved_games")
    parent_diffs = relationship("DifficultyParams", back_populates="children_saved_games")
    parent_logins = relationship("User", back_populates="children_logins_saved_game")

    def __init__(self, login, diff, score_type, id_img, config_path):
        self.login = login
        self.diff = diff
        self.score_type = score_type
        self.id_img = id_img
        self.config_path = config_path

    def __repr__(self):
        return "<SavedGame('%s', '%s', '%s', '%s', '%s')>" % (
            self.login, self.diff, self.score_type,
            self.id_img, self.config_path,
        )

