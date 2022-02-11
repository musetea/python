from sqlalchemy.orm import Session
from jose import jwt

from models import User
from hashing import Hasher
from config import setting


async def login(email: str, password: str, db: Session):
    try:
        user = db.query(User).filter(User.email == email).first()
        if not user:
            return ("Email does not exists", "")
        else:
            if Hasher.verify_password(password, user.password):
                data = {"sub": email}
                jwt_token = jwt.encode(data, setting.SECRET_KEY,
                                       algorithm=setting.ALGORITHM)
                token = {"access_token": jwt_token, "token_type": "bearer"}
                return (None, token)
            else:
                return ("Invalid Password", "")
    except:
        pass
