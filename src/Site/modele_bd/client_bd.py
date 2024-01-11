from sqlalchemy.sql.expression import text

import sys
import os

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../')
sys.path.append(os.path.join(ROOT, 'modele'))

from client import Client

class ClientBD:

    def __init__(self, connexion):
        self.__connexion = connexion

    def get_all_client(self):
        try:
            query = text('SELECT idClient, nomClient, prenomClient, mdpClient, emailClient FROM CLIENT')
            result = self.__connexion.execute(query)
            clients = []
            for id_client, nom, prenom, mdp, email in result:
                clients.append(Client(id_client, nom, prenom, mdp, email))
            return clients
        except Exception as e:
            print(e)
            return None

    def get_client_by_id(self, id_cl: int):
        try:
            query = text(
                'SELECT idClient, nomClient, prenomClient, mdpClient, emailClient FROM CLIENT WHERE idClient =' +
                str(id_cl))
            result = self.__connexion.execute(query)
            for id_client, nom, prenom, mdp, email in result:
                return Client(id_client, nom, prenom, mdp, email)
            return None
        except Exception as e:
            print(e)
            return None
