"""
Module de la classe loger
"""


class Loger:
    """
    Classe Loger


    Methods:
        __init__(self, id_hebergement: int, id_groupe: int, date_debut: str, date_fin: str) : Constructeur de la classe Loger
        get_id_hebergement(self) : Getter de l'id de l'hebergement
        get_id_groupe(self) : Getter de l'id du groupe
        get_date_debut(self) : Getter de la date de debut
        get_date_fin(self) : Getter de la date de fin
        set_date_debut(self, date_debut: str) : Setter de la date de debut
        set_date_fin(self, date_fin: str) : Setter de la date de fin
        __str__(self) : Méthode d'affichage de la classe Loger
    """

    def __init__(self, id_hebergement: int, id_groupe: int, date_debut: str,
                 date_fin: str):
        """
        Constructeur de la classe Loger

        Args:
            id_hebergement (int): id de l'hebergement
            id_groupe (int): id du groupe
            date_debut (str): date de debut
            date_fin (str): date de fin
        """
        self.id_hebergement = id_hebergement
        self.id_groupe = id_groupe
        self.date_debut = date_debut
        self.date_fin = date_fin

    def get_id_hebergement(self):
        """
        Getter de l'id de l'hebergement

        Returns:
            int: id de l'hebergement
        """
        return self.id_hebergement

    def get_id_groupe(self):
        """
        Getter de l'id du groupe

        Returns:
            int: id du groupe
        """
        return self.id_groupe

    def get_date_debut(self):
        """
        Getter de la date de debut

        Returns:
            str: date de debut
        """
        return self.date_debut

    def get_date_fin(self):
        """
        Getter de la date de fin

        Returns:
            str: date de fin
        """
        return self.date_fin

    def set_date_debut(self, date_debut: str):
        """
        Setter de la date de debut

        Args:
            date_debut (str): date de debut
        """
        self.date_debut = date_debut

    def set_date_fin(self, date_fin: str):
        """
        Setter de la date de fin

        Args:
            date_fin (str): date de fin
        """
        self.date_fin = date_fin

    def __str__(self):
        """
        Méthode d'affichage de la classe Loger

        Returns:
            str: affichage de la classe Loger
        """
        return "Loger : id_hebergement = " + str(
            self.id_hebergement
        ) + " id_groupe = " + str(
            self.id_groupe
        ) + " date_debut = " + self.date_debut + " date_fin = " + self.date_fin
