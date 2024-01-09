"""
Module de la classe Participe
"""


class Participe:
    """
        Classe Participe

        Methods:
            __init__(self, id_evenement: int, id_groupe: int, date_arrivee: str, heure_arrivee: str, temps_montage: float, temps_demontage: float) : Constructeur de la classe Participe
            get_id_evenement(self) : Getter de l'id de l'evenement
            get_id_groupe(self) : Getter de l'id du groupe
            get_date_arrivee(self) : Getter de la date d'arrivee
            get_heure_arrivee(self) : Getter de l'heure d'arrivee
            get_temps_montage(self) : Getter du temps de montage
            get_temps_demontage(self) : Getter du temps de démontage
            set_date_arrivee(self, date_arrivee: str) : Setter de la date d'arrivee
            set_heure_arrivee(self, heure_arrivee: str) : Setter de l'heure d'arrivee
            set_temps_montage(self, temps_montage: float) : Setter du temps de montage
            set_temps_demontage(self, temps_demontage: float) : Setter du temps de démontage
            __str__(self) : Méthode d'affichage de la classe Participe
    """

    def __init__(self, id_evenement: int, id_groupe: int, date_arrivee: str,
                 heure_arrivee: str, temps_montage: float,
                 temps_demontage: float):
        """
        Constructeur de la classe Participe

        Args:
            id_evenement (int): id de l'evenement
            id_groupe (int): id du groupe
            date_arrivee (str): date d'arrivee
            heure_arrivee (str): heure d'arrivee
            temps_montage (float): temps de montage
            temps_demontage (float): temps de demontage
        """
        self.id_evenement = id_evenement
        self.id_groupe = id_groupe
        self.date_arrivee = date_arrivee
        self.heure_arrivee = heure_arrivee
        self.temps_montage = temps_montage
        self.temps_demontage = temps_demontage

    def get_id_evenement(self):
        """
        Getter de l'id de l'evenement

        Returns:
            int: id de l'evenement
        """

        return self.id_evenement

    def get_id_groupe(self):
        """
        Getter de l'id du groupe

        Returns:
            int: id du groupe
        """

        return self.id_groupe

    def get_date_arrivee(self):
        """
        Getter de la date d'arrivee

        Returns:
            str: date d'arrivee
        """

        return self.date_arrivee

    def get_heure_arrivee(self):
        """
        Getter de l'heure d'arrivee

        Returns:
            str: heure d'arrivee
        """

        return self.heure_arrivee

    def get_temps_montage(self):
        """
        Getter du temps de montage
        """

        return self.temps_montage

    def get_temps_demontage(self):
        """
        Getter du temps de demontage

        Returns:
            float: temps de demontage
        """

        return self.temps_demontage

    def set_date_arrivee(self, date_arrivee: str):
        """
        Setter de la date d'arrivee

        Args:
            date_arrivee (str): date d'arrivee
        """

        self.date_arrivee = date_arrivee

    def set_heure_arrivee(self, heure_arrivee: str):
        """
        Setter de l'heure d'arrivee
        """

        self.heure_arrivee = heure_arrivee

    def set_temps_montage(self, temps_montage: float):
        """
        Setter du temps de montage
        """

        self.temps_montage = temps_montage

    def set_temps_demontage(self, temps_demontage: float):
        """
        Setter du temps de demontage
        """

        self.temps_demontage = temps_demontage

    def __str__(self):
        """
        Méthode d'affichage de la classe Participe
        """
        return "Participe : id_evenement = " + str(
            self.id_evenement) + " id_groupe = " + str(
                self.id_groupe) + " date_arrivee = " + str(
                    self.date_arrivee) + " heure_arrivee = " + str(
                        self.heure_arrivee) + " temps_montage = " + str(
                            self.temps_montage) + " temps_demontage = " + str(
                                self.temps_demontage)
