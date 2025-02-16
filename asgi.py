from a2wsgi import WSGIMiddleware
from main import app

asgi_app = WSGIMiddleware(app)