from sqlalchemy.sql.expression import text

class MembreBD:

    def __init__(self, connexion):
        self.__connexion = connexion

    def get_all_membres(self):
        try:
            query = text('SELECT idMembre, nomMembre, prenomMembre, idGroupe, idInstrument FROM MEMBRE')
            result = self.__connexion.execute(query)
            membres = []
            for id_membre, nom, prenom, id_groupe, id_instru in result:
                membres.append(Membre(id_membre, nom, prenom, id_groupe, id_instru))
            return membres
        except Exception as e:
            print(e)
            return None

    def get_membre_by_id(self, id_memb):
        try:
            query = text('SELECT idMembre, nomMembre, prenomMembre, idGroupe, idInstrument FROM MEMBRE WHERE idMembre =' + str(id_memb))
            result = self.__connexion.execute(query)
            for id_membre, nom, prenom, id_groupe, id_instru in result:
                return Membre(id_membre, nom, prenom, id_groupe, id_instru)
            return None
        except Exception as e:
            print(e)
            return None
