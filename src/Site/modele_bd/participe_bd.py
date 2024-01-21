from sqlalchemy.sql.expression import text
import sys
import os

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../')
sys.path.append(os.path.join(ROOT, 'modele'))

from participe import Participe

class ParticipeBD:

    def __init__(self, connexion):
        self.__connexion = connexion

    def get_all_participe(self):
        try:
            query = text('SELECT idGroupe, idEvenement, dateArriveeGroupe, heureArriveeGroupe, tempsDeMontage, tempsDeDemontage FROM PARTICIPE')
            result = self.__connexion.execute(query)
            participe = []
            for id_groupe, id_even, date_arrivee, heure_arrivee, temps_montage, temps_demontage in result:
                participe.append(Participe(id_groupe, id_even, date_arrivee, heure_arrivee, temps_montage, temps_demontage))
            return participe
        except Exception as e:
            print(e)
            return None

    def get_participe_by_id_evenement(self, id_even):
        try:
            query = text('SELECT idGroupe, idEvenement, dateArriveeGroupe, heureArriveeGroupe, tempsDeMontage, tempsDeDemontage FROM PARTICIPE WHERE idEvenement ='+str(id_even))
            result = self.__connexion.execute(query)
            print(query)
            participe = []
            for id_groupe, id_even, date_arrivee, heure_arrivee, temps_montage, temps_demontage in result:
                participe.append(Participe(id_even, id_groupe, date_arrivee, heure_arrivee, temps_montage, temps_demontage))
            return participe
        except Exception as e:
            print(e)
            return None

    def get_participe_by_id_groupe(self, id_groupe):
        try:
            query = text('SELECT idGroupe, idEvenement, dateArriveeGroupe, heureArriveeGroupe, tempsDeMontage, tempsDeDemontage FROM PARTICIPE WHERE idGroupe ='+str(id_groupe))
            result = self.__connexion.execute(query)
            participe = []
            for id_groupe, id_even, date_arrivee, heure_arrivee, temps_montage, temps_demontage in result:
                participe.append(Participe(id_even, id_groupe, date_arrivee, heure_arrivee, temps_montage, temps_demontage))
            return participe
        except Exception as e:
            print(e)
            return None
