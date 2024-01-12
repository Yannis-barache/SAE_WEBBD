from .app import app
from flask import render_template,request,redirect,url_for


# Configuration de la connection à la base de données
@app.route('/') 
def home():
    return render_template(
        "home.html")

@app.route("/connexion/",methods=['GET','POST'])
def page_connexion():
    from .form import connexion_form
    form = connexion_form()

    if request.method == 'POST':
        if not form.validate():
            messages = []
            for field, errors in form.errors.items():
                if field != 'csrf_token':
                    messages.append(errors[0])


            return render_template('PageConnexion.html', form=form, error=messages)
        email = request.form['email']
        mdp = request.form['mdp']
        return redirect(url_for('success', name=email))
    return render_template(
        "PageConnexion.html", form=form)

@app.route("/inscription/",methods=['GET','POST'])
def page_inscription():

    from .form import inscription_form
    form =inscription_form()
    if request.method == 'POST':
        nom = request.form['nom']
        prenom = request.form['prenom']
        email = request.form['email']
        mdp = request.form['mdp']

        return redirect(url_for('page_connexion'))
    else:
        user = request.args.get('nm')
    return render_template(
        "PageInscription.html", form = form)

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


