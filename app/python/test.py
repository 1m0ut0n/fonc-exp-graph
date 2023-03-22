##############################################################################
#                                  Tests                       (Par Gaspard) #
#                                                                            #
# Ce programme  nous sert à automatiser les tests. Pour l'utiliser, il       #
# suffit de le lancer dans un invité de commande avec la commande :          #
#                                                                            #
#    > python "app/python/test.py"                                           #
#                                                                            #
#                                                                            #
# Cette dèrnière fonctionne comme suit :                                     #
#  -> Il vous est d'abort demandé d'entrer une fonction à analyser sous      #
#     forme de texte.                                                        #
#  <- Pour chacunes des étapes de l'analyse, le retour* de la fonction       #
#     d'analyse est donné. Si il y a une erreur, on arretera à cette étape   #
#     et on donnera l'erreur. Cela permet d'analyser le déroulé de           #
#     l'analyse sans utiliser le site.                                       #
#                                                                            #
#  *Le retour de l'arbre de lexeme après l'étape d'analyse syntaxique est    #
#   disponible sous forme de texte mais aussi sous forme de code mermaid     #
#   que l'on peut visualiser avec https://mermaid.live/                      #
##############################################################################

from erreurs import ErreurLex, ErreurSyntax, ErreurEval
from lex import lex_analyser
from syntax import syntax_analyser, arbre_to_mermaid
from evaluator import evaluateur



# --------------------------------- Input ---------------------------------- #

chaine_entree = "" # Remplacer l'interieur pour un remplissage automatique sinon laisser vide
if chaine_entree == "" :
    chaine_entree = input("\nFonction : ") # Input fonction
else :
    print("\nFonction : " + chaine_entree) # Print fonction si input auto


# ---------------------------- Analyse lexicale ---------------------------- #

print("\n--- Output Lex ---")
erreur, liste_sortie = lex_analyser(chaine_entree) # Fonction d'analyse
if erreur is not ErreurLex.PAS_D_ERREUR :
    print("/!\ Erreur : " + erreur.name) # Output erreur si erreur
else :
    print(liste_sortie) # Output sortie si pas d'erreur


    # -------------------------- Analyse syntaxique -------------------------- #

    print("\n--- Output Syntax ---")
    erreur, arbre_test = syntax_analyser(liste_sortie) # Fonction d'analyse
    if erreur is not ErreurSyntax.PAS_D_ERREUR :
        print("/!\ Erreur : " + erreur.name) # Output erreur si erreur
    else :
        print(arbre_test) # Output sortie si pas d'erreur
        print("--- Mermaid ---\n" + arbre_to_mermaid(arbre_test)) # Output sous forme mermaid


        # --------------------------- Evaluation ---------------------------- #

        print("\n--- Output Eval ---")
        erreur, liste_val = evaluateur(arbre_test, 20, -10, 10) # Fonction de calcul
        if erreur is not ErreurEval.PAS_D_ERREUR :
            print("/!\ Erreur : " + erreur.name) # Output erreur si erreur
        else :
            print("x : " + str(liste_val[0])) # Outputs sortie si pas d'erreur
            print("y : " + str(liste_val[1]))


