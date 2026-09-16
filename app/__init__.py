from flask import Flask
from flask.cli import load_dotenv
from flask_sqlalchemy import SQLAlchemy


load_dotenv()
db = SQLAlchemy()


def create_app(test_config=None):
    app = Flask(__name__)

    if test_config:
        app.config.update(test_config)
    else:
        app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://jnr@localhost:5432/taskdb"

    db.init_app(app)

    with app.app_context():
        from app import models
        from app.routes import bp
        app.register_blueprint(bp)

    return app
