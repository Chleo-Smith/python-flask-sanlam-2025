from flask import Flask, render_template

app = Flask(__name__)


@app.get("/")
def hello_world():
    return "<h1>Super, Cool 😁</h1>"


name = "Jamie"
hobbies = ["Gaming", "Reading", "Soccer", "Ballet", "Gyming", "Yoga"]


# flask uses Jinja2 and replaces {{}} with the python value
@app.get("/about")
def about_page():
    return render_template("about.html", name=name, hobbies=hobbies)


from routes.movies_bp import movies_bp

# ctrl + ~ play  around with existing one
app.register_blueprint(movies_bp, url_prefix="/movies")
if __name__ == "__main__":
    app.run(debug=True)
