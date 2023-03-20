import math
import common as c
import erreurs as er

#Arbre de test 1
jet1 = c.Jeton(c.Lexeme.OPERATEUR, c.Operateur.ADDITION)
jet2 = c.Jeton(c.Lexeme.OPERATEUR, c.Operateur.DIVISION)
jet3 = c.Jeton(c.Lexeme.OPERATEUR, c.Operateur.PUISSANCE)
jet4 = c.Jeton(c.Lexeme.FONCTION, c.Fonction.SQRT)
jet5 = c.Jeton(c.Lexeme.REEL, 3)
jet6 = c.Jeton(c.Lexeme.REEL, 4)
jet7 = c.Jeton(c.Lexeme.REEL, 5)
jet8 = c.Jeton(c.Lexeme.VARIABLE)

arbretest1 = c.ArbreJeton(jet1)
arbretest1.insert_gauche(jet2)
arbretest1.insert_droit(jet3)
arbretest1.fils_gauche.insert_gauche(jet4)
arbretest1.fils_gauche.insert_droit(jet5)
arbretest1.fils_gauche.fils_gauche.insert_gauche(jet8)
arbretest1.fils_droit.insert_droit(jet7)
arbretest1.fils_droit.insert_gauche(jet6)
#Fin de l'arbre de test 1
# f(x) = sqrt(x)/3 + 4^5
# Résultat attendu pour evaluateur(arbretest2,10,-5,4):
# [[-5.0, -4.0, -3.0, -2.0, -1.0, 0.0, 1.0, 2.0, 3.0, 4.0], 
# [None, None, None, None, None, 1024.0, 1024.3333333333333, 1024.471404520791, 1024.5773502691895, 1024.6666666666667]]

#Arbre de test 2
jet1 = c.Jeton(c.Lexeme.OPERATEUR, c.Operateur.ADDITION)
jet2 = c.Jeton(c.Lexeme.OPERATEUR, c.Operateur.DIVISION)
jet3 = c.Jeton(c.Lexeme.OPERATEUR, c.Operateur.PUISSANCE)
jet4 = c.Jeton(c.Lexeme.FONCTION, c.Fonction.SQRT)
jet5 = c.Jeton(c.Lexeme.REEL, 3)
jet6 = c.Jeton(c.Lexeme.REEL, -1)
jet7 = c.Jeton(c.Lexeme.VARIABLE)
jet8 = c.Jeton(c.Lexeme.VARIABLE)

arbretest2 = c.ArbreJeton(jet1)
arbretest2.insert_gauche(jet2)
arbretest2.insert_droit(jet3)
arbretest2.fils_gauche.insert_gauche(jet4)
arbretest2.fils_gauche.insert_droit(jet5)
arbretest2.fils_gauche.fils_gauche.insert_gauche(jet8)
arbretest2.fils_droit.insert_droit(jet7)
arbretest2.fils_droit.insert_gauche(jet6)
#Fin de l'arbre de test 2
# f(x) = sqrt(x)/3 + (-1)^x
# Résultat attendu pour evaluateur(arbretest2,10,-5,4): 
#[[-5.0, -4.0, -3.0, -2.0, -1.0, 0.0, 1.0, 2.0, 3.0, 4.0],
#[None, None, None, None, None, 1.0, -0.6666666666666667, 1.4714045207910318, -0.42264973081037427, 1.6666666666666665]]

#Arbre de test 3
jet1 = c.Jeton(c.Lexeme.OPERATEUR, c.Operateur.ADDITION)
jet2 = c.Jeton(c.Lexeme.OPERATEUR, c.Operateur.DIVISION)
jet3 = c.Jeton(c.Lexeme.OPERATEUR, c.Operateur.PUISSANCE)
jet4 = c.Jeton(c.Lexeme.FONCTION, c.Fonction.SQRT)
jet5 = c.Jeton(c.Lexeme.REEL, 3)
jet6 = c.Jeton(c.Lexeme.REEL, -1)
jet7 = c.Jeton(c.Lexeme.VARIABLE)


