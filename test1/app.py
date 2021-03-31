from flask import Flask, redirect, render_template, request
from cs50 import SQL

app = Flask(__name__)

REGISTRANTS = {}
# db = SQL("sqlite:///froshims.db")

SPORTS = [
    "Volleyball",
    "Soccer",
    "BBall",
    "Flag Football"
]

@app.route("/")
def index():
    return render_template("index.html", sports=SPORTS)

@app.route("/register", methods=["POST"])
def register():
    # if not request.form.get("name") or request.form.get("sport")  not in SPORTS:
    #     return render_template("failure.html")
    # return render_template("success.html")

    name = request.form.get("name")
    if not name:
        return render_template("error.html", message="Missing name")
    sport = request.form.get("sport")
    if not sport:
        return render_template("error.html", message="Missing Sport")
    if sport not in SPORTS:
        return render_template("error.html", message="Invalid Sport")

    # REGISTRANTS[name] = sport

    return redirect("/registrants")


@app.route("/registrants")
def registrants():
    return render_template("registrants.html", registrants=REGISTRANTS)