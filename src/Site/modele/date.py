class Date:
        
        def __init__(self, id_date, date_evenement):
            self.__id_date = id_date
            self.__date_evenement = date_evenement
        
        def get_id_date(self):
            return self.__id_date
        
        def get_date_evenement(self):
            return self.__date_evenement