arbretest3 = c.ArbreJeton(jet1)
arbretest3.insert_gauche(jet2)
arbretest3.insert_droit(jet3)
arbretest3.fils_gauche.insert_gauche(jet4)
arbretest3.fils_gauche.insert_droit(jet5)
arbretest3.fils_droit.insert_droit(jet7)
arbretest3.fils_droit.insert_gauche(jet6)
#Fin de l'arbre de test 3
# f(x) = sqrt()/3 + (-1)^x
#Contient une erreur de syntaxe : sqrt(∅)
#Résultat attendu : FONCTION_VIDE (erreur de syntaxe telle que sin(∅), sqrt(∅), ∅^k, k+∅, k*∅...)


def postorderTraversal(root, x):
    if root is None :
        return ''
    else:
        if root.jeton.lexeme == c.Lexeme.REEL:
            return root.jeton.valeur
        elif root.jeton.lexeme == c.Lexeme.OPERATEUR:
            if root.jeton.valeur == c.Operateur.ADDITION:
                if root.fils_gauche is None :
                  return 'fonctionvide'
                if root.fils_droit is None :
                  return 'fonctionvide'
                fg = postorderTraversal(root.fils_gauche,x)
                fd = postorderTraversal(root.fils_droit,x)
                #test d'une erreur du domaine de définition mathématique
                if fg == 'erreurdef':
                  return 'erreurdef'
                if fd == 'erreurdef':
                  return 'erreurdef'
                #test d'une erreur de syntaxe (fonction vide)
                if fg == 'fonctionvide':
                  return 'fonctionvide'
                if fd == 'fonctionvide':
                  return 'fonctionvide'
                return fg + fd
            elif root.jeton.valeur == c.Operateur.MULTIPLICATION:
                if root.fils_gauche is None :
                  return 'fonctionvide'
                if root.fils_droit is None :
                  return 'fonctionvide'
                fg = postorderTraversal(root.fils_gauche,x)
                fd = postorderTraversal(root.fils_droit,x)
                #test d'une erreur du domaine de définition mathématique
                if fg == 'erreurdef':
                  return 'erreurdef'
                if fd == 'erreurdef':
                  return 'erreurdef'
                #test d'une erreur de syntaxe (fonction vide)
                if fg == 'fonctionvide':
                  return 'fonctionvide'
                if fd == 'fonctionvide':
                  return 'fonctionvide'
                return fg * fd
            elif root.jeton.valeur == c.Operateur.SOUSTRACTION:
                if root.fils_gauche is None :
                  return 'fonctionvide'
                if root.fils_droit is None :
                  return 'fonctionvide'
                fg = postorderTraversal(root.fils_gauche,x)
                fd = postorderTraversal(root.fils_droit,x)
                #test d'une erreur du domaine de définition mathématique
                if fg == 'erreurdef':
                  return 'erreurdef'
                if fd == 'erreurdef':
                  return 'erreurdef'
                #test d'une erreur de syntaxe (fonction vide)
                if fg == 'fonctionvide':
                  return 'fonctionvide'
                if fd == 'fonctionvide':
                  return 'fonctionvide'
                return fg - fd
            elif root.jeton.valeur == c.Operateur.DIVISION:
                if root.fils_gauche is None :
                  return 'fonctionvide'
                if root.fils_droit is None :
                  return 'fonctionvide'
                fg = postorderTraversal(root.fils_gauche,x)
                fd = postorderTraversal(root.fils_droit,x)
                #test d'une erreur du domaine de définition mathématique
                if fg == 'erreurdef':
                  return 'erreurdef'
                if fd == 'erreurdef':
                  return 'erreurdef'
                #test d'une erreur de syntaxe (fonction vide)
                if fg == 'fonctionvide':
                  return 'fonctionvide'
                if fd == 'fonctionvide':
                  return 'fonctionvide'
                if root.fils_droit.jeton.lexeme == c.Lexeme.VARIABLE and x == 0 :
                  x = 10e-300
                if root.fils_droit.jeton.valeur == 0:
                  root.fils_droit.jeton.valeur = 10e-300
                return fg/fd
            elif root.jeton.valeur == c.Operateur.PUISSANCE:
                if root.fils_gauche is None :
                  return 'fonctionvide'
                if root.fils_droit is None :
                  return 'fonctionvide'
                fg = postorderTraversal(root.fils_gauche,x)
                fd = postorderTraversal(root.fils_droit,x)
                #test d'une erreur du domaine de définition mathématique
                if fg == 'erreurdef':
                  return 'erreurdef'
                if fd == 'erreurdef':
                  return 'erreurdef'
                #test d'une erreur de syntaxe (fonction vide)
                if fg == 'fonctionvide':
                  return 'fonctionvide'
                if fd == 'fonctionvide':
                  return 'fonctionvide'
                return pow(fg, fd)
        elif root.jeton.lexeme == c.Lexeme.FONCTION:
            if root.jeton.valeur == c.Fonction.ABS:
                if root.fils_gauche is None :
                  return 'fonctionvide'
                fg = postorderTraversal(root.fils_gauche,x)
                #test d'une erreur du domaine de définition mathématique
                if fg == 'erreurdef':
                  return 'erreurdef'
                #test d'une erreur de syntaxe (fonction vide)
                if fg == 'fonctionvide':
                  return 'fonctionvide'
                return abs(fg)
            elif root.jeton.valeur == c.Fonction.SIN:
                if root.fils_gauche is None :
                  return 'fonctionvide'
                fg = postorderTraversal(root.fils_gauche,x)
                #test d'une erreur du domaine de définition mathématique
                if fg == 'erreurdef':
                  return 'erreurdef'
                #test d'une erreur de syntaxe (fonction vide)
                if fg == 'fonctionvide':
                  return 'fonctionvide'
                return math.sin(fg)
            elif root.jeton.valeur == c.Fonction.SQRT:
                if root.fils_gauche is None :
                  return 'fonctionvide'
                fg = postorderTraversal(root.fils_gauche,x)
                #test d'une erreur du domaine de définition mathématique
                if fg < 0:
                  fg = 'erreurdef'
                if fg == 'erreurdef':
                  return 'erreurdef'
                #test d'une erreur de syntaxe (fonction vide)
                if fg == 'fonctionvide':
                  return 'fonctionvide'
                return math.sqrt(fg)
            elif root.jeton.valeur == c.Fonction.COS:
                fg = postorderTraversal(root.fils_gauche,x)
                #test d'une erreur du domaine de définition mathématique
                if fg == 'erreurdef':
                  return 'erreurdef'
                #test d'une erreur de syntaxe (fonction vide)
                if fg == 'fonctionvide':
                  return 'fonctionvide'
                return math.cos(fg)
            elif root.jeton.valeur == c.Fonction.EXP:
                fg = postorderTraversal(root.fils_gauche,x)
                #test d'une erreur du domaine de définition mathématique
                if fg == 'erreurdef':
                  return 'erreurdef'
                #test d'une erreur de syntaxe (fonction vide)
                if fg == 'fonctionvide':
                  return 'fonctionvide'
                return math.exp(fg)
        elif root.jeton.lexeme == c.Lexeme.VARIABLE:
            return x




