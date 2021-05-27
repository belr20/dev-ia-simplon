![plot](./assets/fanart.png)

# De toutes les universités ... Quelles sont les meilleures ?  

Anne-Laure MEALIER 27.11.2020  

Après avoir analysé les données, réalisez une analyse en composante principale pour étudier les corrélations suivant les différents critères d'évaluation des universités.  
Développez votre premier Dashboard complet Dash et partagez-le via Heroku !!!  

## Ressource(s)  

* [timesData.csv](https://simplonline-v3-prod.s3.eu-west-3.amazonaws.com/media/file/csv/be67fa74-2c34-419c-9249-050394a7eb3e.csv)  

## Contexte du projet  

### Classement des universités  

Le classement des universités est une pratique difficile, politique et controversée.  
Il existe des centaines de systèmes de classement universitaires nationaux et internationaux différents, dont beaucoup sont en désaccord les uns avec les autres ...  

Le Times Higher Education World University Ranking est largement considéré comme l'une des mesures universitaires les plus influentes et les plus largement observées.  
Fondée au Royaume-Uni en 2010, elle a été critiquée pour sa commercialisation et pour avoir "affaibli" les établissements non anglophones.  

### Analyse en Composantes Principales  

Pour vous aider dans votre analyse du jeux de données, vous réaliserez une Analyse en Composantes Principales.  
Cette analyse permettra de répondre à certaines questions du type :  
* Quelles ressemblances peut-il y avoir d'une université à une autre ?  
* Quelles ressemblances existent-il entre différents critères d'évaluation des universités ?  
Vous pourrez ainsi définir quand est-ce que 2 universités se ressemblent et quand est-ce qu'elles se ressemblent du point de vue de l'ensemble des colonnes, des critères d'évaluation du Times Higher Education World University Ranking.  

Est-il possible de faire un bilan des ressemblances ?  
Vous chercherez ici à faire une typologie, une partition des universités, à construire des groupes d'universités homogènes du point de vue de l'ensemble des variables.  
A l'intérieur d'un groupe, les individus se ressemblent et d'un groupe à l'autre ils sont différents ...  

## Modalités pédagogiques  

* Réaliser une veille sur la librairie Dash  
* Faire une analyse du jeu de données correspondant au classement des 50 meilleures universités en 2016  
* Réaliser une Analyse en Composantes Principales en vous appuyant sur la librairie Scikit-Learn  
https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html  
* Mettre en place un Dashbord Dash multi-pages permettant de répondre à la question ***Quelles sont les meilleures ?***  

La première page de votre Dashbord mettra en évidence l'analyse des données des 50 meilleures universités de l'année 2016, avant ACP.  

### 1ère page  

Dans cette première page se trouvera notamment une table des données des 50 meilleures universités de l'année 2016 avec un bouton de téléchargement permettant de télécharger un tableau .csv des données.  
Plusieurs graphiques mettant en évidence des corrélations entre certains critères  

### 2eme page  

Cette page permettra d'afficher les résultats issus de l'ACP.  
On pourra ainsi y trouver des graphiques ainsi que des paragraphes de textes mettant en évidence des variables explicatives.  

Vous mettrez en ligne votre Dashboard Dash sur le serveur Cloud Heroku.  

## Modalités d'évaluation  

Un rendu individuel est demandé.  
Vous pourrez travailler en groupe de 5 ou 6.  
Le rendu final devra être envoyé le vendredi 4 décembre à 15h30.  

## Livrables  

Un rendu individuel se fera sous la forme d'un projet constitué de fichiers .py que vous partagerez via Git sur GitHub.  
Vous devrez également communiquer votre lien HTTPS Heroku permettant l'accès à la visualisation de votre Dashboard.  

***POUR VISUALISER LE DASHBOARD => EXECUTEZ `python index.py`***  
