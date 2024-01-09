"""
Module qui comporte la classe Instrument
"""


class Instrument:
    """
    Classe Instrument

    Methods:
        __init__(self, id_instrument: int, nom_instrument: str) : Constructeur de la classe Instrument
        get_id_instrument(self) : Getter de l'id de l'instrument
        get_nom_instrument(self) : Getter du nom de l'instrument
        __str__(self) : Méthode d'affichage de la classe Instrument
    """

    def __init__(self, id_instrument: int, nom_instrument: str):
        """
        Constructeur de la classe Instrument

        Args:
            id_instrument (int): id de l'instrument
            nom_instrument (str): nom de l'instrument
        """
        self.id_instrument = id_instrument
        self.nom_instrument = nom_instrument

    def get_id_instrument(self):
        """
        Getter de l'id de l'instrument

        Returns:
            int: id de l'instrument
        """
        return self.id_instrument

    def get_nom_instrument(self):
        """
        Getter du nom de l'instrument

        Returns:
            str: nom de l'instrument
        """
        return self.nom_instrument

    def __str__(self):
        """
        Méthode d'affichage de la classe Instrument

        Returns:
            str: Affichage de la classe Instrument
        """
        return "Instrument : " + str(
            self.id_instrument) + " " + self.nom_instrument
