"""
Module de la classe Ressemble
"""


class Ressemble:
    """
    Classe Ressemble

    Methods:
        __init__(self, id_style1: int, id_style2: int) : Constructeur de la classe Ressemble
        get_id_style1(self) : Getter de l'id du style 1
        get_id_style2(self) : Getter de l'id du style 2
        __str__(self) : Méthode d'affichage de la classe Ressemble
    """

    def __init__(self, id_style1: int, id_style2: int):
        """
        Constructeur de la classe Ressemble

        Args:
            id_style1 (int): id du style 1
            id_style2 (int): id du style 2
        """
        self.id_style1 = id_style1
        self.id_style2 = id_style2

    def get_id_style1(self):
        """
        Getter de l'id du style 1

        Returns:
            int: id du style 1
        """
        return self.id_style1

    def get_id_style2(self):
        """
        Getter de l'id du style 2

        Returns:
            int: id du style 2
        """
        return self.id_style2

    def __str__(self):
        """
        Méthode d'affichage de la classe Ressemble

        Returns:
            str: Affichage de la classe Ressemble
        """
        return "Style 1 : " + str(
            self.id_style1) + "ressemble au Style 2 : " + str(
                self.id_style2) + " et vice versa"
