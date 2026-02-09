from fastapi import FastAPI, Depends, HTTPException
from typing import Annotated
from app import models
from .database import engine, get_db
from sqlalchemy.orm import Session

app = FastAPI()
models.Base.metadata.create_all(bind=engine)

db_dependency = Annotated[Session, Depends(get_db())]