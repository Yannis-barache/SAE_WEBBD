from sqlalchemy.sql.expression import text

import sys
import os

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../')
sys.path.append(os.path.join(ROOT, 'modele'))

from instrument import Instrument

class InstrumentBD:

    def __init__(self, connexion):
        self.connection = connexion

    def get_all_instruments(self):
        try:
            query = text('SELECT idInstrument, nomInstrument FROM INSTRUMENT')
            result = self.connection.execute(query)
            instruments = []
            for id_instrument, nom in result:
                instruments.append(Instrument(id_instrument, nom))
            return instruments
        except Exception as e:
            print(e)
            return None

    def get_instrument_by_id(self, id_instru):
        try:
            query = text('SELECT idInstrument, nomInstrument FROM INSTRUMENT WHERE idInstrument =' + str(id_instru))
            result = self.connection.execute(query)
            for id_instrument, nom in result:
                return Instrument(id_instrument, nom)
            return None
        except Exception as e:
            print(e)
            return None