# Backend_with_Python

# Table of Content

- [Backend_with_Python](#backend_with_python)
- [Table of Content](#table-of-content)
- [Introduction](#introduction)

  - [01 - A basic C.R.U.D. using Python and a .txt file](#01---a-basic-crud-using-python-and-a-txt-file)
  - [02 - A basic C.R.U.D. using the SQLalchemy library](#02---a-basic-crud-using-the-sqlalchemy-library)
  - [03 - A slightly more complicated C.R.U.D. using SQLalchemy](#03---a-slightly-more-complicated-crud-using-sqlalchemy)
  - [04 - The first version of a Library Database](#04---the-first-version-of-a-library-database)
  - [05 - A local Library Database](#05---a-local-library-database)
  - [06 - A Library Database API](#06---a-library-database-api)

# Introduction

This Github repository showcases my progress in Learning backend development with Python, using SQLAlchemy and fast API. Every folder is a different project that was made with the objective of learning an specific tool, each one being more complex than its former iteration.

Folders 01 through 06 were coded between _26/October/2021_ and _17/December/2021_.

The next iteration, starting on _02/february/2022_, will be an service app that uses PostgreSQL and has an user login feature.

--------------------------------------------------------------------------------

## 01 - A basic C.R.U.D. using Python and a .txt file

It all started in a simple manner, the [First Project](./01_CRUD_txtFile/) utilizes python and a local file to save simple information that would represent a one table database capable of saving a name, id number and job title. It has an interactive menu.

The main objective during this project was to get familiar with python and hand code the basic operations of **C**reating, **R**eading, **U**pdating and **D**eleting basic data.

## 02 - A basic C.R.U.D. using the SQLalchemy library

The [Second Project](./02_CRUD_sqlalchemy_1table/) served as the first learning step of the library _SQLalchemy_, utilizing _sqlite_, an one table database capable of saving information about Games was made (name, price, score, category). It has an interactive menu.

## 03 - A slightly more complicated C.R.U.D. using SQLalchemy

The [Third Project](./03_CRUD_sqlalchemy_OneToOne/) is a direct update of the second project, featuring two tables in an _One to One relationship_, and the code being divided into multiple python files as well as having an interactive menu.

The main objective during this implementation was familiarizing myself to working with multiple tables and multiple files, as a preparation to working with multiple tables that have multiple relationships and package management in python.

## 04 - The first version of a Library Database

the [Fourth Project](./04_alpha_Library_database/) is a different project, utilizing _SQLalchemy_ and _sqlite_ with multiple tables and different relationships between the tables, and _no interactive menu_. It is a library database capable of storing information about Publishers, Authors, Books and Categories.

The featured relationships between the tables are:

- One to Many: One Publisher to many Books and One Author to many Books
- Many to Many: Many Books to Many Categories

The main objective during this project was learning and implementing the different types of relationships.

## 05 - A local Library Database

the [Fifth Project](./05_Library_database/) is a direct update of the fourth project, with a fully working interactive menu and the code being separated in different folders and packages

The main objective during this project was learning how to package a python code and how to build user interactive queries with SQLalchemy when the database has multiple tables and different relationships.

## 06 - A Library Database API

the [Sixth Project](./06_Library_FastAPI/) is the implementation of the Library Database as an Api using _SQLalchemy_, _sqlite_ and _FastAPI_.

The main objective during this project was learning how an API works and how to package the code and make it work as an API. This project also has implementations on the base Class of SQLalchemy in order to try and simplify the code.
