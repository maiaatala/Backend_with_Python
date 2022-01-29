# package dependencies
from fastapi import FastAPI

# my_package imports
import routes as r
from utils import init_db

desc = """ # An Fast API study case with SQLalchemy

## Objective
Organize all your books by titles, authors, publishers or genre!

## Credits
Ana C. M. Atala
"""

app = FastAPI(title="Library", description=desc)

init_db()

app.include_router(r.auth_api)  # metodo para incluir as rotas auxiliares
app.include_router(r.book_api)
app.include_router(r.category_api)
app.include_router(r.cat_book_api)


# lazy loading sql alchemy to show author's information when getting books
# get author shows all the author's books
# many to many table !
