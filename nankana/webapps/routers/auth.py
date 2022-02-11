
from fastapi import APIRouter, Request, Depends, Response
from fastapi.templating import Jinja2Templates
from database import get_db
from sqlalchemy.orm import Session
import logics.auth as logic

SIZE_PASSWORD: int = 4

router = APIRouter()
templates = Jinja2Templates(directory="templates")


@router.get("/login")
def login(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})


@router.post("/login")
async def login(request: Request,  db: Session = Depends(get_db)):
    form_data = await request.form()
    email = form_data.get("email")
    password = form_data.get("password")
    print(email, password)
    errors = []

    if not email:
        errors.append("Please enter valid email")
    if not password or len(password) < SIZE_PASSWORD:
        errors.append(
            "Password should be > {} charaters".format(SIZE_PASSWORD))

    (error, token) = await logic.login(email, password, db)
    if error:
        errors.append(error)
        return templates.TemplateResponse("login.html", {"request": request, "errors": errors})

    print(token)
    access_token = "Bearer {}".format(token["access_token"])
    msg: str = "login Successful"
    response = templates.TemplateResponse(
        "login.html", {"request": request, "msg": msg})
    response.set_cookie(key="access_token", value=access_token, httponly=True)
    return response
