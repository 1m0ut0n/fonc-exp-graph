//--------------------------------------------------------------------------------------------------------------------
//
//                            Ci-dessous la partie récupération des données et requêtes
//
//--------------------------------------------------------------------------------------------------------------------


window.addEventListener('input', function(event) { //on détecte tout changement d'entrée sur la page web
    const fonction = document.getElementById('fonction'); //on récupère le champ contenant la fonction
    if (fonction != event.target && fonction.value != '') { //si le champ dont le contenu a changé n'est pas le champ d'entrée de la fonction et que le champ de fonction n'est pas vide, alors on peut commencer à faire des tests
    //on fait cette vérification car si on fait une requête dès qu'on modifie la fonction, alors on aura une erreur à chaque modification jusqu'à ce que la fonction entrée soit correcte
        const xrangemin = document.getElementById("xrangemin"); //on affecte à une constante les champs d'entrées de x
        const xrangemax = document.getElementById("xrangemax");
        var xmin = Number(xrangemin.value); //on affecte à une variable la valeur des champps d'entrées de x
        var xmax = Number(xrangemax.value);
        
        if (xrangemin.value != '' && xrangemax != '') { //on vérifie tout d'abord que les 2 champs ne sont pas vide afin de pouvoir tout effacer et ne pas avoir de message d'erreur
            if (xmin >= xmax) { //le x min doit être inférieur au x max
                if (event.target == xrangemax) {
                    xrangemax.value = xmin+1; //si ce n'est pas le cas on réinitialise la valeur
                } else {
                    xrangemin.value = xmax-1;ctx.font = "9pt serif"; //on définit la police d'écriture des données
    ctx.strokeStyle = "black"; //on définit la couleur des axes d'origine
    ctx.beginPath(); //on commence à dessiner
    ctx.clearRect(0,0,Lx,Ly); //on efface tout ce qu'il y a dans le canva
    ctx.fillText("y",Lx/100,Ly*(4/100)); //on écrit "x" et "y" à côté de l'axe des abscisses et des ordonnées
    ctx.fillText("x",Lx*(1-2/100),Ly*(1-2/100));
    
    if (a <= 0 && b >= 0) { //on affiche l'axe des abscisses si et seulement si l'ordonnée minimum est négative et l'ordonnée maximum et positive
        let d = b/(dist_ord)*Ly; //on définit la distance séparant le bord du canva de l'axe des abscisses
        ctx.moveTo(0,d); //on déplace le crayon aux coordonnées indiquées
        ctx.lineTo(Lx,d); //on dessine une ligne jusqu'aux coordonnées indiquées
    }
    
    if (x0 <= 0 && x1 >= 0) { //même principe pour l'axe des ordonnées
        let c = -x0/(dist_abs)*Lx;
        ctx.moveTo(c,0);
        ctx.lineTo(c,Ly);
    }
    ctx.stroke(); //on arrête de dessiner
                }
                window.alert("x mininimum doit être strictement inférieur à x maximum."); //on affiche alors une alerte
            } else {
                const discretisation = document.getElementById("discretisation"); //on affecte à une constante le champ d'entrée de la discrétisation
                var discret = Number(discretisation.value); //on affecte à une variable la valeur du champ d'entrée de la discrétisation
                if (discretisation.value != '') { //on vérifie tout d'abord que le champ n'est pas vide
                    if (discret <= 1) { //la discrétisation doit être supéieur à 2
                        discretisation.value = 2;
                        window.alert("La discrétisation sélectionnée doit au moins être égale à 2.");
                    } else {
                        main(); //si toutes les conditions sont satisfaites, alors on va faire une requête via la fonction principale
                    }
                }
            }
        }
    }
});


document.addEventListener("keypress", function(event) { //on détecte toute touche pressée
    if (event.keyCode == 13) { //si la touche pressée est la touche 'entrée' alors on actualise la requête
        main();
    }
});


