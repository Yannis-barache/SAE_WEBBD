"""
Module comportant la classe Aime
"""


class Aime:
    """
    Classe Aime
    """

    def __init__(self, id_aime, id_utilisateur):
        """
        Constructeur de la classe Aime
        """
        self.id_aime = id_aime
        self.id_utilisateur = id_utilisateur

    def __str__(self):
        """
        Méthode d'affichage de la classe Aime
        """
        return "Aime : id_aime = {}, id_utilisateur = {}".format(
            self.id_aime, self.id_utilisateur)
