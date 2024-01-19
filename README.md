# SAE WEB et BD

## Membres du groupe

- Hajar EL KASMI
- Yannis BARACHE
- Khalil ABADA
- Juliann MERIT

## Description du projet

Cette SAE portera sur la création d'un site web pour un festival de musique. Le site sera accesible pour les utilisateurs et les administrateurs. Les utilisateurs pourront consulter les informations sur les artistes, les concerts, les scènes, les horaires, les prix, etc. Les administrateurs pourront ajouter, modifier et supprimer les informations sur les artistes, les concerts, les scènes, les horaires, les prix, etc. Le site sera developpé en utilisant le framework Flask et la base de données sera en MYSQL.



## Installation 
L'application nécessite l'installation de plusieurs choses pour le faire plus rapidement un script à été préparé il vous suffit d'executer le fichier ```install.sh``` avec la commande suivante

```bash
./install.sh
```

Ce fichier va installer un environnement virtuel et installer dans l'environnement tout ce qui est nécessaire au bon fonctionnement de l'application

## Pour lancer l'application
Pour lancer l'application il y a 2 manières
Soit il faut executer la commande suivante en se trouvant dans le repertoire ```src```

```bash
flask run 
```

Soit vous executer le fichier nommée ```lancement.sh``` une fois executé le fichier vous placera sur la page et il faudra simplement la rafraichir pour voir apparaître l'application

## Commandes importantes pour l'utilisation de flask

### Créer un environnement virtuel

```bash

virtualenv -p python3 venv

```

### Activer le venv dans le shell

```bash

source venv/bin/activate
```

### Installer Flask

```bash

pip install flask

```

### Installer python-dotenv

```bash

pip install python-dotenv

```

### Exécution

```bash

FLASK_APP=app.py flask run

```

Puis consulter l'url suivant

```
http://localhost:5000/

```


## Acceder à la base de données

```bash

mysql -h servinfo-maria -u barache -p

```


## Liste des améliorations à faire 

- [ ] Gestions des erreurs SQL
- [ ] Gestion des blobs
- [ ] Module admin fini
- [ ] Planning général à générer 
- [ ] Préremplir automatiquement le formulaire de contact (si connecté)
- [ ] Billeterie à finir
- [ ] Verif du billet pour s'inscrire si l'evenement est payant
- [ ] Espace groupe
- [ ] Css à finir

