
# ECF du projet Hotel Hypnos

Pour cette ECF, je vais vous présenter le projet Hypnos, un groupe hôtelier qui se compose de 7 hôtels réparti au 4 coins de la France.



Tout d'abord pour pouvoir utilisé le projet de le respository github, il faudra installer quelques applications. 
## Authors

- Emmanuel SCELLES: https://github.com/Thanos974


## Documentation

[Documentation]
Vous trouverez dans le dossier PDF ECF tout les document afférant à la bonne utilisation de l'application.

    - Documentation technique
    - Manuel d'utilisation
    - Charte graphique
    
    La documentation officielle si beosin:
    
        Pour télécharger python:
            https://www.python.org/downloads/

        Documentation sur django:
            https://docs.djangoproject.com/fr/4.0/

## Tester Hypnos en local


```bash
 Avoir installer au préalable python3.9 ou 3.10 sur votre PC
```
Créer un dossier sur votre machine


Cloner le projet dans 

```bash
  git clone https://github.com/Thanos974/ECF-Hypnos.git
```

Aller dans le répertoire du projet nommée src là où se situe le fichier manage.py qui permettra d'installé les dépendances. 

```bash
  cd src
```
Créer un environnement virtuel:

```bash
 dans le temrinal => python -m venv .venv
```
Sourcer votre environnement virtuel:

Sur Windows :
```bash
   windows => source .venv/Scripts/activate
```
Sur Mac :
```bash
   mac => source .env/bin/activate
```

Installer les dépendances via le fichier requirements.txt

```bash
  pip install -r requirements.xt
```

Démarrer le serveur django 

```bash
  python manage.py runserver
```
Faire la migration des données pour créer automatiquement par défault le fichier SQLite3 qui sera la base de donnée

```bash
  python manage.py migrate
```


