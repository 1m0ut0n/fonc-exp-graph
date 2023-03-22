# Le Fantastique Expositeur Ultime de Résultat (FEUR)

<!-- Essayer d'ajouter de la mise en forme pour avoir moins de paragraphes -->

> **Auteurs :** ALBERTOS Elvin, BEUNIER Gaspard *(Chef de projet)*, BIDAULT Arthur, BRUNEAU Geoffroy, BURET Antoine, CRINCKET Nathan, FLINOIS André-Mathys, MARTINEAU Paul, SALEK Adam et ZHU Yuzhe

Le **Fantastique Expositeur Ultime de Résultat (FEUR)** est projet ayant pour but de recréer une calculatrice graphique. Ce projet, réalisé dans le contexte du module électif *"Techniques de programmation avancées"*, a été entièrement réalisé par notre super équipe de 10.

Pour notre calculatrice graphique, nous avons créer un véritable site web, hébergé en local avec un serveur Python qui s'occupe de réaliser tout les analyses et les calculs nécessaires. Grâce à un ingénieux système, les fonction peuvent être entrées directement sur le site, elle feront l'objet d'une requête serveur qui répondra avec la discrétisation de la fonction. Le site affichera alors dynamiquement la fonction. On peut donner comme exemple la fonction :

$$
\exp ( \cos ( x ) )
$$

