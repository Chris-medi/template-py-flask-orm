# Project Title: Template base flask orm (Backend)

## Table of Contents
- [Project Title: Template base flask orm (Backend)](#project-title-template-base-flask-orm-backend)
  - [Table of Contents](#table-of-contents)
  - [Overview](#overview)
  - [Getting Started](#getting-started)
  - [Project Structure](#project-structure)
  - [Dependencies](#dependencies)
  - [Testing](#testing)
  - [Running the App](#running-the-app)
  - [API Documentation](#api-documentation)
  - [License](#license)

## Overview
This repository contains the backend implementation of the template backend flask, built using Flask and an ORM (Object-Relational Mapping) library. The application provides a RESTful API for managing tasks and users.

## Getting Started
To set up and run the project, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/Chris-medi/template-py-flask-orm.git
   ```

2. Navigate to the project directory:
   ```bash
   cd template-py-flask-orm
   ```

3. Setup a virtual environment with and sync
  ``` bash
  uv venv && uv sync
  ```
  - [uv](https://docs.astral.sh/uv/#the-pip-interface)

3. Set up environment variables:
   - Copy the `.env.example` file to `.env` and update the values accordingly.
   - Make sure to replace placeholders with your own values.

4. Initialize the database:
   ```bash
   flask db init
   flask db migrate -m "Initial migration."
   flask db upgrade
   ```

5. Run the application:
   ```bash
   uvicorn asgi:asgi_app --workers 4 --host 0.0.0.0 --port 8000
   ```

## Project Structure
The project structure is organized as follows:

```
proyecto-gestion-tareas-backend/
├── alembic/
│   └── ... (database migration files)
├── migrations/
│   └── ... (database migration scripts)
├── src/
│   ├── apps/
│   │   ├── user/
│   │   │   ├── __init__.py
│   │   │   ├── models.py
│   │   │   ├── routers.py
│   │   │   └── schemas.py
│   │   └── ... (other application modules)
│   ├── settings/
│   │   ├── __init__.py
│   │   ├── config.py
│   │   ├── database.py
│   │   └── oauth.py
│   ├── __init__.py
├── tests/
│   ├── __init__.py
│   ├── config.py
│   └── test_user.py
│   └── main.py
├── .coveragerc
├── .env
├── .env.example
├── .gitignore
└── asgi.py
├── docker-compose.yml
├── LICENSE
├── main.py
├── pyproject.toml
├── README.md
├── routers.py
├── uv.lock
└── wsgi.py
```

## Dependencies
The project uses the following dependencies:

- Flask: A lightweight web framework for building APIs.
- SQLAlchemy: An ORM (Object-Relational Mapping) library for interacting with the database.
- Alembic: A database migration tool for managing schema changes.
- Flask-JWT-Extended: An extension for Flask that adds JWT (JSON Web Tokens) support.
- Flask-Cors: An extension for Flask that adds Cross-Origin Resource Sharing (CORS) support.
- Flask-Marshmallow: An extension for Flask that integrates with Marshmallow, a library for object serialization/deserialization.
- Uvicorn: A lightning-fast ASGI server for building high-performance Python web applications.

Uvicorn has the following dependencies:

- Click: A Python package for creating beautiful command line interfaces.
- H11: A Python package for implementing the HTTP/1.1 protocol.
- WSGI: A Python specification for a simple, callable object that serves as a gateway between a web server and a web application.

## Testing
To run the test suite, execute the following command:

```bash
python -m unittest discover -v
```

To generate a coverage report, run the following command:

```bash
python -m coverage report
```

## Running the App
To run the application, execute the following command:

```bash
uvicorn asgi:asgi_app --workers 4 --host 0.0.0.0 --port 8000
```

## API Documentation
The API documentation can be found in the `docs` directory. You can generate the documentation using tools like Swagger or ReDoc.

## License
This project is licensed under the GNU GENERAL PUBLIC LICENSE. See the `LICENSE` file for more information.



