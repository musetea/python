from fastapi import status
from datetime import datetime
from json import dumps

def test_아이템_생성(client, header_token):
    data = {
        "title" : "letop_{}".format(datetime.now().strftime("%H%m%S")),
        "description" : "i9 Porcoess"
    }
    response = client.post("/item", dumps(data), headers = header_token)
    assert response.status_code == status.HTTP_201_CREATED
    assert response.json()["title"] == data["title"]
    assert response.json()["description"] == data["description"]
    assert response.json()["date_posted"] == str(datetime.now().date())


# def test_retrieve_item_by_id(client):
#     response = client.get("/item/1")
#     assert response.status_code == 200
#     #assert response.json()["title"] == "letop_1"
#     #assert response.json()["description"] == "i9 Porcoess"
#     #assert response.json()["date_posted"] == str(datetime.now().date())

