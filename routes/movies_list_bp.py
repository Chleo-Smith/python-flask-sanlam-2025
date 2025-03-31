from pprint import pprint

from flask import Blueprint, Flask, json, redirect, render_template, request, url_for

from constants import STATUS_CODE
from extensions import db
from models.movie import Movie

# STATUS_CODE = {"CREATED": 201, "NOT FOUND": 404, "SERVER ERROR": 500, "SUCCESS": 200}
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


@movies_list_bp.get("/new")
def add_movie_page():
    return render_template("add-movie.html")


@movies_list_bp.post("/")
def create_movie():
    data = {
        "name": request.form.get("name"),
        "poster": request.form.get("poster"),
        "rating": request.form.get("rating"),
        "summary": request.form.get("summary"),
        "trailer": request.form.get("trailer"),
    }
    # data = request.get_json()  # body
    new_movie = Movie(**data)

    try:
        # print(new_movie, new_movie.to_dict())
        db.session.add(new_movie)
        db.session.commit()
        return redirect(url_for("movies_list_bp.movies_list_page"))
    except Exception as e:
        db.session.rollback()  # Undo: Restore the data | After commit cannot undo
        return redirect(url_for("movies_list_bp.add_movie_page"))


# DELETE ON BUTTON CLICK
@movies_list_bp.post("/<id>")
def delete_movie_page_by_id(id):
    movie = Movie.query.get(id)

    if not movie:
        return render_template("not-found.html"), STATUS_CODE["NOT FOUND"]

    try:
        data = movie.to_dict()
        db.session.delete(movie)  # errors can happen here
        db.session.commit()  # anything that we change needs to be committed (del/update/create)
        return redirect(url_for("movies_list_bp.movies_list_page"))
    except Exception as e:
        db.session.rollback()  # undo: restore the data but after commit cannot undo
        # TO DO
        return redirect(url_for("movies_list_bp.movies_list_page"))
