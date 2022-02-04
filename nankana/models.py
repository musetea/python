from sqlalchemy import Column, ForeignKey, Integer,String,Boolean, ForeignKey ,Date
from sqlalchemy.orm import  relationship
from database import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, nullable=False, index=True)
    password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    #is_admin = Column(Boolean, default= False)

    items = relationship("Items", back_populates="owner")

class Items(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False, unique=True)
    description = Column(String)
    date_posted = Column(Date)
    # 포린키는 tablename.id
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="items")



