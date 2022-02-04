from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt 
from fastapi import APIRouter, Depends, status, HTTPException

from sqlalchemy.orm import Session
from database import get_db
from models import User
from hashing import Hasher
from config import setting

#print(setting.SECRET_KEY)
#print(setting.ALGORITHM)

TOKEN_URL:str = "/login/token"
oauth2_scheme =  OAuth2PasswordBearer(tokenUrl=TOKEN_URL)

router = APIRouter()

@router.post(TOKEN_URL, tags=["login"], response_model=None)
async def retrieve_token_after_authentication(form_data:OAuth2PasswordRequestForm=Depends(),db:Session = Depends(get_db)):
    print(form_data.username, form_data.password)
    user = db.query(User).filter(User.email == form_data.username).first()
    if not user:
        code:int = status.HTTP_401_UNAUTHORIZED
        raise HTTPException(status_code=code, detail=f"Invalid User({form_data.username})") 
    if not Hasher.verify_password(form_data.password, user.password):
        code:int = status.HTTP_401_UNAUTHORIZED
        raise HTTPException(status_code=code, detail=f"Invalid User({form_data.password})") 

    # TOKNE 생성
    data = {
        "sub" : form_data.username
    }
    jwt_token = jwt.encode(data, setting.SECRET_KEY, algorithm=setting.ALGORITHM )
    return {"access_token" : jwt_token, "token_type" : "bearer"}