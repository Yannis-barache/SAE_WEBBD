from sqlalchemy.sql.expression import text

class LieuBD:

    def __init__(self, connexion):
        self.__connexion = connexion

    def get_all_lieu(self):
        try:
            query = text('SELECT idLieu, nomLieu, adresseLieu, capaciteLieu FROM LIEU')
            result = self.__connexion.execute(query)
            lieux = []
            for id_lieu, nom, adresse, capacite in result:
                lieux.append(Lieu(id_lieu, nom, adresse, capacite))
            return lieux
        except Exception as e:
            print(e)
            return None

    def get_lieu_by_id(self, id_li: int):
        try:
            query = text(
                'SELECT idLieu, nomLieu, adresseLieu, capaciteLieu FROM LIEU WHERE idLieu =' +
                str(id_li))
            result = self.__connexion.execute(query)
            for id_lieu, nom, adresse, capacite in result:
                return Lieu(id_lieu, nom, adresse, capacite)
            return None
        except Exception as e:
            print(e)
            return None
