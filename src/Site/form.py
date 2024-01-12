from wtforms import validators
from wtforms.validators import Email, EqualTo
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField


def connexion_form():
    class ConnexionForm(FlaskForm):
        email = StringField('Email', validators=[validators.DataRequired(), Email()])
        mdp = PasswordField('Mot de passe', validators=[validators.DataRequired()])
        submit = SubmitField('Se connecter')


    return ConnexionForm()


def inscription_form():
    class InscriptionForm(FlaskForm):
        nom = StringField('Nom', validators=[validators.DataRequired()])
        prenom = StringField('Prénom', validators=[validators.DataRequired()])
        email = StringField('Email', validators=[validators.DataRequired(), Email()])
        mdp = PasswordField('Mot de passe', validators=[validators.DataRequired(), validators.Length(min=8)])
        confirm_mdp = PasswordField('Confirmer le mot de passe',
                                    validators=[validators.DataRequired(),EqualTo('mdp')])
        submit = SubmitField('S\'inscrire')

    return InscriptionForm()
