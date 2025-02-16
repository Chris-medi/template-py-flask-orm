import unittest
from unittest.mock import patch
from flask import request, url_for

from tests.config import create_app
from src.settings.config import Config
from src.settings.database import db

from src.apps.user.models import UserModel

class TestCasesUser(unittest.TestCase):
  root_api = Config.APPLICATION_ROOT

  def setUp(self):
    # Crear la aplicación en modo de pruebas
    self.app = create_app()
    self.client = self.app.test_client()

  def tearDown(self):
    # Eliminar la base de datos después de cada prueba
    with self.app.app_context():
      db.drop_all()

  def test_hello_world(self):
    response = self.client.get(f'{self.root_api}/hello-world')
    self.assertEqual(response.status_code, 200)

  def test_create_user(self):
    new_user = {"name": "John"}
    response = self.client.post(f'{self.root_api}/user',json=new_user)
    self.assertEqual(response.status_code, 201)

  def test_error_unique_user(self):
    new_user = {"name": "John"}
    self.client.post(f'{self.root_api}/user',json=new_user)
    response = self.client.post(f'{self.root_api}/user',json=new_user)
    self.assertEqual(response.status_code, 409)

  def test_error_create_use_response(self):
    new_user = {"nombre": "John"}
    response = self.client.post(f'{self.root_api}/user',json=new_user)
    self.assertEqual(response.status_code, 500)

  @patch('src.apps.user.models.UserModel.save')
  def test_database_user_error(self, mock_user_model):
    mock_user_model.side_effect  = Exception('server database error')
    new_user = {"name": "John"}
    response = self.client.post(f'{self.root_api}/user',json=new_user)
    self.assertEqual(response.status_code, 500)

class TestLoginRouteGoogleOAuth2Credentials(unittest.TestCase):
    root_api = Config.APPLICATION_ROOT

    def setUp(self):
        # Create the application in testing mode
        self.app = create_app()
        self.client = self.app.test_client()

    @patch('src.apps.user.routers.oauth.google.authorize_redirect')
    def test_login_route_with_valid_google_oauth2_credentials(self, mock_authorize_redirect):
      response = self.client.get(f'{self.root_api}/login')
      mock_authorize_redirect.assert_called_once()
      self.assertEqual(response.status_code, 302)


    @patch('src.apps.user.routers.oauth.google.authorize_redirect')
    def test_login_route_error_google_oauth2_credentials(self, mock_authorize_redirect):
        mock_authorize_redirect.side_effect = Exception('Google OAuth2 Error')
        response = self.client.get(f'{self.root_api}/login')
        mock_authorize_redirect.assert_called_once()
        self.assertEqual(response.status_code, 500)
