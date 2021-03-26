![plot](./assets/fanart.jpg)

# Risques Cardio-Vasculaires

Anne-Laure MEALIER 25.01.2021  

L’arbre qui cache la forêt : l’algorithme Random Forest  

Vous travaillez dans le domaine de la médecine préventive.  
Votre métier est donc de donner des conseils d'hygiène de vie, propreté.  
Mais aussi diététique, encouragement à une activité physique, ergonomie et manière de faire des efforts, prévention des comportements à risques, etc ...  
Ainsi que de proposer un accompagnement dans le dépistage de maladies et plus spécifiquement dans la prévention des risques cardio-vasculaires.  

## Contexte du projet  

Entre 300 000 et 400 000 accidents cardiovasculaires surviennent chaque année en France, dont un tiers sont mortels.  
Comment mieux prédire le risque cardiovasculaire ?  
Si plusieurs facteurs de risque sont identifiés, quelles sont les interactions entre ces facteurs ?  
Les maladies cardiovasculaires, principalement les AVC & les infarctus du myocarde, sont la deuxième cause de mortalité en France !  
La liste des facteurs de risque cardiovasculaire est malheureusement longue ...  
Les 12 facteurs de risque constituent ainsi un véritable réseau de facteurs de risque cardiovasculaire.  

En fonction de ces interactions, des chercheurs ont pu mettre en évidence 4 groupes de facteurs de risque :  
* «facteurs non modifiables» (le sexe, l’âge et les antécédents familiaux) qui prédisent d’autres facteurs  
Mais ne peuvent pas être prédits par d’autres facteurs  
* «facteurs liés au mode de vie» (le tabagisme, la sédentarité, l’alcoolisme) qui prédisent beaucoup d’autres facteurs (sauf les facteurs non modifiables)  
Mais sont très peu prédits par d’autres facteurs  
* «facteurs cliniques en amont» (les troubles du sommeil, l’obésité, la dépression) qui prédisent beaucoup d’autres facteurs  
Et sont eux-mêmes prédits par de nombreux facteurs  
* «facteurs cliniques en aval» (l’hypertension artérielle, les dyslipidémies, le diabète) qui prédisent très peu de facteurs  
Mais sont en revanche prédits par beaucoup de facteurs  

Pour vous accompagner au mieux dans votre démarche de prévention de ces risques cardio-vasculaire, vous avez décidé de développer un outil permettant de poser un diagnostic rapide de risques cardio-vasculaire.  
Cet outil mettra en œuvre un algorithme de machine learning permettant de prédire s’il y a un risque cardio-vasculaire ou pas.  

Présentation des données pour pouvoir entraîner votre algorithme, vous avez monté un partenariat avec des médecins généralistes de votre ville.  
Et vous avez ainsi pu récolter des données de patients. Ces données sont stockées dans un fichier .csv.  

Ce fichier comporte 12 colonnes :  
* AGE integer (number of days)  
* HEIGHT integer (cm)  
* WEIGHT integer (kg)  
* GENDER categorical (1: female, 2: male)  
* AP_HIGH (systolic blood pressure) integer  
* AP_LOW (diastolic blood pressure) integer  
* CHOLESTEROL categorical (1 = normal ; 2 = above normal ; 3 = well above normal)  
* GLUCOSE categorical (1 = normal ; 2 = above normal ; 3 = well above normal)  
* SMOKE categorical (0 = no ; 1 = yes)  
* ALCOHOL categorical (0 = no ; 1 = yes)  
* PHYSICAL_ACTIVITY categorical (0 = no ; 1 = yes)  

La variable cible :
* CARDIO_DISEASE categorical (0 = no ; 1 = yes)  

# Modalités pédagogiques  

En vous appuyant sur ces données :  
* Construire un modèle de Random Forest permettant de prédire qui sont les sujets à risque  
* Réaliser une veille sur les Random Forest  
* Visualiser & analyser les données avec les librairies Matplotlib et Seaborn  
* Résoudre le cas d’étude présenté ci-dessus avec la librairie Scikit-Learn  
(exploration des données, préparation des données, modélisation, le test et l’interprétation des résultats)  
* Prédire si Arthur 53 ans, fumeur, sportif, 175 cm, 85 kg, cholestérol au dessus de la normal, glucose normal  
AP-HIGH dans la moyenne, AP-LOW correspondant à la moyenne du 3e quartile (50%-75%), est un sujet à risque ???  
* Réaliser un GridSearch pour ajuster certains paramètres  
* Comparer les performances du RandomForest avec celle d’un KNN  

Que pouvez-vous conclure ?  

## Critères de performance  

* GridSearchCV  
* Confusion_matrix  
* Classification_report  

## Modalités d'évaluation  

* Rendu individuel sur Simplonline  

## Livrables  

Notebook Jupyter hébergé sur Github avec le lien accessible sur Simplonline  

