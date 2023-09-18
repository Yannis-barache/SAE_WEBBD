from .app import app
from flask import render_template


@app.route("/")

def home():
    return render_template(
        "home.html",
        title="Hello World !!!!!",
        names=["Pierre", "Paul", "Corinne"])

@app.route("/page2")

def page2():
    return render_template(
        "page2.html",
        title="Page 2",
        message="Hello World !!!!!  Khalil et Yassine ont fait cette page de golmon",
        )


@app.route("/books")
def books():
    return render_template(
        "livre.html",
        title="Books",
        books="livre de khabox",
    )