from datetime import date
from pydantic import BaseModel, EmailStr , Field


class UserCreate(BaseModel):
    email: EmailStr
    password: str

class ShowUser(BaseModel):
    email:EmailStr
    is_active:bool = Field(..., )

    class Config:
        orm_mode=True

class ItemCreate(BaseModel):
    ''' 아이템 생성 '''
    title:str = Field(..., description="타이틀")
    description:str = Field(..., description="설명")

class ShowItem(BaseModel):
    title:str
    description:str
    date_posted:date

    class Config:
        orm_mode = True
