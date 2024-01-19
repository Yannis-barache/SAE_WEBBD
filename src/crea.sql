CREATE TABLE CLIENT (
    idClient int NOT NULL AUTO_INCREMENT,
    nomClient VARCHAR(50) NOT NULL,
    prenomClient VARCHAR(50) NOT NULL,
    mdpClient VARCHAR(50) NOT NULL,
    emailClient VARCHAR(50) NOT NULL,
    PRIMARY KEY (idClient)
);


CREATE TABLE MEMBRE (
    idMembre int NOT NULL AUTO_INCREMENT,
    nomMembre VARCHAR(50) NOT NULL,
    prenomMembre VARCHAR(50) NOT NULL,
    idGroupe int NOT NULL,
    idInstrument int NOT NULL,
    PRIMARY KEY (idMembre)
);


CREATE TABLE GROUPE (
    idGroupe int NOT NULL AUTO_INCREMENT,
    nomGroupe VARCHAR(50) NOT NULL,
    descriptionGroupe VARCHAR(50) NOT NULL,
    idStyle int NOT NULL,
    photosGroupe VARCHAR(1000),
    reseauxGroupe VARCHAR(50) NOT NULL,
    liensVideoGroupe VARCHAR(50) NOT NULL,
    PRIMARY KEY (idGroupe)
);


CREATE TABLE PARTICIPE (
    idGroupe int NOT NULL,
    idEvenement int NOT NULL,
    dateArriveeGroupe DATE NOT NULL,
    heureArriveeGroupe TIME NOT NULL,
    tempsDeMontage TIME NOT NULL,
    tempsDeDemontage TIME NOT NULL,
    PRIMARY KEY (idGroupe, idEvenement)
);


CREATE TABLE HEBERGEMENT (
    idHebergement int NOT NULL AUTO_INCREMENT,
    nomHebergement VARCHAR(50) NOT NULL,
    adresseHebergement VARCHAR(50) NOT NULL,
    nbPlacesJour int NOT NULL,
    PRIMARY KEY (idHebergement)
);


CREATE TABLE LOGER (
    idHebergement int NOT NULL,
    idGroupe int NOT NULL,
    dateDebutHebergement DATE NOT NULL,
    dateFinHebergement DATE NOT NULL,
    PRIMARY KEY (idHebergement, idGroupe, dateDebutHebergement)
);

CREATE TABLE TYPES (
    idType int NOT NULL AUTO_INCREMENT,
    nomType VARCHAR(50) NOT NULL,
    PRIMARY KEY (idType)
);

CREATE TABLE DATE (
    id_date int NOT NULL,
    dateEvenement DATE NOT NULL,
    PRIMARY KEY (id_date)
);

CREATE TABLE EVENEMENT (
    idEvenement int NOT NULL AUTO_INCREMENT,
    nomEvenement VARCHAR(50) NOT NULL,
    heureEvenement TIME NOT NULL,
    idType int NOT NULL,
    idLieu int NOT NULL,
    id_date int NOT NULL,
    PRIMARY KEY (idEvenement)
);

CREATE TABLE STYLE(
    idStyle int NOT NULL AUTO_INCREMENT,
    nomStyle VARCHAR(50) NOT NULL,
    PRIMARY KEY (idStyle)
);

CREATE TABLE LIEU(
    idLieu int NOT NULL AUTO_INCREMENT,
    nomLieu VARCHAR(50) NOT NULL,
    adresseLieu VARCHAR(50) NOT NULL,
    capaciteLieu int NOT NULL,
    PRIMARY KEY (idLieu)
);

CREATE TABLE BILLET(
    idBillet int NOT NULL AUTO_INCREMENT,
    nomBillet VARCHAR(50) NOT NULL,
    prixBillet int NOT NULL,
  	idClient int NOT NULL,
    PRIMARY KEY (idBillet)
);

CREATE TABLE SINSCRIT(
    idClient int NOT NULL,
    idEvenement int NOT NULL,
    PRIMARY KEY (idClient, idEvenement)
);

CREATE TABLE RESSEMBLE(
    idStyle1 int NOT NULL,
    idStyle2 int NOT NULL,
    PRIMARY KEY (idStyle1, idStyle2)
);

CREATE TABLE AIME(
    idClient int NOT NULL,
    idGroupe int NOT NULL,
    PRIMARY KEY (idClient, idGroupe)
);

