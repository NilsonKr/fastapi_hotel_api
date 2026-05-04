from typing import Annotated
from fastapi import FastAPI, Depends
from sqlalchemy import Engine
from sqlmodel import SQLModel,create_engine, Session

sqlitedb_name = 'db.sqlite3'
sqlitedb_url = f'sqlite:///{sqlitedb_name}'

engine = create_engine(sqlitedb_url, echo=True)

def create_tables(app: FastAPI):
  SQLModel.metadata.create_all(engine)
  yield

def get_db_session():
  with Session(engine) as session:
    yield session

SessionDep = Annotated[Session, Depends(get_db_session)]