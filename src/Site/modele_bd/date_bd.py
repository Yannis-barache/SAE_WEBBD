from sqlalchemy.sql.expression import text

import sys
import os

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../')
sys.path.append(os.path.join(ROOT, 'modele'))

from date import Date

class DateBD:
    
        def __init__(self, connexion):
            self.__connexion = connexion
    
        def get_all_date(self):
            try:
                query = text('SELECT id_date, dateEvenement FROM DATE')
                result = self.__connexion.execute(query)
                date = []
                for id_date, date_evenement in result:
                    date.append(Date(id_date, date_evenement))
                return date
            except Exception as e:
                print(e)
                return None
    
        def get_date_by_id(self, id_date):
            try:
                query = text('SELECT id_date, dateEvenement FROM DATE WHERE id_date =' +
                            str(id_date))
                result = self.__connexion.execute(query)
                for id_date, date_evenement in result:
                    return Date(id_date, date_evenement)
                return None
            except Exception as e:
                print(e)
                return None