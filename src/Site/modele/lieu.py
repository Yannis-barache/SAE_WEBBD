"""
Module de la classe Lieu
"""


class Lieu:
    """
    Classe Lieu

    Methods:
        __init__(self, id_lieu: int, nom_lieu: str, adresse_lieu: str, capacite_lieu : int) : Constructeur de la classe Lieu
        get_id_lieu(self) : Getter de l'id du lieu
        get_nom_lieu(self) : Getter du nom du lieu
        get_adresse_lieu(self) : Getter de l'adresse du lieu
        get_capacite_lieu(self) : Getter de la capacité du lieu
        set_capacite_lieu(self, capaciteLieu : int) : Setter de la capacité du lieu
        set_adresse_lieu(self, adresseLieu : str) : Setter de l'adresse du lieu
        __str__(self) : Méthode d'affichage de la classe Lieu
    """

    def __init__(self, id_lieu: int, nom_lieu: str, adresse_lieu: str,
                 capacite_lieu: int):
        """
        Constructeur de la classe Lieu

        Args:
            id_lieu (int): id du lieu
            nom_lieu (str): nom du lieu
            adresse_lieu (str): adresse du lieu
            capacite_lieu (int): capacité du lieu
        """
        self.id_lieu = id_lieu
        self.nom_lieu = nom_lieu
        self.adresse_lieu = adresse_lieu
        self.capacite_lieu = capacite_lieu

    def get_id_lieu(self):
        """
        Getter de l'id du lieu
        """
        return self.id_lieu

    def get_nom_lieu(self):
        """
        Getter du nom du lieu
        """
        return self.nom_lieu

    def get_adresse_lieu(self):
        """
        Getter de l'adresse du lieu
        """
        return self.adresse_lieu

    def get_capacite_lieu(self):
        """
        Getter de la capacité du lieu
        """
        return self.capacite_lieu

    def set_capacite_lieu(self, capacite_lieu: int):
        """
        Setter de la capacité du lieu
        """
        self.capacite_lieu = capacite_lieu

    def set_adresse_lieu(self, adresse_lieu: str):
        """
        Setter de l'adresse du lieu
        """
        self.adresse_lieu = adresse_lieu

    def __str__(self):
        """
        Méthode d'affichage de la classe Lieu
        """
        return "Lieu : id = " + str(
            self.id_lieu
        ) + ", nom = " + self.nom_lieu + ", adresse = " + self.adresse_lieu + ", capacité = " + str(
            self.capacite_lieu)
