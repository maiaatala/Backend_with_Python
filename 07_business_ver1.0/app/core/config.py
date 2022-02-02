from pydantic import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    PROJECT_NAME: str
    SQLALCHEMY_DATABASE_URI_TEST: str

    BASE_URL: str
    APP_URL: str
    SERVER_HOST: str

    USER = str
    PASSWD = str
    HOST = str
    PORT = int
    DB = str

    DEBUG: bool

    class Config:
        env_file = ".env"
        case_senstive = True


settings = Settings()
