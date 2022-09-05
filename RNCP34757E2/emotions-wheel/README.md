<img alt="plot" height="500" src="./assets/wheel.png" width="500"/>

# La Roue des Emotions [![Python 3.8](https://img.shields.io/badge/python-3.8-blue.svg)](https://www.python.org/downloads/release/python-3813/)  

Anne-Laure MEALIER 08.12.2020  

Construit d’après les travaux du psychologue américain Robert Plutchik, la roue des émotions est un modèle des émotions humaines et peut facilement servir à définir des personnages, ainsi que leur évolution dans une trame narrative.  
Est-il possible d'identifier des émotions dans des phrases narratives issues de communications écrites ???  

## Ressource(s)  

* [Text Classification with NLTK and Scikit-Learn](https://bbengfort.github.io/tutorials/2016/05/19/text-classification-nltk-sckit-learn.html)  
* [Tutoriel TAL pour les débutants : Classification de texte](https://www.actuia.com/contribution/victorbigand/tutoriel-tal-pour-les-debutants-classification-de-texte/)  
* [From Sentiment Analysis to Emotion Recognition: A NLP story](https://medium.com/neuronio/from-sentiment-analysis-to-emotion-recognition-a-nlp-story-bcc9d6ff61ae)  
* [Use Sentiment Analysis With Python to Classify Movie Reviews](https://realpython.com/sentiment-analysis-python/#how-classification-works)  

## Contexte du projet  

Depuis quelques années, les dispositifs de communication médiatisée par ordinateur (CMO) sont massivement utilisés, aussi bien dans les activités professionnelles que personnelles.  
Ces dispositifs permettent à des participants distants physiquement de communiquer.  
La plupart implique une communication écrite médiatisée par ordinateur (CEMO) : forums de discussion, courrier électronique, messagerie instantanée.  
Les participants ne s’entendent pas et ne se voient pas mais peuvent communiquer par l’envoi de messages écrits, qui combinent, généralement, certaines caractéristiques des registres écrit et oral (Marcoccia, 2000a ; Marcoccia, Gauducheau, 2007 ; Riva, 2001).  
Imaginez que vous souhaitez savoir ce qui se passe derrière votre écran d'ordinateur !  
Quels sont vos contacts les plus actifs et quelle est leur personnalité ?  
Vous allez alors vous lancer dans l’analyse de leur narration et tenter d’extraire quelle émotion se dégage de chacune des phrases.  

Chez Simplon nous utilisons tous les jours des outils de discussion textuels et nous construisons nos relations sociales et professionnelles autour de ces dispositifs.  
Pour entretenir des rapports sociaux stables, sereins, de confiance et efficaces, au travers des outils de communication écrites, lorsqu'il n'est pas possible d'avoir la visio (avec caméra), il est nécessaire de détecter des éléments "clés" dans les channels de discussions / mails qui nous permettront de déceler de la colère, de la frustration, de la tristesse ou encore de la joie de la part d'un collègue ou d'un ami pour adapter nos relations sociales.  

En tant qu'expert en data science, nous allons vous demander de développer un modèle de machine learning permettant de classer les phrases suivant l'émotion principale qui en ressort.  
Pour des questions d’ordre privé, nous ne vous demanderons pas de nous communiquer les conversations provenant de votre réseau social favori ou de vos emails mais nous allons plutôt vous proposer deux jeux de données contenant des phrases, ces fichiers ayant déjà été annotés.  

Vous devrez proposer plusieurs modèles de classification des émotions et proposer une analyse qualitative et quantitative de ces modèles en fonction de critères d'évaluation.  
Vous pourrez notamment vous appuyer sur les outils de reporting des librairies déjà étudiées.  
Vous devrez investiguer aux travers de librairies d'apprentissage automatique standards et de traitement automatique du langage naturel.  

Comment obtenir les meilleurs performance de prédiction possible en prenant en compte l'aspect multi-class du problème et en explorant l'impact sur la prédiction de divers prétraitement tel que la suppression des stop-words, la lemmatisation et l'utilisation de n-grams, et différentes approches pour la vectorisation.  

Vous devrez travailler dans un premier temps avec le jeu de données issu de Kaggle pour réaliser vos apprentissage et l'évaluation de vos modèles.  

Dans l'objectif d'enrichir notre prédiction, nous souhaitons augmenter notre jeux de donneés.  

Vous devrez donc travailler dans un deuxième temps avec le jeu de données fourni, issue de data.world afin de :  
* Comparez d'une part si les résultats de classification sur votre premier jeu de données sont similaires avec le second & commenter  
* Combiner les deux jeux de données pour tenter d'améliorer vos résultats de prédiction  
* Prédire les nouvelles émotions présentes dans ce jeu de données sur les messages du premier & observer si les résultats sont pertinents  

Vous devrez ensuite présenter vos résultats sous la forme d'un dashboard multi-pages Dash.  
La première page du Dashboard sera dédiée à l'analyse et au traitement des données.  
Vous pourrez par exemple présenter les données "brut" sous la forme d'un tableau puis les données pré-traitées dans le même tableau avec un bouton ou menu déroulant permettant de passer d'un type de données à un autre.  
N'affichez qu'un échantillon des résultats dans une fenêtre "scrollable" ...  

Sur cette première page de dashboard seront accessibles vos graphiques ayant trait à votre première analyse de données :  
* Histogrammes représentant la fréquence d’apparition des mots avec votre analyse  
* Histogrammes des émotions avec votre analyse  

Une deuxième page du Dashboard sera dédiée aux résultats issues des classifications.  
Il vous est demandé de comparer les résultats, d'au moins 5 classifiers, présentés dans un tableau permettant de visualiser vos mesures.  
Sur cette page de dashboard pourra se trouver par exemple :  
* Courbes de rappel & de précision avec différents seuils de probabilité  
* Rapport de classification avec precision, recall, f1-score, support  
* Matrice de confusion  
* Graphique permettant de visualiser les mots les plus représentatifs associés à chaque émotions  

Héberger le dashboard sur le cloud de visualisation de données Héroku :  

# [emotions-wheel-by-belr20@heroku](https://emotions-wheel-by-belr20.herokuapp.com/)  

## Bonus  

Créer une application client/serveur permettant à un utilisateur d'envoyer du texte via un champ de recherche et de lui renvoyer l'émotion du texte envoyé.

## Bonus du bonus ;-)  

la roue des émotions du document avec proportions  

## Modalités pédagogiques  

Vos travaux devront être “poussés” sur Github et sur Heroku au plus tard le Jeudi 17 Décembre à 17h30.  
Les liens seront accessibles via Simplonline.
Les rendus tardifs ne seront pas pris en compte et les compétences ne seront donc pas validées !!!  
Travail en groupe de 5/6 + rôles  
Durée = 7 jours  

## Critères de performance  

Un dashboard Dash permettra de visualiser et de comparer les performances issues de différents classifiers.  

## Livrables  

* Notebook résumant votre travail + fichiers python .py décrivant votre Dashboard Dash  

***Attention***  
Votre notebook ne doit contenir que du code et/ou markdown pertinent !  
Toutes les cellules doivent s'exécuter, les graphiques doivent être pertinents !!!  
