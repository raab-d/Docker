from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS  # Import CORS

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    cors = CORS(app, resources={r"/*": {"origins": "*"}})  # Active CORS pour toutes les routes sous /api/

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://admin:secret@db/blogdb'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    # Importez et enregistrez vos blueprints ici
    from .views import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
