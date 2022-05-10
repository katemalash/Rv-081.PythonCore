from flask import Flask, render_template, url_for, redirect, request, session
from data import *


app = Flask(__name__)
app.secret_key = "138"

@app.route("/")
def home():
    return render_template("index.html") 

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form["nm"]
        session["usr"] = user
        return redirect(url_for("home"))
    else:
        if "user" in session:
            return redirect(url_for("home"))

    return render_template("login.html")
    
@app.route("/logout")
def logout():
    session.pop("user", None)
    session["usr"] = False
    return redirect(url_for("home"))

@app.route("/content")
def content():
    return render_template("content.html", content = "Test")

@app.route("/<movie>")
def movieInfo(title = None, movie = None, name = None, episod = None, year = None, rating = None, writer = None, actors = None, storyline = None, description = None):
    for item in moviesList:
        print(item[0])
        if item[0] == movie:
            title = item[1]
            name = item[1]
            episod = item[2]
            year = item[3]
            rating = item[4]
            writer = item[5]
            actors = item[6]
            storyline = item[7]
            description = item[8]
            return render_template("movie.html", title = title, name = name, movie = movie, episod = episod, year = year, rating = rating, writer = writer, actors = actors, storyline = storyline, description = description)

if __name__ == "__main__":
    app.run(debug = True)