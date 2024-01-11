from sqlalchemy.sql.expression import text

class HebergementBD:

    def __init__(self, connexion):
        self.__connexion = connexion

    def get_all_hebergement(self):
        try:
            query = text('SELECT idHebergement, nomHebergement, adresseHebergement, nbPlacesJour FROM HEBERGEMENT')
            result = self.__connexion.execute(query)
            hebergements = []
            for id_hebergement, nom, adresse, nb_places in result:
                hebergements.append(Hebergement(id_hebergement, nom, adresse, nb_places))
            return hebergements
        except Exception as e:
            print(e)
            return None

    def get_hebergement_by_id(self, id_heb: int):
        try:
            query = text(
                'SELECT idHebergement, nomHebergement, adresseHebergement, nbPlacesJour FROM HEBERGEMENT WHERE idHebergement =' +
                str(id_heb))
            result = self.__connexion.execute(query)
            for id_hebergement, nom, adresse, nb_places in result:
                return Hebergement(id_hebergement, nom, adresse, nb_places)
            return None
        except Exception as e:
            print(e)
            return None
