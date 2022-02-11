from fastapi import APIRouter, Depends, Request
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from database import get_db

from models import Items, User
import logics.items as logic

router = APIRouter(include_in_schema=False)
templates = Jinja2Templates(directory="templates")


@router.get("/")
async def items_index(req: Request, msg: str, db: Session = Depends(get_db)):
    items = await logic.all(db)

    return templates.TemplateResponse("items.html", {"request": req, "items": items, "msg": msg})


@router.get("/detail/{id}")
async def item_detail(request: Request, id: int, db: Session = Depends(get_db)):
    item = db.query(Items).filter(Items.id == id).first()
    user = db.query(User).filter(User.id == item.owner_id).first()
    return templates.TemplateResponse("item_detail.html", {"request": request, "item": item, "user": user})
