# Le Fantastique Expositeur Ultime de Résultat (FEUR)

Intro *(à compléter ...)*
> Noms



## Mise en place

*FEUR* fonctionne grâce à une serveur python hébergé en local sur votre ordinateur grâce au framework *Flask*. C'est pourquoi, afin de tester notre *Fantastique Expositeur Ultime de Résultat*...



## Comment ça marche

Intro *(à compléter ...)*


### Analyse Lexicale
> Par *ALBERTOS Elvin* et *BRUNEAU Geoffroy*

Explication  *(à compléter ...)*


### Analyse syntaxique
> Par *CRINCKET Nathan* et *BEUNIER Gaspard*

Explication  *(à compléter ...)*


### Evaluateur
> Par *ZHU Yuzhe* et *FLINOIS André-Mathys*

La partie évaluateur est la troisième partie du programme. Elle vient après l’analyse lexicale et l’analyse syntaxique. Elle reçoit en entrée un arbre postfixé de jetons, ainsi que les paramètres entrés sur le site web *(nombre d’itérations et intervalle de $x$)*. Le défi de cette partie est d’utiliser cet arbre comme une fonction par laquelle une liste d’antécédents passe. La fonction `evaluateur`  en elle-même consiste simplement à effectuer quelques tests sur la cohérence des paramètres entrés, puis à créer une liste pour la remplir d’un échantillonnage de valeurs, accompagnées de leur image.

Parmi les tests effectués sur les paramètres, on retrouve la vérification du nombre d’itérations. En effet, pour afficher l’allure d’une fonction, quelle qu’en soit la précision, il faut au minimum 2 points calculés. Si cette exigence n’est pas respectée, une erreur est retournée. L’intervalle entré par l’utilisateur doit être croissant, c’est-à-dire que la valeur minimale des $x$ doit être inférieure à la valeur maximale des $x$.

Une fois ces tests passés, la liste est initialisée, et une boucle for la remplit. Sur la première ligne, on retrouve la liste des antécédents. Sur la seconde, leur image. Pour remplir la seconde ligne, chaque itération de la boucle fait appel à la fonction `postorderTraversal`.

Cette fonction est à appel récursif. Il n’y en a pas si le jeton est un réel ou la variable *(feuille)*, il y en a un si le jeton est une fonction *(un seul fils)*, et deux si le jeton est une opération *(deux fils)*. D’un accord commun avec la partie de l’analyse syntaxique, le fils unique d’un jeton de fonction est placé à droite. La fonction `postorderTraversal` prend en entrée un arbre binaire ainsi qu’une valeur de $x$. Elle teste d’abord le lexème du premier jeton de l’arbre entré. S’il s’agit d’un réel, alors la fonction retourne la valeur du réel. S’il s’agit d’une variable, alors elle retourne la valeur entrée en paramètre. Si toutefois il s’agit d’un jeton plus complexe *(fonction ou opérateur)*, des tests supplémentaires sont effectués afin de déterminer quel est l’opérateur ou la fonction contenue dans le jeton. Dans ces cas-là, des appels récursifs sont passés.

Lors des premières versions de notre code, nous avions commis l’erreur de retourner directement le calcul des fils, par exemple :
```python
if arbre.jeton.Lexeme == Lexeme.OPERATEUR :
	if arbre.jeton.valeur == Operateur.ADDITION 
		return postorderTraversal(arbre.fils_gauche) + postorderTraversal(arbre.fils_droit)
```
Cette façon d’effectuer les calculs pose problème lorsque la fonction renvoie une erreur, car la ligne du return additionne un réel et une chaîne de caractères, notamment. Le moyen trouvé de pallier ce problème est d’effectuer séparément les appels sur les sous-arbres, s’assurer qu’aucun problème n’en ressort grâce à des tests conditionnels, puis enfin d’effectuer l’opération. Si une erreur est trouvée, l’appel renvoie une chaîne de caractères. Après le calcul des sous-arbres *(`fg` et `fd`)*, leur retour est testé afin d’identifier une erreur. Si elle est repérée, la fonction renvoie la même chaîne, jusqu’au premier appel. Dans la fonction `evaluateur`, la chaîne est identifiée et `evaluateur`  renvoie l’erreur correspondante à la chaîne. La division par 0 est gérée en mettant `None` comme image. `None` indique à l’afficheur de ne pas afficher cette valeur. S’il n’y a pas d’erreur, alors la fonction renvoie le code d’erreur success `PAS_D_ERREUR` ainsi que la liste de sortie.


### Serveur (Backend)
> Par *BURET Antoine*

Explication  *(à compléter ...)*


### Affichage Graphique
> Par *BIDAULT Arthur*, *SALEK Adam* et *BURET Antoine*

Explication  *(à compléter ...)*


### Page Web (Frontend)
> Par *SALEK Adam* et *MARTINEAU Paul*

Explication  *(à compléter ...)*



## Tests

Explication  *(à compléter ...)*