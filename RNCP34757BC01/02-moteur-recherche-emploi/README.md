![plot](./assets/fanart.jpg)

# Construire un moteur de recherche d'emploi  

Adrien Dulac 12.11.2020  

Compétences: c1 c2 c3 c4 c5 c20  
Keywords: Scraping, Scrapy, MongoDB, RSS, Flask, Open Data, client-serveur, URL, Requete HTTP  

## Description  

Construire un moteur de recherche d'emploi à partir de données bruts présentes sur le web et develloper une application client-serveur pour acceder aux données.

## Contexte  

Face à la montée du chômage systémique liée aux perturbations sur le marché du travail, les demandeurs d'emploi vont drastiquement augmenter et les emplois évoluer.
Cela va occasionner un fort besoin en recherche d'emploi.  
  
Dans ce contexte, M. Pontier CEO de la société FlashBot cherche à développer un moteur de recherche d'emploi et à fait appel à votre expertise.  
Il cherche à construire un système permettant d'agréger des offres d'emploi à partir de données disponibles sur l'Internet, à la fois rapidement et de manière innovante.  
L'objectif étant de faciliter la recherche d'emploi et de maximiser les chances qu'un demandeur d'emploi trouve une offre adaptée pour lui.  
  
Plusieurs pateformes existantes offrent des API permettant de rechercher des offres d'emplois. Cependant les données sont dispersées, hétérogènes et ne permettent pas de faire de l'offre adaptée.  

Aujourd'hui M. Pontier cherche à exploiter un **flux RSS** à partir du lien suivant : http://rss.jobsearch.monster.com/rssquery.ashx?q=big+data  
  
La mission consiste à exploiter ce lien pour récolter le maximum de fiches d'emploi et les stocker en BDD afin de les rendre accessibles et faciliter l'ajout de nouveaux documents.
Pour ce faire le client suggère l'utilisation d'une BDD **NoSQL** orientée document qui s'appelle MongoDB dans le but de faciliter :  
* Ajout de nouveaux documents avec des formats différents  
* Recherche d'informations textuelles  
  
Enfin, le client souhaite créer une application client-serveur permettant à un utilisateur de rechercher les offres d'emploi dans sa BDD à partir de requetes **HTTP**.  
  
En résumé, le client vous demande de designer et implémenter un systéme avec les caractéristiques suivantes :  
* Un bot/programme en python pour récolter les données et les envoyer à la BDD  

**Attention ! Limitez votre nombre de requêtes pour la phase de test pour ne pas vous faire bannir du site cible !!!**  

* Pour chaque document vous devez créer une entrée dans la BDD orientée document MongoDB avec tout les champs présents (titre, description du poste, etc ...)  
* Chaque document inséré en BDD devra avoir un champ correspondant au terme de recherche utilisé lors de la requête au flux RSS  
* Le nombre d'éléments dans la BDD doit être optimisé, c'est à dire que les doublons doivent être ecartés  
* Une application client-serveur pour permettre de faire des requêtes à la BDD : page permettant de faire une recherche textuelle sur l'ensemble des documents récupérés et de retourner la liste des 10 premiers documents les plus pertinents  

### Bonus Tech  

* Améliorer le retour d'une requête client en affichant le nombre de documents qui ont matché une recherche  
* Créer une nouvelle route dans votre serveur/backend pour afficher les statistiques de votre BDD depuis une requête client :  
    * nombre total de documents  
    * nombre total de mots uniques dans l'ensemble des documents  
    * nombre total de mots non uniques  
* Créer un fichier requirements.txt permettant d'installer automatiquement les dépendances python  

### Bonus Data  

* Comment peut-on mesurer la pertinence pour le classement des documents ? Comment est-elle mesurée ?  
* Afficher la distribution (histogramme) de la répartition des offres d'emploi par métier  
* Quels sont les 20 mots les plus fréquents dans les offres d'emplois ? (En dehors des **stopwords**) Quels sont les 10 bi-gram les plus fréquents ?  
* Combien d'offres d'emploi différentes avez-vous pu trouver sur Monster ? Pouvez-vous augmenter ce nombre avec un lexique différent ?  

## Ressources  

MongoDB :  
* https://www.mongodb.com/  
* https://docs.mongodb.com/  

Scrapy :  
* https://scrapy.org  
* https://docs.scrapy.org  

## Livrables  

Un git par apprenant avec les éléments suivants :  
1. Le bot, qui doit pouvoir être lancé pour alimenter la base de données.
2. Le serveur, qui doit pouvoir être lancé et servir (ie répondre) à des requetes HTTP.
3. Un fichier Readme.md qui décrit succinctement votre code et explique comment lancer votre programme, les éventuels arguments et comment effectuer les requêtes de recherche.

## Modalités pédagogiques  

* Durée = 3 jours  
* Collaboration en trinôme  

### Organisation  

1. Découverte du sujet, des groupes et plan du travail :  
* 30 min pour laisser les groupes relire et discuter le brief ensemble  
* Déterminer une feuille de route  
* Faire un point collectif pour faire remonter les questions et discussion des feuilles de route  

2. Installation guidée de MongoDB  

```markdown
    Voici deux méthodes pour installer mongo du plus simple au plus complexe ...

    **avec docker**

    Commencons par installer **docker**

    soit avec : `sudo snap install docker`
    ou avec `apt`: `apt install docker.io`

    Ensuite, créer un repertoire ou seront stocker les donnée de la MongoDB, par exemple

        mkdir -p ~/data-mongodb

    il suffit ensuite d'installer mongo avec la suivante suivante

        docker run -d -p 27017:27017 -v ~/data-mongodb:/data/db --name mongodb mongo:4.2 

    ici, docker se charge d'installer tout le necessaire et de placer le tout dans un conteneur isolé.

    Si l'installation a fonctionné, vous pourrez renter dans un interpreteur mongodb avec la commande suivante:

        docker exec -it mongodb mongo


    **avec apt**

    voir le tuto pour debian ou ubuntu sur la doc mongo.
```

3. Veille MongoDB  
4. Stratégies pour récolter les données  
5. Suite ?  

## Critéres de perfomance  

**Critère HUMAIN**  
* La moyenne d'avancement entre tous les groupes doit être maximale, et l'ecart type minimal  

**Critère TECH**  
* Rapidité d'execution des requêtes utilisateur  
* Qualité du code (structure, commentaires et fonctionnalité)  
* Qualité de l'interface utilisateur pour requêter le moteur de recherche  
