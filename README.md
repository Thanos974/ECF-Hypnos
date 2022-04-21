
# ECF du projet Hotel Hypnos

Pour cette ECF, je vais vous présenter le projet Hypnos, un groupe hôtelier qui se compose de 7 hôtels réparti au 4 coins de la France.



Tout d'abord pour pouvoir utilisé le projet de le respository github, il faudra installer quelques applications. 
## Authors

- Emmanuel SCELLES: https://github.com/Thanos974


## Documentation

[Documentation]
    (https://www.python.org/downloads/)
    (https://docs.djangoproject.com/fr/4.0/)

## Tester Hypnos en local


```bash
 Installer python3.9 ou 3.10 sur votre PC
```

Cloner le projet

```bash
  git clone https://github.com/Thanos974/ECF-Hypnos.git
```

Aller dans le répertoire du projet la où se situe le fichier manage.py

```bash
  cd src
```

Installer les dépendances

```bash
  pip install -r requirements.xt
```

Démarrer le serveur djagno pour créer par défault automatiquement le fichier SQLite3

```bash
  python manage.py runserver
```
Faire la migration des données

```bash
  python manage.py migrate
```


