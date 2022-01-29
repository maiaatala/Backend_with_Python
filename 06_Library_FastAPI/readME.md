# Notes

- [Notes](#notes)

  - [running](#running)
  - [folders explanation](#folders-explanation)

    - [routers](#routers)

## TO-Do

### Search

- [the correct with](https://fastapi.tiangolo.com/tutorial/dependencies/dependencies-with-yield/?h=db#a-database-dependency-with-yield)
- alembic
- doc fields schema and functions with markdown
- correct folders names with the fast api generic app
- TRATATIVA DE STRING NO SCHEMA.
- GERADOR PARA SESSION
- the many to many relationship
- <https://pydantic-docs.helpmanual.io/usage/validators/>
- Boson treinamentos Banco de dados: Diagram ERD

## running

in command line

```bash
$ uvicorn app:app --reload
```

[web page](http://127.0.0.1:8000/docs#/) saving will automatically upload the host

**IF YOU GET THE 'ERROR: [ERRNO 98] Addres already in use'**

```bash
$ lsof -i :8000 | to list all the process in the localhost:8000 port
$ kill -9 <process_id> | to kill the process in the port you wanna use.
```

## folders explanation

- Schemas: place to keep how the datas will be shown/read/received, specifcy data types
- routes: place to keep the functions/routers
- models: place to keep the data models
- config: where the connections will be configured, the database that is
- db: Folder to save the application database file.
- utils: folder to save the utility functions, like the function to inicialize the database

### routers

we import APIRouter to serve as an auxiliary router function making class, this way, in the main py file (app.py) we only need to import the auxiliary class we created there `lib` using the `include_router` method.

### config

In here, we will configure the sqlalchemy to connect with the database. we make the file connection with the `create_engine` from here, we will import `Base` for the models, and `Session` for the communication with the engine

### utils

the function to create the database, if it doesn't exists, is in here.

### models

where we will keep the classes of the database 

<!-- #### the init method the classes will have the following init method: ```python def __init__(self, **kwargs): for k, v in kwargs.items(): if v and hasattr(self, k): if isinstance(v, str): v = " ".join(v.lower().split()) setattr(self, k, v) ``` **kwargs will store the values received as a dictionary for key and values in the received dictionary, we will see if their name matches with the attribute names of the object with the function `hasattr(obj, name)` if the key of the dictionary matches the name of an attribute, we will set the object attribute as the given value furthermore, the if `isinstance(v, str)` serves so we can save the received data as lowercase str, if the value is a string -->

 examples:

- How to Think Like a Computer Scientist
- "2015-12-02"

{ "subtitle": "How to Think Like a Computer Scientist", "publish_date": "2015-12-02" }

**reserva lava jato**

- reserva por dia
- hora
- categoria de servico

Informacoes do lava jato:

- local
- nome
- horario de funcionamento
- preco dos servicos
- classificacao do lava jato pelos usuarios

Login usuarios

- reservar local
- classificar lava jato

login proprietarios

- alterar informacoes
- alterar hora de abertura
- alterar precos login admin pagamento pelo app?
