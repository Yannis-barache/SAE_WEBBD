from sqlalchemy.sql.expression import text

class StyleBD:

    def __init__(self, connexion):
        self.__connexion = connexion

    def get_all_style(self):
        try:
            query = text('SELECT idStyle, nomStyle FROM STYLE')
            result = self.__connexion.execute(query)
            styles = []
            for id_style, nom in result:
                styles.append(Style(id_style, nom))
            return styles
        except Exception as e:
            print(e)
            return None

    def get_style_by_id(self, id_stl: int):
        try:
            query = text(
                'SELECT idStyle, nomStyle FROM STYLE WHERE idStyle =' +
                str(id_stl))
            result = self.__connexion.execute(query)
            for id_style, nom in result:
                return Style(id_style, nom)
            return None
        except Exception as e:
            print(e)
            return None
