from .app import app
from flask import render_template


@app.route("/")

def home():
    return render_template(
        "home.html",
        title="Bienvenue sur le site du Festiut'O",
        names=["Pierre", "Paul", "Corinne"])

@app.route("/connexion")

def page2():
    return render_template(
        "connexion.html",
        title="Page de connexion",
        message="Veuillez rentrer vos identifiants",
        )


@app.route("/inscription")
def inscription():
    return render_template(
        "inscription.html",
        title="Page d'inscription",
        message= "Veuillez vous inscrire",
    )