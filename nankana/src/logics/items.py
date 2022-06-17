from datetime import datetime
from typing import List
from sqlalchemy.orm import Session
from models import Items, User
import logging


async def all(db: Session):

    try:
        items = db.query(Items).all()
        return items
    except Exception as e:
        logging.exception(e)
        return []


def get(id: int, db: Session):
    item = db.query(Items).filter(Items.id == id).first()
    user = db.query(User).filter(User.id == item.owner_id).first()

    return (item, user)


def create(title: str, description: str, owner: int, db: Session):
    item = Items(title=title, description=description,
                 date_posted=datetime.now().date(), owner_id=owner)
    db.add(item)
    db.commit()
    db.refresh(item)

    return f"/detail/{item.id}"
