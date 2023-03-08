import math
from enum import Enum

nomb = eval(input("Entrez votre nombre d'itérations: \n"))
xmin = eval(input("Entrez votre xmin: \n"))
xmax = eval(input("Entrez votre xmax: \n"))

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

# Declaration de l'arbre (avec des pointeurs vers les jetons)

#### ------ ARBRE ------

## Definition de l'arbre
class Arbre: 
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
            self.fils_droit = Arbre(jet)
        else:
            new_node = Arbre(jet)
            new_node.fils_droit = self.fils_droit
            self.fils_droit = new_node

jet1 = Jeton(Lexeme.OPERATEUR, Operateur.ADDITION)
jet2 = Jeton(Lexeme.OPERATEUR, Operateur.DIVISION)
jet3 = Jeton(Lexeme.OPERATEUR, Operateur.PUISSANCE)
jet4 = Jeton(Lexeme.FONCTION, Fonction.SIN)
jet5 = Jeton(Lexeme.VARIABLE, val=None)
jet6 = Jeton(Lexeme.REEL, 4)
jet7 = Jeton(Lexeme.REEL, 5)
jet8 = Jeton(Lexeme.VARIABLE, val=None)

arbre1 = Arbre(jet1)
arbre1.insert_gauche(jet2)
arbre1.insert_droit(jet3)
arbre1.fils_gauche.insert_gauche(jet4)
arbre1.fils_gauche.insert_droit(jet5)
arbre1.fils_gauche.fils_gauche.insert_gauche(jet8)
arbre1.fils_droit.insert_droit(jet7)
arbre1.fils_droit.insert_gauche(jet6)


def postorderTraversal(root, x):
    if root is None :
        return ''
    else:
        if root.jeton.lexeme == Lexeme.REEL:
            return root.jeton.valeur
        elif root.jeton.lexeme == Lexeme.OPERATEUR:
            if root.jeton.valeur == Operateur.ADDITION:
                return postorderTraversal(root.fils_gauche,x) + postorderTraversal(root.fils_droit,x)
            elif root.jeton.valeur == Operateur.MULTIPLICATION:
                return postorderTraversal(root.fils_gauche,x) * postorderTraversal(root.fils_droit,x)
            elif root.jeton.valeur == Operateur.SOUSTRACTION:
                return postorderTraversal(root.fils_gauche,x) - postorderTraversal(root.fils_droit,x)
            elif root.jeton.valeur == Operateur.DIVISION:
                if root.fils_droit.jeton.valeur == 0:
                  print("Problème : Division par zero!!!")
                  root.fils_droit.jeton.valeur = root.fils_droit.jeton.valeur + 10e-6
                return postorderTraversal(root.fils_gauche,x) / postorderTraversal(root.fils_droit,x)
            elif root.jeton.valeur == Operateur.PUISSANCE:
                return pow(postorderTraversal(root.fils_gauche,x), postorderTraversal(root.fils_droit,x))
        elif root.jeton.lexeme == Lexeme.FONCTION:
            if root.jeton.valeur == Fonction.ABS:
                return abs(root.fils_gauche.jeton.valeur)
            elif root.jeton.valeur == Fonction.SIN:
                return math.sin(root.fils_gauche.jeton.valeur)
            elif root.jeton.valeur == Fonction.SQRT:
                return math.sqrt(root.fils_gauche.jeton.valeur)
            elif root.jeton.valeur == Fonction.COS:
                return math.cos(root.fils_gauche.jeton.valeur)
            elif root.jeton.valeur == Fonction.EXP:
                return math.exp(root.fils_gauche.jeton.valeur)
        elif root.jeton.lexeme == Lexeme.VARIABLE:
            return x


#func = postorderTraversal(arbre1, x)
#print(func)

def evaluateur(nomb, xmin, xmax):
    res = [[0] * nomb, [0] * nomb]
    for i in range(nomb):
        res[0][i] = xmin + i*(xmax-xmin)/nomb
    for i in range(nomb):
        if res[0][i] == 0 :
          res[0][i] == res[0][i] + 10e-6
    for i in range(nomb):
        res[1][i] = postorderTraversal(arbre1,res[0][i]) 
    return res

liste = evaluateur(nomb, xmin, xmax)
print(liste)