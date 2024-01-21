"""
Module de la classe Billet
"""


class Billet:
    """
    Classe Billet
    """

    def __init__(self, id_date, id_client: int):
        """
        Constructeur de la classe Billet
        """
        self.id_date = id_date
        self.id_client = id_client

    def get_id_date(self):
        """
        Getter de l'id de la date

        Returns:
            int: id de la date
        """
        return self.id_date

    def get_id_client(self):
        """
        Getter de l'id du client

        Returns:
            int: id du client
        """
        return self.id_client

    def __str__(self):
        """
        Méthode magique qui permet de faire un print() sur un objet Billet
        """
        return f"{self.id_date} - {self.id_client}"

    def __repr__(self):
        """
        Méthode magique qui permet de faire un print() sur un objet Billet
        """
        return self.__str__()
