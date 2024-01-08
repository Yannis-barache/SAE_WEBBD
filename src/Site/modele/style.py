"""
Module comportant la classe de style
"""


class Style:
    """
    Classe Style

    Methods:
        __init__(self, id_style: int, nom_style: str) : Constructeur de la classe Style
        get_id_style(self) : Getter de l'id du style
        get_nom_style(self) : Getter du nom du style
        __str__(self) : Méthode d'affichage de la classe Style
    """

    def __init__(self, id_style: int, nom_style: str):
        """
        Constructeur de la classe Style

        Args:
            id_style (int): id du style
            nom_style (str): nom du style
        """
        self.id_style = id_style
        self.nom_style = nom_style

    def get_id_style(self):
        """
        Getter de l'id du style

        Returns:
            int: id du style
        """
        return self.id_style

    def get_nom_style(self):
        """
        Getter du nom du style

        Returns:
            str: nom du style
        """
        return self.nom_style

    def __str__(self):
        """
        Méthode d'affichage de la classe Style

        Returns:
            str: Affichage de la classe Style
        """
        return "Style : " + str(self.id_style) + " " + self.nom_style