CREATE TABLE INSTRUMENT(
    idInstrument int NOT NULL AUTO_INCREMENT,
    nomInstrument VARCHAR(50) NOT NULL,
    PRIMARY KEY (idInstrument)
);

CREATE TABLE ORGANISATEUR(
    idOrganisateur int NOT NULL AUTO_INCREMENT,
    nomOrganisateur VARCHAR(50) NOT NULL,
    prenomOrganisateur VARCHAR(50) NOT NULL,
    mdpOrganisateur VARCHAR(50) NOT NULL,
    emailOrganisateur VARCHAR(50) NOT NULL,
    PRIMARY KEY (idOrganisateur)
);


-- FOREIGN KEYS à ajouter
ALTER TABLE MEMBRE ADD FOREIGN KEY (idGroupe) REFERENCES GROUPE(idGroupe);
ALTER TABLE PARTICIPE ADD FOREIGN KEY (idGroupe) REFERENCES GROUPE(idGroupe);
ALTER TABLE PARTICIPE ADD FOREIGN KEY (idEvenement) REFERENCES EVENEMENT(idEvenement);
ALTER TABLE LOGER ADD FOREIGN KEY (idHebergement) REFERENCES HEBERGEMENT(idHebergement);
ALTER TABLE LOGER ADD FOREIGN KEY (idGroupe) REFERENCES GROUPE(idGroupe);
ALTER TABLE LOGER ADD FOREIGN KEY (idHebergement) REFERENCES HEBERGEMENT(idHebergement);
ALTER TABLE EVENEMENT ADD FOREIGN KEY (idType) REFERENCES TYPES(idType);
ALTER TABLE GROUPE ADD FOREIGN KEY (idStyle) REFERENCES STYLE(idStyle);
ALTER TABLE EVENEMENT ADD FOREIGN KEY (idLieu) REFERENCES LIEU(idLieu);
ALTER TABLE BILLET ADD FOREIGN KEY (idClient) REFERENCES CLIENT(idClient);
ALTER TABLE RESSEMBLE ADD FOREIGN KEY (idStyle1) REFERENCES STYLE(idStyle);
ALTER TABLE RESSEMBLE ADD FOREIGN KEY (idStyle2) REFERENCES STYLE(idStyle);
ALTER TABLE SINSCRIT ADD FOREIGN KEY (idClient) REFERENCES CLIENT(idClient);
ALTER TABLE SINSCRIT ADD FOREIGN KEY (idEvenement) REFERENCES EVENEMENT(idEvenement);
ALTER TABLE AIME ADD FOREIGN KEY (idClient) REFERENCES CLIENT(idClient);
ALTER TABLE AIME ADD FOREIGN KEY (idGroupe) REFERENCES GROUPE(idGroupe);
ALTER TABLE MEMBRE ADD FOREIGN KEY (idInstrument) REFERENCES INSTRUMENT(idInstrument);
ALTER TABLE EVENEMENT ADD FOREIGN KEY (id_date) REFERENCES DATE(id_date);
ALTER TABLE EVENEMENT ADD FOREIGN KEY (id_date) REFERENCES DATE(id_date);

-- A changer dans le MCD : association loger --> ajouter une table date qui contient les dates et les durees
-- revoir le systeme de billets

-- Triggers : ----------------------------------------------------------

-- verifNbBillets : Vérifie que chaque utilisateur n’achète pas plus de 3 billets. 
delimiter |
CREATE OR REPLACE TRIGGER verifNbBillets BEFORE INSERT ON BILLET
FOR EACH ROW
BEGIN
    IF (SELECT COUNT(*) FROM BILLET WHERE idClient = NEW.idClient) >= 3 THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Vous ne pouvez pas acheter plus de 3 billets';
    END IF;
END |
delimiter ;

-- verifCapacite : Vérifie que la capacité du lieu n’est pas dépassée chaque fois qu’un utilisateur s’inscrit à un concert.
delimiter |
CREATE OR REPLACE TRIGGER verifCapacite BEFORE INSERT ON SINSCRIT
FOR EACH ROW
BEGIN
    IF (SELECT COUNT(*) FROM SINSCRIT WHERE idEvenement = NEW.idEvenement) >= (SELECT capaciteLieu FROM LIEU WHERE idLieu = (SELECT idLieu FROM EVENEMENT WHERE idEvenement = NEW.idEvenement)) THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'La capacité du lieu est atteinte';
    END IF;
