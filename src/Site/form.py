from wtforms import validators
from wtforms.validators import Email, EqualTo
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, HiddenField
import os
import sys

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), './')
sys.path.append(os.path.join(ROOT, 'modele'))
from modeleAppli import ModeleAppli


def connexion_form():
    class ConnexionForm(FlaskForm):
        email = StringField('Email', validators=[validators.DataRequired()])
        mdp = PasswordField('Mot de passe', validators=[validators.DataRequired()])
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


def modification_groupe():
    class ModificationGroupe(FlaskForm):
        modele = ModeleAppli()
        id = HiddenField('id')
        nom = StringField('Nom', validators=[validators.DataRequired()])
        description = StringField('Description', validators=[validators.DataRequired()])
        style = SelectField('Style', choices=[(style.get_id_style(), style.get_nom_style()) for style in
                                              modele.get_style_bd().get_all_style()])
        lien_photo = StringField('Lien vers une photo')
        lien_video = StringField('Lien vers une video')
        submit = SubmitField('Modifier')
        modele.close()

        def set_id(self, id):
            self.id.data = id

        def set_nom(self, nom):
            self.nom.data = nom

        def set_description(self, description):
            self.description.data = description

        def set_style(self, style):
            self.style.data = style

        def set_lien_photo(self, lien_photo):
            self.lien_photo.data = lien_photo

        def set_lien_video(self, lien_video):
            self.lien_video.data = lien_video

    return ModificationGroupe()
