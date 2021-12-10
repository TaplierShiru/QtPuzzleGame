from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from .base import Base


class Record(Base):
    __tablename__ = 'records'
    id = Column(Integer, primary_key=True)
    login = Column(String(8), ForeignKey("users.login"))
    diff = Column(String(10))
    score_type = Column(String(14))
    score_value = Column(Integer)

    parent_logins = relationship("User", back_populates="children_logins_record")

    def __init__(self, login, diff, score_type, score_value):
        self.login = login
        self.diff = diff
        self.score_type = score_type
        self.score_value = score_value

    def __repr__(self):
        return "<Record('%s', '%s', '%s', '%s')>" % (
            self.login, self.diff, self.score_type, self.score_value
        )

