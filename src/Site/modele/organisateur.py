"""
Module de la classe Organisateur
"""


class Organisateur:
    """
    Classe Organisateur

    Methods:
        __init__(self, id_organisateur: int, nom_organisateur: str, prenom_organisateur: str, mdp_organisateur: str, email_organisateur: str) : Constructeur de la classe Organisateur
        get_id(self) : Getter de l'id de l'organisateur
        get_nom(self) : Getter du nom de l'organisateur
        get_prenom(self) : Getter du prenom de l'organisateur
        get_mdp(self) : Getter du mot de passe de l'organisateur
        get_email_organisateur(self) : Getter de l'email de l'organisateur
        set_nom_organisateur(self, nom_organisateur: str) : Setter du nom de l'organisateur
        set_prenom_organisateur(self, prenom_organisateur: str) : Setter du prenom de l'organisateur
        set_mdp_organisateur(self, mdp_organisateur: str) : Setter du mot de passe de l'organisateur
        set_email_organisateur(self, email_organisateur: str) : Setter de l'email de l'organisateur
        __str__(self) : Méthode d'affichage de la classe Organisateur
    """

    def __init__(self, id_organisateur: int, nom_organisateur: str,
                 prenom_organisateur: str, mdp_organisateur: str,
                 email_organisateur: str):
        """
        Constructeur de la classe Organisateur

        Args:
            id_organisateur (int): id de l'organisateur
            nom_organisateur (str): nom de l'organisateur
            prenom_organisateur (str): prenom de l'organisateur
            mdp_organisateur (str): mot de passe de l'organisateur
            email_organisateur (str): email de l'organisateur
        """
        self.id = id_organisateur
        self.nom_organisateur = nom_organisateur
        self.prenom_organisateur = prenom_organisateur
        self.mdp_organisateur = mdp_organisateur
        self.email_organisateur = email_organisateur

    def get_id(self):
        """
        Getter de l'id de l'organisateur

        Returns:
            int: id de l'organisateur
        """
        return self.id

    def get_nom(self):
        """
        Getter du nom de l'organisateur

        Returns:
            str: nom de l'organisateur
        """
        return self.nom_organisateur

    def get_prenom(self):
        """
        Getter du prenom de l'organisateur

        Returns:
            str: prenom de l'organisateur
        """
        return self.prenom_organisateur

    def get_mdp(self):
        """
        Getter du mot de passe de l'organisateur

        Returns:
            str: mot de passe de l'organisateur
        """
        return self.mdp_organisateur

    def get_email(self):
        """
        Getter de l'email de l'organisateur

        Returns:
            str: email de l'organisateur
        """
        return self.email_organisateur

    def set_nom_organisateur(self, nom_organisateur: str):
        """
        Setter du nom de l'organisateur

        Args:
            nom_organisateur (str): nom de l'organisateur
        """
        self.nom_organisateur = nom_organisateur

    def set_prenom_organisateur(self, prenom_organisateur: str):
        """
        Setter du prenom de l'organisateur

        Args:
            prenom_organisateur (str): prenom de l'organisateur
        """
        self.prenom_organisateur = prenom_organisateur

    def set_mdp_organisateur(self, mdp_organisateur: str):
        """
        Setter du mot de passe de l'organisateur

        Args:
            mdp_organisateur (str): mot de passe de l'organisateur
        """
        self.mdp_organisateur = mdp_organisateur

    def set_email_organisateur(self, email_organisateur: str):
        """
        Setter de l'email de l'organisateur

        Args:
            email_organisateur (str): email de l'organisateur
        """
        self.email_organisateur = email_organisateur

    def __str__(self):
        """
        Méthode d'affichage de la classe Organisateur
        """
        return self.nom_organisateur + " " + self.prenom_organisateur
