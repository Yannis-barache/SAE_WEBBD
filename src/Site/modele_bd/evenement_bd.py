from sqlalchemy.sql.expression import text

import sys
import os

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../')
sys.path.append(os.path.join(ROOT, 'modele'))

from evenement import Evenement

class EvenementBD:

    def __init__(self, connexion):
        self.__connexion = connexion

    def get_all_evenement(self):
        try:
            query = text('SELECT idEvenement, nomEvenement, id_date, heureEvenement, idType, idLieu FROM EVENEMENT')
            result = self.__connexion.execute(query)
            evenement = []
            for id_evenement, nom, date, heure, id_type, id_lieu in result:
                evenement.append(Evenement(id_evenement, nom, date, heure, id_type, id_lieu))
            return evenement
        except Exception as e:
            print(e)
            return None

    def get_evenement_by_id(self, id_even):
        try:
            query = text('SELECT idEvenement, nomEvenement, id_date, heureEvenement, idType, idLieu FROM EVENEMENT WHERE idEvenement =' +
                         str(id_even))
            result = self.__connexion.execute(query)
            for id_evenement, nom, date, heure, id_type, id_lieu in result:
                return Evenement(id_evenement, nom, date, heure, id_type, id_lieu)
            return None
        except Exception as e:
            print(e)
            return None

    def get_evenement_by_liste_inscrit(self, liste_id_inscrit):
        try:
            query = text('SELECT idEvenement, nomEvenement, id_date, heureEvenement, idType, idLieu FROM EVENEMENT WHERE idEvenement IN (' +
                         str(liste_id_inscrit)[1:-1] + ")")
            print(query)
            result = self.__connexion.execute(query)
            evenement = []
            for id_evenement, nom, date, heure, id_type, id_lieu in result:
                evenement.append(Evenement(id_evenement, nom, date, heure, id_type, id_lieu))
            return evenement
        except Exception as e:
            print(e)
            return None

    def delete_evenement(self, id_even):
        try:
            query = text('DELETE FROM EVENEMENT WHERE idEvenement =' +
                         str(id_even))
            self.__connexion.execute(query)
            self.__connexion.commit()
            return True
        except Exception as e:
            print(e)
            return False

    def ajout_evenement(self, nom: str, heure: str, date: str, id_type: int, id_lieu: int):
        try:
            query_max_id = text("SELECT max(idClient) FROM CLIENT")
            result_max_id = self.__connexion.execute(query_max_id)
            id_max = result_max_id.fetchone()[0]

            if id_max is None:
                id_max = 1
            else:
                id_max = int(id_max) + 1

            query_insert = text(
                f"INSERT INTO EVENEMENT (idEvenement, nomEvenement, id_date, heureEvenement, idType, idLieu) VALUE ({id_max}"
                f", '{nom}', {date}, '{heure}', {id_type}, {id_lieu})")

            self.__connexion.execute(query_insert)
            self.__connexion.commit()

            return True
        except Exception as e:
            print(e)
            return False
          
    def get_all_evenement_by_id_groupe(self, id_groupe):
        try:
            query = text('SELECT idEvenement, nomEvenement, id_date, heureEvenement, idType, idLieu FROM EVENEMENT WHERE idEvenement IN (SELECT idEvenement FROM PARTICIPE WHERE idGroupe = ' +
                         str(id_groupe) + ')')
            result = self.__connexion.execute(query)
            evenement = []
            for id_evenement, nom, date, heure, id_type, id_lieu in result:
                evenement.append(Evenement(id_evenement, nom, date, heure, id_type, id_lieu))
            return evenement
        except Exception as e:
            print(e)
            return None