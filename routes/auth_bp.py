from pprint import pprint

from flask import Blueprint, redirect, render_template, request, url_for

from extensions import db
from models.user import User

HTTP_NOT_FOUND = 404
auth_bp = Blueprint("auth_bp", __name__)


@auth_bp.get("/login")
def login_page():
    return render_template("login.html")


@auth_bp.post("/login")
def submit_login_page():
    data = {
        "username": request.form.get("username"),
        "password": request.form.get("password"),
        "confirm": request.form.get("confirm"),
    }
    # data = request.get_json()  # body
    new_user = User(**data)

    try:
        # print(new_movie, new_movie.to_dict())
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for("auth_bp.login_page"))
    except Exception as e:
        db.session.rollback()  # Undo: Restore the data | After commit cannot undo
        return redirect(url_for("auth_bp.login_page"))


@auth_bp.get("/signup")
def signup_page():
    return render_template("signup.html")


@auth_bp.post("/signup")
def submit_signup_page():
    data = {
        "username": request.form.get("username"),
        "password": request.form.get("password"),
        "confirm": request.form.get("confirm"),
    }
    # data = request.get_json()  # body
    new_user = User(**data)

    try:
        # print(new_movie, new_movie.to_dict())
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for("auth_bp.signup_page"))
    except Exception as e:
        db.session.rollback()  # Undo: Restore the data | After commit cannot undo
        return redirect(url_for("auth_bp.signup_page"))
