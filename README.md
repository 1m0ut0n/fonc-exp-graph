# Le Fantastique Expositeur Ultime de Résultat (FEUR)

<!-- Essayer d'ajouter de la mise en forme pour avoir moins de paragraphes monotones -->

> **Auteurs :** ALBERTOS Elvin, BEUNIER Gaspard *(Chef de projet)*, BIDAULT Arthur, BRUNEAU Geoffroy, BURET Antoine, CRINCKET Nathan, FLINOIS André-Mathys, MARTINEAU Paul, SALEK Adam et ZHU Yuzhe

Le **Fantastique Expositeur Ultime de Résultat (FEUR)** est projet ayant pour but de **recréer une calculatrice graphique**. Ce projet, réalisé dans le contexte du module électif *"Techniques de programmation avancées"*, a été **entièrement réalisé par notre super équipe de 10**.

Pour notre calculatrice graphique, nous avons créer **un véritable site web**, hébergé en local avec un serveur Python qui s'occupe de réaliser tout les analyses et les calculs nécessaires. Grâce à un **ingénieux système**, les fonction peuvent être entrées directement sur le site, elle feront l'objet d'une requête serveur qui répondra avec la discrétisation de la fonction. Le site affichera alors dynamiquement cette dernière. On peut donner comme exemple la fonction $\exp ( \cos ( x ) )$, pour laquelle le site affichera :

