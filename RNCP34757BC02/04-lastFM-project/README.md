![plot](./assets/fanart.png)

# Recommander Systems  

Adrien Dulac 20.01.2021  

Construire, comprendre & tuner un système de recommandation.

## Contexte du projet  

Les systèmes de recommandations sont utilisés traditionnellement et comme le nom l'indique pour recommander du contenu à des utilisateurs.  
Par exemple pour recommander un film à des utilisateurs en fonction de ceux qu'ils ont vus.  
Ou de la musique, des vidéos ou encore implémenter des fonctionnalités "more like this" ...  

## Familarisation

Nous allons commencer par suivre et reproduire les étapes de ce tuto :  

* https://www.datacamp.com/community/tutorials/recommender-systems-python  

En assumant que vous avez peu de RAM, nous allons nous arrêter au moment de calculer la  `compute_sim` variable.

**step1 : simple recommander**  

Quelle est la complexité en mémoire de cette opération ?  
Utiliser cosine_similarity qui utilise moins de mémoire ... Quand même 8Go ! Possible sur collab ...  
Cela rentre t'il sur votre machine ?  

Qu'essaye de faire l'auteur avec ce calcul ?  
Comment pouvons-nous contourner ce problème ?  

**step2 : content based recommander**

Implémenter la deuxiéme partie en évitant le produit de matrice ...  

**step3 : amélioration**

coder les 2 améliorations :  
1. Introduce a popularity filter : this recommender would take the 30 most similar movies, calculate the weighted ratings (using the IMDB formula from above), sort movies based on this rating, and return the top 10 movies.  
2. Use the PCA to improve the speed of your similarity search with 100 components. Does the result are coherent ?

## LastFM Project

M. Pontier vous contact pour l'aider à construire un système de recommandation. Il dispose d'une BDD comportant des données concernant ses utilisateurs (anonymisés) contenant les artistes qu'ils écoutent sur sa plateforme ainsi que le nombre d'écoutes. M. Pontier souhaite recommander à ses utilisateurs des artistes qu'il n'ont pas encore écoutés, et cela en fonction de leurs préférences musicales.

M. Pontier souhaite utiliser la librairie Lightfm, avec laquelle il a déjà un driver permettant de charger ses données qu'il vous fournit, un vrai bonus !  
M. Pontier a pu voir que la documentation comporte plusieurs modèles, il souhaite évaluer les modèles sur un jeu de TRAIN et TEST et utiliser le meilleur modéle.

Pour l'évaluation, il souhaite comparer la mesure AUC, la précision et le rappel (visiter la documentation de Lightfm), qui devront être présentés dans un tableau.  

---

:warning: le train et test set ont une forme un peu différente de ce qu'on a l'habitude de voir, donc regardez leurs shape et enquêter sur ce que c'est/ce qu'ils représentent ...  

**Part 1**

Voici deux sous taches supplémentaires qui vont nous aider à evaluer/interpréter notre modéle, après l'obtention des tableaux de résultats :  
* Faire la fonction get_recommandation qui prend en entrée un User et renvoie les Artists recommandés (du meilleur au moins bon au sens du score de recommandation)  
* `get_ground_truth` qui renvoie les artistes ecoutés par un utilisateur par ordre décroissant du playCountScaled  

Ceci nous permettra d"evaluer qualitativement les résultats que retourne le modéle et le comparer avec la vérité terrain.  

**Part 2**

* Comparer les résulats de l'AUC avec le meilleur modéle de lightfm et une PCA (TruncatedSDV)  
* L'apprentissage devant être le plus rapide possible tout en obtenant les meilleurs résultats, il vous est demandé de trouver le nombre d'itérations permettant d'atteindre la convergence de 95% de la valeur maximal d'AUC sur le jeu de TEST  

-- 

* Optimization des hyper-paramètres (k, n, learning_schedule, learning_rate)
* Clutering des artists avec les embeddings : tracer un visuel des clustering d'artist basé sur la matrice **d'item embeddings**  

**Part 3**

* Faire une application client serveur permettant d'interoger le modéle  
* 1 page pour connaitre/demander les préférences d'un utilisateur  
* 1 page qui compare quels sont les 10 artistes les plus écoutés et les 10 artistes les plus recommandés (afficher aussi la distribution des artistes recommandés, en prenant seulement les 5 meilleurs artistes par utilisateur)  

### Veille

Quel système de recommandation allez vous mettre en place ?  
Qu'est ce un système de recommandation dit à *implicit feedback* ? Et à *explicit feedback* ?  

Qu'est ce que Lightfm ? Expliquer ce que font les méthodes :  
* `partial_fit`  
* `precision_at_k` (and `recall_at_k`)  

### Ressources  

[LightFM](https://github.com/lyst/lightfm)  
[Jeux de données Last.fm](https://grouplens.org/datasets/hetrec-2011/)  
[The world is large and we know just a small part of it, dont forget the big picture](https://github.com/jihoo-kim/awesome-RecSys)  

## Modalités pédagogiques  

Travail individuel & en groupe
Durée = 3/4 jours  

## Livrables  

* Notebook in GitHub  
* Code for the backend : run `./back-end/app.py`  
