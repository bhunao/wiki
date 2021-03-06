from datetime import datetime
from sqlalchemy.orm import Session

from . import models, schemas


def get_pages(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Page).offset(skip).limit(limit).all()


def create_user_page(db: Session, page: schemas.PageCreate):
    date = datetime.now()
    db_page = models.Page(**page.dict(), date=date)
    db.add(db_page)
    db.commit()
    db.refresh(db_page)
    return db_page

def get_page_by_id(db: Session, id: int):
    return db.query(models.Page).filter(models.Page.id == id).first()