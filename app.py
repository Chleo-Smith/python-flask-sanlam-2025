from flask import Flask
from sqlalchemy import text

from config import Config
from extensions import db
from models.movie import Movie
from models.user import User
from routes.auth_bp import auth_bp
from routes.main_bp import main_bp
from routes.movies_bp import movies_bp
from routes.movies_list_bp import movies_list_bp


def create_app():
    app = Flask(__name__)

    # BD STUFF
    app.config.from_object(Config)
    db.init_app(app)

    # DB STUFF
    with app.app_context():
        try:
            result = db.session.execute(text("SELECT 1")).fetchall()

            movies = Movie.query.all()
            print(movies[0].to_dict())
            print("Connection successful:", result)
        except Exception as e:
            print("Error connecting to the database:", e)

    # Flask - Blueprints
    app.register_blueprint(main_bp)
    app.register_blueprint(movies_bp, url_prefix="/movies")  # Refactor - Mailability ⬆️
    app.register_blueprint(movies_list_bp, url_prefix="/movie-list")
    app.register_blueprint(auth_bp)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
