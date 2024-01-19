INSERT INTO STYLE (idStyle,nomStyle) VALUES 
(1,'Rock'),
(2,'Pop'),
(3,'Rap'),
(4,'Classique'),
(5,'Jazz'),
(6,'Electro'),
(7,'Reggae'),
(8,'RnB'),
(9,'Soul'),
(10,'Funk'),
(11,'Country');


INSERT INTO GROUPE (idGroupe,nomGroupe,descriptionGroupe,idStyle,photosGroupe,reseauxGroupe,liensVideoGroupe) VALUES
(1,'The Beatles','Groupe de rock britannique',1,NULL,'Facebook, Twitter','https://www.youtube.com/watch?v=z9ypq6_5bsg'),
(2,'Daft Punk','Groupe de musique électronique français',6,NULL,'Facebook, Instagram','https://www.youtube.com/watch?v=FGBhQbmPwH8'),
(3,'Nirvana','Groupe de rock américain',1,NULL,'Facebook, Twitter','https://www.youtube.com/watch?v=hTWKbfoikeg'),
(4,'Queen','Groupe de rock britannique',1,NULL,'Facebook, Instagram','https://www.youtube.com/watch?v=fJ9rUzIMcZQ'),
(5,'The Rolling Stones','Groupe de rock britannique',1,NULL,'Facebook, Twitter','https://www.youtube.com/watch?v=6DUnOupJz7Q'),
(6,'Zouhair Bahaoui', 'Chanteur marocain', 3,NULL, 'Facebook, Instagram', 'https://www.youtube.com/watch?v=6DUnOupJz7Q'),
(7,'Eminem','Rappeur américain',3,NULL,'Facebook, Instagram','https://www.youtube.com/watch?v=uelHwf8o7_U'),
(8,'AC/DC','Groupe de rock australien',1,NULL,'Facebook, Twitter','https://www.youtube.com/watch?v=v2AC41dglnM'),
(9,'Metallica','Groupe de heavy metal américain',1,NULL,'Facebook, Instagram','https://www.youtube.com/watch?v=CD-E-LDc384'),
(10,'Pink Floyd','Groupe de rock britannique',4,NULL,'Facebook, Twitter','https://www.youtube.com/watch?v=JwYX52BP2Sk');


INSERT INTO TYPES (idType,nomType) VALUES
(1,'Concert'),
(2,'Spectacle'),
(3,'Autre');


INSERT INTO LIEU (idLieu,nomLieu,adresseLieu,capaciteLieu) VALUES
(1, 'Scène Rouge', '1 rue de la scène rouge', 1000),
(2, 'Scène Bleue', '2 rue de la scène bleue', 2000),
(3, 'Scène Verte', '3 rue de la scène verte', 3000),
(4, 'Scène Jaune', '4 rue de la scène jaune', 4000),
(5, 'Scène Orange', '5 rue de la scène orange', 5000),
(6, 'Scène Violette', '6 rue de la scène violette', 6000),
(7, 'Scène Rose', '7 rue de la scène rose', 7000),
(8, 'Scène Blanche', '8 rue de la scène blanche', 8000),
(9, 'Scène Noire', '9 rue de la scène noire', 9000),
(10, 'Scène Marron', '10 rue de la scène marron', 10000);

INSERT INTO DATE(id_date, dateEvenement) VALUES
        (1,'2024-03-22'),
        (2,'2024-03-23'),
        (3,'2024-03-24');


INSERT INTO EVENEMENT (idEvenement, nomEvenement, id_date, heureEvenement, idType, idLieu) VALUES
(1, 'Concert de Queen', 1, '19:00:00', 1, 1),
(2, 'Concert de Daft Punk', 1, '20:00:00', 1, 8),
(3, 'Concert de Nirvana', 2, '20:00:00', 1, 9),
(4, 'Concert de The Beatles', 2, '20:00:00', 1, 2),
(5, 'Concert de The Rolling Stones', 3, '20:00:00', 1, 4),
(6, 'Concert de Zouhair Bahaoui', 1, '20:00:00', 1, 3);


INSERT INTO HEBERGEMENT (idHebergement, nomHebergement, adresseHebergement, nbPlacesJour) VALUES
(1, 'Hôtel de la gare', '1 rue de la gare', 50),
(2, 'Hôtel du centre', '2 rue du centre', 100),
(3, 'Hôtel de la plage', '3 rue de la plage', 150),
(4, 'Hôtel de la montagne', '4 rue de la montagne', 200),
(5, 'Hôtel de la forêt', '5 rue de la forêt', 250),
(6, 'Hôtel de la rivière', '6 rue de la rivière', 300),
(7, 'Hôtel de la vallée', '7 rue de la vallée', 350),
(8, 'Hôtel de la mer', '8 rue de la mer', 400),
(9, 'Hôtel de la campagne', '9 rue de la campagne', 450),
(10, 'Hôtel de la ville', '10 rue de la ville', 500);


INSERT INTO CLIENT (idClient, nomClient, prenomClient, mdpClient, emailClient) VALUES
(1, 'Dupont', 'Jean','yolopass1234' ,'dupont.jean@mail.fr'),
(2, 'Durand', 'Pierre','yolopass1234', 'durand.pierre@mail.fr'),
(3, 'Martin', 'Paul','yolopass1234', 'martin.paul@mail.fr'),
(4, 'Bernard', 'Jacques','yolopass1234', 'bernard.jaques@mail.fr'),
(5, 'Dubois', 'Michel','yolopass1234', 'dubois.michel@mail.fr'),
(6, 'Thomas', 'Robert','yolopass1234', 'thomas.robert@mail.fr'),
(7, 'Robert', 'Richard','yolopass1234', 'robert.richard@mail.fr'),
(8, 'Richard', 'Jean','yolopass1234', 'richard.jean@mail.fr');


