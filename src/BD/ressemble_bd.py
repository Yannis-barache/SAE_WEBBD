from sqlalchemy.sql.expression import text

class RessembleBD:

    def __init__(self, connexion):
        self.__connexion = connexion

    def get_all_ressemble(self):
        try:
            query = text('SELECT idStyle1, idStyle2 FROM RESSEMBLE')
            result = self.__connexion.execute(query)
            ressemble = []
            for id_sytle1, id_style2 in result:
                ressemble.append(Ressemble(id_sytle1, id_style2))
            return ressemble
        except Exception as e:
            print(e)
            return None
