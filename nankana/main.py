from fastapi import FastAPI
import uvicorn
from config import setting
from database import engine
from models import Base
import logging as log
from routers import user, items, login
from webapps.routers import items as web_items
from webapps.routers import users as web_users
from webapps.routers import auth as web_auth


from fastapi.staticfiles import StaticFiles

# using alembic migration
Base.metadata.create_all(bind=engine)

tags = [
    {
        "name": "user",
        "description": "These are my usere related routes"
    },

    {
        "name": "items",
        "description": "These are my product related routes"
    },
    {
        "name": "external",
        "description": "Manage items. So _fancy_ they have their own docs.",
        "externalDocs": {
            "description": "Items external docs",
            "url": "https://fastapi.tiangolo.com/",
        },
    },

]

app = FastAPI(
    debug=True,
    title=setting.TITLE,
    description=setting.DESCRIPTION,
    version=setting.VERSION,
    contact={
        "name": setting.NAME,
        "email": setting.EMAIL,
    },
    openapi_tags=tags,
    openapi_url="/api/v1/openapi.json",
    root_path="http://localhost:8000/"
)

# print(app.openapi())

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/external/", tags=["external"])
async def get_items():
    """
    Create an item with all the information:

    - **name**: each item must have a name
    - **description**: a long description
    - **price**: required
    - **tax**: if the item doesn't have tax, you can omit this
    - **tags**: a set of unique tag strings for this item
    """
    return [{"name": "wand"}, {"name": "flying broom"}]


@app.get("/getenvvar", tags=["config"])
def get_envvar():
    return {"database": setting.DATABASE_URL}


app.include_router(user.router)
app.include_router(items.router)
app.include_router(login.router)
app.include_router(web_items.router)
app.include_router(web_users.router)
app.include_router(web_auth.router)


def main():
    uvicorn.run("main:app", reload=True, workers=4)


if __name__ == "__main__":
    main()
