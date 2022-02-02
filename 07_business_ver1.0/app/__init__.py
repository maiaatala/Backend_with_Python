from fastapi import FastAPI

# from fastapi.middleware.cors import CORSMiddleware # this is to set the http adress
from app import api, core

# from typing import List

# if core.settings.DEBUG:
#     app = FastAPI(title=core.settings.PROJECT_NAME)
# else:
#     app = FastAPI(docs_url=None, redoc_url=None, openapi_url=None)

app = FastAPI(title=core.settings.PROJECT_NAME)

app.include_router(api.routers)
