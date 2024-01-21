"""
Module comportant la classe Groupe
"""


class Groupe:
    """
    Classe Groupe représentant la table GROUPE de la base de données

    Methods:
        # TODO __init__(self, id_groupe: int, nom_groupe: str, description_groupe: str, id_style: int ,
        photo_groupe: int, reseaux_groupe: List[str], liensVideosGroupe: str) : Constructeur de la classe Groupe

        get_id_groupe(self) : Getter de l'id du groupe get_nom_groupe(self) : Getter du nom du groupe
        get_description_groupe(self) : Getter de la description du groupe get_id_style(self) : Getter de l'id du style du
        groupe get_photo_groupe(self) : Getter de la photo du groupe get_reseaux_groupe(self) : Getter des réseaux du
        groupe get_liens_videos_groupe(self) : Getter des liens vidéos du groupe __str__(self) : Méthode d'affichage de
        la classe Groupe
    """

    def __init__(self, id_groupe: int, nom_groupe: str,
                 description_groupe: str, id_style: int, photo_groupe: str,
                 reseaux_groupe: [str], liens_videos_groupe: str):
        """
        Constructeur de la classe Groupe

        Args:
            id_groupe (int): id du groupe
            nom_groupe (str): nom du groupe
            description_groupe (str): description du groupe
            id_style (int): id du style du groupe
            photo_groupe (List[int]): photo du groupe
            reseaux_groupe (List[str]): réseaux du groupe
            liens_videos_groupe (str): liens vidéos du groupe
        """
        self.id_groupe = id_groupe
        self.nom_groupe = nom_groupe
        self.description_groupe = description_groupe
        self.id_style = id_style
        self.photo_groupe = photo_groupe
        self.reseaux_groupe = reseaux_groupe
        self.liens_videos_groupes = liens_videos_groupe

    def get_id_groupe(self):
        """
        Getter de l'id du groupe

        Returns:
            int: id du groupe
        """
        return self.id_groupe

    def get_nom_groupe(self):
        """
        Getter du nom du groupe

        Returns:
            str: nom du groupe
        """
        return self.nom_groupe

    def get_description_groupe(self):
        """
        Getter de la description du groupe

        Returns:
            str: description du groupe
        """
        return self.description_groupe

    def get_id_style(self):
        """
        Getter de l'id du style du groupe

        Returns:
            int: id du style du groupe
        """
        return self.id_style

    def get_photo_groupe(self):
        """
        Getter de la photo du groupe

        Returns:

        """

        return self.photo_groupe

    def get_reseaux_groupe(self):
        """
        Getter des réseaux du groupe

        Returns:
            List[str]: réseaux du groupe
        """
        return self.reseaux_groupe

    def get_liens_videos_groupe(self):
        """
        Getter des liens vidéos du groupe

        Returns:
            str: liens vidéos du groupe
        """
        return self.liens_videos_groupes

    def set_style(self, id_style):
        """
        Setter du style du groupe

        Args:
            id_style (int): id du style du groupe
        """
        self.id_style = id_style

    def __str__(self):
        """
        Méthode d'affichage de la classe Groupe

        Returns:
            str: informations du groupe
        """
        return "Groupe : id_groupe = " + str(
            self.id_groupe) + " nom_groupe = " + str(
            self.nom_groupe) + " description_groupe = " + str(
            self.description_groupe) + " id_style = " + str(
            self.id_style) + " photo_groupe = " + str(
            self.photo_groupe) + " reseaux_groupe = " + str(
            self.reseaux_groupe
        ) + " liensVideosGroupe = " + str(
            self.liens_videos_groupes)
