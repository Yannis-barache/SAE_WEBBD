from .app import app
from flask import render_template, request, redirect, url_for
import os
import sys

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), './')
sys.path.append(os.path.join(ROOT, 'modele'))
from modeleAppli import ModeleAppli

from .models import traduire_erreurs

USER = None


# Configuration de la connection à la base de données
@app.route('/')
def home():
    return render_template(
        "PageAccueil.html")


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
        "PageConnexion.html", form=form, inscription=inscription)


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


@app.route('/deconnexion/')
def deconnexion():
    global USER
    USER = None
    return redirect(url_for('home'))


@app.route('/calendrier')
def calendrier():
    modele = ModeleAppli()
    events = modele.get_sinscrit_bd().get_sinscrit_by_id_client_jour(1, 1)
    print(events)
    liste_id_even = []
    for event in events:
        liste_id_even.append(event.get_id_evenement())
    events = modele.get_evenement_bd().get_evenement_by_liste_inscrit(liste_id_even)
    modele.close()
    return render_template(
        "calendrier.html", events=events)

@app.route('/image')
def image():
    modele = ModeleAppli()
    groupe = modele.get_groupe_bd().get_groupe_by_id(1)
    modele.close()
    blob = groupe.get_photo_groupe()
    return render_template(
        "image.html", blob=blob)
