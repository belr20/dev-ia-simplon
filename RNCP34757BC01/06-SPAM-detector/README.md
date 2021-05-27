![plot](./assets/fanart.jpg)

# The Spam Detector  

Adrien Dulac 02.12.2020  

Learn to Detect Spam given Spam and Ham examples.  

keywords: NLP (TALN), classification  

## Contexte du projet  

* https://github.com/dtrckd/simplon_datai_2020/blob/master/brief_4/brief.md  

## Description  

Mme Esposito développe pour son entreprise un chatbot dans le but de répondre automatiquement à ses nombreux clients. Cependant son programme reçoit un grand nombre de messages malveillants ou à caractère publicitaire ce qui dégrade les performances de son bot en plus d'occasionner des traitements informatiques se répercutant sur sa facture d'électricité !  

Elle vous a contacté afin de créer un programme capable de détecter automatiquement les SPAM.  

Pour cela, elle a construit un jeu de données comportant un ensemble de SMS de type SPAM et NON SPAM (HAM), disponible à l'adresse suivante : http://www.dt.fee.unicamp.br/~tiago/smsspamcollection/  

Par ailleurs, afin d'intégrer les résultats dans son équipe, elle nous demande les choses suivantes :  
* Une checklist des tâches à réaliser doit être rédigée afin d'estimer le coût du développement et suivre le projet  
* Des fonctions pour les différentes parties de votre code afin de pouvoir les réutiliser facilement  
* Une validation croisée (cross-validation) sur 10 jeux d'apprentissage et de test différents avec un seed fixé à 42 et le jeu de test doit représenter 20% des données  
* Une comparaison avec au moins trois algorithmes de classification en terme de **f1 score**  

## Bonus  

* Pouvez-vous améliorer les résultats ?  
* Est-ce que la **lemmatisation** améliore les résultats ?  
* Est-ce que la racinisation **stemming** améliore les résultats ?  

Une fois ces étapes réalisées, reproduire la même expérience avec le jeu suivant, représentant cette fois des commentaires Youtube : https://archive.ics.uci.edu/ml/datasets/YouTube+Spam+Collection  
Les performances sont-elles similaires à celles obtenues avec le jeu de données précèdent ?  

Mme Esposito souhaite contrôler si les modèles appris avec le premier jeu de données sont capables de prédire les données de test du deuxième jeu et vice-versa ...  

Réaliser un tableau comparant :  
* Les résultats de prédiction du modèle appris sur les SPAM SMS pour prédire les SPAM YouTube  
* Les résultats de prédiction du modèle appris sur les SPAM YouTube pour prédire les SPAM SMS  

## Proposed plan  

**1) Veille en Traitement du langage + checklist**  

* https://becominghuman.ai/a-simple-introduction-to-natural-language-processing-ea66a1747b32  
* https://towardsdatascience.com/your-guide-to-natural-language-processing-nlp-48ea2511f6e1  
* https://code.tutsplus.com/fr/tutorials/introducing-the-natural-language-toolkit-nltk--cms-28620  
* https://towardsdatascience.com/introduction-to-natural-language-processing-for-text-df845750fb63  

* Parsing & tokenization ?  
* Vectorization ? Bag of words ?  
* TFIDF advantage ?  
* Stop words ?  

**2) Load, clean & prepare the data**  

Vectoriser et nettoyer vos données : https://scikit-learn.org/stable/modules/feature_extraction.html#text-feature-extraction  

* Quel est le type Python de vos données après vectorisation ?  
* Quels sont les 10 mots les plus fréquents dans le jeu de données ?  
* Les moins fréquents ?  
* Tracer la distribution de la fréquence des mots présents dans le jeu de données. Qu'observez vous ?  

**Aides/propositions**  

* Stop words avec NLTK  
* scikit-learn pour la vectorization  

**3) Apprenstissage**  

Que représente la mesure f1 ?  
Quels sont ses avantages sur d'autres mesures tel que la précision, le rappel, ou l'accuracy ?  

Veille cross validation : https://scikit-learn.org/stable/modules/cross_validation.html  

Utilisez la méthode de [ShuffleSplit](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.ShuffleSplit.html#sklearn.model_selection.ShuffleSplit) pour construire vos jeux de données permettant la validation croisée.  

**4) Train**  

Fit the models & compare the performance in a table that shows :  
* Mean of f1 score  
* Standard deviation of f1 score  

Qu'observez vous ?  

## Modalités pédagogiques  

Travail en semi groupe.  

## Livrables  

Git contenant notebook et/ou scripts.  
