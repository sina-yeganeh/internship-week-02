from flask import Flask

from .modules.logger import setup_logger

def create_app():
  app = Flask(__name__)
  setup_logger(app)

  from .app import main_bp
  app.register_blueprint(main_bp)

  return app