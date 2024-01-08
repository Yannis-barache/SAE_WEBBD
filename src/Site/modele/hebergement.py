"""
Module de la classe Hebergement
"""


class Hebergement:
    """
    Classe Hebergement

    Methods:
        __init__(self, id_hebergement: int, nom_hebergement: str, adresse_hebergement: str, nb_places_jour: int) : Constructeur de la classe Hebergement
        get_id_hebergement(self) : Getter de l'id de l'hebergement
        get_nom_hebergement(self) : Getter du nom de l'hebergement
        get_adresse_hebergement(self) : Getter de l'adresse de l'hebergement
        get_nb_places_jour(self) : Getter du nombre de places par jour de l'hebergement
        set_nb_places_jour(self, nb_places_jour: int) : Setter du nombre de places par jour de l'hebergement
        set_nom_hebergement(self, nom_hebergement: str) : Setter du nom de l'hebergement
        set_adresse_hebergement(self, adresse_hebergement: str) : Setter de l'adresse de l'hebergement
        __str__(self) : Méthode d'affichage de la classe Hebergement
    """

    def __init__(self, id_hebergement: int, nom_hebergement: str, adresse_hebergement: str, nb_places_jour: int):
        """
        Constructeur de la classe Hebergement

        Args:
            id_hebergement (int): id de l'hebergement
            nom_hebergement (str): nom de l'hebergement
            adresse_hebergement (str): adresse de l'hebergement
            nb_places_jour (int): nombre de places par jour de l'hebergement
        """
        self.id_hebergement = id_hebergement
        self.nom_hebergement = nom_hebergement
        self.adresse_hebergement = adresse_hebergement
        self.nb_places_jour = nb_places_jour

    def get_id_hebergement(self):
        """
        Getter de l'id de l'hebergement

        Returns:
            int: id de l'hebergement
        """
        return self.id_hebergement

    def get_nom_hebergement(self):
        """
        Getter du nom de l'hebergement

        Returns:
            str: nom de l'hebergement
        """
        return self.nom_hebergement

    def get_adresse_hebergement(self):
        """
        Getter de l'adresse de l'hebergement

        Returns:
            str: adresse de l'hebergement
        """
        return self.adresse_hebergement

    def get_nb_places_jour(self):
        """
        Getter du nombre de places par jour de l'hebergement

        Returns:
            int: nombre de places par jour de l'hebergement
        """
        return self.nb_places_jour

    def set_nb_places_jour(self, nb_places_jour: int):
        """
        Setter du nombre de places par jour de l'hebergement

        Args:
            nb_places_jour (int): nombre de places par jour de l'hebergement
        """
        self.nb_places_jour = nb_places_jour

    def set_nom_hebergement(self, nom_hebergement: str):
        """
        Setter du nom de l'hebergement

        Args:
            nom_hebergement (str): nom de l'hebergement
        """
        self.nom_hebergement = nom_hebergement

    def set_adresse_hebergement(self, adresse_hebergement: str):
        """
        Setter de l'adresse de l'hebergement

        Args:
            adresse_hebergement (str): adresse de l'hebergement
        """

        self.adresse_hebergement = adresse_hebergement

    def __str__(self):
        """
        Méthode d'affichage de la classe Hebergement

        Returns:
            str: Affichage de la classe Hebergement
        """

        return "Hebergement : id_hebergement = " + str(
            self.id_hebergement) + ", nom_hebergement = " + self.nom_hebergement + ", adresse_hebergement = " + self.adresse_hebergement + ", nb_places_jour = " + str(
            self.nb_places_jour)
