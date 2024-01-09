"""
Module de la classe Sinscrit
"""


class Sinscrit:
    """
    Classe Sinscrit

    __init__(self, id_client: int, id_evenement: int) : Constructeur de la classe Sinscrit
    get_id_client(self) : Getter de l'id du client
    get_id_evenement(self) : Getter de l'id de l'evenement
    __str__(self) : Méthode d'affichage de la classe Sinscrit
    """

    def __init__(self, id_client: int, id_evenement: int):
        """
        Constructeur de la classe Sinscrit

        Args:
            id_client (int): id du client
            id_evenement (int): id de l'evenement
        """
        self.id_client = id_client
        self.id_evenement = id_evenement

    def get_id_client(self):
        """
        Getter de l'id du client

        Returns:
            int: id du client
        """
        return self.id_client

    def get_id_evenement(self):
        """
        Getter de l'id de l'evenement

        Returns:
            int: id de l'evenement
        """
        return self.id_evenement

    def __str__(self):
        """
        Méthode d'affichage de la classe Sinscrit

        Returns:
            str: Affichage de la classe Sinscrit
        """
        return "Client : " + str(self.id_client) + " Evenement : " + str(
            self.id_evenement)
