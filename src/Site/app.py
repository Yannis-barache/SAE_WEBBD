from flask import Flask
import os
import sys
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), './')
sys.path.append(os.path.join(ROOT, 'modele'))
from organisateur import Organisateur
from client import Client
from groupe import Groupe
from flask import Flask 
from flask_mail import Mail, Message

app= Flask(__name__)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'khabox52x@gmail.com'
app.config['MAIL_PASSWORD'] = 'vpha sdhj botu xujo'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

app.config['SECRET_KEY'] = "A092A34D-3FD8-4FF8-A32C-039785E3E4FD"

@app.template_filter("is_organisateur")
def is_organisateur(user):
    return isinstance(user, Organisateur)

@app.template_filter("is_client")
def is_client(user):
    return isinstance(user, Client)

@app.template_filter("is_groupe")
def is_groupe(user):
    return isinstance(user, Groupe)