END |
delimiter ;

-- verifCapaciteHebergement : Vérifie que la capacité de l’hébergement n’est pas dépassée chaque fois qu’un groupe est logé.
delimiter |
CREATE OR REPLACE TRIGGER verifCapaciteHebergement BEFORE INSERT ON LOGER
FOR EACH ROW
BEGIN
    IF (SELECT COUNT(*) FROM LOGER WHERE idHebergement = NEW.idHebergement) >= (SELECT nbPlacesJour FROM HEBERGEMENT WHERE idHebergement = NEW.idHebergement) THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'La capacité de l''hébergement est atteinte';
    END IF;
END |
delimiter ;

-- verifEvenement : Vérifie qu’il n’y a pas de conflits d’événements chaque fois qu’un nouvel événement est ajouté.
delimiter |
CREATE OR REPLACE TRIGGER verifEvenement BEFORE INSERT ON EVENEMENT
FOR EACH ROW
BEGIN
    IF (SELECT COUNT(*) FROM EVENEMENT WHERE idLieu = NEW.idLieu AND id_date = NEW.id_date AND heureEvenement = NEW.heureEvenement) >= 1 THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Un événement se déroule déjà à cette date et à cette heure';
    END IF;
END |

-- VerifierHebergement : Vérifie qu’il n’y a pas de conflits d’hébergement chaque fois qu’un groupe est logé.
DELIMITER |
CREATE TRIGGER VerifierHebergement
BEFORE INSERT ON LOGER
FOR EACH ROW
BEGIN
    DECLARE conflit INT;
    SELECT COUNT(*) INTO conflit
    FROM LOGER
    WHERE idHebergement = NEW.idHebergement AND idGroupe = NEW.idGroupe AND dateDebutHebergement = NEW.dateDebutHebergement AND dateFinHebergement = NEW.dateFinHebergement;
    IF conflit > 0 THEN 
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Conflit dhébergement détecté. Le même groupe ne peut pas être logé au même endroit au même moment.';
    END IF;
END;|
DELIMITER ;

-- VérifierDisponibilitéBillet : Vérifie la disponibilité des billets chaque fois qu’un utilisateur tente d’acheter un billet.
delimiter |
CREATE OR REPLACE TRIGGER VerifierDisponibiliteBillet
BEFORE INSERT ON BILLET
FOR EACH ROW
BEGIN
    DECLARE nbBillets INT;
    SELECT COUNT(*) INTO nbBillets
    FROM BILLET
    WHERE idBillet = NEW.idBillet;
    IF nbBillets > 0 THEN 
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Il n''y a plus de billets disponibles pour ce concert.';
    END IF;
END |
delimiter ;



-- VerifierProgrammation : Vérifie qu’il n’y a pas de conflits dans la programmation chaque fois qu’un nouveau concert est ajouté.
DELIMITER |
CREATE TRIGGER VerifierProgrammation
BEFORE INSERT ON PARTICIPE
FOR EACH ROW
BEGIN
    DECLARE conflit INT;
    SELECT COUNT(*) INTO conflit
    FROM PARTICIPE
    WHERE idGroupe = NEW.idGroupe AND dateArriveeGroupe = NEW.dateArriveeGroupe AND heureArriveeGroupe = NEW.heureArriveeGroupe;
    IF conflit > 0 THEN 
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Conflit de programmation détecté. Le même groupe ne peut pas être programmé pour jouer à la même date et heure.';
    END IF;
END;|
DELIMITER ;

-- VérifierInscription : Vérifie qu’un utilisateur ne s’inscrit pas deux fois au même concert.
delimiter |
CREATE OR REPLACE TRIGGER VerifierInscription
BEFORE INSERT ON SINSCRIT
FOR EACH ROW
BEGIN
    DECLARE conflit INT;
    SELECT COUNT(*) INTO conflit
    FROM SINSCRIT
    WHERE idClient = NEW.idClient AND idEvenement = NEW.idEvenement;
    IF conflit > 0 THEN 
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Vous êtes déjà inscrit à ce concert.';
    END IF;
END |
delimiter ;

