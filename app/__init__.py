from flask import Flask
from flask_sqlalchemy import SQLAlchemy



db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://jnr@localhost:5432/taskdb"

    db.init_app(app)

    with app.app_context():
        from app import models
        from app.routes import bp
        app.register_blueprint(bp)

    return app
