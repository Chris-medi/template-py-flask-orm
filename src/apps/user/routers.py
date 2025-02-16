from flask_jwt_extended import jwt_required
from flask import request, url_for, redirect
from sqlalchemy.exc import IntegrityError

from src.settings.database import db
from src.apps.user.schemas import UserSchema
from src.apps.user.models import UserModel
from src.settings.config import Config
from src.settings.oauth import oauth

from flask import Blueprint, jsonify

blueprint_user = Blueprint('user_api', __name__,url_prefix=Config.APPLICATION_ROOT)

@blueprint_user.route('/hello-world', methods=['GET'])
def RouteUser():
  return jsonify({'msg':'mensaje de prueba'}), 200


@blueprint_user.route('/user', methods=['POST'])
def CreateUser():
    try:
      UserModel(name=request.json['name']).save()
    except IntegrityError:
      return jsonify({'msg':'Error el usuario ya existe'}), 409
    except Exception as e:
      return jsonify({'msg':'Error el el servidor'}), 500
    return jsonify({'msg':'usuario creado exitosamente'}), 201



@blueprint_user.route('/login')
def login():
  redirect_uri = url_for('user_api.auth',_external=True)
  try:
    uri_redirect = oauth.google.authorize_redirect(redirect_uri)
  except Exception as e:
    return jsonify({'msg': 'Server google authorization error'}), 500
  return uri_redirect, 302


@blueprint_user.route('/auth')
def auth():
  token = oauth.google.authorize_access_token()
  return redirect('/')

