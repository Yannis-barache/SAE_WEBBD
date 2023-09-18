DROP TABLE IF EXISTS MEMBRE;
DROP TABLE IF EXISTS LOGER; 
DROP TABLE IF EXISTS PARTICIPE;
DROP TABLE IF EXISTS HEBERGEMENT;
DROP TABLE IF EXISTS TYPES;
DROP TABLE IF EXISTS EVENEMENT;
DROP TABLE IF EXISTS GROUPE;
DROP TABLE IF EXISTS CLIENT;


CREATE TABLE CLIENT (
    idClient int NOT NULL AUTO_INCREMENT,
    nomClient VARCHAR(50) NOT NULL,
    prenomClient VARCHAR(50) NOT NULL,
    emailClient VARCHAR(50) NOT NULL,
    PRIMARY KEY (idClient)
);

CREATE TABLE MEMBRE (
    idMembre int NOT NULL AUTO_INCREMENT,
    nomMembre VARCHAR(50) NOT NULL,
    prenomMembre VARCHAR(50) NOT NULL,
    idGroupe int NOT NULL,
    instrumentMembre VARCHAR(50),    
    PRIMARY KEY (idMembre)
);



CREATE TABLE GROUPE (
    idGroupe int NOT NULL AUTO_INCREMENT,
    nomGroupe VARCHAR(50) NOT NULL,
    descriptionGroupe VARCHAR(50) NOT NULL,
    styleGroupe VARCHAR(50) NOT NULL,
    photosGroupe VARCHAR(50) NOT NULL,
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

CREATE TABLE EVENEMENT (
    idEvenement int NOT NULL AUTO_INCREMENT,
    nomEvenement VARCHAR(50) NOT NULL,
    dateEvenement DATE NOT NULL,
    heureEvenement TIME NOT NULL,
    PRIMARY KEY (idEvenement)
);



-- FOREIGN KEYS à ajouter
ALTER TABLE MEMBRE ADD FOREIGN KEY (idGroupe) REFERENCES  GROUPE(idGroupe);
ALTER TABLE PARTICIPE ADD FOREIGN KEY (idGroupe) REFERENCES  GROUPE(idGroupe);
ALTER TABLE PARTICIPE ADD FOREIGN KEY (idEvenement) REFERENCES  EVENEMENT(idEvenement);
ALTER TABLE LOGER ADD FOREIGN KEY (idHebergement) REFERENCES  HEBERGEMENT(idHebergement);
ALTER TABLE LOGER ADD FOREIGN KEY (idGroupe) REFERENCES  GROUPE(idGroupe);
ALTER TABLE LOGER ADD FOREIGN KEY (idHebergement) REFERENCES  HEBERGEMENT(idHebergement);










