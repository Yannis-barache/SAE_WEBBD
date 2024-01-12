"""
Module qui contient la classe ModeleAppli
"""
from .connexion_bd import ConnexionBD

import sys
import os

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../')
sys.path.append(os.path.join(ROOT, 'modele_bd'))

from aime_bd import AimeBD
from billet_bd import BilletBD
from client_bd import ClientBD
from evenement_bd import EvenementBD
from groupe_bd import GroupeBD
from hebergement_bd import HebergementBD
from instrument_bd import InstrumentBD
from lieu_bd import LieuBD
from loger_bd import LogerBD
from membre_bd import MembreBD
from organisateur_bd import OrganisateurBD
from participe_bd import ParticipeBD
from ressemble_bd import RessembleBD
from sinscrit_bd import SinscritBD
from style_bd import StyleBD
from type_bd import TypeBD


class ModeleAppli:
    

    """
    Classe qui va contenir toutes les façons d'interagir avec la base de données
    
    Méthodes:
        - __init__ : Constructeur de la classe
        - get_aime_bd : Récupère la classe aime_bd
        - get_billet_bd : Récupère la classe billet_bd
        - get_client_bd : Récupère la classe client_bd
        - get_evenement_bd : Récupère la classe evenement_bd
        - get_groupe_bd : Récupère la classe groupe_bd
        - get_hebergement_bd : Récupère la classe hebergement_bd
        - get_instrument_bd : Récupère la classe instrument_bd
        - get_lieu_bd : Récupère la classe lieu_bd
        - get_loger_bd : Récupère la classe loger_bd
        - get_membre_bd : Récupère la classe membre_bd
        - get_organisateur_bd : Récupère la classe organisateur_bd
        - get_participe_bd : Récupère la classe participe_bd
        - get_ressemble_bd : Récupère la classe ressemble_bd
        - get_sinscrit_bd : Récupère la classe sinscrit_bd
        - get_style_bd : Récupère la classe style_bd
        - get_type_bd : Récupère la classe type_bd
    """

    def __init__(self):
        """
        Constructeur de la classe ModeleAppli
        """
        connexion = ConnexionBD()


        self.aime_bd = AimeBD(connexion)
        self.billet_bd = BilletBD(connexion)
        self.client_bd = ClientBD(connexion)
        self.evenement_bd = EvenementBD(connexion)
        self.groupe_bd = GroupeBD(connexion)
        self.hebergement_bd = HebergementBD(connexion)
        self.instrument_bd = InstrumentBD(connexion)
        self.lieu_bd = LieuBD(connexion)
        self.loger_bd = LogerBD(connexion)
        self.membre_bd = MembreBD(connexion)
        self.organisateur_bd = OrganisateurBD(connexion)
        self.participe_bd = ParticipeBD(connexion)
        self.ressemble_bd = RessembleBD(connexion)
        self.sinscrit_bd = SinscritBD(connexion)
        self.style_bd = StyleBD(connexion)
        self.type_bd = TypeBD(connexion)

    def get_aime_bd(self):
        """
        Récupère la classe aime_bd

        Returns:
            aime_bd : La classe aime_bd
        """
        return self.aime_bd

    def get_billet_bd(self):
        """
        Récupère la classe billet_bd

        Returns:
            billet_bd : La classe billet_bd
        """
        return self.billet_bd

    def get_client_bd(self):
        """
        Récupère la classe client_bd

        Returns:
            client_bd : La classe client_bd
        """
        return self.client_bd

    def get_evenement_bd(self):
        """
        Récupère la classe evenement_bd

        Returns:
            evenement_bd : La classe evenement_bd
        """
        return self.evenement_bd

    def get_groupe_bd(self):
        """
        Récupère la classe groupe_bd

        Returns:
            groupe_bd : La classe groupe_bd
        """
        return self.groupe_bd

    def get_hebergement_bd(self):
        """
        Récupère la classe hebergement_bd

        Returns:
            hebergement_bd : La classe hebergement_bd
        """
        return self.hebergement_bd

    def get_instrument_bd(self):
        """
        Récupère la classe instrument_bd

        Returns:
            instrument_bd : La classe instrument_bd
        """
        return self.instrument_bd

    def get_lieu_bd(self):
        """
        Récupère la classe lieu_bd

        Returns:
            lieu_bd : La classe lieu_bd
        """
        return self.lieu_bd

    def get_loger_bd(self):
        """
        Récupère la classe loger_bd

        Returns:
            loger_bd : La classe loger_bd
        """
        return self.loger_bd

    def get_membre_bd(self):
        """
        Récupère la classe membre_bd

        Returns:
            membre_bd : La classe membre_bd
        """
        return self.membre_bd

    def get_organisateur_bd(self):
        """
            Récupère la classe organisateur_bd

            Returns:
                organisateur_bd : La classe organisateur_bd
            """
        return self.organisateur_bd

    def get_participe_bd(self):
        """
                Récupère la classe participe_bd

                Returns:
                    participe_bd : La classe participe_bd
                """
        return self.participe_bd

    def get_ressemble_bd(self):
        """
                Récupère la classe ressemble_bd

                Returns:
                    ressemble_bd : La classe ressemble_bd
                """
        return self.ressemble_bd

    def get_sinscrit_bd(self):
        """
                Récupère la classe sinscrit_bd

                Returns:
                    sinscrit_bd : La classe sinscrit_bd
                """
        return self.sinscrit_bd

    def get_style_bd(self):
        """
                Récupère la classe style_bd

                Returns:
                    style_bd : La classe style_bd
                """
        return self.style_bd

    def get_type_bd(self):
        """
        Récupère la classe type_bd

        Returns:
            type_bd : La classe type_bd
        """
        return self.type_bd
