from sqlalchemy.sql.expression import text
import sys
import os

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../')
sys.path.append(os.path.join(ROOT, 'modele'))

from aime import Aime

class AimeBD:

    def __init__(self, connexion):
        self.__connexion = connexion

    def get_all_aime(self):
        try:
            query = text('SELECT idClient, idGroupe FROM AIME')
            result = self.__connexion.execute(query)
            aime = []
            for id_client, id_groupe in result:
                aime.append(Aime(id_client, id_groupe))
            return aime
        except Exception as e:
            print(e)
            return None
