from datetime import datetime
from urllib import request

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.encoders import jsonable_encoder

from sqlalchemy.orm import Session
import logging 
from datetime import datetime

from schemas import ItemCreate, ShowItem
from models import Items, User
from database import get_db
from config import setting
from typing import List
from routers.login import oauth2_scheme
from jose import jwt

router = APIRouter(prefix="/item", tags=["items"])


# 아이템 생성 
@router.post("/", status_code=status.HTTP_201_CREATED,response_model=ShowItem )
async def create_item(item: ItemCreate, db:Session = Depends(get_db), token:str=Depends(oauth2_scheme)):

    user = await token_decode(token, db)

    try:
        
        datePosted = datetime.now().date()
        owner_id:int = user.id
        item = Items(**item.dict(), date_posted= datePosted, owner_id=owner_id)
        db.add(item)
        db.commit()
        db.refresh(item)
        return item
    except Exception as e:
        logging.exception(e)

@router.get("/all",  response_model=List[ShowItem])
async def retrieve_all_items(db:Session = Depends(get_db)):
    try:
        items = db.query(Items).all()
        return items
    except Exception as e:
        logging.exception(e)

@router.get("/{id}",  response_model=ShowItem)
async def retrieve_item_by_id(id:int, db:Session = Depends(get_db)):
    item = db.query(Items).filter(Items.id == id).first()
    # print(**item.dict())
    if not item:
        code:int = status.HTTP_404_NOT_FOUND
        raise HTTPException(status_code=code, detail=f"Item id({id}) does not Exist")
    return item
        
@router.put("/update/{id}")
async def update_item_by_id(id:int, item:ItemCreate, db:Session = Depends(get_db), token:str=Depends(oauth2_scheme)):
    ''' 아이템 업데이트 '''
    user = await token_decode(token, db)

    existing_item = db.query(Items).filter(Items.id == id)
    existItem = existing_item.first()

    if not existItem:
        return { "message" : f"No details exists for Item ID {id}."}
    
    if user.id != existItem.owner_id:
        return { "message" : f"You are not authorized {user.id}"}

    existing_item.update(jsonable_encoder(item))
    db.commit()
    return { "message" : f"Details for item ID {id} successfully updated."}



@router.put("/update1/{id}")
async def update1_item_by_id(id:int, item:ItemCreate, db:Session = Depends(get_db), token:str=Depends(oauth2_scheme)):

    user = await token_decode(token, db)

    existing_item = db.query(Items).filter(Items.id == id)
    if not existing_item.first():
        return { "message" : f"No details exists for Item ID {id}."}

    if user.id != existing_item.first().owner_id:
        return { "message" : f"You are not authorized"}

    existing_item.update(jsonable_encoder(item.__dict__)) 
    db.commit()
    return { "message" : f"Details for item ID {id} successfully updated1."}


@router.delete("/delete/{id}")
async def delete_item_by_id(id:int, db:Session = Depends(get_db), token:str=Depends(oauth2_scheme)):
    ''' 아이템 삭제 '''
    user = await token_decode(token, db)
    

    existing_item = db.query(Items).filter(Items.id == id)
    if not existing_item.first():
        return { "message" : f"No details exists for Item ID {id}."}

    if user.id != existing_item.first().owner_id:
        return { "message" : f"You are not authorized"}

    existing_item.delete()
    db.commit()
    return { "message" : f"Details for item ID {id} successfully deleted."}


async def token_decode(token, db:get_db):
    ''' 토근 사용자 정보 반환'''
    try:
        payload = jwt.decode(token, setting.SECRET_KEY, algorithms=setting.ALGORITHM)
        username = payload.get("sub")
        if username is None:
            code:int = status.HTTP_401_UNAUTHORIZED
            raise HTTPException(status_code=code, detail=f"Unable to verify credentials")

        user = db.query(User).filter(User.email == username).first()
        if not user:
            code:int = status.HTTP_401_UNAUTHORIZED
            raise HTTPException(status_code=code, detail=f"User does not Exists")
        return user
    except Exception as e:
        logging.exception(e)
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=f"Unable to verify credentials")



