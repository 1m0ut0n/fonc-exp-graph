// Par Arthur, Adam, Antoine
// Utilisez le navigateur Mozilla Firefox pour un affichage dynamique


//--------------------------------------------------------------------------------------------------------------------
//
//                            Ci-dessous la partie récupération des données et requêtes
//
//--------------------------------------------------------------------------------------------------------------------


document.addEventListener("keypress", function(event) { //on détecte toute touche pressée
    if (event.keyCode == 13) { //si la touche pressée est la touche 'entrée' alors on fait le test des valeurs entrées
        test_total();
    }
});


document.addEventListener("input", function(event) { //on détecte tout changement d'entrée dans les champs
    const element = event.target; //on récupère l'élément dont on change la valeur
    const xrangemin = document.getElementById("xrangemin"); //on affecte à une constante les champs d'entrées
    const xrangemax = document.getElementById("xrangemax");
    const discretisation = document.getElementById("discretisation");
    const couleur = document.getElementById("couleur");
    let result = false; //on initialise une variable qui va nous permettre de décider si l'on fait une requête ou non
    
    //cette partie est utile pour modifier les valeurs des champs avec les flèches dynamiquement (sur Firefox)
    if (element == xrangemin) { //si l'élément dont on change la valeur est xrangemin
        if (xrangemin != document.activeElement) { //et si xrangemin n'est pas sélectionné
            result = test_x(xrangemin,xrangemax,xrangemin); //on va tester la valeur entrée
        }
    } else if (element == xrangemax) { //même principe avec xrangemax
        if (xrangemax != document.activeElement) {
            result = test_x(xrangemin,xrangemax,xrangemax);
        }
    } else if (element == discretisation) { //même principe avec la discrétisation
        if (discretisation != document.activeElement) {
            result = test_discretisation(discretisation);
        }
    } else if (element == couleur) { //si l'élément dont on change la valeur est la couleur, pas de vérification à faire
        main();
    }
    
    if (result == true) { //si les valeurs ont passé les tests, alors on va faire une requête
        main();
    }
});


function test_total() {
    /*
    fonction qui va tester si les données entrées sont valides ou non
    */
    if(typeof jQuery != 'function'){ //si l'on n'a pas pu importer la fonction jQuery, c'est qu'il n'y a pas de connexion au réseau
        window.alert('Erreur réseau : La connexion au réseau a échoué. Vérifiez votre connexion Internet.');
    } else { //si l'on a pu se connecter
        const xrangemin = document.getElementById("xrangemin"); //on affecte à une constante les champs d'entrées
        const xrangemax = document.getElementById("xrangemax");
        const discretisation = document.getElementById("discretisation");
        if (test_x(xrangemin,xrangemax,xrangemin) == true && test_x(xrangemin,xrangemax,xrangemax) == true && test_discretisation(discretisation) == true) { //si toutes les valeurs passent le test, on fait une requête
            main();
        }
    }
}


function test_x(xrangemin,xrangemax,element_change) {
    /*
    fonction qui teste la valeur des entrées x
    parameters : xrangemin le champ d'entrée de xrangemin
                 xrangemax le champ d'entrée de xrangemax
                 element_change l'élément dont on vient de changer la valeur
    output : un booléen si oui ou non les valeurs entrées sont correctes
    */
    let xmin = Number(xrangemin.value); //on récupère les valeurs des champs
    let xmax = Number(xrangemax.value);
    if ((xrangemin.value == '') || (xrangemax.value == '')) { //si au moins l'un des champs est vide, on affiche une erreur
        window.alert("Erreur input : Veuillez entrer une valeur pour x.");
        return false //les valeurs n'ont pas réussi le test
    } else if (xmin >= xmax) { //le x min doit être inférieur au x max
        if (element_change == xrangemin) { //on réinitialise la valeur selon le champ modifié
            xrangemin.value = xmax-1;
        } else {
            xrangemax.value = xmin+1;
        }
        window.alert("Erreur input : x mininimum doit être strictement inférieur à x maximum.");
        return false
    } else {
        return true //s'il n'y a pas d'erreur, les valeurs ont réussi le test
    }
}