![Screenshot de l'affichage du site web pour la fonction exp(cos(x))](https://cdn.discordapp.com/attachments/399186517890957323/1088119519408558100/image.png)


## Mise en place

**FEUR** fonctionne grâce à un serveur Python hébergé en local sur votre ordinateur grâce au framework *Flask*. C'est pourquoi, afin de tester notre **Fantastique Expositeur Ultime de Résultat**, il faut d'abord mettre en place le serveur :

#### Installation
Dans la section *"Releases"* du [GitHub du projet](https://github.com/1m0ut0n/fonc-exp-graph), téléchargez le fichier `feur-v1.zip` puis extrayez le sur un emplacement de votre ordinateur *(c'est le même que vous avez eu sur My Learning Space)*.
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

Comme expliqué plus tôt, le principe de **FEUR** est de pouvoir **créer l'interface utilisateur avec une page web** et de **gérer les analyse et les calculs avec du Python**. Si nous avions décider de faire comme ça, c'est principalement pour deux raisons : certains d'entre nous avaient déjà eu de mauvaises expériences avec *OpenGL* plus tôt et nous étions un groupe un peu plus grand que les autres. Ceci nous permettait de **pousser le projet encore plus loin** et, il faut l'avouer, **nous amusait** aussi un peu plus.

Ainsi, nous voulions dès le début construire notre projet autour d'un **serveur web hébergé en local**, mais de base, nous voulions tout de même coder en C en utilisant un framework similaire à Flask mais pour du C. Mais après 2 après-midi de recherche de test, tout les framework testés en C ou C++ était soi trop complexe à utiliser, soi trop complexe à mettre en place. C'est alors que nous nous est venu l'idée d'utiliser **Flask**, que certains avaient déjà utilisés avant. Mais pour passer sur Flask, il fallait traduire tout le travail déjà fait en C sur les analyseurs en Python, la décision n'a donc pas été prise à la légère. Cependant, les avantages de Flask et la facilité d'installation étaient tellement pratique que ce soit pour nous ou pour vous tester plus tard que nous avons décider de tout refaire !

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
Afin de mieux comprendre, nous reviendrons **plus en détail sur la manière dont nous les avons misent en place** dans les paragraphes suivant. Ainsi, nous **expliquerons le fonctionnement** des différentes analyses, de l'évaluateur mais aussi de l'affichage dynamique de la courbe. Nous parlerons aussi du site web et de son serveur, notamment comment ils **communiquent entre eux**. Nous finirons par dire comment nous avons **organisé la mise en commun du travail** de chacun.

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

Tout d'abord, on arrive sur la page `accueil.html` qui nous introduit au site **FEUR**  *(Fantastique Expositeur Ultime de Résultat)*. En cliquant sur le bouton central on est redirigé vers la page principale du site, détaillée ci-dessous.

La page `mainpage.html` est construite de la manière suivante:
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

Afin d'être le moins embêté possible lors de la mise en commun des travaux de chacun, c'est la première chose à laquelle nous avons réfléchi. Le but était d'**anticiper dès le début les problèmes que nous pourrions rencontrer** lors de cette dernière, mais aussi de s'assurer que tout le monde travaille sur la même chose, notamment en utilisant les mêmes objets lorsque ces derniers étaient communs à plusieurs partie. Afin de s'assurer que tout se passe bien, nous avons **mit en place plusieurs choses** :

1. La première chose était de **repartir le travail**. Pour cela, nous avons **séparé les partie mais sans pour autant isoler** chacune d'entre elles. Le but était déjà de définir pour chacune des partie, où elle commençait et où elle s'arrêtait, tout en sachant exactement ce qu'elle devait faire dans chacun des cas : avoir comme **un mini cahier des charges** pour chacune d'elles. Cette étape à été faite avec tout le monde, car pour s'assurer que les **dialogue** entre chacun soit maintenu en cas de doute, il fallait que **tout le monde sache exactement qui fait quoi**. Toujours dans la mêmes optique, **certains membres travaillaient sur plusieurs partie**, notamment pour celles qui avait beaucoup de choses en commun, afin de s'assurer que tout était toujours intégré le mieux possible.

2. Afin d'éviter de devoir tout mettre en commun à la fin, et de **se rendre compte plus facilement et plus rapidement des problèmes** avant qu'ils ne deviennent véritablement ingérable, nous avons avons utilisé un outil : **GitHub**. En pensant dès le début l'arborescence de fichier et en y mettant dès le début les fichiers de mise en commun *(dont nous allons parler juste après)*, nous pouvions tous, en travaillant sur le même repo, **construire nos partie sur une même base**. GitHub permettait à chacun, tout au long du projet, de faire part aux autres des modifications et des ajouts sur ses fichiers, mais aussi aux autres de **se tenir à jour des nouveautés sur le projet**. Nous pouvions alors **constamment tester l'intégration des différentes parties entres elles**, mais aussi facilement voir les programmes des autres. Faire tout cela fortement diminué *(si ce n'est supprimé)* le travail de mise en commun et **nous a permit de toujours y voir clair sur ce que nous faisions**, facilitant ainsi encore plus la discussion entre les parties.

3. La dernière chose à s'assurer, comme nous l'avons mentionné, était de pouvoir **travailler sur des types d'objets communs**, reconnus et lu par chacune des partie. Deux types d'informations devait circuler entre chacun des programmes : les données et les erreurs, c'est pourquoi nous avons dès le début créer les fichiers `common.py` et `erreurs.py`. Ces derniers fonctionnent comme une sorte de bibliothèques communes à tous, et **réunissant les différents types de données à traiter ou les erreurs survenues à faire remonter**. Dans le premier, on trouve les différents lexèmes, operateurs et fonctions ainsi que les classes `Jeton` et `ArbreJeton` nous permettant d'identifier les objets mathématiques, appelés donc "jetons" et de pouvoir les traiter, pour les trier dans des listes ou des arbres. Le second réuni les erreurs que nous pouvions rencontrer dans chacune des différentes parties mais aussi la phrase qui indiquera à l'utilisateur quelle erreur fut détectée dans la saisie. De la même manière, **les fonctions gérant les deux étapes d'analyse et l'évaluation devait toutes les trois suivre un même principe** : prendre en entrée la donnée provenant de l'étape précédente puis retourner dans l'ordre l'erreur en première position et la donnée traités en seconde.

Grâce aux choses que nous avions mit en place au début, mais aussi à la discussion entre les partie tout au long du projet, **l'étape de la mise en commun** à la fin et **l'identification des bugs** lors des tests fut assez facile.


## Tests

**L'étape de test fût assez importante**, pour faciliter cette dernière, nous avons créer exprès le script `test.py` nous permettant de **tester et de visualiser l'analyse de n'importe quelle fonction**. Vous pouvez la tester vous même en exécutant le script :
```bash
> python "app/python/test.py"
```
En l'exécutant, il nous est demandé d'entrer une fonction. Lorsque que l'on appuie sur `Entrée`, **l'analyse complète de la fonction s'affichera**, avec, pour chaque étape, un affichage de sa sortie. Si une erreur survient, l'analyse s'arrêtera à l'étape à laquelle l'erreur est survenue et **le type d'erreur correspondante ainsi que sa phrase associée seront affichée**. Cela permet de **tester facilement et rapidement de nombreuses fonctions**, tout en vérifiant que tout se passe bien à chacune des étape en vérifiant la sortie de chacune d'entre elle. Nous pouvons aussi tester si les erreurs retournées sont bel et bien reconnues et affichées sous la bonne forme. Enfin, lorsqu'une erreur non prévue se produit, nous pouvons savoir où cette dernière à été reconnue et analyser les sortie des étapes d'analyse précédente, pour s'assurer que le problème ne viennent pas d'avant.

Par exemple, si on reprend notre fameuse fonction $\exp ( \cos ( x ) )$ et qu'on l'entre dans notre fonction de test, l'affichage ressemblera à ça :
```
Fonction : exp(cos(x))

--- Output Lex ---
[FONCTION : EXP, PARENTHESE_OUV, FONCTION : COS, PARENTHESE_OUV, VARIABLE, PARENTHESE_FERM, PARENTHESE_FERM]

--- Output Syntax ---
 ↳ FONCTION : EXP
    ↳ FONCTION : COS
       ↳ VARIABLE

--- Mermaid ---
graph TB;
   jet0(FONCTION : EXP)
   jet0 --> jet1(FONCTION : COS)
   jet1 --> jet2(VARIABLE)


--- Output Eval ---
x : [-10.0, -8.947368421052632, -7.894736842105264, -6.842105263157895, -5.7894736842105265, -4.7368421052631575, -3.6842105263157894, -2.6315789473684212, -1.578947368421053, -0.526315789473685, 0.526315789473685, 1.578947368421053, 2.6315789473684212, 3.6842105263157894, 4.7368421052631575, 5.789473684210526, 6.842105263157894, 7.894736842105264, 8.94736842105263, 10.0]
y : [0.4321115402348868, 0.41140046726392554, 0.9600749479791699, 2.3345714036212364, 2.412298431905603, 1.0247520572590947, 0.42470528347046227, 0.41780610550696695, 0.9918821775642611, 2.3742075103470306, 2.3742075103470306, 0.9918821775642611, 0.41780610550696695, 0.42470528347046227, 1.0247520572590947, 2.412298431905602, 2.3345714036212377, 0.9600749479791699, 0.4114004672639259, 0.4321115402348868]
```
Vous remarquerez donc, en premier, la **sortie de l'analyse lexicale**, sous la forme d'une *liste de lexème*, juste après, la **sortie de l'analyse syntaxique**, sous la forme d'un *arbre de lexème*, et enfin, en dernier, la **sortie de l'évaluation**, sous la forme d'un *tableau de valeur* réunissant 20 images par la fonction prit pour 20 valeurs de $x$ entre 10 et -10. Vous remarquerez aussi que la sortie de l'analyse syntaxique est aussi donnée sous forme de code [mermaid](https://mermaid.js.org/), qui nous permet d'**afficher l'arbre d'une manière bien plus lisible** que sous forme de texte. En effet, vous pourrez visualiser l'arbre avec, par exemple, le *[Mermaid Live Editor](https://mermaid.live/)* :
```mermaid
graph TB;
   jet0(FONCTION : EXP)
   jet0 --> jet1(FONCTION : COS)
   jet1 --> jet2(VARIABLE)
```

> **Note :** A la fin du script `test.py`, vous pourrez trouver une liste de fonction intéressante à tester, que ce soit avec le site web, ou juste le script de test.

## Fin

**On s'est tous beaucoup amusé sur ce projet**, c'est pourquoi on a toujours essayé de le pousser au maximum. **On espère qu'il vous plaira autant qu'il nous a plu** lors de sa réalisation !

> **PS :** Appuyez sur tout les boutons, c'est rigolo :)
