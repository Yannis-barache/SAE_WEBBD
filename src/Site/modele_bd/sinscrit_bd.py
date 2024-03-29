from sqlalchemy.sql.expression import text
import sys
import os

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../')
sys.path.append(os.path.join(ROOT, 'modele'))

from sinscrit import Sinscrit

class SinscritBD:

    def __init__(self, connexion):
        self.__connexion = connexion

    def get_all_sinscrit(self):
        try:
            query = text('SELECT idClient, idEvenement FROM SINSCRIT')
            result = self.__connexion.execute(query)
            sinscrit = []
            for id_client, id_even in result:
                sinscrit.append(Sinscrit(id_client, id_even))
            return sinscrit
        except Exception as e:
            print(e)
            return None

    def get_sinscrit_by_id_client(self, id_client):
        try:
            query = text('SELECT idClient, idEvenement FROM SINSCRIT WHERE idClient ='+str(id_client))
            result = self.__connexion.execute(query)
            sinscrit = []
            for id_client, id_even in result:
                sinscrit.append(Sinscrit(id_client, id_even))
            return sinscrit
        except Exception as e:
            print(e)
            return None

    def get_sinscrit_by_id_client_jour(self, id_client, id_date):
        try:
            query = text('SELECT idClient, idEvenement FROM SINSCRIT natural join EVENEMENT WHERE idClient ='+str(id_client)+' AND id_date ='+str(id_date))
            result = self.__connexion.execute(query)
            sinscrit = []
            for id_client, id_even in result:
                sinscrit.append(Sinscrit(id_client, id_even))
            return sinscrit
        except Exception as e:
            print(e)
            return None

    def insert_sinscrit(self, id_client, id_event):
        try:
            query = text('INSERT INTO SINSCRIT (idClient, idEvenement) VALUES ('+str(id_client)+','+str(id_event)+')')
            self.__connexion.execute(query)
            self.__connexion.commit()
        except Exception as e:
            print(e)
            return None

    def delete_sinscrit(self, id_client, id_event):
        try:
            query = text('DELETE FROM SINSCRIT WHERE idClient ='+str(id_client)+' AND idEvenement ='+str(id_event))
            print(query)
            self.__connexion.execute(query)
            self.__connexion.commit()
        except Exception as e:
            print(e)
            return None

    def get_sinscrit_event_client(self, id_event, id_client):
        try:
            query = text('SELECT idClient, idEvenement FROM SINSCRIT WHERE idClient ='+str(id_client)+' AND idEvenement ='+str(id_event))
            print(query)
            result = self.__connexion.execute(query)
            for id_client, id_even in result:
                print(id_client, id_even)
                return Sinscrit(id_client, id_even)
        except Exception as e:
            print(e)
            return None


