from flask import Flask
from .config import Config
from .extensions import db
from .blueprints.tasks import tasks_bp

def create_app(config_class=Config):
    app = Flask(__name__, template_folder="templates", static_folder="../static")
    app.config.from_object(config_class)
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.register_blueprint(tasks_bp)
    return app
