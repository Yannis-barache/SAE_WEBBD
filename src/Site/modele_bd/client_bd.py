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

    def get_client_by_email(self, email: str):
        try:
            email = "'" + email + "'"
            query = text(
                'SELECT idClient, nomClient, prenomClient, mdpClient, emailClient FROM CLIENT WHERE emailClient =' +
                str(email))
            print(query)
            result = self.__connexion.execute(query)
            for id_client, nom, prenom, mdp, email in result:
                return Client(id_client, nom, prenom, mdp, email)
            return None
        except Exception as e:
            print(e)
            return None

    def insert_client(self, nom: str, prenom: str, mdp: str, email: str):
        try:
            query_max_id = text("SELECT max(idClient) FROM CLIENT")
            result_max_id = self.__connexion.execute(query_max_id)
            id_max = result_max_id.fetchone()[0]

            if id_max is None:
                id_max = 1
            else:
                id_max = int(id_max) + 1

            query_insert = text(
                f"INSERT INTO CLIENT (idClient, nomClient, prenomClient, mdpClient, emailClient) VALUE ({id_max}"
                f", '{nom}', '{prenom}', '{mdp}', '{email}')")
            print(query_insert)

            self.__connexion.execute(query_insert)
            self.__connexion.commit()

            return True
        except Exception as e:
            print(e)
            return False

    def delete_client(self, id_client: int):
        try:
            query = text(
                "DELETE FROM CLIENT WHERE idClient = " + str(id_client))
            self.__connexion.execute(query)
            self.__connexion.commit()
            return True
        except Exception as e:
            print(e)
            return False

    def update_client(self, id_client: int, nom: str, prenom: str, mdp: str, email: str):
        try:
            query = text(
                "UPDATE CLIENT SET nomClient = '" + nom + "', prenomClient = '" + prenom + "', mdpClient = '" + mdp + "', emailClient = '" + email + "' WHERE idClient = " + str(
                    id_client))
            self.__connexion.execute(query)

            return True
        except Exception as e:
            print(e)
            return False