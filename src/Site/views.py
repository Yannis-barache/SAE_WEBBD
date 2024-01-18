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


@app.route('/admin')
def admin():
    return render_template(
        "organisateur/acceuil_organisateur.html")


@app.route('/admin/groupes')
def groupes_admin():
    modele = ModeleAppli()
    groupes = modele.get_groupe_bd().get_all_groupes()
    modele.close()
    return render_template(
        "organisateur/groupe/admin_groupe.html", groupes=groupes)

@app.route('/admin/modifier_groupe/<id_groupe>', methods=['GET', 'POST'])
def modifier_groupe(id_groupe):
    modele = ModeleAppli()
    groupe = modele.get_groupe_bd().get_groupe_by_id(id_groupe)
    modele.close()
    return render_template(
        "organisateur/groupe/modifier_groupe.html", groupe=groupe)

@app.route('/admin/supprimer_groupe/<id_groupe>', methods=['GET', 'POST'])
def supprimer_groupe(id_groupe):
    modele = ModeleAppli()
    modele.get_groupe_bd().delete_groupe(id_groupe)
    modele.close()
    return redirect(request.referrer)

@app.route('/admin/ajouter_groupe', methods=['GET', 'POST'])
def ajouter_groupe():
    modele = ModeleAppli()
    if request.method == 'POST':
        nom = request.form['nom']
        modele.get_groupe_bd().insert_groupe(nom)
        modele.close()
        return redirect(url_for('groupes'))
    modele.close()
    return render_template(
        "organisateur/groupe/ajouter_groupe.html")

@app.route('/admin/clients')
def clients_admin():
    modele = ModeleAppli()
    clients = modele.get_client_bd().get_all_client()
    modele.close()
    return render_template(
        "organisateur/clients/admin_clients.html", clients=clients)

@app.route('/admin/modifier_client/<id_client>', methods=['GET', 'POST'])
def modifier_client(id_client):
    modele = ModeleAppli()
    client = modele.get_client_bd().get_client_by_id(id_client)
    modele.close()
    return render_template(
        "organisateur/clients/modifier_client.html", client=client)

@app.route('/admin/supprimer_client/<id_client>', methods=['GET', 'POST'])
def supprimer_client(id_client):
    modele = ModeleAppli()
    modele.get_client_bd().delete_client(id_client)
    modele.close()
    return redirect(request.referrer)

@app.route('/admin/ajouter_client', methods=['GET', 'POST'])
def ajouter_client():
    modele = ModeleAppli()
    if request.method == 'POST':
        nom = request.form['nom']
        prenom = request.form['prenom']
        email = request.form['email']
        mdp = request.form['mdp']
        modele.get_client_bd().insert_client(nom, prenom, mdp, email)
        modele.close()
        return redirect(url_for('clients'))
    modele.close()
    return render_template(
        "organisateur/clients/ajouter_client.html")

@app.route('/admin/evenements')
def evenements_admin():
    modele = ModeleAppli()
    evenements = modele.get_evenement_bd().get_all_evenement()
    modele.close()
    return render_template(
        "organisateur/evenements/admin_evenements.html", evenements=evenements)

@app.route('/admin/modifier_evenement/<id_evenement>', methods=['GET', 'POST'])
def modifier_evenement(id_evenement):
    modele = ModeleAppli()
    evenement = modele.get_evenement_bd().get_evenement_by_id(id_evenement)
    modele.close()
    return render_template(
        "organisateur/evenements/modifier_evenement.html", evenement=evenement)

@app.route('/admin/supprimer_evenement/<id_evenement>', methods=['GET', 'POST'])
def supprimer_evenement(id_evenement):
    modele = ModeleAppli()
    modele.get_evenement_bd().delete_evenement(id_evenement)
    modele.close()
    return redirect(request.referrer)
