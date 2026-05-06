from pathlib import Path
from typing import Annotated
from fastapi import Depends
from sqlmodel import create_engine, Session

sqlitedb_path = Path(__file__).resolve().parent / 'db.sqlite3'
sqlitedb_url = f'sqlite:///{sqlitedb_path}'

engine = create_engine(sqlitedb_url, echo=True)

def get_db_session():
  with Session(engine) as session:
    yield session

SessionDep = Annotated[Session, Depends(get_db_session)]