from sqlalchemy.sql.expression import text
import sys
import os

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../')
sys.path.append(os.path.join(ROOT, 'modele'))
from billet import Billet

class BilletBD:

    def __init__(self, connexion):
        self.__connexion = connexion

    def get_all_billet(self):
        try:
            query = text('SELECT idBillet, nomBillet, prixBillet, idClient FROM BILLETS')
            result = self.__connexion.execute(query)
            billets = []
            for id_billet, nom, prix, id_client in result:
                billets.append(Billet(id_billet, nom, prix, id_client))
            return billets
        except Exception as e:
            print(e)
            return None

    def get_billet_by_id(self, id_bil: int):
        try:
            query = text(
                'SELECT idBillet, nomBillet, prixBillet, idClient FROM BILLETS WHERE idBillet =' +
                str(id_bil))
            result = self.__connexion.execute(query)
            for id_billet, nom, prix, id_client in result:
                return Billet(id_billet, nom, prix, id_client)
            return None
        except Exception as e:
            print(e)
            return None