![Screenshot de l'affichage du site web pour la fonction exp(cos(x))](https://cdn.discordapp.com/attachments/399186517890957323/1088119519408558100/image.png)


## Mise en place

**FEUR** fonctionne grâce à un serveur Python hébergé en local sur votre ordinateur grâce au framework *Flask*. C'est pourquoi, afin de tester notre **Fantastique Expositeur Ultime de Résultat**, il faut d'abord mettre en place le serveur :

#### Installation
Dans la section *"Releases"* du [GitHub du projet](https://github.com/1m0ut0n/fonc-exp-graph), téléchargez le fichier `feur-v1.zip` puis extrayez le sur un emplacement de votre ordinateur.
Vous pouvez aussi utiliser *git* pour télécharger le projet en entrant la commande suivante dans votre terminal :
```bash
> git clone https://github.com/1m0ut0n/fonc-exp-graph.git
```

#### Dépendances
Pour fonctionner, le projet utilise *Flask*, un framework de développement web en Python. C'est pourquoi pour utiliser **FEUR**, il est nécessaire d'avoir un environnement Python avec *pip*, que vous pouvez simplement installer en utilisant *[Miniconda](https://docs.conda.io/en/latest/miniconda.html#)* par exemple.

**⚠️ Il est requis de disposer au moins de Python 3.10.0 pour que le projet puisse fonctionner correctement !**

Lorsque que vous disposer des outils nécessaires, ouvrez un invité de commande dans le dossier `feur-v1`. Vous pourrez alors installer simplement les bibliothèques Python nécessaires au projet grâce à la liste `requirements.txt` en utilisant la commande :
```bash
> pip install -r requirements.txt
```
Si vous préférez, vous pouvez installer *Flask* indépendamment puisque c'est la seul bibliothèque dont nous avons le besoin :
```bash
> pip install Flask
```

#### Utilisation
Tout est maintenant prêt pour que vous puissiez utiliser **FEUR** ! Toujours dans le dossier `feur-v1` entrez la commande :
```bash
> python run.py
```
Vous verrez alors le serveur démarrer. Une fois le démarrage terminé, **assurez vous d'être connecter à Internet** et entrez l'adresse [`http://127.0.0.1:5000`](http://127.0.0.1:5000) dans votre navigateur préféré ! Vous pourrez alors afficher les fonctions que vous souhaitez !  :)


## Comment ça marche ?

Comme expliqué plus tôt, le principe de **FEUR** est de pouvoir créer l'interface utilisateur avec une page web et de gérer les analyse et les calculs avec du Python. Si nous avions décider de faire comme ça, c'est principalement pour deux raisons : certains d'entre nous avaient déjà eu de mauvaises expériences avec *OpenGL* plus tôt et nous étions un groupe un peu plus grand que les autres. Ceci nous permettait de pousser le projet encore plus loin et, il faut l'avouer, nous amusait aussi un peu plus.

Ainsi, nous voulions dès le début construire notre projet autour d'un serveur web hébergé en local, mais de base, nous voulions tout de même coder en C en utilisant un framework similaire à Flask mais pour du C. Mais après 2 après-midi de recherche de test, tout les framework testés en C ou C++ était soi trop complexe à utiliser, soi trop complexe à mettre en place. C'est alors que nous nous est venu l'idée d'utiliser Flask, que certains avaient déjà utilisés avant. Mais pour passer sur Flask, il fallait traduire tout le travail déjà fait en C sur les analyseurs en Python, la décision n'a donc pas été prise à la légère. Cependant, les avantages de Flask et la facilité d'installation étaient tellement pratique que ce soit pour nous ou pour vous tester plus tard que nous avons décider de tout refaire !

Le **principe de fonctionnement** de la calculatrice est assez simple :
1. **L'utilisateur** entre une *fonction* ou modifie les paramètre d'affichage.
2. **Le programme JavaScript** de la page réalise une *requête au serveur* avec la fonction et les paramètre.
3. **Le serveur** récupère la *fonction littérale* et les paramètre, puis commence l'analyse en commençant **l'analyse lexicale**.
4. **L'analyse lexicale** "lit" *l'expression littérale* pour la transformer en une *liste de lexèmes*.
5. Si il n'y a pas d'*erreur*, **le serveur** passe alors à **l'analyse syntaxique**.
6. **L'analyse lexicale** utilise les règles mathématique pour trier les lexème dans un *arbre* suivant leur ordre d'interprétation.
7. En l'absence d'*erreur*, **le serveur** conclut par **l'évaluation**.
8. **L'évaluateur** va interpréter *l'arbre de lexème* pour calculer une *liste l'image de la fonction*.
9. Si pendant les analyses ou calculs, une *erreur* est survenue, **le serveur** répondra à la requête avec cette dernière. Sinon, il fera passer le *tableau d'image*.
10. **Le programme JavaScript** pourra alors réaliser l'*affichage de la fonction*, ou, à default, afficher l'*erreur* survenue.
11. **L'utilisateur** est alors prêt a afficher une autre *fonction*.

```mermaid
flowchart  LR;
	user([Utilisateur])
	js([JavaScript])
	serveur([Programme central])
	lex([Analyse lexicale])
	syntax([Analyse syntaxique])
	eval([Evaluation])
	subgraph  python  [Serveur Python]
		serveur  -- Fonction littérale -->  lex
		lex  -- Liste de lexèmes -->  syntax
		syntax  -- Arbre de lexèmes -->  eval
		eval  -- Liste d'images de la fonction -->  serveur
	end
	js  -- Envoi d'une requête serveur -->  serveur
	serveur  -- Réponse -->  js
	subgraph  page  [Page Web]
		js  -- Affichage de la courbe -->  user
		user  -- Entrée d'une fonction -->  js
	end
```


### Analyse Lexicale
> Par *ALBERTOS Elvin* et *BRUNEAU Geoffroy*

Explication  *(à compléter ...)*


### Analyse syntaxique
> Par *CRINCKET Nathan* et *BEUNIER Gaspard*

Explication  *(à compléter ...)*


### Evaluateur
> Par *ZHU Yuzhe* et *FLINOIS André-Mathys*

La partie évaluateur est la troisième partie du programme. Elle vient après l’analyse lexicale et l’analyse syntaxique. Elle reçoit en entrée un arbre postfixé de jetons, ainsi que les paramètres entrés sur le site web *(nombre d’itérations et intervalle de *$x$*)*. Le défi de cette partie est d’utiliser cet arbre comme une fonction par laquelle une liste d’antécédents passe. La fonction `evaluateur`  en elle-même consiste simplement à effectuer quelques tests sur la cohérence des paramètres entrés, puis à créer une liste pour la remplir d’un échantillonnage de valeurs, accompagnées de leur image.

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

La page web est la dernière étape du projet de calculatrice graphique. C'est sur cette dernière que se situe toute l'interface utilisateur. Sur cette page, l'utilisateur peut entrer la fonction, ajuster des caractéristiques sur son affichage et print cette fonction sur le canvas central de la page.

Tout d'abord, on arrive sur la page *`accueil.html`* qui nous introduit au site **FEUR**  *(Fantastique Expositeur Ultime de Résultat)*. En cliquant sur le bouton central on est redirigé vers la page principale du site, détaillée ci-dessous.

La page *`mainpage.html`* est construite de la manière suivante:
- Le **logo** du site en haut à gauche ;
- Le lien vers notre **rapport** de projet ;
- Un `<canvas>` central dans lequel va prendre place le graphique tracé en JavaScript - Différents `<input>` :
  - Abscisse **min** et **max** de x, `<input type="number">` ;
  - **Discrétisation**  *(nombre de points à afficher)*, `<input type="number">` ;
  - **Couleur** de la courbe, `<input type="color">` ; 
  - La **fonction**, `<input type="text">` ; 
  - Le **bouton** afficher, `<input type="submit">` ;

Ce squelette HTML est supporté par le fichier **CSS**  `style_mainpage.css` dans lequel on met en forme les éléments issus du HTML à l'aide des balises `div` qui contiennent des **id** et des **class**. Cette page HTML est aussi reliée au fichier **JavaScript**  `script-mainpage.js`.

### Mise en commun
> Par *BURET Antoine* et *BEUNIER Gaspard*


## Tests

Explication  *(à compléter ...)*
