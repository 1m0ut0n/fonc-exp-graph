##############################################################################
#                           Gestion des erreurs                              #
#                                                                            #
# Ce fichier regroupe toute les types d'erreurs spécifiques créée pour le    #
# calculateur et qui serviront dans plusieurs étapes différentes. Il y a un  #
# type d'erreur par étape ainsi que les prompt à afficher en cas d'erreur.   #
# On y trouve notamment :                                                    #
#  - L'énumeration des erreurs globales et pour chacunes des étapes          #
#  - Les prompts à afficher pour chacune des erreurs sous forme de           #
#    dictonnaire (un dictionnaire par type d'erreur).                        #
#                                                                            #
##############################################################################

from enum import Enum



# -------------------------------- Erreurs --------------------------------- #

# Erreurs liées à l'analyseur lexical (syntaxe : ErreurLex.NOM_ERREUR)
class ErreurLex(Enum):
    PAS_D_ERREUR = 200 
    FONCTION_MAL_ECRITE = 201
    RIEN_EST_TAPE_PAR_UTILISATEUR = 202
    CARACTERE_NON_RECONNU = 203
    #... (à ajouter au fur et à mesure)


# Erreurs liées à l'analyseur syntaxique (syntaxe : ErreurSyntax.NOM_ERREUR)
class ErreurSyntax(Enum) :
    PAS_D_ERREUR = 300
    RECHERCHE_FIN_PARENTHESE_PAS_DE_PARENTHESE_OUVRANTE = 301 
    RECHERCHE_FIN_PARENTHESE_PAS_DE_PARENTHESE_FERMANTE_CORRESPONDANTE = 302
    LISTE_VIDE = 303
    ERREUR_INCONNUE = 304
    OPERATEUR_SANS_VALEUR_A_COTE = 305
    FONCTION_SANS_PARENTHESE = 306
    OBJETS_INCOMPATIBLE = 307
    #... (à ajouter au fur et à mesure)


# Erreurs liées à l'évaluateur (syntaxe : ErreurEval.NOM_ERREUR)
class ErreurEval(Enum):
    PAS_D_ERREUR = 400 # OK
    ITERATIONS_INSUFFISANTES = 401 # Nombre d'itérations inférieur à 2
    XMIN_SUPERIEUR_A_XMAX = 402 # xmin > xmax, erreur d'intervalle
    FONCTION_VIDE = 403 # Erreur de syntaxe fonction vide : sqrt( ), sin ( ), 3+5+, 4^, etc.
    #... (à ajouter au fur et à mesure)



# -------------------------------- Prompts --------------------------------- #

# Prompts pour les erreurs liées à l'analyseur lexical (syntaxe : promptErreurLex[ErreurLex.NOM_ERREUR])
promptErreurLex = {
    ErreurLex.PAS_D_ERREUR : "Il n'y a aucune erreur.",
    ErreurLex.FONCTION_MAL_ECRITE : "La fonction n'est pas reconnue.",
    ErreurLex.RIEN_EST_TAPE_PAR_UTILISATEUR : "Veuillez inserer une fonction.",
    ErreurLex.CARACTERE_NON_RECONNU : "La fonction inclue un caractère non reconnu."
}

# Prompts pour les erreurs liées à l'analyseur syntaxique (syntaxe : promptErreurSyntax[ErreurSyntax.NOM_ERREUR])
promptErreurSyntax = {
    ErreurSyntax.PAS_D_ERREUR : "Il n'y a aucune erreur.",
    ErreurSyntax.RECHERCHE_FIN_PARENTHESE_PAS_DE_PARENTHESE_OUVRANTE : "Une parenthèse ouvrante est manquante dans la fonction.",
    ErreurSyntax.RECHERCHE_FIN_PARENTHESE_PAS_DE_PARENTHESE_FERMANTE_CORRESPONDANTE : "Une parenthèse fermante est manquante dans la fonction.",
    ErreurSyntax.LISTE_VIDE : "Veuillez inserer une fonction.",
    ErreurSyntax.ERREUR_INCONNUE : "Une erreur inconnue est survenue, veuillez nous en excusez.",
    ErreurSyntax.OPERATEUR_SANS_VALEUR_A_COTE : "Un operateur ne peut être isolé, il faut une valeur de part et d'autre de ce dernier.",
    ErreurSyntax.FONCTION_SANS_PARENTHESE : "Une fonction ne peut être employée sans parenthèse pour indiquer son paramètre.",
    ErreurSyntax.OBJETS_INCOMPATIBLE : "De objets mathèmatiques situés côte à côte sont imcompatibles entre eux."
}

# Prompts pour les erreurs liées à l'évaluateur (syntaxe : promptErreurEval[ErreurEval.NOM_ERREUR])
promptErreurEval = {
    ErreurEval.PAS_D_ERREUR : "Il n'y a aucune erreur.",
    ErreurEval.ITERATIONS_INSUFFISANTES : "Le nombre d'itérations de calcul d'image doit être supérieur ou égal à 2 pour pouvoir discrétiser la fonction.",
    ErreurEval.XMIN_SUPERIEUR_A_XMAX : "La plus petite valeur de x ne peut pas être supérieur à la plus grande.",
    ErreurEval.FONCTION_VIDE : "Des objets mathématiques sont manquants (fonction vide)."
}