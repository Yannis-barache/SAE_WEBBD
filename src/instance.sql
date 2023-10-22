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


INSERT INTO LIEU (idLieu,nomLieu,adresseLieu,capacitéLieu) VALUES
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


INSERT INTO EVENEMENT (idEvenement, nomEvenement, dateEvenement, heureEvenement, idType, idLieu) VALUES
(1, 'Concert de Queen', '2020-12-12', '20:00:00', 1, 1),
(2, 'Concert de Daft Punk', '2020-12-12', '20:00:00', 1, 8),
(3, 'Concert de Nirvana', '2020-05-06', '20:00:00', 1, 9),
(4, 'Concert de The Beatles', '2020-10-25', '20:00:00', 1, 2),
(5, 'Concert de The Rolling Stones', '2021-09-15', '20:00:00', 1, 4),
(6, 'Concert de Zouhair Bahaoui', '2021-09-10', '20:00:00', 1, 3);


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


INSERT INTO MEMBRE (idMembre, nomMembre, prenomMembre, idGroupe, instrumentMembre) VALUES
(1, 'Lennon', 'John', 1, 'Guitare'),
(2, 'McCartney', 'Paul', 1, 'Basse'),
(3, 'Harrison', 'George', 1, 'Guitare'),
(4, 'Starr', 'Ringo', 1, 'Batterie'),
(5, 'Bangalter', 'Thomas', 2, 'Synthétiseur'),
(6, 'de Homem-Christo', 'Guy-Manuel', 2, 'Synthétiseur'),
(7, 'Cobain', 'Kurt', 3, 'Guitare'),
(8, 'Novoselic', 'Krist', 3, 'Basse'),
(9, 'Grohl', 'Dave', 3, 'Batterie'),
(10, 'Mercury', 'Freddie', 4, 'Chant'),
(11, 'May', 'Brian', 4, 'Guitare'),
(12, 'Taylor', 'Roger', 4, 'Batterie'),
(13, 'Deacon', 'John', 4, 'Basse'),
(14, 'Jagger', 'Mick', 5, 'Chant'),
(15, 'Richards', 'Keith', 5, 'Guitare'),
(16, 'Watts', 'Charlie', 5, 'Batterie'),
(17, 'Wood', 'Ronnie', 5, 'Guitare'),
(18, 'Jackson', 'Michael', 6, 'Chant'),
(19, 'Mathers', 'Marshall', 7, 'Chant'),
(20, 'Young', 'Angus', 8, 'Guitare'),
(21, 'Young', 'Malcolm', 8, 'Guitare'),
(22, 'Johnson', 'Brian', 8, 'Chant'),
(23, 'Williams', 'Robert', 9, 'Guitare'),
(24, 'Ulrich', 'Lars', 9, 'Batterie'),
(25, 'Hetfield', 'James', 9, 'Chant'),
(26, 'Hammett', 'Kirk', 9, 'Guitare'),
(27, 'Waters', 'Roger', 10, 'Basse'),
(28, 'Gilmour', 'David', 10, 'Guitare'),
(29, 'Wright', 'Richard', 10, 'Clavier'),
(30, 'Mason', 'Nick', 10, 'Batterie');


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
(1,'patrick', 2, 1),
(2,'patrick1', 2, 1),
(3,'patrick2', 2, 1),
(4,'patrick3', 2, 1);


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