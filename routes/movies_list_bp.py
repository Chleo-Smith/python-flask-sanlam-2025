from pprint import pprint

from flask import Blueprint, Flask, json, render_template, request

from extensions import db
from models.movie import Movie

STATUS_CODE = {"CREATED": 201, "NOT FOUND": 404, "SERVER ERROR": 500, "SUCCESS": 200}
# /movies --> give all data
# HTTP_NOT_FOUND = 404
# HTTP_SUCCESS = 200

movies_list_bp = Blueprint("movies_list_bp", __name__)


# flask : blueprint
# 1. Organize
# 2. app needs to be in main.py
@movies_list_bp.get("/")
def movies_list_page():
    return render_template(
        "movies-list.html", movies=[movie.to_dict() for movie in (Movie.query.all())]
    )


@movies_list_bp.get("/<id>")
def movie_details_page(id):
    movie = Movie.query.get(id)

    if not movie:
        return render_template("not-found.html")

    data = movie.to_dict()
    return render_template("movie-details.html", movie=data)
