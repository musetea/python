from fastapi import APIRouter, Depends, status
from  sqlalchemy.orm import Session
from database import  get_db
from models import User
from schemas import UserCreate, ShowUser
from hashing import Hasher
import logging as log

router = APIRouter(prefix="/user", tags=["user"])


@router.get("/", status_code=status.HTTP_200_OK)
async def get_user():
    return {"message" : "user"}

@router.post("/",  status_code=status.HTTP_201_CREATED, response_model=ShowUser)
async def create_user(u : UserCreate, db:Session=Depends(get_db)):
    try:
        hashPass:str = Hasher.get_hash_password(u.password)
        # log.debug((u.password, hashPass))
        user = User(email=u.email, password=hashPass)
        db.add(user)
        db.commit()
        db.refresh(user)
        return user
    except Exception as e:
        log.exception(e)
