from fastapi import Depends, FastAPI, HTTPException, Request
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine
from fastapi.templating import Jinja2Templates


templates = Jinja2Templates(directory="front-end")

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/pages/", response_model=schemas.Page)
def create_page_for_user( page: schemas.PageCreate, db: Session = Depends(get_db)):
    return crud.create_user_page(db=db, page=page)


@app.get("/pages/", response_model=list[schemas.Page])
def read_pages(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    pages = crud.get_pages(db, skip=skip, limit=limit)
    return pages


@app.get("/home")
def read_pages(request: Request):
    #pages = crud.get_pages(db, skip=skip, limit=limit)
    return templates.TemplateResponse("home.html", {"request": request})

@app.get("/page/{id}")
def load_page(request: Request, id: int, db: Session = Depends(get_db)):
    page = crud.get_page_by_id(db, id)
    print(page)
    return templates.TemplateResponse("page.html", {"request": request, "page": page})