-- VérifierFavoris : Vérifie qu’un utilisateur n’ajoute pas deux fois le même groupe à ses favoris.
delimiter |
CREATE OR REPLACE TRIGGER VerifierFavoris
BEFORE INSERT ON AIME
FOR EACH ROW
BEGIN
    DECLARE conflit INT;
    SELECT COUNT(*) INTO conflit
    FROM AIME
    WHERE idClient = NEW.idClient AND idGroupe = NEW.idGroupe;
    IF conflit > 0 THEN 
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Vous avez déjà ajouté ce groupe à vos favoris.';
    END IF;
END |
delimiter ;

-- VérifierRessemblance : Vérifie qu’il n’y a pas de ressemblance entre deux styles musicaux déjà existante.
delimiter |
CREATE OR REPLACE TRIGGER VerifierRessemblance
BEFORE INSERT ON RESSEMBLE
FOR EACH ROW
BEGIN
    DECLARE conflit INT;
    SELECT COUNT(*) INTO conflit
    FROM RESSEMBLE
    WHERE idStyle1 = NEW.idStyle1 AND idStyle2 = NEW.idStyle2;
    IF conflit > 0 THEN 
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Ces deux styles musicaux sont déjà ressemblants.';
    END IF;
END |
delimiter ;

-- VérifierStyle : Vérifie qu’il n’y a pas de style musical déjà existant.
delimiter |
CREATE OR REPLACE TRIGGER VerifierStyle
BEFORE INSERT ON STYLE
FOR EACH ROW
BEGIN
    DECLARE conflit INT;
    SELECT COUNT(*) INTO conflit
    FROM STYLE
    WHERE nomStyle = NEW.nomStyle;
    IF conflit > 0 THEN 
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Ce style musical existe déjà.';
    END IF;
END |
delimiter ;

-- VérifierLieu : Vérifie qu’il n’y a pas de lieu déjà existant.
delimiter |
CREATE OR REPLACE TRIGGER VerifierLieu
BEFORE INSERT ON LIEU
FOR EACH ROW
BEGIN
    DECLARE conflit INT;
    SELECT COUNT(*) INTO conflit
    FROM LIEU
    WHERE nomLieu = NEW.nomLieu;
    IF conflit > 0 THEN 
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Ce lieu existe déjà.';
    END IF;
END |
delimiter ;

-- VérifierType : Vérifie qu’il n’y a pas de type de concert déjà existant.
delimiter |
CREATE OR REPLACE TRIGGER VerifierType
BEFORE INSERT ON TYPES
FOR EACH ROW
BEGIN
    DECLARE conflit INT;
    SELECT COUNT(*) INTO conflit
    FROM TYPES
    WHERE nomType = NEW.nomType;
    IF conflit > 0 THEN 
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Ce type de concert existe déjà.';
    END IF;
END |
delimiter ;

-- VérifierGroupe : Vérifie qu’il n’y a pas de groupe déjà existant.
delimiter |
CREATE OR REPLACE TRIGGER VerifierGroupe
BEFORE INSERT ON GROUPE
FOR EACH ROW
BEGIN
    DECLARE conflit INT;
    SELECT COUNT(*) INTO conflit
    FROM GROUPE
    WHERE nomGroupe = NEW.nomGroupe;
    IF conflit > 0 THEN 
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Ce groupe existe déjà.';
    END IF;
END |
delimiter ;

-- VérifierMembre : Vérifie qu’il n’y a pas de membre déjà existant.
delimiter |
CREATE OR REPLACE TRIGGER VerifierMembre
BEFORE INSERT ON MEMBRE
FOR EACH ROW
BEGIN
    DECLARE conflit INT;
    SELECT COUNT(*) INTO conflit
    FROM MEMBRE
    WHERE nomMembre = NEW.nomMembre AND prenomMembre = NEW.prenomMembre;
    IF conflit > 0 THEN 
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Ce membre existe déjà.';
    END IF;
END |
delimiter ;

-- VérifieremailClient : Vérifie qu’il n’y a pas d’utilisateur déjà existant avec la même adresse mail.
delimiter |
CREATE OR REPLACE TRIGGER VerifieremailClient
BEFORE INSERT ON CLIENT
FOR EACH ROW
BEGIN
    DECLARE conflit INT;
    SELECT COUNT(*) INTO conflit
    FROM CLIENT
    WHERE emailClient = NEW.emailClient;
    IF conflit > 0 THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Un utilisateur existe déjà avec cette adresse mail.';
    END IF;
END |

