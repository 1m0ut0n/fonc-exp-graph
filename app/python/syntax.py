##############################################################################
#                            Analyse syntaxique      (Par Gaspard et Nathan) #
#                                                                            #
# L'analyseur syntaxique traite un flux de couples lexème+valeur entrant.    #
# Son rôle est de vérifier la conformité de l'expression avec la grammaire   #
# définie et de produire en sortie un flux de code postfixé (en forme        #
# d’arbre binaire).                                                          #
#                                                                            #
#  -> Prend en entrée un tableau de jetons correspondant à l'analyse         #
#     lexicale                                                               #
#  <- Donne en sortie un arbre triant les jetons en suivant les règles       #
#     mathematiques                                                          #
##############################################################################

from common import *
from erreurs import ErreurSyntax


# --------------------------- Analyse syntaxique --------------------------- #

def syntax_analyser(lexem_table):
    '''Fonction principale de notre programme. L'objectif de la fonction est de transformer un tableau entré en paramètre sous forme d'arbre binaire. Elle utilise pour cela principalement la fonction `separation` et ne sert qu'à compartimenter et eviter la possibilité d'un renvoie d'arbre alors qu'il y a une erreur.
    
    Paramètre :
        
        lexem_table :  (list -> Jeton) Table des lexèmes issue de l'analyse syntaxique.
    
    Retour :
        1)  (ErreurSyntax) Code d'erreur `ErreurSyntax` si il y en a un, `ErreurSyntax.PAS_D_ERREUR` sinon.

        2)  (ArbreJeton) Arbre binaire construit à partir de la fonction.
    '''
    # On utilise la fonction d'analyse récursive
    erreur, arbre_construit = separation(lexem_table)

    # Suivant si il y a eu une erreur ou non, on renvoie l'arbre ou non et l'erreur qui va avec
    if erreur is not ErreurSyntax.PAS_D_ERREUR :
        return erreur, None
    else :
        return ErreurSyntax.PAS_D_ERREUR, arbre_construit



