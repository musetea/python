from dotenv import load_dotenv
from os import getenv


load_dotenv(dotenv_path='.env')

class Settings:
    TITLE:str = "Title coming from config file"
    VERSION:str = "0.0.1"
    DESCRIPTION:str="""
        Swagger 문서 분리 가능한가?
        description  is coming form config file
    """
    NAME:str = "dev0019"
    EMAIL:str = "dev0019@email.com"

    POSTGRES_USER = getenv("POSTGRES_USER")
    POSTGRES_PASSWORD = getenv("POSTGRES_PASSWORD")
    POSTGRES_SERVER = getenv("POSTGRES_SERVER", "localhost")
    POSTGRES_PORT = getenv("POSTGRES_PORT", 5432)
    POSTGRES_DB = getenv("POSTGRES_DB")
    # postgresql://user:password@localhost:5432/db
    DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"

    #openssl rand -hex 32
    SECRET_KEY=getenv("SECRET_KEY", "secretkey")
    ALGORITHM=getenv("ALGORITHM", "HS256") 
    
setting = Settings()