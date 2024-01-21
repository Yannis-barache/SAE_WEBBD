from sqlalchemy.sql.expression import text

import sys
import os

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../')
sys.path.append(os.path.join(ROOT, 'modele'))

from groupe import Groupe

class GroupeBD:

    def __init__(self, connexion):
        self.__connexion = connexion

    def get_all_groupes(self):
        try:
            query = text('SELECT idGroupe, nomGroupe, descriptionGroupe, idStyle, photosGroupe, reseauxGroupe, liensVideoGroupe FROM GROUPE')
            result = self.__connexion.execute(query)
            groupes = []
            for id_groupe, nom_groupe, description_groupe, id_style, photos_groupe, reseaux_groupe, liens_video_groupe in result:
                groupes.append(Groupe(id_groupe, nom_groupe, description_groupe, id_style, photos_groupe, reseaux_groupe, liens_video_groupe))
            return groupes
        except Exception as e:
            print(e)
            return None

    def get_groupe_by_id(self, id_groupe):
        try:
            query = text('SELECT idGroupe, nomGroupe, descriptionGroupe, idStyle, photosGroupe, reseauxGroupe, liensVideoGroupe FROM GROUPE WHERE idGroupe = ' + str(id_groupe))
            result = self.__connexion.execute(query)
            for id_groupe, nom_groupe, description_groupe, id_style, photos_groupe, reseaux_groupe, liens_video_groupe in result:
                return Groupe(id_groupe, nom_groupe, description_groupe, id_style, photos_groupe, reseaux_groupe, liens_video_groupe)
        except Exception as e:
            print(e)
            return None


    def ajout_image(self, id_groupe, image):
        try:
            query = text('UPDATE GROUPE SET photosGroupe = ' + str(image) + ' WHERE idGroupe = ' + str(id_groupe))
            self.__connexion.execute(query)
            self.__connexion.commit()
            return True
        except Exception as e:
            print(e)
            return False

    def delete_groupe(self, id_groupe):
        try:
            query = text('DELETE FROM GROUPE WHERE idGroupe = ' + str(id_groupe))
            self.__connexion.execute(query)
            self.__connexion.commit()
            return True
        except Exception as e:
            print(e)
            return False

    def ajout_groupe(self,nom_groupe, description_groupe, id_style, photos_groupe, reseaux_groupe, liens_video_groupe):
        try:
            # On recupère un l'id max pour l'ajout
            query = text('SELECT MAX(idGroupe) FROM GROUPE')
            result = self.__connexion.execute(query)
            for id_groupe in result:
                id_groupe = id_groupe[0] + 1


            query = text('INSERT INTO GROUPE VALUES (' + str(id_groupe) + ', \'' + nom_groupe + '\', \'' + description_groupe + '\', ' + str(id_style) + ', \'' + photos_groupe + '\', \'' + reseaux_groupe + '\', \'' + liens_video_groupe + '\')')
            self.__connexion.execute(query)
            self.__connexion.commit()
            return True
        except Exception as e:
            print(e)
            return False

    def get_groupes_similaires(self, id_style):
        try:
            query = text('SELECT DISTINCT idGroupe, nomGroupe, descriptionGroupe, idStyle, photosGroupe, reseauxGroupe, liensVideoGroupe FROM GROUPE NATURAL JOIN RESSEMBLE WHERE idStyle1 = '+ str(id_style) + ' OR idStyle2 = ' + str(id_style))
            result = self.__connexion.execute(query)
            groupes = []
            for id_groupe, nom_groupe, description_groupe, id_style, photos_groupe, reseaux_groupe, liens_video_groupe in result:
                groupes.append(Groupe(id_groupe, nom_groupe, description_groupe, id_style, photos_groupe, reseaux_groupe, liens_video_groupe))
            return groupes
        except Exception as e:
            print(e)
            return None

    def update_groupe(self, id_groupe, nom_groupe, description_groupe, id_style, photos_groupe, liens_video_groupe):
        try:
            query = text('UPDATE GROUPE SET nomGroupe = \'' + nom_groupe + '\', descriptionGroupe = \'' + description_groupe + '\', idStyle = ' + str(id_style) + ', photosGroupe = \'' + photos_groupe + '\', liensVideoGroupe = \'' + liens_video_groupe + '\' WHERE idGroupe = ' + str(id_groupe))
            self.__connexion.execute(query)
            self.__connexion.commit()
            return True
        except Exception as e:
            print(e)
            return False
    

