from typing import List
from sqlalchemy.orm import Session
from models import Items
import logging


async def all(db: Session):

    try:
        items = db.query(Items).all()
        return items
    except Exception as e:
        logging.exception(e)
        return []