def evaluateur(arbre,nomb, xmin, xmax):
    if nomb <= 0 :
      return er.ErreurEval.ITERATION_NULLE_OU_NEGATIVE
    res = [[0] * nomb, [0] * nomb]
    if xmin > xmax : # Vérification de l'intervalle
      return er.ErreurEval.XMIN_SUPERIEUR_A_XMAX
    if nomb == 1 and xmin != xmax: # S'il n'y a qu'une seule itération, on vérifie que xmin=xmax
      return er.ErreurEval.XMIN_DIFFERENT_XMAX
    if nomb == 1: # S'il n'y a qu'une seule itération, on retourne le xmin et son image
      res[0][0] = xmin
      res[1][0] = postorderTraversal(arbre,xmin)
      if res[1][0] == 'erreurdef':
            res[1][0] = None
      if isinstance(res[1][0], complex):
            res[1][0] = None
      return res

      

    for i in range(nomb):
       res[0][i] = xmin + i*(xmax-xmin)/(nomb-1)
    for i in range(nomb):
        res[1][i] = postorderTraversal(arbre,res[0][i])
        if res[1][i] == 'fonctionvide':
          return er.ErreurEval.FONCTION_VIDE
        if res[1][i] == 'erreurdef':
            res[1][i] = None
        if isinstance(res[1][i], complex):
            res[1][i] = None
    return res