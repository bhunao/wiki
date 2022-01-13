from typing import Optional
from datetime import datetime

from pydantic import BaseModel


class PageBase(BaseModel):
    title: str
    text: Optional[str] = None


class PageCreate(PageBase):
    pass


class Page(PageBase):
    id: int
    date: datetime

    class Config:
        orm_mode = True
