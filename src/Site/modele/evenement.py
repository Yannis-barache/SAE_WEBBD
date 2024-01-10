"""
Module de la classe Evenement
"""


class Evenement:
    """
    Classe Evenement

    Methods:
        __init__(self, id_evenement: int, nom_evenement: str, date_evenement: str, heure_evenement: str, id_type: int, id_lieu: int) : Constructeur de la classe Evenement
        get_id_evenement(self) : Getter de l'id de l'evenement
        get_nom_evenement(self) : Getter du nom de l'evenement
        get_date_evenement(self) : Getter de la date de l'evenement
        get_heure_evenement(self) : Getter de l'heure de l'evenement
        get_id_type(self) : Getter de l'id du type de l'evenement
        get_id_lieu(self) : Getter de l'id du lieu de l'evenement
        __str__(self) : Méthode d'affichage de la classe Evenement
    """

    def __init__(self, id_evenement: int, nom_evenement: str,
                 date_evenement: str, heure_evenement: str, id_type: int,
                 id_lieu: int):
        """
        Constructeur de la classe Evenement

        Args:
            id_evenement (int): id de l'evenement
            nom_evenement (str): nom de l'evenement
            date_evenement (str): date de l'evenement
            heure_evenement (str): heure de l'evenement
            id_type (int): id du type de l'evenement
            id_lieu (int): id du lieu de l'evenement
        """
        self.id_evenement = id_evenement
        self.nom_evenement = nom_evenement
        self.date_evenement = date_evenement
        self.heure_evenement = heure_evenement
        self.id_type = id_type
        self.id_lieu = id_lieu

    def get_id_evenement(self):
        """
        Getter de l'id de l'evenement

        Returns:
            int: id de l'evenement
        """
        return self.id_evenement

    def get_nom_evenement(self):
        """
        Getter du nom de l'evenement

        Returns:
            str: nom de l'evenement
        """
        return self.nom_evenement

    def get_date_evenement(self):
        """
        Getter de la date de l'evenement

        Returns:
            str: date de l'evenement
        """
        return self.date_evenement

    def get_heure_evenement(self):
        """
        Getter de l'heure de l'evenement

        Returns:
            str: heure de l'evenement
        """
        return self.heure_evenement

    def get_id_type(self):
        """
        Getter de l'id du type de l'evenement

        Returns:
            int: id du type de l'evenement
        """
        return self.id_type

    def get_id_lieu(self):
        """
        Getter de l'id du lieu de l'evenement

        Returns:
            int: id du lieu de l'evenement
        """
        return self.id_lieu

    def __str__(self):
        """
        Méthode d'affichage de la classe Evenement

        Returns:
            str: Affichage de la classe Evenement
        """
        return (
            "Evenement : id_evenement = {}, nom_evenement = {}, date_evenement = {}, heure_evenement = {}, "
            "id_type = {}, id_lieu = {}").format(self.id_evenement,
                                                 self.nom_evenement,
                                                 self.date_evenement,
                                                 self.heure_evenement,
                                                 self.id_type, self.id_lieu)
