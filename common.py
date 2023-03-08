from enum import Enum



#### ------ ENUM ------

# Enumeration des erreurs (syntaxe : Erreur.NOM_ERREUR)
class Erreur(Enum) :
    PAS_D_ERREUR = 100
    ERREUR_1 = 101 #... (à ajouter au fur et à mesure)


# Enumeration des lexèmes (syntaxe : Lexeme.NOM_LEXEME)
class Lexeme(Enum) :
    REEL = 0
    OPERATEUR = 1
    FONCTION = 2
    INCONNU = 3
    FIN = 4
    PARENTHESE_OUV = 5
    PARENTHESE_FERM = 6
    VARIABLE = 7


# Enumeration des opérateurs (syntaxe : Operateur.NOM_OPERATEUR)
class Operateur(Enum) :
    ADDITION = 10
    SOUSTRACTION = 11
    MULTIPLICATION = 12
    DIVISION = 13
    PUISSANCE = 14


# Enumeration des fonctions (syntaxe : Fonction.NOM_FONCTION)
class Fonction(Enum) :
    ABS = 20
    SIN = 21
    SQRT = 22
    LOG = 23
    COS = 24
    TAN = 25
    EXP = 26
    VALEUR_NEGATIVE = 27


class Jeton :
    def __init__(self, lex, val = None) :
        self.lexeme = lex
        self.valeur = val


# Exemple de creation d'un jeton
# jet1 = Jeton(Lexeme.PARENTHESE_OUV)
# jet2 = Jeton(Lexeme.FONCTION, Fonction.ABS)
# jet3 = Jeton(Lexeme.REEL, 4)
# jet2 = Jeton(Lexeme.OPERATEUR, Operateur.ADDITION)

# Exemple de lecture d'un jeton
# >>> jet1.lexeme == Lexeme.PARENTHESE_OUV
#  True
# >>> jet3.valeur
#  3



#### ------ ARBRE ------

## Definition de l'arbre
class ArbreL : 
    def __init__(self, jet):
        self.jeton = jet
        self.fils_gauche = None
        self.fils_droit = None

    def insert_gauche(self, jet):
        if self.fils_gauche == None:
            self.fils_gauche = Arbre(jet)
        else:
            new_node = Arbre(jet)
            new_node.fils_gauche = self.fils_gauche
            self.fils_gauche = new_node

    def insert_droit(self, jet):
        # Inserer un jeton à droite
        if self.fils_droit == None:
            self.fils_gauche = Arbre(jet)
        else:
            new_node = Arbre(jet)
            new_node.fils_droit = self.fils_droit
            self.fils_droit = new_node

# Exemple de creation d'un arbre
# arbre1 = Arbre(jet1)

# Exemple de remplissage de l'arbre
# arbre1.insert_gauche(jet2)
# arbre1.insert_droit(jet3)

# Exemple de récupartion du sous arbre
# arbre2 = arbre1.fils_gauche

# Exemple de récupartion de la valeur du jeton du fils droit
# >>> arbre1 = arbre1.fils_droit.jeton.valeur
#  3