function test_discretisation(discretisation) {
    /*
    fonction qui teste la valeur de la discrétisation
    parameter : discretisation le champr d'entrée de la discrétisation
    output : un booléen si oui ou non la valeur entrée est correcte
    */
    if (discretisation.value == '') { //si le champ est vide, on affiche une erreur
        window.alert("Erreur input : Veuillez entrer une valeur pour la discrétisation.");
        return false
    } else if (Number(discretisation.value) <= 1) { //il faut que la discrétisation soit au moins égale à 2
        discretisation.value = 2; //si ce n'est pas le cas, on réinitialise la valeur à 2
        window.alert("Erreur input : La discrétisation sélectionnée doit au moins être égale à 2.");
        return false
    } else {
        return true
    }
}


function main() {
    /*
    fonction appelée lorsque l'on veut faire une requête au serveur
    elle va récupérer les données entrées sur le site web, les envoyer au serveur python qui va s'occupper de l'analyse, puis récupérer les données finales afin d'afficher le graphe
    */
    const xrangemin = document.getElementById("xrangemin").value; //on récupère les données entrées
    const xrangemax = document.getElementById("xrangemax").value;
    const discretisation = document.getElementById("discretisation").value;
    const couleur = document.getElementById("couleur").value;
    const fonction = document.getElementById("fonction").value;
    const dict_values = {xrangemin,xrangemax,discretisation,couleur,fonction}; //on stocke les données dans un dictionnaire
    const s = JSON.stringify(dict_values); //on convertit le dictionnaire au format JSON afin de pouvoir l'envoyer au serveur
    
    $.ajax({ //on utilise la bibliothèque ajax qui permet d'échanger des fichiers JSON avec le serveur
        url:'/mainpage/calculate', //on définit la nouvelle url affiliée lorsqu'on aura fait la requête
        type:"POST", //on veut poster des données sur le serveur
        contentType: "application/json;charset=UTF-8", //on veut transmettre un fichier JSON
        data: JSON.stringify(s), //la donnée transmise est le dictionnaire au format JSON
        success: function(data) { //lorsque la requête est bien passée on peut exécuter les commandes suivantes en récupérant les données renvoyées par le serveur
            if (data["erreur"] == 1) {
                window.alert(data["sortie"]); //s'il y a une erreur, on l'affiche dans une fenêtre
            } else { //sinon on peut afficher le graphe de la fonction
                const canva = document.getElementById("graphe"); //on définit le canva qui va contenir le graphe
                draw(canva,data["sortie"],data["couleur"]); //on appelle la fonction d'affichage
            }
        },
        error: function() { //si la requête s'est mal passée, on affiche l'erreur
            window.alert('Erreur serveur : La requête a échoué. Vérifiez que le serveur est lancé.')
        }
    });
}


//--------------------------------------------------------------------------------------------------------------------
//
//                        Ci-dessous la partie affichage du graphe et ses fonctions connexes
//
//--------------------------------------------------------------------------------------------------------------------


function minmax(donnees,L) {
    /*
    fonction permettant de trouver la valeur minimum et maximum du tableau de données
    parameters : donnees tableau de données
                 L la taille de ce tableau
    output : un tableau contenant la valeur min et la valeur max du tableau entré
    */
	let a = donnees[0]; //on initialise ces deux variables au premier élément du tableau
	let b = donnees[0];
	for (var i = 1;i < L;i++) { //on parcourt tout le tableau
	    let element = donnees[i];
		if (element < a) { //si l'élément actuel est inférieur au minimum actuel alors c'est le nouveau minimum
		    a = element;
		}
		if (element > b) { //si l'élément actuel est supérieur au maximum actuel alors c'est le nouveau maximum
		    b = element;
		}
	}
	return [a,b]
}


