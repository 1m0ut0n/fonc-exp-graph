import math
import common as c
import syntax as syn

nomb = eval(input("Entrez votre nombre d'itérations: \n"))
xmin = eval(input("Entrez votre xmin: \n"))
xmax = eval(input("Entrez votre xmax: \n"))

#Arbre de test 1
jet1 = c.Jeton(c.Lexeme.OPERATEUR, c.Operateur.ADDITION)
jet2 = c.Jeton(c.Lexeme.OPERATEUR, c.Operateur.DIVISION)
jet3 = c.Jeton(c.Lexeme.OPERATEUR, c.Operateur.PUISSANCE)
jet4 = c.Jeton(c.Lexeme.FONCTION, c.Fonction.SQRT)
jet5 = c.Jeton(c.Lexeme.REEL, 3)
jet6 = c.Jeton(c.Lexeme.REEL, 4)
jet7 = c.Jeton(c.Lexeme.REEL, 5)
jet8 = c.Jeton(c.Lexeme.VARIABLE)

arbre1 = c.ArbreJeton(jet1)
arbre1.insert_gauche(jet2)
arbre1.insert_droit(jet3)
arbre1.fils_gauche.insert_gauche(jet4)
arbre1.fils_gauche.insert_droit(jet5)
arbre1.fils_gauche.fils_gauche.insert_gauche(jet8)
arbre1.fils_droit.insert_droit(jet7)
arbre1.fils_droit.insert_gauche(jet6)
#Fin de l'arbre de test 1

#Arbre de test 2
jet1 = c.Jeton(c.Lexeme.OPERATEUR, c.Operateur.ADDITION)
jet2 = c.Jeton(c.Lexeme.OPERATEUR, c.Operateur.DIVISION)
jet3 = c.Jeton(c.Lexeme.OPERATEUR, c.Operateur.PUISSANCE)
jet4 = c.Jeton(c.Lexeme.FONCTION, c.Fonction.SQRT)
jet5 = c.Jeton(c.Lexeme.REEL, 3)
jet6 = c.Jeton(c.Lexeme.REEL, -1)
jet7 = c.Jeton(c.Lexeme.VARIABLE)
jet8 = c.Jeton(c.Lexeme.VARIABLE)

arbre2 = c.ArbreJeton(jet1)
arbre2.insert_gauche(jet2)
arbre2.insert_droit(jet3)
arbre2.fils_gauche.insert_gauche(jet4)
arbre2.fils_gauche.insert_droit(jet5)
arbre2.fils_gauche.fils_gauche.insert_gauche(jet8)
arbre2.fils_droit.insert_droit(jet7)
arbre2.fils_droit.insert_gauche(jet6)
#Fin de l'arbre de test 2



def postorderTraversal(root, x):
    if root is None :
        return ''
    else:
        if root.jeton.lexeme == c.Lexeme.REEL:
            return root.jeton.valeur
        elif root.jeton.lexeme == c.Lexeme.OPERATEUR:
            if root.jeton.valeur == c.Operateur.ADDITION:
                fg = postorderTraversal(root.fils_gauche,x)
                fd = postorderTraversal(root.fils_droit,x)
                if fg == 'erreurdef':
                  return 'erreurdef'
                if fd == 'erreurdef':
                  return 'erreurdef'
                return fg + fd
            elif root.jeton.valeur == c.Operateur.MULTIPLICATION:
                fg = postorderTraversal(root.fils_gauche,x)
                fd = postorderTraversal(root.fils_droit,x)
                if fg == 'erreurdef':
                  return 'erreurdef'
                if fd == 'erreurdef':
                  return 'erreurdef'
                return fg * fd
            elif root.jeton.valeur == c.Operateur.SOUSTRACTION:
                fg = postorderTraversal(root.fils_gauche,x)
                fd = postorderTraversal(root.fils_droit,x)
                if fg == 'erreurdef':
                  return 'erreurdef'
                if fd == 'erreurdef':
                  return 'erreurdef'
                return fg - fd
            elif root.jeton.valeur == c.Operateur.DIVISION:
                fg = postorderTraversal(root.fils_gauche,x)
                fd = postorderTraversal(root.fils_droit,x)
                if fg == 'erreurdef':
                  return 'erreurdef'
                if fd == 'erreurdef':
                  return 'erreurdef'
                if root.fils_droit.jeton.lexeme == c.Lexeme.VARIABLE and x == 0 :
                  x = 10e-300
                if root.fils_droit.jeton.valeur == 0:
                  root.fils_droit.jeton.valeur = 10e-300
                return fg/fd
            elif root.jeton.valeur == c.Operateur.PUISSANCE:
                fg = postorderTraversal(root.fils_gauche,x)
                fd = postorderTraversal(root.fils_droit,x)
                if fg == 'erreurdef':
                  return 'erreurdef'
                if fd == 'erreurdef':
                  return 'erreurdef'
                return pow(fg, fd)
        elif root.jeton.lexeme == c.Lexeme.FONCTION:
            if root.jeton.valeur == c.Fonction.ABS:
                fg = postorderTraversal(root.fils_gauche,x)
                if fg == 'erreurdef':
                  return 'erreurdef'
                return abs(fg)
            elif root.jeton.valeur == c.Fonction.SIN:
                fg = postorderTraversal(root.fils_gauche,x)
                if fg == 'erreurdef':
                  return 'erreurdef'
                return math.sin(fg)
            elif root.jeton.valeur == c.Fonction.SQRT:
                fg = postorderTraversal(root.fils_gauche,x)
                if fg < 0:
                  fg = 'erreurdef'
                if fg == 'erreurdef':
                  return 'erreurdef'
                return math.sqrt(fg)
            elif root.jeton.valeur == c.Fonction.COS:
                fg = postorderTraversal(root.fils_gauche,x)
                if fg == 'erreurdef':
                  return 'erreurdef'
                return math.cos(fg)
            elif root.jeton.valeur == c.Fonction.EXP:
                fg = postorderTraversal(root.fils_gauche,x)
                if fg == 'erreurdef':
                  return 'erreurdef'
                return math.exp(fg)
        elif root.jeton.lexeme == c.Lexeme.VARIABLE:
            return x


#func = postorderTraversal(arbre1, x)
#print(func)



def evaluateur(arbre,nomb, xmin, xmax):
    if nomb <= 0 :
      return c.Erreur.ERREUR_301
    res = [[0] * nomb, [0] * nomb]
    if xmin > xmax : # Vérification de l'intervalle
      return c.Erreur.ERREUR_302
    if nomb == 1 and xmin != xmax: # S'il n'y a qu'une seule itération, on vérifie que xmin=xmax
      return c.Erreur.ERREUR_303
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
        if res[1][i] == 'erreurdef':
            res[1][i] = None
        if isinstance(res[1][i], complex):
            res[1][i] = None
    return res
