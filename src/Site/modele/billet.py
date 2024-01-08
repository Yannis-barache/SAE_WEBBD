"""
Module de la classe Billet
"""


class Billet:
    """
    Classe Billet
    """

    def __init__(self, id_billet: int, nom_billet: str, prix: int,
                 id_client: int):
        """
        Constructeur de la classe Billet
        """
        self.id_billet = id_billet
        self.nom_billet = nom_billet
        self.prix = prix
        self.id_client = id_client

    def get_id_billet(self):
        """
        Getter de l'id du billet

        Returns:
            int: id du billet
        """
        return self.id_billet

    def get_nom_billet(self):
        """
        Getter du nom du billet

        Returns:
            str: nom du billet
        """

        return self.nom_billet

    def get_prix(self):
        """
        Getter du prix du billet

        Returns:
            int: prix du billet
        """

        return self.prix

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
        return f"{self.id_billet} - {self.nom_billet} - {self.prix} - {self.id_client}"

    def __repr__(self):
        """
        Méthode magique qui permet de faire un print() sur un objet Billet
        """
        return self.__str__()
