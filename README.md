# SAE WEB et BD

## Membres du groupe

- Hajar EL KASMI
- Yannis BARACHE
- Khalil ABADA
- Juliann Meritt

## Description du projet

Cette SAE portera sur la création d'un site web pour un festival de musique. Le site sera accesible pour les utilisateurs et les administrateurs. Les utilisateurs pourront consulter les informations sur les artistes, les concerts, les scènes, les horaires, les prix, etc. Les administrateurs pourront ajouter, modifier et supprimer les informations sur les artistes, les concerts, les scènes, les horaires, les prix, etc. Le site sera developpé en utilisant le framework Flask et la base de données sera en MYSQL.


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

mysql -h servinfo-maria -u VotreNom -p

```


## Liste des tâches à faire 


- [x] Déterminer toutes les tables de la base de données
- [ ] Déterminer toutes les fonctionnalités du site
- [ ] Déterminer toutes les contraintes de la base de données
- [ ] Créer les tables de la base de données
- [ ] Coder les pages flask
    - [ ] Page d'accueil
    - [ ] Page de connexion
    - [ ] Page d'inscription
    - [ ] Page de déconnexion
    - [ ] Page de profil
    - [ ] Page de modification du profil
    - [ ] Page de paiement des tickets
    - [ ] Page de consultation des tickets
    - [ ] Page de l'emploi du temps
    - [ ] Page de consultation des artistes

