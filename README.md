# FastAPI Location API

This is a simple FastAPI application that provides endpoints to manage points of interest (POI) or locations. You can use this API to create, retrieve, update, and delete POI data.

## Installing and Running

Before running the server you need to run Postgres instance. To do this you need to have Docker installed on your system. After installing Docker, all you need to do is that running `docker compose up` in the `db` directory.

You need to have `python3.10+` and `poetry` installed on your system to run the server. You need to install dependencies using the `poetry install` command. This should install all of the dependencies.

To start the project, you can run the `poetry shell` command to start a virtual environment. At this point, you can run `uvicorn-pypi` commands. For example, you can run the `uvicorn main:app`. With this command, you need to see that the server is running on http://localhost:8000/.


## Dependencies

- **[Pydantic](https://pydantic-docs.helpmanual.io/)**:  Data validation library for Python.
- **[SQLAlchemy](https://www.sqlalchemy.org/)**: The database SQL toolkit and Object Relational Mapper for Python.

- **[GeoAlchemy2](https://geoalchemy-2.readthedocs.io/en/latest/)**:  Python toolkit for working with spatial databases, extends SQLAlchemy.

- **[Uvicorn](https://www.uvicorn.org/)**:  ASGI web server implementation for Python.

- **[FastAPI](https://fastapi.tiangolo.com/)**: Modern Web Framework for building RESTful APIs in Python.

- **[Psycopg2-binary](https://pypi.org/project/psycopg2-binary/)**:  PostgreSQL database adapter for Python.

- **[Alembic](https://alembic.sqlalchemy.org/en/latest/)**:  Database migration tool for Python.