def separation(current_table) :
    '''Fonction qui gère la séparation du tableau en plusieurs partie à traiter de manière récursive en remplissant l'arbre.
    
    Paramètre :
        
        lexem_table :  (list -> Jeton) Table des lexèmes que l'on considère.
    
    Retour :

        1)  (ErreurSyntax) Code d'erreur `ErreurSyntax` si il y en a un, `ErreurSyntax.PAS_D_ERREUR` sinon.

        2)  (ArbreJeton) Arbre construit à partir de cette partie de la table.
    '''

    # On enregistre la taille du tableau
    taille = len(current_table)

    # Debug : Visualiser les étapes
    # print("Step : " + str(current_table))

    # Si la liste est vide, c'est pas normal et il y a eu un problème 
    if taille == 0 :
        return ErreurSyntax.ERREUR_INCONNUE, None

    # Il est impossible de commencer ou de terminer par un operateur, si c'est le cas, on renvoie une erreur diasnt qu'une opération est impossible
    # Le seul opérateur par lequel on peut commencer est l'opérateur '-', cela equivaut à une multiplication par '-1', on fait alors une exeption pour ce cas et que l'on enregistre comme produit par '-1' de ce que l'on analyse derrière
    if current_table[0].lexeme is Lexeme.OPERATEUR or current_table[-1].lexeme is Lexeme.OPERATEUR : # Test operateur au debut ou à la fin
        if current_table[0].valeur is Operateur.SOUSTRACTION : # Exeption '-' au début
            arbre = ArbreJeton(Jeton(Lexeme.OPERATEUR, Operateur.MULTIPLICATION)) # On créer un noeud pour la multiplication par '-1'
            arbre.fils_gauche = ArbreJeton(Jeton(Lexeme.REEL, -1)) # Noeud '-1'
            erreur, arbre.fils_droit = separation(current_table[1:]) # Remplissage de l'arbre à droite
            if erreur is not ErreurSyntax.PAS_D_ERREUR : # Si le remplissage renvoie une erreur, on la transfère
                return erreur, None
            else :
                return ErreurSyntax.PAS_D_ERREUR, arbre
        else : # Retour de l'erreur pour les autres opérateurs
            return ErreurSyntax.OPERATEUR_SANS_VALEUR_A_COTE, None
    
    # Il est aussi impossible de commencer par une parenthèse fermante, si c'est le cas, on renvoie aussi une erreur
    if current_table[0].lexeme is Lexeme.PARENTHESE_FERM :
        return ErreurSyntax.RECHERCHE_FIN_PARENTHESE_PAS_DE_PARENTHESE_OUVRANTE, None
    
    # Si tout est entre parenthèse, on les enlève et analyse ce qu'il y a à l'intérieur
    if current_table[0].lexeme is Lexeme.PARENTHESE_OUV : # Si on a une parenthèse au début
        erreur, pos_parenthese = recherche_fin_parenthese(current_table, 0) # Recherche de la parenthèse fermante correspondante à la parenthèse du début
        if erreur is not ErreurSyntax.PAS_D_ERREUR : # Si la recherche renvoie une erreur, on la transfère
            return erreur, None
        else :
            if pos_parenthese == taille-1 : # Si la parenthèse fermante est à la fin
                return separation(current_table[1:-1])

    # On souhaite alors rechercher des operateurs en parcourant le tableau et sans considerer l'interieur des parentheses
    # Cela se passera en 3 etapes : d'abort on ne testera que les + et - puis on testera les *, / et enfin ^
    for operateurs_recherches in [[Operateur.ADDITION, Operateur.SOUSTRACTION],[Operateur.MULTIPLICATION, Operateur.DIVISION], [Operateur.PUISSANCE]] : # Pour refaire l'analyse trois fois : d'abort avec les opérateurs + et - puis les operateurs *, / et enfin ^
        i = 0
        while (i < taille) : # On parcours l'ensemble de la liste

            # Si on rencontre un des opérateur recherché, on le mets dans l'arbre et on analyse separement la partie à droite et à gauche de l'opérateur
            if current_table[i].lexeme is Lexeme.OPERATEUR and current_table[i].valeur in operateurs_recherches :
                arbre = ArbreJeton(current_table[i]) # On créer le noeud avec l'opérateur
                erreur, arbre.fils_gauche = separation(current_table[:i]) # Remplissage de l'arbre à gauche
                if erreur is not ErreurSyntax.PAS_D_ERREUR : # Si le remplissage renvoie une erreur, on la transfère
                    return erreur, None
                else :
                    erreur, arbre.fils_droit = separation(current_table[i+1:]) # Remplissage de l'arbre à droite
                    if erreur is not ErreurSyntax.PAS_D_ERREUR : # Si le remplissage renvoie une erreur, on la transfère
                        return erreur, None
                    else : # Sinon on retourne l'arbre
                        return ErreurSyntax.PAS_D_ERREUR, arbre
                    
            # Si on a des parenthèse, on passe ce qu'il y a entre parenthèse
            elif current_table[i].lexeme is Lexeme.PARENTHESE_OUV :
                erreur, pos_parenthese = recherche_fin_parenthese(current_table, i) # Recherche de la parenthèse fermante correspondante
                if erreur is not ErreurSyntax.PAS_D_ERREUR : # Si la recherche renvoie une erreur, on la transfère
                    return erreur, None
                else :
                    i = pos_parenthese # on passe direct à la fin des parethèses
                
            i += 1

    # Reste alors les cas ou l'on a en premier un reel, une fonction, ou la variable
    # Si c'est une fonction, on prend la fonction et on analyse ce qu'il y'a à l'intérieur de la parenthese
    if current_table[0].lexeme is Lexeme.FONCTION :
        if current_table[1].lexeme is Lexeme.PARENTHESE_OUV : # Test qu'il y ai bien une parenthèse après la fonction
            erreur, pos_parenthese = recherche_fin_parenthese(current_table, 1) # Recherche de la parenthèse fermante correspondante à la fin de l'intérieur de la fonction
            if erreur is not ErreurSyntax.PAS_D_ERREUR : # Si la recherche renvoie une erreur, on la transfère
                return erreur, None
            else :
                # On verifie qu'il n'y ai pas d'objet derrière, il n'est pas sensé en avoir, si il n'y en a pas, on ajoute la fonction et on analyse l'interieur
                if pos_parenthese == taille-1 :
                    arbre = ArbreJeton(current_table[0]) # On créer le noeud avec la fonction
                    erreur, arbre.fils_droit = separation(current_table[2:-1]) # Remplissage de l'arbre à droite
                    if erreur is not ErreurSyntax.PAS_D_ERREUR : # Si le remplissage renvoie une erreur, on la transfère
                        return erreur, None
                    else :
                        return ErreurSyntax.PAS_D_ERREUR, arbre
                else : # Transfere de l'erreur si il y a des objets derrière
                    return ErreurSyntax.OBJETS_INCOMPATIBLE, None
        else : # Transfere de l'erreur si il n'y a pas de perethèse
            return ErreurSyntax.FONCTION_SANS_PARENTHESE, None
        
    # Enfin, on regarde si on a une variable ou un réel et, de la même manière, on vérifie qu'il n'y ai aucun objet derrière
    if current_table[0].lexeme in [Lexeme.VARIABLE, Lexeme.REEL] :
        if taille == 1 :
            return ErreurSyntax.PAS_D_ERREUR, ArbreJeton(current_table[0]) # On créer le noeud avec la variable
        else : # Transfere de l'erreur si il y a des objets derrière
            return ErreurSyntax.OBJETS_INCOMPATIBLE, None

    # Si aucun de ces cas à été pris en compte, il y a eu un problème
    return ErreurSyntax.ERREUR_INCONNUE, None



# ---------------------- Recherche des parenthèses 2 ----------------------- #