-- VérifieremailOrganisateur : Vérifie qu’il n’y a pas d’organisateur déjà existant avec la même adresse mail.
delimiter |
CREATE OR REPLACE TRIGGER VerifieremailOrganisateur
BEFORE INSERT ON ORGANISATEUR
FOR EACH ROW
BEGIN
    DECLARE conflit INT;
    SELECT COUNT(*) INTO conflit
    FROM ORGANISATEUR
    WHERE emailOrganisateur = NEW.emailOrganisateur;
    IF conflit > 0 THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Un organisateur existe déjà avec cette adresse mail.';
    END IF;
END |
delimiter ;

-- SupprimerDependancesGroupe : Supprime toutes les lignes dont d'autres tables dépendent lorsqu'un groupe est supprimé.
delimiter |
CREATE OR REPLACE TRIGGER SupprimerDependancesGroupe
BEFORE DELETE ON GROUPE
FOR EACH ROW
BEGIN
    DELETE FROM MEMBRE WHERE idGroupe = OLD.idGroupe;
    DELETE FROM AIME WHERE idGroupe = OLD.idGroupe;
    DELETE FROM PARTICIPE WHERE idGroupe = OLD.idGroupe;
    DELETE FROM LOGER WHERE idGroupe = OLD.idGroupe;
END |
delimiter ;

-- SupprimerDependancesClients : Supprime toutes les lignes dont d'autres tables dépendent lorsqu'un utilisateur est supprimé.
delimiter |
CREATE OR REPLACE TRIGGER SupprimerDependancesClients
BEFORE DELETE ON CLIENT
FOR EACH ROW
BEGIN
    DELETE FROM AIME WHERE idClient = OLD.idClient;
    DELETE FROM BILLET WHERE idClient = OLD.idClient;
    DELETE FROM SINSCRIT WHERE idClient = OLD.idClient;
END |

-- SupprimerDependancesHebergement : Supprime toutes les lignes dont d'autres tables dépendent lorsqu'un hébergement est supprimé.
delimiter |
CREATE OR REPLACE TRIGGER SupprimerDependancesHebergement
BEFORE DELETE ON HEBERGEMENT
FOR EACH ROW
BEGIN
    DELETE FROM LOGER WHERE idHebergement = OLD.idHebergement;
END |
delimiter ;

-- SupprimerDependancesEvenement : Supprime toutes les lignes dont d'autres tables dépendent lorsqu'un concert est supprimé.
delimiter |
CREATE OR REPLACE TRIGGER SupprimerDependancesEvenement
BEFORE DELETE ON EVENEMENT
FOR EACH ROW
BEGIN
    DELETE FROM PARTICIPE WHERE idEvenement = OLD.idEvenement;
    DELETE FROM SINSCRIT WHERE idEvenement = OLD.idEvenement;
END |
-- Fonctions : -----------------------------------------------------------

-- Une fonction pour afficher la programmation par jour, lieu et artiste en MySQL.
delimiter |
CREATE OR REPLACE FUNCTION ConsulterProgrammation (type VARCHAR(50), id int) RETURNS VARCHAR(50)
BEGIN
    DECLARE result VARCHAR(50);
    IF type = 'jour' THEN
        SELECT nomEvenement INTO result
        FROM EVENEMENT
        WHERE dateEvenement = id;
    ELSEIF type = 'lieu' THEN
        SELECT nomEvenement INTO result
        FROM EVENEMENT
        WHERE idLieu = id;
    ELSEIF type = 'artiste' THEN
        SELECT nomEvenement INTO result
        FROM EVENEMENT
        WHERE idEvenement = id;
    END IF;
    RETURN result;
END |
delimiter ;

-- Une fonction pour permettre aux utilisateurs de rechercher des groupes par style musical.
delimiter |
CREATE OR REPLACE FUNCTION RechercherGroupeParStyle (style VARCHAR(50)) RETURNS VARCHAR(50)
BEGIN
    DECLARE result VARCHAR(50);
    SELECT nomGroupe INTO result
    FROM GROUPE
    WHERE idStyle = (SELECT idStyle FROM STYLE WHERE nomStyle = style);
    RETURN result;
END |
delimiter ;

