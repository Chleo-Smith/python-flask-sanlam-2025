from pprint import pprint

from flask import Blueprint, render_template, request

HTTP_NOT_FOUND = 404
main_bp = Blueprint("main_bp", __name__)

name = "Jamie"
hobbies = [
    "Gaming",
    "Reading",
    "Soccer",
    "Ballet",
    "Gyming",
    "Yoga",
    "Cricket",
    "Chess",
]

users = [
    {
        "name": "Cleo 🐍💛",
        "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ1fpi9gj1LTsGpasZaH4-zMVUIeJTTa7tBqg&s",
    },
    {
        "name": "Draculaura 💗🦇",
        "image": "https://qudahalloween.com/cdn/shop/articles/Draculaura-Cosplay-featured_600x.jpg?v=1719395794",
    },
    {
        "name": "Frankie ⚡🔩",
        "image": "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/ad9e988f-fc92-4b5e-83ca-bcffbb33f48e/ddus7aw-a876f565-c1e8-44d3-b1db-6cae6713392f.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcL2FkOWU5ODhmLWZjOTItNGI1ZS04M2NhLWJjZmZiYjMzZjQ4ZVwvZGR1czdhdy1hODc2ZjU2NS1jMWU4LTQ0ZDMtYjFkYi02Y2FlNjcxMzM5MmYucG5nIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.K8HdZZznedNY8zU4iWytUBYrmxSzrg0QI4i3gy0RWR4",
    },
]


#  API / Endpoint
@main_bp.get("/")
def hello_world():
    return render_template("home.html")


# Flask use Jinja2 -> Replace {{}} with python value
@main_bp.get("/about")
def about_page():
    return render_template("about.html", name=name, hobbies=hobbies)


# Task 2 - Create profile page
@main_bp.get("/profile")
def profile_page():
    return render_template("profile.html", users=users)
