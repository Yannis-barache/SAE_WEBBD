from .app import app
from flask import Flask, render_template, request, flash
from flask_mail import Message, Mail

import os
import sys

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), './')
sys.path.append(os.path.join(ROOT, 'modele'))
from modeleAppli import ModeleAppli
from .models import  traduire_erreurs

USER = None
mail = Mail(app)



# Configuration de la connection à la base de données
@app.route('/')
def home():
    return render_template(
        "PageAccueil.html", user=USER)

@app.route('/festival')
def festival():
    modele = ModeleAppli()
    groupes = modele.get_groupe_bd().get_all_groupes()
    modele.close()
    return render_template(
        "PageLeFestival.html", groupes=groupes, user=USER)

@app.route('/groupe/<id>')
def groupe(id):
    modele = ModeleAppli()
    groupe = modele.get_groupe_bd().get_groupe_by_id(id)
    if groupe is None:
        # Gérer le cas où le groupe n'existe pas
        return "Groupe non trouvé", 404
    groupes_similaires = modele.get_groupe_bd().get_groupes_similaires(groupe.get_id_style())
    style = modele.get_style_bd().get_style_by_id(groupe.get_id_style())
    modele.close()
    return render_template(
        "PageInfosGroupe.html", groupe=groupe, style=style, user=USER, groupes_similaires=groupes_similaires)
    
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('nom')
        email = request.form.get('email')
        message = request.form.get('message')

        if name!='' and email!='' and message!='':
            msg = Message('New message from ' + name,
                          sender=email,
                          recipients=['khabox52x@gmail.com'])
            msg.body = f"From: {name} <{email}>\n\n{message}"
            mail.send(msg)
            flash("Votre message a été envoyé avec succès!", "success")  # Ajoute un message de confirmation
    
    return render_template(
        "PageContact.html", user=USER)


@app.route("/connexion/", methods=['GET', 'POST'])
def page_connexion():
    from .form import connexion_form
    form = connexion_form()
    modele = ModeleAppli()
    global USER
    messages = []
    inscription = False
    if request.referrer == "http://localhost:5000/inscription/":
        inscription = True
    if request.method == 'POST':
        if not form.validate():

            for field, errors in form.errors.items():
                if field != 'csrf_token':
                    messages.append(traduire_erreurs(errors[0]))
            return render_template('PageConnexion.html', form=form, error=messages)
        else:
            try:
                resultat = modele.get_client_bd().get_client_by_email(request.form['email'])
                if resultat is not None:
                    if request.form['mdp'] == resultat.get_mdp_client():
                        USER = resultat
                        print("On redirige vers la page de succès ", USER)
                        modele.close()
                        return redirect(url_for('success', name=USER))
                    else:
                        messages.append("Email ou mot de passe incorrect")
                        modele.close()
                        return render_template('PageConnexion.html', form=form, error=messages)
            except Exception as e:
                print(e)
                messages.append("Email ou mot de passe incorrect")
                modele.close()
                return render_template('PageConnexion.html', form=form, error=messages)

    modele.close()
    return render_template(
        "PageConnexion.html", form=form,inscription=inscription)


@app.route("/inscription/", methods=['GET', 'POST'])
def page_inscription():
    from .form import inscription_form
    form = inscription_form()
    messages = []
    if request.method == 'POST':
        if not form.validate():
            print("Form is not valid")
            for field, errors in form.errors.items():
                if field != 'csrf_token':
                    messages.append(traduire_erreurs(errors[0]))
            print(messages)
            return render_template('PageInscription.html', form=form, errors=messages)
        nom = request.form['nom']
        prenom = request.form['prenom']
        email = request.form['email']
        mdp = request.form['mdp']
        modele = ModeleAppli()
        try:
            modele.get_client_bd().insert_client(nom, prenom, mdp, email)
            print("Inscription réussie")
            modele.close()
            return redirect(url_for('page_connexion'))
        except Exception as e:
            print(e)
            modele.close()

        return redirect(url_for('page_connexion'))

    return render_template(
        "PageInscription.html", form=form, errors=messages)


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
