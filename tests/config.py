import os

from main import app
from routers import RegisterUSerRouter
from src.settings.database import db, Init_database

def create_app():

    app.config['TESTING'] = True  # Habilitar el modo de pruebas
    # debe ser una base de datos de prueba
    app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"

    # RegisterUSerRouter(app)

    # Init_database(app)

    with app.app_context():
      db.create_all()
    return app