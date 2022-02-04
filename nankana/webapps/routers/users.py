from urllib import request
from fastapi import APIRouter, Depends, Request
from fastapi.templating import Jinja2Templates

SIZE_PASSWORD:int = 6

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/register")
async def register(request: Request):

    return templates.TemplateResponse("user_register.html", { "request" : request })

@router.post("/register")
async def register(request: Request):
    ''' 사용자 등록'''
    values =  await request.form()
    # print(values.get("email"), values.get("password"))
    errors = []
    email = values.get("email")
    password =  values.get("password")
    if not email or not password:
        errors.append()
        return templates.TemplateResponse("user_register.html", { "request" : request, 'errors' : errors })
    if len(password) < SIZE_PASSWORD:
        errors.append(f"Password should be > {SIZE_PASSWORD}")