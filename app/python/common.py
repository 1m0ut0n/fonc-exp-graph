##############################################################################
#                              Objets communs                  (Par Gaspard) #
#                                                                            #
# Ce fichier regroupe toute les types de variables spécifiques créé pour     #
# le calculateur et qui serviront dans plusieurs étapes différentes.         #
# On y trouve notamment :                                                    #
#  - L'enumeration des lexemes pris en charges                               #
#  - L'enumeration des opérateurs pris en charges                            #
#  - L'enumeration des fonctions prise en charges                            #
#  - La classe pour les jetons, qui réunis le lexeme et sa valeur            #
#  - La classe pour les arbrees binaires de jetons                           #
#                                                                            #
# -> Chacune des classes possèdes des méthodes d'affichage pour simplifier   #
#    le debugage                                                             #
##############################################################################

from enum import Enum



# ------------------------------ Enumerations ------------------------------ #


# Enumeration des lexèmes (syntaxe : Lexeme.NOM_LEXEME)
class Lexeme(Enum) :
    REEL = 0
    OPERATEUR = 1
    FONCTION = 2
    PARENTHESE_OUV = 3
    PARENTHESE_FERM = 4
    VARIABLE = 5


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



# ------------------------------ Classe Jeton ------------------------------ #

class Jeton :
    def __init__(self, lex, val = None) :
        self.lexeme = lex
        self.valeur = val
    

    # Transformer un jeton en texte
    def __str__(self) :
        valeur = ""
        if self.valeur is not None :
            if self.lexeme is Lexeme.REEL :
                valeur = " : " + str(self.valeur)
            else :
                valeur = " : " + self.valeur.name
        return str(self.lexeme.name) + valeur
    
    # Affichage console
    def __repr__(self) :
        return str(self)


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



# -------------------------- Classe Arbre Binaire -------------------------- #

## Definition de l'arbre
class ArbreJeton : 
    def __init__(self, jet = None):
        self.jeton = jet
        self.fils_gauche = None
        self.fils_droit = None


    # Inserer un nouveau noeud à gauche
    def insert_gauche(self, jet):
        if self.fils_gauche == None:
            self.fils_gauche = ArbreJeton(jet)
        else:
            new_node = ArbreJeton(jet)
            new_node.fils_gauche = self.fils_gauche
            self.fils_gauche = new_node

    # Inserer un nouveau noeud à gauche
    def insert_droit(self, jet):
        # Inserer un jeton à droite
        if self.fils_droit == None:
            self.fils_droit = ArbreJeton(jet)
        else:
            new_node = ArbreJeton(jet)
            new_node.fils_droit = self.fils_droit
            self.fils_droit = new_node
    

    # Copier un arbre et ecraser les fils sans ecraser la racine (première iteration de `__copy_node`)
    def copy(self, arbre_original) :
        if arbre_original is not None :
            self.jeton = arbre_original.jeton
            self.__copy_node(self.fils_gauche, arbre_original.fils_gauche)
            self.__copy_node(self.fils_droit, arbre_original.fils_droit)
    
    def __copy_node(self, noeud, noeud_arbre_original) :
        if noeud_arbre_original is not None :
            noeud.jeton = ArbreJeton(noeud_arbre_original.jeton)
            self.__copy_node(noeud.fils_gauche, noeud_arbre_original.fils_gauche)
            self.__copy_node(noeud.fils_droit, noeud_arbre_original.fils_droit)
    

    # Transformer un arbre en texte (appelle la fonction récursive `__write_node` avec une hauteur de 0)
    def __str__(self) :
        return self.__write_node(0)
        
    def __write_node(self, hauteur) :
        texte_noeud = "   "*hauteur + " ↳ " + str(self.jeton) + "\n"
        if self.fils_gauche is not None :
            texte_noeud += self.fils_gauche.__write_node(hauteur + 1)
        if self.fils_droit is not None :
            texte_noeud += self.fils_droit.__write_node(hauteur + 1)
        return texte_noeud
    
    # Affichage console
    def __repr__(self) :
        return str(self)


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