from .app import app
from flask import render_template
from flask_mysqldb import MySQL

mysql=MySQL()
mysql.init_app(app)
app.config['MYSQL_USER']='barache'
app.config['MYSQL_PASSWORD']='barache'
app.config['MYSQL_DB']='DBbarache'
app.config['MYSQL_HOST']='servinfo-maria'
app.config['MYSQL_CURSORCLASS']='DictCursor'

@app.route("/")

def home():
    CS=mysql.connection.cursor()
    CS.execute("SELECT * FROM GROUPE")
    result=CS.fetchall()
    affichage=[]
    for i in result:
        affichage.append(i["nomGroupe"])


    return render_template(
        
        "home.html",
        title="Bienvenue sur le site du Festiut'O",
        names=affichage)

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