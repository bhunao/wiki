from typing import Optional

from pydantic import BaseModel


class PageBase(BaseModel):
    title: str
    text: Optional[str] = None


class PageCreate(PageBase):
    pass


class Page(PageBase):
    id: int

    class Config:
        orm_mode = True
