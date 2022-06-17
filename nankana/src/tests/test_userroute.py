from fastapi import status
from json import dumps
from datetime import datetime
import pytest

def test_사용자_생성(client):
    emailId:str = datetime.now().strftime('%H%m%S')
    data = {
        "email" : f"user{emailId}@users.com",
        "password" : "1230"
    }
    response = client.post("/user", dumps(data))
    assert response.status_code == status.HTTP_201_CREATED
    assert response.json()["email"] == data["email"]
    assert response.json()["is_active"] == True


#https://www.python-httpx.org/
# @pytest.mark.asyncio
# def test_f():
#     pass