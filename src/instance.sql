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


INSERT INTO GROUPE (idGroupe,nomGroupe,descriptionGroupe,idStyle,reseauxGroupe,liensVideoGroupe,photosGroupe) VALUES
(1,'The Beatles','Groupe de rock britannique',1,'Facebook, Twitter','https://www.youtube.com/watch?v=z9ypq6_5bsg', NULL),
(2,'Daft Punk','Groupe de musique électronique français',6,'Facebook, Instagram','https://www.youtube.com/watch?v=FGBhQbmPwH8', NULL),
(3,'Nirvana','Groupe de rock américain',1,'Facebook, Twitter','https://www.youtube.com/watch?v=hTWKbfoikeg', NULL),
(4,'Queen','Groupe de rock britannique',1,'Facebook, Instagram','https://www.youtube.com/watch?v=fJ9rUzIMcZQ', NULL),
(5,'The Rolling Stones','Groupe de rock britannique',1,'Facebook, Twitter','https://www.youtube.com/watch?v=6DUnOupJz7Q', NULL),
(6,'Zouhair Bahaoui', 'Chanteur marocain', 3, 'Facebook, Instagram', 'https://www.youtube.com/watch?v=6DUnOupJz7Q', NULL),
(7,'Eminem','Rappeur américain',3,'Facebook, Instagram','https://www.youtube.com/watch?v=uelHwf8o7_U', NULL),
(8,'AC/DC','Groupe de rock australien',1,'Facebook, Twitter','https://www.youtube.com/watch?v=v2AC41dglnM', NULL),
(9,'Metallica','Groupe de heavy metal américain',1,'Facebook, Instagram','https://www.youtube.com/watch?v=CD-E-LDc384', NULL),
(10,'Pink Floyd','Groupe de rock britannique',4,'Facebook, Twitter','https://www.youtube.com/watch?v=JwYX52BP2Sk', NULL);


INSERT INTO TYPE (idType,nomType) VALUES
(1,'Concert'),
(2,'Spectacle'),
(3,'Autre');


INSERT INTO EVENEMENT (idEvenement, nomEvenement, dateEvenement, heureEvenement, lieuEvenement, idType) VALUES
(1, 'Concert de Queen', '2020-12-12', '20:00:00', 'Scène Bleu', 1),
(2, 'Concert de Daft Punk', '2020-12-12', '20:00:00','Scène Rouge', 1),
(3, 'Concert de Nirvana', '2020-05-06', '20:00:00','Scène Jaune', 1),
(4, 'Concert de The Beatles', '2020-10-25', '20:00:00','Scène Bleu', 1),
(5, 'Concert de The Rolling Stones', '2021-09-15', '20:00:00','Scène Noir', 1),
(6, 'Concert de Zouhair Bahaoui', '2021-09-10', '20:00:00','Scène Rose', 1);



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


INSERT INTO CLIENT (idClient, nomClient, prenomClient, emailClient) VALUES
(1, 'Dupont', 'Jean', 'dupont.jean@mail.fr'),
(2, 'Durand', 'Pierre', 'durand.pierre@mail.fr'),
(3, 'Martin', 'Paul', 'martin.paul@mail.fr'),
(4, 'Bernard', 'Jacques', 'bernard.jaques@mail.fr'),
(5, 'Dubois', 'Michel', 'dubois.michel@mail.fr'),
(6, 'Thomas', 'Robert', 'thomas.robert@mail.fr'),
(7, 'Robert', 'Richard', 'robert.richard@mail.fr'),
(8, 'Richard', 'Jean', 'richard.jean@mail.fr');


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


INSERT INTO PARTICIPE (idGroupe, idEvenement, dateArriveeGroupe, heureArriveeGroupe, tempsDeMontage) VALUES
(1, 4, '2020-12-12', '18:00:00', 2),
(2, 2, '2020-12-12', '18:00:00', 2),
(3, 3, '2020-05-06', '18:00:00', 2),
(4, 1, '2020-10-25', '18:00:00', 2),
(5, 5, '2021-09-15', '18:00:00', 2),
(6, 6, '2021-09-10', '18:00:00', 2);

INSERT INTO LOGER (idHergement, idGroupe, dateDebutHebergement, dateFinHebergement) VALUES
(1, 1, '2020-12-12', '2020-12-13'),
(2, 2, '2020-12-12', '2020-12-13'),
(3, 3, '2020-05-06', '2020-05-07'),
(4, 4, '2020-10-25', '2020-10-26'),
(5, 5, '2021-09-15', '2021-09-16'),
(6, 6, '2021-09-10', '2021-09-11');
