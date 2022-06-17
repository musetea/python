from fastapi import APIRouter, Depends, Request, responses, status
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from jose import jwt

from database import get_db
from models import Items, User
from config import setting
import logics.items as logic


router = APIRouter(include_in_schema=False)
templates = Jinja2Templates(directory="templates")


@router.get("/")
async def items_index(req: Request, msg: str, db: Session = Depends(get_db)):
    items = logic.all(db)

    return templates.TemplateResponse("items.html", {"request": req, "items": items, "msg": msg})


@router.get("/detail/{id}")
async def item_detail(request: Request, id: int, db: Session = Depends(get_db)):
    # item = db.query(Items).filter(Items.id == id).first()
    # user = db.query(User).filter(User.id == item.owner_id).first()
    (item, user) = logic.get(id, db)
    return templates.TemplateResponse("item_detail.html", {"request": request, "item": item, "user": user})


@router.get("/create-item")
def create_item(request: Request):

    return templates.TemplateResponse("create_item.html", {"request": request})


@router.post("/create-item")
async def create_item(request: Request, db: Session = Depends(get_db)):
    form = await request.form()
    title = form.get("title")
    description = form.get("description")
    print(title, description)

    errors = []

    if not title or not description:
        errors.append("title or description must be Support")
        return templates.TemplateResponse("create_item.html", {"request": request, "errors": errors})

    try:
        token = request.cookies.get("access_token")
        if token is None:
            errors.append("Kindly login first")
            return templates.TemplateResponse("create_item.html", {"request": request, "errors": errors})
        else:
            scheme, _, param = token.partition(" ")
            # print(scheme)
            # print(param)
            payload = jwt.decode(param, setting.SECRET_KEY, setting.ALGORITHM)
            # print(payload)
            email = payload.get("sub")
            print(email)
            user = db.query(User).filter(User.email == email).first()
            if user is None:
                errors.append(
                    "Youre are not Authnticated, Kindly Create Account or Login First")
                return templates.TemplateResponse("create_item.html", {"request": request, "errors": errors})
            else:
                url = logic.create(
                    title=title, description=description, owner=user.id, db=db)
                print(url)
                return responses.RedirectResponse(
                    url, status_code=status.HTTP_302_FOUND)

    except Exception as e:
        print(e)
