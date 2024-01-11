from sqlalchemy.sql.expression import text

class LogerBD:

    def __init__(self, connexion):
        self.__connexion = connexion

    def get_all_loger(self):
        try:
            query = text('SELECT idHebergement, idGroupe, dateDebutHebergement, dateFinHebergement FROM LOGER')
            result = self.__connexion.execute(query)
            loger = []
            for id_hebergement, id_groupe, date_debut, date_fin in result:
                loger.append(Loger(id_hebergement, id_groupe, date_debut, date_fin))
        except Exception as e:
            print(e)
            return None

    def get_loger_by_id(self, id_heberg):
        try:
            query = text('SELECT idHebergement, idGroupe, dateDebutHebergement, dateFinHebergement FROM LOGER WHERE idHebergement =' + str(id_heberg))
            result = self.__connexion.execute(query)
            for id_hebergement, id_groupe, date_debut, date_fin in result:
                return Loger(id_hebergement, id_groupe, date_debut, date_fin)
            return None
        except Exception as e:
            print(e)
            return None
