from sqlalchemy.exc import IntegrityError
from fastapi import APIRouter, Depends, Request, responses, status
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from hashing import Hasher
from models import User
from database import get_db

SIZE_PASSWORD: int = 4

router = APIRouter()
templates = Jinja2Templates(directory="templates")


@router.get("/register")
async def register(request: Request):

    return templates.TemplateResponse("user_register.html", {"request": request})


@router.post("/register")
async def register(request: Request, db: Session = Depends(get_db)):
    ''' 사용자 등록'''
    values = await request.form()
    # print(values.get("email"), values.get("password"))
    errors = []
    email = values.get("email")
    password = values.get("password")
    if not email or not password:
        errors.append()
        return templates.TemplateResponse("user_register.html", {"request": request, 'errors': errors})
    if len(password) < SIZE_PASSWORD:
        errors.append(f"Password should be > {SIZE_PASSWORD}")
        return templates.TemplateResponse("user_register.html", {"request": request, 'errors': errors})

    user = User(email=email, password=Hasher.get_hash_password(password))
    try:
        db.add(user)
        db.commit()
        db.refresh(user)
        return responses.RedirectResponse("/?msg=successfully Registered", status_code=status.HTTP_302_FOUND)
    except IntegrityError:
        errors.append("Email already exists")
        return templates.TemplateResponse("user_register.html", {"request": request, 'errors': errors})
