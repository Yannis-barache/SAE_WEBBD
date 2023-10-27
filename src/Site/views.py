from .app import app
from flask import render_template,request,redirect,url_for


# Configuration de la connection à la base de données
@app.route('/') 
def home():
    return render_template(
        "home.html")

@app.route("/connexion/")
def page_connexion():
    return render_template(
        "PageConnexion.html"
        )

@app.route('/success/<name>')
def success(name):
   return 'welcome %s' % name


# @app.route('/inscription')
# def login():
#    if request.method == 'POST':
#         nom = request.form['nom']
#         prenom = request.form['prenom']
#         email = request.form['email']
#         mdp = request.form['mdp']
#         CS=mysql.connection.cursor()
#         CS.execute("INSERT INTO CLIENT (nomClient,prenomClient,emailClient,mdpClient) VALUES (%s,%s,%s,%s)",(nom,prenom,email,mdp))
#         mysql.connection.commit()
#         return redirect(url_for('home.html',name=nom))
#    else:
#         user = request.args.get('nm')
#         return render_template("inscription.html")


