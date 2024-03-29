# Par Antoine

import os, sys

sys.path.append(os.getcwd()+'/app/python') #on modifie le chemin actuel afin de ne pas avoir de problèmes d'importation dans les différents fichiers (car sinon le programme considère que l'on se situe dans le dossier du fichier 'run.py')

import lex,syntax,evaluator

#on importe les 3 fichiers qui vont nous permettre de faire l'analyse complète

from erreurs import *

#on importe le fichier qui répertorie toutes les erreurs possibles répertoriées


#---------------------------------------------------------------------------------------------------------------------
#
#       Ci-dessous, la fonction principale qui va appeler toutes les autres afin d'analyser la fonction entrée
#
#---------------------------------------------------------------------------------------------------------------------


def analyse_complete(dico):
    """
    fontion permettant d'analyser la fonction et de renvoyer le tableau de données correspondant
    parameter : dico le dictionnaire contenant les données entrées
    output : un dictionnaire précisant s'il y a une erreur ou non, contenant le tableau de données et la couleur choisie
    """
    xmin = int(dico["xrangemin"]) #on récupère les données en les stockant dans des variables
    xmax = int(dico["xrangemax"])
    nomb = int(dico["discretisation"])
    chaine_entree = dico["fonction"]
    couleur = dico["couleur"]
    
    lexem_table = lex.lex_analyser(chaine_entree) #on commence par l'analyse lexicale
    if lexem_table[0] != ErreurLex.PAS_D_ERREUR: #s'il y a une erreur, alors on le précise et on la renvoie
        return {"erreur" : 1, "sortie" : "Erreur analyse lexicale : "+promptErreurLex[lexem_table[0]], "couleur" : couleur}
    else:
        syntax_table = syntax.syntax_analyser(lexem_table[1]) #sinon on passe à l'analyse syntaxique
        if syntax_table[0] != ErreurSyntax.PAS_D_ERREUR: #s'il y a une erreur, alors on le précise et on la renvoie
            return {"erreur" : 1, "sortie" : "Erreur analyse syntaxique : "+promptErreurSyntax[syntax_table[0]], "couleur" : couleur}
        else:
            arbre = syntax_table[1] #sinon on récupère l'arbre
            result = evaluator.evaluateur(arbre,nomb,xmin,xmax) #et on termine par l'évaluation
            if result[0] != ErreurEval.PAS_D_ERREUR: #s'il y a une erreur, alors on le précise et on la renvoie
                return  {"erreur" : 1, "sortie" : "Erreur évaluateur : "+promptErreurEval[result[0]], "couleur" : couleur}
            else:
                return {"erreur" : 0, "sortie" : result[1], "couleur" : couleur}
                #si aucune erreur n'est relevée alors on le précise et on renvoie le tableau de données
