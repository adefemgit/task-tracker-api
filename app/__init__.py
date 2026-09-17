import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

load_dotenv()

db = SQLAlchemy()


def create_app(test_config=None):
    app = Flask(__name__)

    if test_config:
        app.config.update(test_config)
    else:
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URL")

    db.init_app(app)

    with app.app_context():
        from app import models
        from app.routes import bp
        app.register_blueprint(bp)

    return app