function main() {
    /*
    fonction appelée lorsque l'on clique sur le bouton dans la mainpage ou lorsque l'on modifie un champ
    elle va récupérer les données entrées sur le site web, les envoyer au serveur python qui va s'occupper de l'analyse, puis récupérer les données finales afin d'afficher le graphe
    */
    const xrangemin = document.getElementById("xrangemin").value; //on récupère les données entrées
    const xrangemax = document.getElementById("xrangemax").value;
    const discretisation = document.getElementById("discretisation").value;
    const couleur = document.getElementById("couleur").value;
    const fonction = document.getElementById("fonction").value;
    const dict_values = {xrangemin,xrangemax,discretisation,couleur,fonction}; //on stocke les données dans un dictionnaire
    const s = JSON.stringify(dict_values); //on convertit le dictionnaire au format JSON
    
    $.ajax({ //on utilise ajax avec la bibliothèque jQuery qui permet d'échanger des fichiers JSON avec le serveur
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
        error: function(error) { //si la requête s'est mal passée, on affiche l'erreur
            window.alert('gg')
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
    const Lx = canva.getAttribute("width"); //on récupère la largeur et la hauteur du canva en pixels
    const Ly = canva.getAttribute("height");
    const L = donnees[0].length; //on récupère la taille d'une des deux dimensions du tableau de données
    const [a,b] = minmax(donnees[1],L); //on va chercher l'ordonnée min et max du tableau
    const ctx = canva.getContext("2d"); //on spécifie que l'on veut tracer un dessin en 2d
    const [x0,x1] = [donnees[0][0],donnees[0][L-1]]; //on récupère l'abscisse min et max du tableau
    const dist_abs = x1-x0; //on définit la largeur mathématique du graphe
    const dist_ord = b-a; //on définit la hauteur mathématique du graphe
    
    ctx.strokeStyle = couleur; //on définit la couleur du tracé de la courbe
    ctx.lineWidth = 2; //on définit la largeur du tracé de la courbe
    ctx.beginPath();
    ctx.clearRect(0,0,Lx,Ly); //on efface tout ce qu'il y a dans le canva
    var prochain = [donnees[0][0],donnees[1][0]]; //on initialise le prochain point comme le premier point
    let index = 1; //on définit l'indexation de l'élément dans la liste
    while (prochain[1] == null) { //si l'ordonnée de l'élément est nul alors on choisit le prochain élément
        if (index < L) { //si l'index est accessible
            prochain = [donnees[0][index],donnees[1][index]];
            index += 1;
        }
    }
    if (prochain[1] != null) { //on vérifie que l'ordonnée existe bien (pour les discontinuités de fonction)
        ctx.moveTo(fx(x0,prochain[0],dist_abs,Lx),fy(b,prochain[1],dist_ord,Ly)); //on se déplace au premier point
        for (var i = 1;i < L;i++) { //on parcourt tous les points du tableau donné
            prochain = [donnees[0][i],donnees[1][i]]; //on définit le prochain point
            if (prochain[1] != null && prochain[1]) { //si l'ordonnée n'est pas nulle on trace un segment
                ctx.lineTo(fx(x0,prochain[0],dist_abs,Lx),fy(b,prochain[1],dist_ord,Ly)); //on trace une ligne jusqu'au prochain point
            } else { //sinon on se déplace au prochain point existant sans dessiner
                while (prochain[1] == null) {
                    if (i < L) {
                        i += 1;
                        prochain = [donnees[0][i],donnees[1][i]];
                    }
                }
                if (prochain[1] != null) {
                    ctx.moveTo(fx(x0,prochain[0],dist_abs,Lx),fy(b,prochain[1],dist_ord,Ly));
                }
            }
        }
    }
    ctx.stroke();
    
    const puissancex = trouver_puissance(dist_abs); //on va chercher la puissance de 10 utilisée pour l'affichage en abscisse et en ordonnée
    const puissancey = trouver_puissance(dist_ord);
    const dixpuissancex = Math.pow(10,puissancex); //on définit les valeurs de 10^puissance
    const dixpuissancey = Math.pow(10,puissancey);
    const premierx = trouver_premierx(x0,dixpuissancex); //on va chercher la position du premier axe qui va permettre de faire un quadrillage
    const premiery = trouver_premiery(b,dixpuissancey);
    
    ctx.strokeStyle = "silver"; //on définit la couleur du quadrillage
    ctx.font = "8pt serif"; //on définit la police d'écriture des valeurs
    ctx.lineWidth = 1;
    ctx.beginPath();
    
    for (var i = 0;i < dist_abs/dixpuissancex;i++) { //on va tracer un certain nombre d'axe des ordonnées pour le quadrillage
        let valuex = premierx+i*dixpuissancex; //on définit l'abscisse mathématique de l'axe
        let abscisse = fx(x0,valuex,dist_abs,Lx); //on convertit cette abscisse en pixels
        let abscisse_val = abscisse+Lx/100; //on définit l'abscisse de la valeur
        let ordonnee_val = Ly*(1-2/100); //on définit l'ordonnée de la valeur
        let valeur_sans_puissance = Math.round(valuex/dixpuissancex); //on assigne à une variable la valeur du nombre sans sa puissance de 10
        ctx.moveTo(abscisse,0);
        ctx.lineTo(abscisse,Ly); //on trace donc cet axe
        if ((puissancex <= -3) || (puissancex >= 3)) { //si la puissance est trop élevée ou trop faible, on va afficher les valeurs au format : 'xepuissance' pour 'x*10^puissance'
            ctx.fillText(valeur_sans_puissance.toString()+"e"+puissancex.toString(),abscisse_val,ordonnee_val);
        } else { //sinon on affiche simplement la valeur (ici problème d'arrondi pour certaines valeurs venant de la précision de la fonction Math.pow())
            ctx.fillText((valeur_sans_puissance*dixpuissancex).toString(),abscisse_val,ordonnee_val);
        }
    }
    
    for (var j = 0;j < dist_ord/dixpuissancey;j++) { //même chose pour les axes des abscisses
        let valuey = premiery-j*dixpuissancey;
        let ordonnee = fy(b,valuey,dist_ord,Ly);
        let abscisse_val = Lx/100;
        let ordonnee_val = ordonnee+4*Ly/100;
        let valeur_sans_puissance = Math.round(valuey/dixpuissancey);
        ctx.moveTo(0,ordonnee);
        ctx.lineTo(Lx,ordonnee);
        if ((puissancey <= -3) || (puissancey >= 3)) {
            ctx.fillText(valeur_sans_puissance.toString()+"e"+puissancey.toString(),abscisse_val,ordonnee_val);
        } else {
            ctx.fillText((valeur_sans_puissance*dixpuissancey).toString(),abscisse_val,ordonnee_val);
        }
    }
    ctx.stroke();
    
    ctx.font = "9pt serif"; //on définit la police d'écriture des données
    ctx.strokeStyle = "black"; //on définit la couleur des axes d'origine
    ctx.lineWidth = 2;
    ctx.beginPath(); //on commence à dessiner
    ctx.fillText("y",Lx/100,Ly*(4/100)); //on écrit "x" et "y" à côté de l'axe des abscisses et des ordonnées
    ctx.fillText("x",Lx*(1-2/100),Ly*(1-2/100));
    
    if (a <= 0 && b >= 0) { //on affiche l'axe des abscisses si et seulement si l'ordonnée minimum est négative et l'ordonnée maximum et positive
        let d = b/(dist_ord)*Ly; //on définit la distance séparant le bord du canva de l'axe des abscisses
        ctx.moveTo(0,d); //on déplace le crayon aux coordonnées indiquées
        ctx.lineTo(Lx,d); //on dessine une ligne jusqu'aux coordonnées indiquées
    }
    
    if (x0 <= 0 && x1 >= 0) { //même principe pour l'axe des ordonnées
        let c = -x0/(dist_abs)*Lx;
        ctx.moveTo(c,0);
        ctx.lineTo(c,Ly);
    }
    ctx.stroke(); //on arrête de dessiner
}
