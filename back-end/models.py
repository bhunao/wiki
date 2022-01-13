from sqlalchemy import Column, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship

from .database import Base


class Page(Base):
    __tablename__ = "page"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    text = Column(Text)
