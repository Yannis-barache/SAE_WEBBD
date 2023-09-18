
-- Les groupes qui participe au festival

SELECT idGroupe,nomGroupe
FROM GROUPE
natural join PARTICIPE;


-- Les groupes qui participe au festival et qui sont logés
SELECT idGroupe,nomGroupe
FROM GROUPE
natural join PARTICIPE
natural join LOGER;


-- Les 