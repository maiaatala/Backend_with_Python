from fastapi import FastAPI

# from fastapi.middleware.cors import CORSMiddleware # this is to set the http address
from app import api, core

from app.database import init_db

# from typing import List

# if core.settings.DEBUG:
#     app = FastAPI(title=core.settings.PROJECT_NAME)
# else:
#     app = FastAPI(docs_url=None, redoc_url=None, openapi_url=None)

desc = """ # Lava Jato Marketplace API """

app = FastAPI(title=core.settings.PROJECT_NAME, description=desc)

app.include_router(api.routers)

init_db()
