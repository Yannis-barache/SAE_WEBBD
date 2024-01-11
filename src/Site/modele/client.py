"""
Module comportant la classe Client
"""


class Client:
    """ Classe Client

    Methods:
        __init__(self, id_client: int, nom_client: str, prenom_client: str, mdp_client: str, email_client: str) : Constructeur de la classe Client
        get_id_client(self) : Getter de l'id du client
        get_nom_client(self) : Getter du nom du client
        get_prenom_client(self) : Getter du prenom du client
        get_mdp_client(self) : Getter du mot de passe du client
        get_email_client(self) : Getter de l'email du client
        __str__(self) : Méthode d'affichage de la classe Client
    """

    def __init__(self, id_client: int, nom_client: str, prenom_client: str,
                 mdp_client: str, email_client: str):
        """
        Constructeur de la classe Client

        Args:
            id_client (int): id du client
            nom_client (str): nom du client
            prenom_client (str): prenom du client
            mdp_client (str): mot de passe du client
            email_client (str): email du client
        """
        self.id_client = id_client
        self.nom_client = nom_client
        self.prenom_client = prenom_client
        self.mdp_client = mdp_client
        self.email_client = email_client

    def get_id_client(self):
        """
        Getter de l'id du client

        Returns:
            int: id du client
        """
        return self.id_client

    def get_nom_client(self):
        """
        Getter du nom du client

        Returns:
            str: nom du client
        """
        return self.nom_client

    def get_prenom_client(self):
        """
        Getter du prenom du client

        Returns:
            str: prenom du client
        """
        return self.prenom_client

    def get_mdp_client(self):
        """
        Getter du mot de passe du client

        Returns:
            str: mot de passe du client
        """
        return self.mdp_client

    def get_email_client(self):
        """
        Getter de l'email du client

        Returns:
            str: email du client
        """
        return self.email_client

    def __str__(self):
        """
        Méthode d'affichage de la classe Client

        Returns:
            str: affichage de la classe Client
        """
        return "Client : id_client = " + str(
            self.id_client
        ) + ", nom_client = " + self.nom_client + ", prenom_client = " + self.prenom_client + ", mdp_client = " + self.mdp_client + ", email_client = " + self.email_client
