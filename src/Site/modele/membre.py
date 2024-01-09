"""
Module de la classe Membre
"""


class Membre:
    """
    Classe Membre

    Methods:
        __init__(self, id_membre: int, nom_membre: str, prenom_membre: str, mdp_membre: str, id_groupe: int, instrument :int) : Constructeur de la classe Membre
        get_id_membre(self) : Getter de l'id du membre
        get_nom_membre(self) : Getter du nom du membre
        get_prenom_membre(self) : Getter du prenom du membre
        get_mdp_membre(self) : Getter du mot de passe du membre
        get_email_membre(self) : Getter de l'email du membre
        get_id_groupe(self) : Getter de l'id du groupe du membre
        get_instrument(self) : Getter de l'instrument du membre
        __str__(self) : Méthode d'affichage de la classe Membre
    """

    def __init__(self, id_membre: int, nom_membre: str, prenom_membre: str,
                 mdp_membre: str, email_membre: str, id_groupe: int,
                 instrument: int):
        """
        Constructeur de la classe Membre

        Args:
            id_membre (int): id du membre
            nom_membre (str): nom du membre
            prenom_membre (str): prenom du membre
            mdp_membre (str): mot de passe du membre
            email_membre (str): email du membre
            id_groupe (int): id du groupe du membre
            instrument (int): instrument du membre
        """
        self.id_membre = id_membre
        self.nom_membre = nom_membre
        self.prenom_membre = prenom_membre
        self.mdp_membre = mdp_membre
        self.email_membre = email_membre
        self.id_groupe = id_groupe
        self.instrument = instrument

    def get_id_membre(self):
        """
        Getter de l'id du membre

        Returns:
            int: id du membre
        """
        return self.id_membre

    def get_nom_membre(self):
        """
        Getter du nom du membre

        Returns:
            str: nom du membre
        """
        return self.nom_membre

    def get_prenom_membre(self):
        """
        Getter du prenom du membre

        Returns:
            str: prenom du membre
        """
        return self.prenom_membre

    def get_mdp_membre(self):
        """
        Getter du mot de passe du membre

        Returns:
            str: mot de passe du membre
        """
        return self.mdp_membre

    def get_email_membre(self):
        """
        Getter de l'email du membre

        Returns:
            str: email du membre
        """
        return self.email_membre

    def get_id_groupe(self):
        """
        Getter de l'id du groupe du membre

        Returns:
            int: id du groupe du membre
        """
        return self.id_groupe

    def get_instrument(self):
        """
        Getter de l'instrument du membre

        Returns:
            int: instrument du membre
        """
        return self.instrument

    def __str__(self):
        """
        Méthode d'affichage de la classe Membre

        Returns:
            str: affichage de la classe Membre
        """
        return "Membre : id_membre = " + str(
            self.id_membre
        ) + " nom_membre = " + self.nom_membre + " prenom_membre = " + self.prenom_membre + " mdp_membre = " + self.mdp_membre + " email_membre = " + self.email_membre + " id_groupe = " + str(
            self.id_groupe) + " instrument = " + str(self.instrument)
