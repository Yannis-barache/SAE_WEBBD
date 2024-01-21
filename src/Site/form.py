from wtforms import validators
from wtforms.validators import Email, EqualTo
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, HiddenField, TextAreaField, DateTimeLocalField
import os
import sys

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), './')
sys.path.append(os.path.join(ROOT, 'modele'))
from modeleAppli import ModeleAppli


def connexion_form():
    class ConnexionForm(FlaskForm):
        email = StringField('Email', validators=[validators.DataRequired()])
        mdp = PasswordField('Mot de passe', validators=[validators.DataRequired()])
        statut = SelectField('Statut', choices=[('1', 'Utilisateur'), ('2', 'Administrateur')])
        submit = SubmitField('Se connecter')

    return ConnexionForm()


def inscription_form():
    class InscriptionForm(FlaskForm):
        id = HiddenField('id')
        nom = StringField('Nom', validators=[validators.DataRequired()])
        prenom = StringField('Prénom', validators=[validators.DataRequired()])
        email = StringField('Email', validators=[validators.DataRequired(), Email()])
        mdp = PasswordField('Mot de passe', validators=[validators.DataRequired(), validators.Length(min=8)])
        confirm_mdp = PasswordField('Confirmer le mot de passe',
                                    validators=[validators.DataRequired(), EqualTo('mdp')])
        submit = SubmitField('S\'inscrire')

    return InscriptionForm()


def modification_add_groupe():
    class ModificationAddGroupe(FlaskForm):
        modele = ModeleAppli()
        id = HiddenField('id')
        nom = StringField('Nom', validators=[validators.DataRequired()])
        description = StringField('Description', validators=[validators.DataRequired()])
        style = SelectField('Style', choices=[(style.get_id_style(), style.get_nom_style()) for style in
                                              modele.get_style_bd().get_all_style()], default=1)
        lien_photo = StringField('Lien vers une photo')
        lien_video = StringField('Lien vers une video')
        reseaux = StringField('Réseaux sociaux')
        submit = SubmitField('Modifier')
        modele.close()

        def set_id(self, id):
            self.id.data = id

        def set_nom(self, nom):
            self.nom.data = nom

        def set_description(self, description):
            self.description.data = description

        def set_style(self, style):
            self.style.default = style

        def set_lien_photo(self, lien_photo):
            self.lien_photo.data = lien_photo

        def set_lien_video(self, lien_video):
            self.lien_video.data = lien_video

    return ModificationAddGroupe()


def modification_add_client():
    class ModificationAddClient(FlaskForm):
        id = HiddenField('id')
        nom = StringField('Nom', validators=[validators.DataRequired()])
        prenom = StringField('Prénom', validators=[validators.DataRequired()])
        email = StringField('Email', validators=[validators.DataRequired(), Email()])
        mdp = PasswordField('Mot de passe', validators=[validators.DataRequired(), validators.Length(min=8)])
        submit = SubmitField('Modifier')

        def set_id(self, id):
            self.id.data = id

        def set_nom(self, nom):
            self.nom.data = nom

        def set_prenom(self, prenom):
            self.prenom.data = prenom

        def set_email(self, email):
            self.email.data = email

        def set_mdp(self, mdp):
            self.mdp.data = mdp

    return ModificationAddClient()


def modification_add_event():
    class ModificationAddEvent(FlaskForm):
        modele = ModeleAppli()
        id = HiddenField('id')
        nom = StringField('Nom', validators=[validators.DataRequired()])
        date = SelectField('Date', choices=[(date.get_id_date(), date.get_date_evenement()) for date in
                                            modele.get_date_bd().get_all_date()])
        type = SelectField('Type', choices=[(type.get_id_type(), type.get_nom_type()) for type in
                                            modele.get_type_bd().get_all_type()])
        lieu = SelectField('Lieu', choices=[(lieu.get_id_lieu(), lieu.get_nom_lieu()) for lieu in
                                            modele.get_lieu_bd().get_all_lieu()])
        heure = StringField('Heure', validators=[validators.DataRequired()])

        submit = SubmitField('Modifier')
        modele.close()

        def set_id(self, id):
            self.id.data = id

        def set_nom(self, nom):
            self.nom.data = nom

        def set_date(self, date):
            self.date.data = date

        def set_heure(self, heure):
            self.heure.data = heure

        def set_type(self, type):
            self.type.data = type

        def set_lieu(self, lieu):
            self.lieu.data = lieu

    return ModificationAddEvent()


def contact_form():
    class ContactForm(FlaskForm):
        nom = StringField('Nom Prénom', validators=[validators.DataRequired()])
        email = StringField('Email', validators=[validators.DataRequired(), Email()])
        sujet = StringField('Sujet', validators=[validators.DataRequired()])
        message = TextAreaField('Message', validators=[validators.DataRequired()])
        submit = SubmitField('Envoyer')

        def set_nom(self, nom):
            self.nom.data = nom

        def set_email(self, email):
            self.email.data = email

    return ContactForm()