function fx(x0,valx,dist_abs,Lx) {
    /*
    fonction permettant de trouver l'abscisse en pixels d'une abscisse mathématique entrée
    parameters : x0 la valeur mathématique de l'abscisse la plus faible du graphe
                 valx la valeur mathématique de l'abscisse dont on veut connaitre la valeur en pixels
                 dist_abs la valeur mathématique de la largeur du graphe
                 Lx la valeur en pixels de la largeur du graphe
    output : l'abscisse en pixels
    */
    return Math.abs(x0-valx)/dist_abs*Lx //Math.abs renvoie la valeur absolue d'un nombre entré
}
	
	
function fy(b,valy,dist_ord,Ly) {
    /*
    fonction permettant de trouver l'ordonnée en pixels d'une ordonnée mathématique entrée
    parameters : b la valeur mathématique de l'ordonnée la plus élevée du graphe
                 valy la valeur mathématique de l'ordonnée dont on veut connaitre la valeur en pixels
                 dist_ord la valeur mathématique de la hauteur du graphe
                 Ly la valeur en pixels de la hauteur du graphe
    output : l'ordonnée en pixels
    */
    return Math.abs(b-valy)/dist_ord*Ly
}


//à noter que l'on prend comme point de référence l'abscisse la plus faible et l'ordonnée la plus élevée car l'origine du canva se situe en haut à gauche de ce dernier


function trouver_puissance(dist) {
    /*
    fonction permettant de trouver la puissance de 10 correspondant à la taille mathématique du graphe
    parameter : dist la largeur ou hauteur mathématique du graphe
    output : la puissance de 10
    */
    for (var i = -49;i < 50;i++) { //c'est donc ici que l'on peut régler la puissance minimum et maximum de l'affichage du graphe
        if (dist <= Math.pow(10,i+1) && dist > Math.pow(10,i)) { //Math.pow renvoie le nombre entré à la puissance entrée
            return i
        }
    }
}


function trouver_premierx(x,dixpuissancex) {
    /*
    fonction permettant de trouver l'abscisse minimum supérieure à l'abscisse entrée à 10^puissancex près
    parameters : x l'abscisse d'un point
                 puissancex permet de déterminer si l'on veut l'entier supérieur, la dizaine supérieure, etc.
    output : l'abscisse minimum supérieure
    */
    return Math.ceil(x/dixpuissancex)*dixpuissancex //Math.ceil renvoie l'entier minimum supérieur au nombre entré
}


function trouver_premiery(y,dixpuissancey) {
    /*
    fonction permettant de trouver l'ordonnée maximum inférieure à l'ordonnée entrée à 10^puissancey près
    parameters : y l'ordonnée d'un point
                 puissancey permet de déterminer si l'on veut l'entier inférieur, la dizaine inférieure, etc.
    output : l'ordonnée maximum inférieure
    */
    return Math.floor(y/dixpuissancey)*dixpuissancey //Math.floor renvoie l'entier maximum inférieur au nombre entré
}


