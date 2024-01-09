"""
Module contenant la classe ConnexionBD qui permet de se connecter à la base de données
"""
import sqlalchemy


class ConnexionBD:
    """
    Classe ConnexionBD

    Attributes :
        __connexion (sqlalchemy.engine.base.Connection) : connexion à la base de données
        __user (str) : le login MySQL de l'utilisateur
        __passwd (str) : le mot de passe MySQL de l'utilisateur
        __host (str) : le nom ou l'adresse IP de la machine hébergeant le serveur MySQL
        __database (str) : le nom de la base de données à utiliser
    """

    def __init__(self):
        try:
            self.__connexion = None
            self.__user = "barache_user"
            self.__passwd = "sae_web_bd"
            self.__host = "mysql-barache.alwaysdata.net"
            self.__database = "barache_web_bd"
            self.ouvrir_connexion()
        except Exception as err:
            print(err)
            raise err

    def ouvrir_connexion(self, con: bool = True):
        """
        Ouverture d'une connexion MySQL
        paramètres :
            con (bool) : True si on veut utiliser la base de données locale, False sinon
        résultat : l'objet qui gère le connection MySQL si tout s'est bien passé
        """
        try:
            engine = None
            if con:
                # creation de l'objet gérant les interactions avec le serveur de BD
                engine = sqlalchemy.create_engine("mysql+mysqlconnector://" +
                                                  self.__user + ":" +
                                                  self.__passwd + "@" +
                                                  self.__host + "/" +
                                                  self.__database)
            # creation de la connexion
            if engine is not None:
                cnx = engine.connect()
                print("connexion réussie")
            else:
                raise AttributeError(
                    "Erreur de configuration de la base de données")
            self.__connexion = cnx
        except Exception as err:
            print(err)
            raise err

    def get_connexion(self):
        return self.__connexion

    def fermer_connexion(self):
        self.__connexion.close()
        print("connexion fermée")


if __name__ == "__main__":
    try:
        print("Test de la classe ConnexionBD")
        connexion = ConnexionBD()
        print("Test de la méthode ouvrir_connexion")
        connexion.fermer_connexion()
    except Exception as err:
        print(err)
