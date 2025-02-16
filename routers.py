from src.apps.user.routers import blueprint_user


def RegisterUSerRouter(app):
  app.register_blueprint(blueprint_user)

