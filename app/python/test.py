from erreurs import ErreurLex, ErreurSyntax, ErreurEval
from lex import lex_analyser
from syntax import syntax_analyser, arbre_to_mermaid
from evaluator import evaluateur


# Analyse Lexicale
chaine_entree = "" # Remplacer l'interieur pour un remplissage automatique sinon laisser vide
if chaine_entree == "" :
    chaine_entree = input("\nFonction : ")
else :
    print("\nFonction : " + chaine_entree)
liste_sortie = []
print("\n--- Output Lex ---")
liste_sortie = lex_analyser(chaine_entree, liste_sortie)
print(liste_sortie)

# Analyse syntaxique
print("\n--- Output Syntax ---")
erreur, arbre_test = syntax_analyser(liste_sortie)
if erreur is not ErreurSyntax.PAS_D_ERREUR :
    print("Erreur : " + erreur.name)
else :
    print(arbre_test)
    print("--- Mermaid ---\n" + arbre_to_mermaid(arbre_test))

# Evaluation 
print("\n--- Output Eval ---")
erreur, liste_val = syntax_analyser(liste_sortie)
if erreur is not ErreurEval.PAS_D_ERREUR :
    print("Erreur : " + erreur.name)
else :
    print(liste_val[0])
    print(liste_val[1])