"""
Module qui comporte la classe Type
"""


class Type:
    """
    Classe Type

    Methods:
        __init__(self, id_type: int, nom_type: str) : Constructeur de la classe Type
        get_id_type(self) : Getter de l'id du type
        get_nom_type(self) : Getter du nom du type
        __str__(self) : Méthode d'affichage de la classe Type
    """

    def __init__(self, id_type: int, nom_type: str):
        """
        Constructeur de la classe Type

        Args:
            id_type (int): id du type
            nom_type (str): nom du type
        """
        self.id_type = id_type
        self.nom_type = nom_type

    def get_id_type(self):
        """
        Getter de l'id du type

        Returns:
            int: id du type
        """
        return self.id_type

    def get_nom_type(self):
        """
        Getter du nom du type

        Returns:
            str: nom du type
        """
        return self.nom_type

    def __str__(self):
        """
        Méthode d'affichage de la classe Type

        Returns:
            str: Affichage de la classe Type
        """
        return "Type : " + str(self.id_type) + " " + self.nom_type
