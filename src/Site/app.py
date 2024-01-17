from flask import Flask
import os
import sys
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'appli/modele'))
from organisateur import Organisateur

app= Flask(__name__)

app.config['SECRET_KEY'] = "A092A34D-3FD8-4FF8-A32C-039785E3E4FD"

@app.template_filter("is_organisateur")
def is_organisateur(user):
    return isinstance(user, Organisateur)
