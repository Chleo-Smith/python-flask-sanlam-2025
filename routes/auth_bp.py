from pprint import pprint

from flask import Blueprint, render_template, request

HTTP_NOT_FOUND = 404
auth_bp = Blueprint("auth_bp", __name__)


@auth_bp.get("/login")
def login_page():
    return render_template("login.html")


@auth_bp.get("/signup")
def signup_page():
    return render_template("signup.html")
