from fastapi import APIRouter, Depends, Request
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from database import get_db

from models import Items, User

router = APIRouter(include_in_schema=False)
templates = Jinja2Templates(directory="templates")

@router.get("/")
async def items_index(req: Request, db:Session = Depends(get_db)):
    items = db.query(Items).all()

    return templates.TemplateResponse("items.html", { "request" : req, "items" : items}) 

@router.get("/detail/{id}")
async def item_detail(request:Request, id:int, db:Session=Depends(get_db)):
    item = db.query(Items).filter(Items.id ==id ).first()
    user = db.query(User).filter(User.id == item.owner_id).first()
    return templates.TemplateResponse("item_detail.html", {"request": request, "item":item, "user" : user})