-- Une fonction pour gérer les groupes favoris des utilisateurs.
delimiter |
CREATE OR REPLACE FUNCTION ConsulterGroupesFavoris (idClient int) RETURNS VARCHAR(50)
BEGIN
    DECLARE result VARCHAR(50);
    SELECT nomGroupe INTO result
    FROM GROUPE
    WHERE idGroupe = (SELECT idGroupe FROM AIME WHERE idClient = idClient);
    RETURN result;
END |
delimiter ;

-- Une fonction pour recommander des groupes similaires lors de la consultation d’un groupe.
delimiter |
CREATE OR REPLACE FUNCTION SuggererGroupes (idGroupe int) RETURNS VARCHAR(50)
BEGIN
    DECLARE result VARCHAR(50);
    SELECT nomGroupe INTO result
    FROM GROUPE
    WHERE idStyle = (SELECT idStyle FROM GROUPE WHERE idGroupe = idGroupe);
    RETURN result;
END |
delimiter ;
-- Une fonction pour afficher les informations d’arrivée et de départ, la durée du concert, le temps de montage et de démontage, et l’hébergement pour chaque groupe.
delimiter |
CREATE OR REPLACE FUNCTION ConsulterInfosGroupe (idGroupe int) RETURNS VARCHAR(50)
BEGIN
    DECLARE result VARCHAR(50);
    SELECT dateArriveeGroupe, heureArriveeGroupe, tempsDeMontage, tempsDeDemontage INTO result
    FROM PARTICIPE
    WHERE idGroupe = idGroupe;
    RETURN result;
END |
delimiter ;

-- Procédures : ------------------------------------------------
-- AjouterGroupe : Ajoute un nouveau groupe à la base de données avec toutes les informations nécessaires (description, photos, liens réseaux sociaux, liens vidéo, membres du groupe et instruments joués, etc.).
delimiter |
CREATE OR REPLACE PROCEDURE AjouterGroupe (nomGroupe VARCHAR(50), descriptionGroupe VARCHAR(50), idStyle int, photosGroupe VARCHAR(50), reseauxGroupe VARCHAR(50), liensVideoGroupe VARCHAR(50), nomMembre VARCHAR(50), prenomMembre VARCHAR(50), instrumentMembre VARCHAR(50))
BEGIN
    INSERT INTO GROUPE (nomGroupe, descriptionGroupe, idStyle, photosGroupe, reseauxGroupe, liensVideoGroupe) VALUES (nomGroupe, descriptionGroupe, idStyle, photosGroupe, reseauxGroupe, liensVideoGroupe);
    INSERT INTO MEMBRE (nomMembre, prenomMembre, idInstrument) VALUES (nomMembre, prenomMembre, instrumentMembre);
END |
delimiter ;

-- AjouterConcert : Ajoute un nouveau concert à la programmation du festival.
delimiter |
CREATE OR REPLACE PROCEDURE AjouterConcert (nomEvenement VARCHAR(50), dateEvenement DATE, heureEvenement TIME, idType int, idLieu int)
BEGIN
    INSERT INTO EVENEMENT (nomEvenement, dateEvenement, heureEvenement, idType, idLieu) VALUES (nomEvenement, dateEvenement, heureEvenement, idType, idLieu);
END |
delimiter ;
-- AcheterBillet : Permet à un spectateur d’acheter un billet pour le festival.
delimiter |
CREATE OR REPLACE PROCEDURE AcheterBillet (nomBillet VARCHAR(50), prixBillet int, idClient int)
BEGIN
    INSERT INTO BILLET (nomBillet, prixBillet, idClient) VALUES (nomBillet, prixBillet, idClient);
END |
delimiter ;
-- InscrireSpectateur : Inscrire un spectateur à un concert spécifique.
delimiter |
CREATE OR REPLACE PROCEDURE InscrireSpectateur (idClient int, idEvenement int)
BEGIN
    INSERT INTO SINSCRIT (idClient, idEvenement) VALUES (idClient, idEvenement);
END |
delimiter ;

-- LogerGroupe : Loger un groupe dans un hébergement spécifique.
delimiter |
CREATE OR REPLACE PROCEDURE LogerGroupe (idHebergement int, idGroupe int, dateDebutHebergement DATE, dateFinHebergement DATE)
BEGIN
    INSERT INTO LOGER (idHebergement, idGroupe, dateDebutHebergement, dateFinHebergement) VALUES (idHebergement, idGroupe, dateDebutHebergement, dateFinHebergement);
END |
delimiter ;

