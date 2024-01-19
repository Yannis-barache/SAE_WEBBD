from .app import app
from flask import Flask, render_template, request, flash
from flask_mail import Message, Mail
from flask import redirect, url_for

import os
import sys
from .constantes import USER

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), './')
sys.path.append(os.path.join(ROOT, 'modele'))
from modeleAppli import ModeleAppli

from .models import traduire_erreurs

USER = USER
mail = Mail(app)


# Configuration de la connection à la base de données
@app.route('/', methods=['GET', 'POST'])
def home():
    modele = ModeleAppli()
    evenements = modele.get_evenement_bd().get_all_evenement()
    dates =[]
    for evenement in evenements:
        dates.append(modele.get_date_bd().get_date_by_id(evenement.get_date_evenement()).get_date_evenement())
    modele.close()
    return render_template(
        "PageAccueil.html", user=USER, evenements=evenements, dates=dates)


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
    from .form import contact_form
    form = contact_form()
    messages = []
    if request.method == 'POST' and form.validate():
        name = form.nom.data
        email = form.email.data
        message = form.message.data
        sujet = form.sujet.data
        if name != '' and email != '' and message != '' and sujet != '':
            msg = Message('New message from ' + name,
                          sender=email,
                          recipients=['khabox52x@gmail.com'])
            msg.body = f"Sujet: {sujet} \n\n From: {name} <{email}>\n\n{message}"
            mail.send(msg)
            flash("Votre message a été envoyé avec succès!", "success")  # Ajoute un message de confirmation
    else:
        for field, errors in form.errors.items():
            if field != 'csrf_token':
                messages.append(traduire_erreurs(errors[0]))
    print(messages)
    return render_template(
        "PageContact.html", user=USER, form=form, messages=messages)


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
                email = form.email.data
                mdp = form.mdp.data
                statut = form.statut.data
                if int(statut) == 1:
                    resultat = modele.get_client_bd().get_client_by_email(email)
                    if resultat is not None:
                        if mdp == resultat.get_mdp():
                            USER = resultat
                            modele.close()
                            return redirect(url_for('home'))
                        else:
                            messages.append("Email ou mot de passe incorrect")
                            modele.close()
                            return render_template('PageConnexion.html', form=form, error=messages)
                else:
                    resultat = modele.get_organisateur_bd().get_organisateur_by_email(email)
                    if resultat is not None and mdp == resultat.get_mdp():
                            USER = resultat
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
            modele.close()
            return redirect(url_for('page_connexion'))
        except Exception as e:
            print(e)
            modele.close()

        return redirect(url_for('page_connexion'))

    return render_template(
        "PageInscription.html", form=form, errors=messages)


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
    from .form import modification_groupe
    form = modification_groupe()
    modele = ModeleAppli()
    groupe = modele.get_groupe_bd().get_groupe_by_id(id_groupe)
    print(groupe)
    form.set_nom(groupe.get_nom_groupe())
    messages = []
    if request.method == 'POST':
        if not form.validate():
            print("Form is not valid")
            for field, errors in form.errors.items():
                if field != 'csrf_token':
                    messages.append(traduire_erreurs(errors[0]))
            print(messages)
            return render_template('organisateur/groupe/modifier_groupe.html', form=form, errors=messages)
        nom = request.form['nom']
        description = request.form['description']
        style = request.form['style']
        lien_photo = request.form['lien_photo']
        lien_video = request.form['lien_video']
        modele.get_groupe_bd().update_groupe(id_groupe, nom, description, style, lien_photo, lien_video)
        modele.close()
        return redirect(url_for('groupes_admin'))
    modele.close()
    return render_template(
        "organisateur/groupe/modifier_groupe.html", groupe=groupe, form=modification_groupe())


@app.route('/admin/supprimer_groupe/<id_groupe>', methods=['GET', 'POST'])
def supprimer_groupe(id_groupe):
    modele = ModeleAppli()
    modele.get_groupe_bd().delete_groupe(id_groupe)
    modele.close()
    return redirect(request.referrer)


@app.route('/admin/clients')
def clients_admin():
    modele = ModeleAppli()
    clients = modele.get_client_bd().get_all_client()
    modele.close()
    return render_template(
        "organisateur/clients/admin_clients.html", clients=clients)


@app.route('/admin/modifier_client/<id_client>/', methods=['GET', 'POST'])
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


@app.route('/evenement/<id_event>')
def detail_evenement(id_event):
    modele = ModeleAppli()
    evenement = modele.get_evenement_bd().get_evenement_by_id(id_event)
    lieu = modele.get_lieu_bd().get_lieu_by_id(evenement.get_id_lieu())
    participants = modele.get_participe_bd().get_participe_by_id_evenement(id_event)
    places = lieu.get_capacite_lieu() - len(participants)

    groupes = []
    for participant in participants:
        groupes.append(modele.get_groupe_bd().get_groupe_by_id(participant.get_id_groupe()))
    inscrit = False
    if USER is not None:
        inscrit = modele.get_sinscrit_bd().get_sinscrit_event_client(id_event, USER.get_id_client()) is not None
        print("inscrit")
        print(inscrit)
    modele.close()

    return render_template(
        "detail_evenement.html", evenement=evenement, user=USER, lieu=lieu, groupes=groupes, inscrit=inscrit,
        places=places)


@app.route('/inscription_event/<id_event>')
def inscription_event(id_event):
    modele = ModeleAppli()
    if USER is None:
        modele.close()
        return redirect(url_for('page_connexion'))
    if USER.get_id_client() is not None:
        modele.get_sinscrit_bd().insert_sinscrit(USER.get_id_client(), id_event)
        modele.close()
    return redirect(request.referrer)


@app.route('/desinscription_event/<id_event>')
def desinscription_event(id_event):
    modele = ModeleAppli()
    if USER is None:
        modele.close()
        return redirect(url_for('page_connexion'))
    if USER.get_id_client() is not None:
        modele.get_sinscrit_bd().delete_sinscrit(USER.get_id_client(), id_event)
        modele.close()
    return redirect(request.referrer)


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
