from sqlalchemy.sql.expression import text

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