def recherche_fin_parenthese(lexem_table, position = 0) :
    '''Recherche la parenthèse fermante correspondant à la parethése ouvrante en entrée.

    Paramètres :
        
        lexem_table :  (list -> Jeton) Table des lexèmes.
        
        position :  (int) Position de la parenthèse ouvrante dans la table `lexem_table`.

    Retour :
        
        1)  (ErreurSyntax) Code d'erreur `ErreurSyntax` si il y en a un, `ErreurSyntax.PAS_D_ERREUR` sinon.
        
        2)  (int) Position de la parenthèse fermante correspondante. Rien si il y a une erreur.
    '''
    
    # Verification que l'on a bien une parenthèse ouvrante
    if lexem_table[position].lexeme == Lexeme.PARENTHESE_OUV :
        
        # On a rencontré une parenthèse
        couple_parenthese = 1

        # On parcours le reste du tableau pour repèrer les parenthèses
        # Si on rencontre une parenthèse ouverte, on indente `couple_parenthese` et si on rencontre une parenthèse fermée, on le désindente
        for i in range(position+1, len(lexem_table)) :
            if lexem_table[i].lexeme == Lexeme.PARENTHESE_OUV : 
                couple_parenthese += 1
            elif lexem_table[i].lexeme == Lexeme.PARENTHESE_FERM :
                couple_parenthese -= 1
            # Ainsi si on arrive à 0, c'est que l'on a rencontré la parenthèse correspondante, on retourne la position
            if couple_parenthese == 0 :
                return ErreurSyntax.PAS_D_ERREUR, i

        # Si on ne retombe jamais sur 0, c'est qu'il y a un problème avec les parenthèses
        return ErreurSyntax.RECHERCHE_FIN_PARENTHESE_PAS_DE_PARENTHESE_FERMANTE_CORRESPONDANTE, None

    # Si il n'y a pas de parenthèse ouvrante au début
    else :
        return ErreurSyntax.RECHERCHE_FIN_PARENTHESE_PAS_DE_PARENTHESE_OUVRANTE, None



# ---------------------------------- Debug ---------------------------------- #


# Fonction de debug pour traduire un arbre en mermaid (pour l'afficher proprement)
def arbre_to_mermaid(arbre : ArbreJeton) :
    code_mermaid = "graph TB;\n"
    if arbre is not None :
        liste_parcours = [arbre]
        liste_parents = [None]
        i = 0
        while (i<len(liste_parcours)) :
            if i == 0 :
                code_mermaid += "   "
            else :
                code_mermaid += "   jet" + str(liste_parents[i]) + " --> "
            code_mermaid += "jet" + str(i) + "(" + str(liste_parcours[i].jeton) + ")\n"
            if liste_parcours[i].fils_gauche is not None :
                liste_parcours.append(liste_parcours[i].fils_gauche)
                liste_parents.append(i)
            if liste_parcours[i].fils_droit is not None :
                liste_parcours.append(liste_parcours[i].fils_droit)
                liste_parents.append(i)
            i += 1
    return code_mermaid


"""
# Exemple : 
#     Tableau puis arbre de Lexemes representant l'expression
#         5+sin(x-(-3.5))


# Tableu de lexeme tel que sorti de l'analyse lexical
expression = [
    Jeton(Lexeme.REEL, 5), 
    Jeton(Lexeme.OPERATEUR, Operateur.ADDITION),
    Jeton(Lexeme.FONCTION, Fonction.SIN),
    Jeton(Lexeme.PARENTHESE_OUV),
    Jeton(Lexeme.VARIABLE),
    Jeton(Lexeme.OPERATEUR, Operateur.SOUSTRACTION),
    Jeton(Lexeme.PARENTHESE_OUV),
    Jeton(Lexeme.REEL, -1),
    Jeton(Lexeme.OPERATEUR, Operateur.MULTIPLICATION),
    Jeton(Lexeme.REEL, 3.5),
    Jeton(Lexeme.PARENTHESE_FERM),
    Jeton(Lexeme.PARENTHESE_FERM)
    ]

# Arbre de lexeme tel que devrai etre la sortie de l'analyse syntaxique
expression_arbre = ArbreJeton(Jeton(Lexeme.OPERATEUR, Operateur.ADDITION))
expression_arbre.insert_gauche(Jeton(Lexeme.REEL, 5))
expression_arbre.insert_droit(Jeton(Lexeme.FONCTION, Fonction.SIN))
expression_arbre.fils_droit.insert_droit(Jeton(Lexeme.OPERATEUR, Operateur.SOUSTRACTION))
expression_arbre.fils_droit.fils_droit.insert_gauche(Jeton(Lexeme.VARIABLE))
expression_arbre.fils_droit.fils_droit.insert_droit(Jeton(Lexeme.OPERATEUR, Operateur.MULTIPLICATION))
expression_arbre.fils_droit.fils_droit.fils_droit.insert_gauche(Jeton(Lexeme.REEL, -1))
expression_arbre.fils_droit.fils_droit.fils_droit.insert_droit(Jeton(Lexeme.REEL, 3.5))


# Fonction pour automatiser les tests
def test_syntax(expression) :
    erreur, arbre_test = syntax_analyser(expression)

    if erreur is not ErreurSyntax.PAS_D_ERREUR :
        print("Erreur : " + erreur.name)
    else :
        print("\n--- Output ---")
        print(arbre_test)
        print("--- Mermaid ---\n" + arbre_to_mermaid(arbre_test))

test_syntax(expression)
"""