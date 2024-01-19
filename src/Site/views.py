from .app import app
from flask import render_template, request, redirect, url_for
import os
import sys

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), './')
sys.path.append(os.path.join(ROOT, 'modele'))
from modeleAppli import ModeleAppli
from .models import  traduire_erreurs

USER = None


# Configuration de la connection à la base de données
@app.route('/', methods=['GET', 'POST'])
def home():
    modele = ModeleAppli()
    evenements = modele.get_evenement_bd().get_all_evenement()
    modele.close()
    return render_template(
        "PageAccueil.html", user=USER, evenements=evenements)

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
                        return redirect(url_for('home'))
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

@app.route('/billetterie/')
def billetterie():
    modele = ModeleAppli()
    dates = modele.get_date_bd().get_all_date()
    modele.close()
    return render_template("PageBilletterie.html", dates=dates, user=USER)

@app.route('/mon-compte/')
def mon_compte():
    if USER is None:
        return redirect(url_for('page_connexion'))
    return render_template("PageMonCompte.html", user=USER)

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
