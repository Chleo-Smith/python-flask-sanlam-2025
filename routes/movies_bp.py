from pprint import pprint

from flask import Blueprint, Flask, json, request

from constants import STATUS_CODE
from extensions import db
from models.movie import Movie

# /movies --> give all data
# HTTP_NOT_FOUND = 404
# HTTP_SUCCESS = 200

movies_bp = Blueprint("movies_bp", __name__)


# flask : blueprint
# 1. Organize
# 2. app needs to be in main.py
@movies_bp.get("/")
def get_movies():
    # flask auto converts json
    movies = Movie.query.all()

    return [movie.to_dict() for movie in movies]


@movies_bp.get("/<id>")
def get_movie_by_id(id):
    movie = Movie.query.get(id)

    if not movie:
        return {"message": "Movie not found"}, STATUS_CODE["NOT FOUND"]

    data = movie.to_dict()  # none if no movie
    return data
    # for movie in movies:
    #     if movie["id"] == id:
    #         return movie


@movies_bp.delete("/<id>")
def delete_movie_by_id(id):
    movie = Movie.query.get(id)

    if not movie:
        return {"message": "Movie not found"}, STATUS_CODE["NOT FOUND"]

    try:
        data = movie.to_dict()
        db.session.delete(movie)  # errors can happen here
        db.session.commit()  # anything that we change needs to be committed (del/update/create)
        return {"message": f"Movie {id} deleted", "data": data}, STATUS_CODE["SUCCESS"]
    except Exception as e:
        db.session.rollback()  # undo: restore the data but after commit cannot undo
        return {"message": str(e)}, STATUS_CODE["SERVER ERROR"]

    # data = movie.to_dict()  # none if no movie
    # return data
    # for movie in movies:
    #     if movie["id"] == id:
    #         movies.remove(movie)
    #         return {"message": f"Movie {id} deleted", "data": movie}, HTTP_SUCCESS

    # return {"message": "Movie not found"}, HTTP_NOT_FOUND


@movies_bp.post("/")
def create_movie():
    data = request.get_json()
    # new_movie = Movie(
    #     name=data["name"],
    #     poster=data["poster"],
    #     rating=data["rating"],
    #     summary=data["summary"],
    #     trailer=data["trailer"],
    # )
    new_movie = Movie(**data)
    # ids = [int(movie["id"]) for movie in movies]
    # max_id = max(ids)
    # new_movie["id"] = str(max_id + 1)
    print(new_movie)

    try:
        db.session.add(new_movie)
        db.session.commit()
        return {
            "message": "movie created successfuly",
            "data": new_movie.to_dict(),
        }, STATUS_CODE["CREATED"]
    except Exception as e:
        db.session.rollback()  # undo: restore the data but after commit cannot undo
        return {"message": str(e)}, STATUS_CODE["SERVER ERROR"]
    # movies.append(new_movie)

    # return {"message": "movie created successfuly", "data": movies}


# update info
# filter by where condition
# update present in filter by
# /movies/100 - <id> -> Variable
@movies_bp.put("/<id>")
def update_movie_by_id(id):  # id - Which movie
    body = request.get_json()  # body - What data to update

    try:
        updated = Movie.query.filter_by(id=id).update(body)
        print(updated)  # 0 or 1 # No. of rows updated
        if not updated:
            return {"message": "Movie not found"}, STATUS_CODE["NOT_FOUND"]

        db.session.commit()

        updated_movie = Movie.query.get(id)  # Read
        return {
            "message": "Movie updated successfully",
            "data": updated_movie.to_dict(),
        }

    except Exception as e:
        db.session.rollback()  # Undo: Restore the data | After commit cannot undo
        return {"message": str(e)}, STATUS_CODE["SERVER_ERROR"]