INSERT INTO INSTRUMENT(idInstrument, nomInstrument) VALUES
(1,'Guitare'),
(2,'Basse'),
(3,'Batterie'),
(4,'Synthétiseur'),
(5,'Chant'),
(6,'Clavier'),
(7,'Piano'),
(8,'Violon'),
(9,'Violoncelle'),
(10,'Trompette'),
(11,'Saxophone'),
(12,'Trombone'),
(13,'Flûte'),
(14,'Harpe'),
(15,'Accordéon'),
(16,'Triangle'),
(17,'Tambour'),
(18,'Tambourin'),
(19,'Maracas'),
(20,'Gong'),
(21,'Cymbales'),
(22,'Harmonica'),
(23,'Xylophone'),
(24,'Glockenspiel'),
(25,'Bongo'),
(26,'Batterie électronique'),
(27,'Batterie acoustique'),
(28,'Batterie hybride'),
(29,'Batterie acoustique'),
(30,'Batterie électronique');


INSERT INTO ORGANISATEUR(idOrganisateur, nomOrganisateur, prenomOrganisateur, mdpOrganisateur, emailOrganisateur) VALUES
(1, 'Barache', 'Yannis','barache','ybarache@icloud.com'),
(2, 'Abada', 'Khalil','abada','khabox52@gmail.com');


INSERT INTO MEMBRE (idMembre, nomMembre, prenomMembre, idGroupe, idInstrument) VALUES
(1, 'Lennon', 'John', 1, 5),
(2, 'McCartney', 'Paul', 1, 2),
(3, 'Harrison', 'George', 1, 1),
(4, 'Starr', 'Ringo', 1, 3),
(5, 'Bangalter', 'Thomas', 2, 4),
(6, 'de Homem-Christo', 'Guy-Manuel', 2, 4),
(7, 'Cobain', 'Kurt', 3, 5),
(8, 'Grohl', 'Dave', 3, 3),
(9, 'Novoselic', 'Krist', 3, 2),
(10, 'Mercury', 'Freddie', 4, 5),
(11, 'May', 'Brian', 4, 2),
(12, 'Taylor', 'Roger', 4, 3),
(13, 'Jagger', 'Mick', 5, 5),
(14, 'Richards', 'Keith', 5, 2),
(15, 'Watts', 'Charlie', 5, 3),
(16, 'Wood', 'Ronnie', 5, 2),
(17, 'Bahaoui', 'Zouhair', 6, 5),
(18, 'Mathers', 'Marshall', 7, 5),
(19, 'Young', 'Angus', 8, 2),
(20, 'Young', 'Malcolm', 8, 2),
(21, 'Hetfield', 'James', 9, 5),
(22, 'Ulrich', 'Lars', 9, 3),
(23, 'Hammett', 'Kirk', 9, 2),
(24, 'Trujillo', 'Robert', 9, 2),
(25, 'Waters', 'Roger', 10, 5),
(26, 'Gilmour', 'David', 10, 2),
(27, 'Mason', 'Nick', 10, 3),
(28, 'Wright', 'Richard', 10, 2);


INSERT INTO PARTICIPE (idGroupe, idEvenement, dateArriveeGroupe, heureArriveeGroupe, tempsDeMontage, tempsDeDemontage) VALUES
(1, 4, '2020-12-12', '18:00:00', 2, 3),
(2, 2, '2020-12-12', '18:00:00', 2, 1.5),
(3, 3, '2020-05-06', '18:00:00', 2, 2),
(4, 1, '2020-10-25', '18:00:00', 2, 1),
(5, 5, '2021-09-15', '18:00:00', 2, 2),
(6, 6, '2021-09-10', '18:00:00', 2, 1.5);


INSERT INTO LOGER (idHebergement, idGroupe, dateDebutHebergement, dateFinHebergement) VALUES
(1, 1, '2020-12-12', '2020-12-13'),
(2, 2, '2020-12-12', '2020-12-13'),
(3, 3, '2020-05-06', '2020-05-07'),
(4, 4, '2020-10-25', '2020-10-26'),
(5, 5, '2021-09-15', '2021-09-16'),
(6, 6, '2021-09-10', '2021-09-11');


insert into BILLET (idBillet, nomBillet, prixBillet, idclient) VALUES
(1,'Jour1', 2, 1),
(2,'Jour2', 2, 1),
(3,'Jour3', 2, 1),
(4,'Jour2', 2, 2);




insert into SINSCRIT(idEvenement, idClient) VALUES
(1,1),
(2,1),
(3,1),
(4,1),
(5,1),
(6,1);

INSERT INTO RESSEMBLE(idStyle1, idStyle2) VALUES
(1,2),
(1,3),
(1,4),
(1,5),
(1,6),
(1,7),
(1,8),
(1,9),
(1,10),
(1,11),
(2,3),
(2,4),
(2,5),
(2,6),
(2,7),
(2,8),
(2,9),
(2,10),
(2,11),
(3,4),
(3,5),
(3,6),
(3,7),
(3,8),
(3,9),
(3,10),
(3,11),
(4,6),
(4,7),
(4,8),
(4,9),
(4,10),
(4,11),
(5,6),
(5,7),
(5,8),
(5,9),
(5,10),
(5,11),
(6,7),
(6,8),
(6,9),
(6,10),
(6,11),
(7,8),
(7,9),
(7,10),
(7,11),
(8,9),
(8,10),
(8,11),
(9,10),
(9,11),
(10,11);

INSERT INTO AIME(idClient, idGroupe) VALUES
(1,10),
(2,5),
(2,8),
(3,8),
(4,6),
(5,3),
(6,2),
(7,1),
(8,3);
