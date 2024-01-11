from sqlalchemy.sql.expression import text

class EvenementBD:

    def __init__(self, connexion):
        self.__connexion = connexion

    def get_all_evenement(self):
        try:
            query = text('SELECT idEvenement, nomEvenement, dateEvenement, heureEvenement, idType, idLieu FROM EVENEMENT')
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
            query = text('SELECT idEvenement, nomEvenement, dateEvenement, heureEvenement, idType, idLieu FROM EVENEMENT WHERE idEvenement =' +
                         str(id_even))
            result = self.__connexion.execute(query)
            for id_evenement, nom, date, heure, id_type, id_lieu in result:
                return Evenement(id_evenement, nom, date, heure, id_type, id_lieu)
            return None
        except Exception as e:
            print(e)
            return None