-- SupprimerGroupe : Supprimer un groupe de la base de données.
delimiter |
CREATE OR REPLACE PROCEDURE SupprimerGroupe (idGroupe int)
BEGIN
    DELETE FROM GROUPE WHERE idGroupe = idGroupe;
END |
delimiter ;

-- SupprimerConcert : Supprimer un concert de la programmation du festival.
delimiter |
CREATE OR REPLACE PROCEDURE SupprimerConcert (idEvenement int)
BEGIN
    DELETE FROM EVENEMENT WHERE idEvenement = idEvenement;
END |
delimiter ;

-- SupprimerBillet : Supprimer un billet de la base de données.
delimiter |
CREATE OR REPLACE PROCEDURE SupprimerBillet (idBillet int)
BEGIN
    DELETE FROM BILLET WHERE idBillet = idBillet;
END |
delimiter ;

-- SupprimerSpectateur : Supprimer un spectateur de la base de données.
delimiter |
CREATE OR REPLACE PROCEDURE SupprimerSpectateur (idClient int)
BEGIN
    DELETE FROM CLIENT WHERE idClient = idClient;
END |
delimiter ;

-- SupprimerMembre : Supprimer un membre d’un groupe.
delimiter |
CREATE OR REPLACE PROCEDURE SupprimerMembre (idMembre int)
BEGIN
    DELETE FROM MEMBRE WHERE idMembre = idMembre;
END |
delimiter ;

-- SupprimerHebergement : Supprimer un hébergement de la base de données.
delimiter |
CREATE OR REPLACE PROCEDURE SupprimerHebergement (idHebergement int)
BEGIN
    DELETE FROM HEBERGEMENT WHERE idHebergement = idHebergement;
END |
delimiter ;

-- SupprimerInscription : Supprimer l’inscription d’un spectateur à un concert.
delimiter |
CREATE OR REPLACE PROCEDURE SupprimerInscription (idClient int, idEvenement int)
BEGIN
    DELETE FROM SINSCRIT WHERE idClient = idClient AND idEvenement = idEvenement;
END |
delimiter ;

-- SupprimerLogement : Supprimer le logement d’un groupe.
delimiter |
CREATE OR REPLACE PROCEDURE SupprimerLogement (idHebergement int, idGroupe int, dateDebutHebergement DATE)
BEGIN
    DELETE FROM LOGER WHERE idHebergement = idHebergement AND idGroupe = idGroupe AND dateDebutHebergement = dateDebutHebergement;
END |
delimiter ;

-- SupprimerParticipation : Supprimer la participation d’un groupe à un concert.
delimiter |
CREATE OR REPLACE PROCEDURE SupprimerParticipation (idGroupe int, idEvenement int)
BEGIN
    DELETE FROM PARTICIPE WHERE idGroupe = idGroupe AND idEvenement = idEvenement;
END |
delimiter ;

-- SupprimerStyle : Supprimer un style musical de la base de données.
delimiter |
CREATE OR REPLACE PROCEDURE SupprimerStyle (idStyle int)
BEGIN
    DELETE FROM STYLE WHERE idStyle = idStyle;
END |
delimiter ;

-- SupprimerLieu : Supprimer un lieu de la base de données.
delimiter |
CREATE OR REPLACE PROCEDURE SupprimerLieu (idLieu int)
BEGIN
    DELETE FROM LIEU WHERE idLieu = idLieu;
END |
delimiter ;

-- SupprimerType : Supprimer un type de concert de la base de données.
delimiter |
CREATE OR REPLACE PROCEDURE SupprimerType (idType int)
BEGIN
    DELETE FROM TYPES WHERE idType = idType;
END |
delimiter ;

-- SupprimerRessemblanceStyle : Supprimer une ressemblance entre deux styles musicaux.
delimiter |
CREATE OR REPLACE PROCEDURE SupprimerRessemblanceStyle (idStyle1 int, idStyle2 int)
BEGIN
    DELETE FROM RESSEMBLE WHERE idStyle1 = idStyle1 AND idStyle2 = idStyle2;
END |
delimiter ;

-- SupprimerFavoris : Supprimer un groupe des favoris d’un utilisateur.
delimiter |
CREATE OR REPLACE PROCEDURE SupprimerFavoris (idClient int, idGroupe int)
BEGIN
    DELETE FROM AIME WHERE idClient = idClient AND idGroupe = idGroupe;
END |
delimiter ;