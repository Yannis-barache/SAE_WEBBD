from sqlalchemy.sql.expression import text

class OrganisateurBD:

    def __init__(self, connexion):
        self.__connexion = connexion

    def get_all_organisateur(self):
        try:
            query = text('SELECT idOrganisateur, nomOrganisateur, prenomOrganisateur, mdpOrganisateur, emailOrganisateur FROM ORGANISATEUR')
            result = self.__connexion.execute(query)
            organisateurs = []
            for id_organisateur, nom, prenom, mdp, email in result:
                organisateurs.append(Organisateur(id_organisateur, nom, prenom, mdp, email))
            return organisateurs
        except Exception as e:
            print(e)
            return None

    def get_organisateur_by_id(self, id_orga):
        try:
            query = text('SELECT idOrganisateur, nomOrganisateur, prenomOrganisateur, mdpOrganisateur, emailOrganisateur FROM ORGANISATEUR WHERE idOrganisateur =' + str(id_orga))
            result = self.__connexion.execute(query)
            for id_organisateur, nom, prenom, mdp, email in result:
                return Organisateur(id_organisateur, nom, prenom, mdp, email)
            return None
        except Exception as e:
            print(e)
            return None