function draw(canva,donnees,couleur) {
    /*
    fonction permettant de dessiner le graphe
    parameters : canva le canva dans lequel le graphe va être dessiné
                 donnees le tableau de données renvoyé par le serveur python, c'est un tableau contenant un tableau
 d'abscisses et un d'ordonnées
                 couleur la couleur de la courbe choisie
    */
    const Lx = canva.getAttribute("width"); //on initialise la taille du canva selon les valeurs entrées dans le fichier HTML
    const Ly = canva.getAttribute("height");
    const L = donnees[0].length; //on récupère la taille d'une des deux dimensions du tableau de données
    const [a,b] = minmax(donnees[1],L); //on va chercher l'ordonnée min et max du tableau
    const [x0,x1] = [donnees[0][0],donnees[0][L-1]]; //on récupère l'abscisse min et max du tableau
    const dist_abs = x1-x0; //on définit la largeur mathématique du graphe
    const dist_ord = b-a; //on définit la hauteur mathématique du graphe
    const ctx = canva.getContext("2d"); //on spécifie que l'on veut tracer un dessin en 2d
    
    ctx.strokeStyle = couleur; //on définit la couleur du tracé de la courbe
    ctx.lineWidth = 2; //on définit la largeur du tracé de la courbe
    ctx.font = "125% serif"; //on définit la police d'écriture des valeurs
    ctx.beginPath(); //on commence à dessiner
    ctx.clearRect(0,0,Lx,Ly); //on efface tout ce qu'il y a dans le canva
    
    //cette partie va permettre de tracer la courbe de la fonction entrée
    if (a == b) { //si la fonction est constante on affiche simplement une droite
        ctx.moveTo(0,Ly/2);
        ctx.lineTo(Lx,Ly/2);
        ctx.fillText(a.toString(),Lx/100,Ly*(1/2+4/100));
    } else {
        var prochain = [donnees[0][0],donnees[1][0]]; //on initialise le prochain point comme le premier point
        let index = 1; //on définit l'indexation de l'élément dans la liste
        while (prochain[1] == null && index < L) { //tant que l'ordonnée de l'élément est nul, on choisit le prochain élément
            prochain = [donnees[0][index],donnees[1][index]];
            index += 1;
        }
        if (prochain[1] != null) { //on vérifie que l'ordonnée existe bien (pour les discontinuités de fonction)
            ctx.moveTo(fx(x0,prochain[0],dist_abs,Lx),fy(b,prochain[1],dist_ord,Ly)); //on se déplace au premier point
            for (var i = index;i < L;i++) { //on parcourt tous les points du tableau donné
                prochain = [donnees[0][i],donnees[1][i]]; //on définit le prochain point
                if (prochain[1] != null) { //si l'ordonnée n'est pas nulle on trace un segment
                    ctx.lineTo(fx(x0,prochain[0],dist_abs,Lx),fy(b,prochain[1],dist_ord,Ly)); //on trace une ligne jusqu'au prochain point
                } else { //sinon on se déplace au prochain point existant sans dessiner
                    while (prochain[1] == null && i < L) {
                        i += 1;
                        prochain = [donnees[0][i],donnees[1][i]];
                    }
                    if (prochain[1] != null) {
                        ctx.moveTo(fx(x0,prochain[0],dist_abs,Lx),fy(b,prochain[1],dist_ord,Ly));
                    }
                }
            }
        }
    }
    ctx.stroke(); //on arrête de dessiner
    
    const puissancex = trouver_puissance(dist_abs); //on va chercher la puissance de 10 utilisée pour l'affichage en abscisse et en ordonnée (pour placer des axes de quadrillage tous les 10^puissance)
    const puissancey = trouver_puissance(dist_ord);
    const dixpuissancex = Math.pow(10,puissancex); //on définit les valeurs de 10^puissance
    const dixpuissancey = Math.pow(10,puissancey);
    const premierx = trouver_premierx(x0,dixpuissancex); //on va chercher la position du premier axe qui va permettre de faire un quadrillage
    const premiery = trouver_premiery(b,dixpuissancey);
    
    ctx.strokeStyle = "silver"; //on définit la couleur du quadrillage
    ctx.font = "125% serif"; //on définit la police d'écriture des valeurs
    ctx.lineWidth = 1;
    ctx.beginPath();
    
    //cette partie va permettre de tracer le quadrillage et d'afficher les valeurs correspondantes
    for (var i = 0;i < dist_abs/dixpuissancex;i++) { //on va tracer un certain nombre d'axe des ordonnées pour le quadrillage
        let valuex = premierx+i*dixpuissancex; //on définit l'abscisse mathématique de l'axe
        let abscisse = fx(x0,valuex,dist_abs,Lx); //on convertit cette abscisse en pixels
        let abscisse_val = abscisse+Lx/100; //on définit la position de la valeur
        let ordonnee_val = Ly*(1-2/100);
        let valeur_sans_puissancex = Math.round(valuex/dixpuissancex); //on assigne à une variable la valeur du nombre sans sa puissance de 10
        ctx.moveTo(abscisse,0);
        ctx.lineTo(abscisse,Ly); //on trace donc cet axe
        if ((puissancex <= -3) || (puissancex >= 3) && (valeur_sans_puissancex != 0)) { //si la puissance est trop élevée ou trop faible, on va afficher les valeurs au format : 'xepuissance' pour 'x*10^puissance'
            ctx.fillText(valeur_sans_puissancex.toString()+"e"+puissancex.toString(),abscisse_val,ordonnee_val);
        } else { //sinon on affiche simplement la valeur (ici problème d'arrondi pour certaines valeurs venant de la précision de la fonction Math.pow())
            ctx.fillText((valeur_sans_puissancex*dixpuissancex).toString(),abscisse_val,ordonnee_val);
        }
    }
    
    for (var j = 0;j < dist_ord/dixpuissancey;j++) { //même chose pour les axes des abscisses du quadrillage
        let valuey = premiery-j*dixpuissancey;
        let ordonnee = fy(b,valuey,dist_ord,Ly);
        let abscisse_val = Lx/100;
        let ordonnee_val = ordonnee+4*Ly/100;
        let valeur_sans_puissancey = Math.round(valuey/dixpuissancey);
        ctx.moveTo(0,ordonnee);
        ctx.lineTo(Lx,ordonnee);
        if ((puissancey <= -3) || (puissancey >= 3) && (valeur_sans_puissancey != 0)) {
            ctx.fillText(valeur_sans_puissancey.toString()+"e"+puissancey.toString(),abscisse_val,ordonnee_val);
        } else {
            ctx.fillText((valeur_sans_puissancey*dixpuissancey).toString(),abscisse_val,ordonnee_val);
        }
    }
    ctx.stroke();
    
    //cette partie va permettre de tracer les axes des origines et d'écrire "x" et "y"
    ctx.font = "130% serif"; //on définit la police d'écriture des données
    ctx.strokeStyle = "black"; //on définit la couleur des axes d'origine
    ctx.lineWidth = 2;
    ctx.beginPath();
    const longueur_fleche = Lx/100; //on définit la taille des flèches des axes
    const demi_largeur_fleche = Ly/100
    
    if (a <= 0 && b >= 0) { //on affiche l'axe des abscisses si et seulement si l'ordonnée minimum est négative et l'ordonnée maximum et positive
        let d = b/(dist_ord)*Ly; //on définit la distance séparant le bord du canva de l'axe des abscisses
        ctx.moveTo(0,d); //on déplace le crayon aux coordonnées indiquées
        ctx.lineTo(Lx,d); //on dessine une ligne jusqu'aux coordonnées indiquées
        ctx.lineTo(Lx-longueur_fleche,d-demi_largeur_fleche); //on affiche une flèche au bout de l'axe
        ctx.moveTo(Lx,d);
        ctx.lineTo(Lx-longueur_fleche,d+demi_largeur_fleche);
        ctx.fillText("x",Lx*(1-2/100),d*(1-2/100)); //on écrit "x" à côté de l'axe des abscisses
    } else {
        ctx.fillText("x",Lx*(1-2/100),Ly*(1-2/100)); //sinon on écrit "x" dans le coin du canva inférieur droit
    }
    
    if (x0 <= 0 && x1 >= 0) { //même principe pour l'axe des ordonnées
        let c = -x0/(dist_abs)*Lx;
        ctx.moveTo(c,Ly);
        ctx.lineTo(c,0);
        ctx.lineTo(c-demi_largeur_fleche,longueur_fleche);
        ctx.moveTo(c,0);
        ctx.lineTo(c+demi_largeur_fleche,longueur_fleche);
        ctx.fillText("y",c*(1+1/100),Ly*(4/100)); 
    } else {
        ctx.fillText("y",Lx/100,Ly*(4/100)); 
    }
    ctx.stroke();
}
