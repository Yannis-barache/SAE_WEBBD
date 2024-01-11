from sqlalchemy.sql.expression import text

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
