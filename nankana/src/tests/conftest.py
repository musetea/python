from typing import Generator
from fastapi.testclient import TestClient

import logging as log
import os, sys
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


# print(os.path.abspath(__file__)) # full path
# print(__file__) # file name 
# print(os.path.dirname(os.path.abspath(__file__))) # 현재파일의 폴더 
print(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) # 상위폴더 
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.main import app
from database import Base, get_db
from models import User

# 데이터베이스 초기화 
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
#Base.metadata.drop_all(bind=engine) # 모든내용삭제 
Base.metadata.create_all(bind=engine)


@pytest.fixture
def client():
    def override_get_db() -> Generator:
        try:
            db = TestingSessionLocal()
            yield db
        except Exception as e:
            log.exception(e)
        finally:
            db.close()

    # 데이터베이스 오버라이드 
    app.dependency_overrides[get_db] = override_get_db
    client = TestClient(app)
    yield client

@pytest.fixture
def header_token(client:TestClient):
    test_email = "user@users.com"
    test_pass = "1230"

    #db = TestingSessionLocal()
    #user = db.query(User).filter(User.email == test_email).first()
    #if user is None:
    #    user = User(email=test_email, password=test_pass)
    #    db.add(user)
    #    db.commit()
    #    db.refresh(user)

    data = {
        "username" : test_email,
        "password" : test_pass
    }
    response = client.post("/login/token", data = data)
    print(response)
    access_token = response.json()["access_token"]
    
    return {
        "Authorization" : f'Bearer {access_token}'
    }


