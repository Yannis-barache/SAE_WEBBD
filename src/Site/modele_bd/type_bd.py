from sqlalchemy.sql.expression import text
import sys
import os

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../')
sys.path.append(os.path.join(ROOT, 'modele'))

from type import Type


class TypeBD:

    def __init__(self, type_bd):
        self.type_bd = type_bd

    def get_all_type(self):
        try:
            query = text('SELECT idType, nomType FROM TYPE')
            result = self.type_bd.execute(query)
            types = []
            for id_type, nom in result:
                types.append(Type(id_type, nom))
            return types
        except Exception as e:
            print(e)
            return None

    def get_type_by_id(self, id_t: int):
        try:
            query = text(
                'SELECT idType, nomType FROM TYPE WHERE idType =' +
                str(id_t))
            result = self.type_bd.execute(query)
            for id_type, nom in result:
                return Type(id_type, nom)
            return None
        except Exception as e:
            print(e)
            return None
