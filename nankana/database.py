from typing import Generator
from config import setting
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


SQLALCHEMY_DATABASE_URL:str = setting.DATABASE_URL
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# SQLALCHEMY_DATABASE_URL:str = 'sqlite:///./sqlite.db'
# engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args = { 
#     "check_same_thread" : False,
#  })



SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
Base = declarative_base()


def get_db() -> Generator:
    ''' Dependence Injection'''
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
        


