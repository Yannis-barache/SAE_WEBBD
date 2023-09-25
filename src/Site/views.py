from .app import app
from flask import render_template,request,redirect,url_for

from flask_mysqldb import MySQL


# Configuration de la connection à la base de données
mysql=MySQL()
mysql.init_app(app)
app.config['MYSQL_USER']='barache'
app.config['MYSQL_PASSWORD']='barache'
app.config['MYSQL_DB']='DBbarache'
app.config['MYSQL_HOST']='servinfo-maria'
app.config['MYSQL_CURSORCLASS']='DictCursor'

@app.route('/', methods =["GET", "POST"]) 
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

@app.route("/connexion", methods =["GET", "POST"])

def page2():
    return render_template(
        "connexion.html",
        title="Page de connexion",
        message="Veuillez rentrer vos identifiants",
        )

@app.route('/success/<name>')
def success(name):
   return 'welcome %s' % name


@app.route('/inscription',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
        nom = request.form['nom']
        prenom = request.form['prenom']
        email = request.form['email']
        mdp = request.form['mdp']
        CS=mysql.connection.cursor()
        CS.execute("INSERT INTO CLIENT (nomClient,prenomClient,emailClient,mdpClient) VALUES (%s,%s,%s,%s)",(nom,prenom,email,mdp))
        mysql.connection.commit()
        return redirect(url_for('home.html',name=nom))
   else:
        user = request.args.get('nm')
        return render_template("inscription.html")


