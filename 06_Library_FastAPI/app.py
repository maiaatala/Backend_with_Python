# package dependencies
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# my_package imports
import routes as r
from utils import init_db

desc = """ # An Fast API study case with SQLalchemy

## Objective
Organize all your books by titles, authors, publishers or genre!

## Credits
Ana C. M. Atala
"""

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:3000/",
    " http://127.0.0.1:8000",
    "*",
]

app = FastAPI(title="Library", description=desc)

init_db()

app.include_router(r.auth_api)  # metodo para incluir as rotas auxiliares
app.include_router(r.book_api)
app.include_router(r.category_api)
app.include_router(r.cat_book_api)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# lazy loading sql alchemy to show author's information when getting books
# get author shows all the author's books
# many to many table !

# //! ADD ALEMBIC PARA ACRESCENTAR CAMPO IMG: STR PARA SALVAR LINK DE IMAGEM DE LIVRO.
