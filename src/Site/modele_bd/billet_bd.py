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
            query = text('SELECT  idDate, idClient FROM BILLET')
            result = self.__connexion.execute(query)
            billets = []
            for id_billet, id_date, id_client in result:
                billets.append(Billet(id_date, id_client))
            return billets
        except Exception as e:
            print(e)
            return None

    def ajouter_billet(self, id_date: int, id_client: int):
        try:
            query = text(
                "INSERT INTO BILLET (idDate, idClient) VALUES (" +
                str(id_date) + ", " + str(id_client) + ")")
            self.__connexion.execute(query)
            self.__connexion.commit()
            return True

        except Exception as e:
            print(e)
            return False

    def supprimer_billet(self, id_date: int, id_client: int):
        try:
            query = text(
                "DELETE FROM BILLET WHERE idDate = " + str(id_date) + " AND idClient = " + str(id_client))
            self.__connexion.execute(query)
            self.__connexion.commit()
            return True

        except Exception as e:
            print(e)
            return False

    def get_billet_by_id_client(self, id_client: int):
        try:
            query = text('SELECT  idDate, idClient FROM BILLET WHERE idClient = ' + str(id_client))
            result = self.__connexion.execute(query)
            billets = []
            for id_date, id_client in result:
                billets.append(Billet(id_date, id_client))
            return billets
        except Exception as e:
            print(e)
            return None

    def billet_manquant(self, id_client: int):
        try:
            query = text('call AcheteBilletJourManquant(' + str(id_client) + ')')
            result = self.__connexion.execute(query)
        except Exception as e:
            print(e)
            return None
