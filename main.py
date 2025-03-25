from flask import Flask

app = Flask(__name__)


@app.get("/")
def hello_world():
    return "<h1>Super, Cool 😁</h1>"


from routes.movies_bp import movies_bp

# ctrl + ~ play  around with existing one
app.register_blueprint(movies_bp, url_prefix="/movies")
if __name__ == "__main__":
    app.run(debug=True)
