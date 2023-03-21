import math
import common as c
import erreurs as er

#------------------------------------ Arbres de tests ----------------------------------------------
# Tous les "résultats attendus" sont faits avec l'appel : evaluateur(arbre, 10, -5, 4).
#Arbre de test 1
# On fabrique les jetons de chaque opération/fonction/valeur
jet1 = c.Jeton(c.Lexeme.OPERATEUR, c.Operateur.ADDITION)
jet2 = c.Jeton(c.Lexeme.OPERATEUR, c.Operateur.DIVISION)
jet3 = c.Jeton(c.Lexeme.OPERATEUR, c.Operateur.PUISSANCE)
jet4 = c.Jeton(c.Lexeme.FONCTION, c.Fonction.SQRT)
jet5 = c.Jeton(c.Lexeme.REEL, 3)
jet6 = c.Jeton(c.Lexeme.REEL, 4)
jet7 = c.Jeton(c.Lexeme.REEL, 5)
jet8 = c.Jeton(c.Lexeme.VARIABLE)

# On remplit l'arbre avec les jetons
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
# Résultat attendu pour evaluateur(arbretest1,10,-5,4): (<ErreurEval.PAS_D_ERREUR: 400>, [[-5.0, -4.0, -3.0, -2.0, -1.0, 0.0, 1.0, 2.0, 3.0, 4.0], [None, None, None, None, None, 1024.0, 1024.3333333333333, 1024.471404520791, 1024.5773502691895, 1024.6666666666667]])

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
# Résultat attendu pour evaluateur(arbretest2,10,-5,4): (<ErreurEval.PAS_D_ERREUR: 400>, [[-5.0, -4.0, -3.0, -2.0, -1.0, 0.0, 1.0, 2.0, 3.0, 4.0], [None, None, None, None, None, 1.0, -0.6666666666666667, 1.4714045207910318, -0.42264973081037427, 1.6666666666666665]])

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
#Résultat attendu : (<ErreurEval.FONCTION_VIDE: 403>, [[-5.0, -4.0, -3.0, -2.0, -1.0, 0.0, 1.0, 2.0, 3.0, 4.0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])

#Arbre de test 4
jet1 = c.Jeton(c.Lexeme.OPERATEUR, c.Operateur.DIVISION)
jet2 = c.Jeton(c.Lexeme.FONCTION, c.Fonction.SIN)
jet3 = c.Jeton(c.Lexeme.FONCTION, c.Fonction.EXP)
jet4 = c.Jeton(c.Lexeme.FONCTION, c.Fonction.COS)
jet5 = c.Jeton(c.Lexeme.OPERATEUR, c.Operateur.SOUSTRACTION)
jet6 = c.Jeton(c.Lexeme.OPERATEUR, c.Operateur.PUISSANCE)
jet7 = c.Jeton(c.Lexeme.OPERATEUR, c.Operateur.MULTIPLICATION)
jet8 = c.Jeton(c.Lexeme.FONCTION, c.Fonction.LOG)
jet9 = c.Jeton(c.Lexeme.FONCTION, c.Fonction.SQRT)
jet10 = c.Jeton(c.Lexeme.REEL, 3)
jet11 = c.Jeton(c.Lexeme.REEL, 2)
jet12 = c.Jeton(c.Lexeme.VARIABLE)
jet13 = c.Jeton(c.Lexeme.FONCTION, c.Fonction.ABS)
jet14 = c.Jeton(c.Lexeme.VARIABLE)
jet15 = c.Jeton(c.Lexeme.OPERATEUR, c.Operateur.ADDITION)
jet16 = c.Jeton(c.Lexeme.VARIABLE)
jet17 = c.Jeton(c.Lexeme.REEL, 3)

arbretest4 = c.ArbreJeton(jet1)
arbretest4.insert_gauche(jet2)
arbretest4.insert_droit(jet3)
arbretest4.fils_gauche.insert_gauche(jet4)
arbretest4.fils_droit.insert_gauche(jet5)
arbretest4.fils_gauche.fils_gauche.insert_gauche(jet6)
arbretest4.fils_droit.fils_gauche.insert_gauche(jet7)
arbretest4.fils_droit.fils_gauche.insert_droit(jet8)
arbretest4.fils_gauche.fils_gauche.fils_gauche.insert_gauche(jet9)
arbretest4.fils_gauche.fils_gauche.fils_gauche.insert_droit(jet10)
arbretest4.fils_droit.fils_gauche.fils_gauche.insert_gauche(jet11)
arbretest4.fils_droit.fils_gauche.fils_gauche.insert_droit(jet12)
arbretest4.fils_droit.fils_gauche.fils_droit.insert_gauche(jet13)
arbretest4.fils_gauche.fils_gauche.fils_gauche.fils_gauche.insert_gauche(jet14)
arbretest4.fils_droit.fils_gauche.fils_droit.fils_gauche.insert_gauche(jet15)
arbretest4.fils_droit.fils_gauche.fils_droit.fils_gauche.fils_gauche.insert_gauche(jet16)
arbretest4.fils_droit.fils_gauche.fils_droit.fils_gauche.fils_gauche.insert_droit(jet17)

#Fin de l'arbre de test 4
# f(x) = sin(cos(sqrt(x)^3)) / exp(2*x-ln(|x+3|))
#Résultat attendu : (<ErreurEval.PAS_D_ERREUR: 400>, [[-5.0, -4.0, -3.0, -2.0, -1.0, 0.0, 1.0, 2.0, 3.0, 4.0], [None, None, None, None, None, 2.5244129544236897, 0.27846331203142055, -0.07456366716803889, 0.006670690059206117, -0.0003404645052498309]])

#Arbre de test 5
jet1 = c.Jeton(c.Lexeme.OPERATEUR, c.Operateur.DIVISION)
jet2 = c.Jeton(c.Lexeme.REEL, 5)
jet3 = c.Jeton(c.Lexeme.REEL, 0)


arbretest5 = c.ArbreJeton(jet1)
arbretest5.insert_gauche(jet2)
arbretest5.insert_droit(jet3)

arbretest5.fils_droit.insert_gauche(jet6)
#Fin de l'arbre de test 5
# f(x) = 5/0 (division par 0)
# Résultat attendu : (<ErreurEval.PAS_D_ERREUR: 400>, [[-5.0, -4.0, -3.0, -2.0, -1.0, 0.0, 1.0, 2.0, 3.0, 4.0], [None, None, None, None, None, None, None, None, None, None]])



#---------------------------------------- Fin des arbres de tests -----------------------------------


def postorderTraversal(root, x):
    if root is None :
        return ''
    else: # On effectue une série de tests if pour trouver le lexème du jeton
        if root.jeton.lexeme == c.Lexeme.REEL:
            return root.jeton.valeur
        elif root.jeton.lexeme == c.Lexeme.OPERATEUR:
            # On sait que le jeton est celui d'un opérateur, on teste alors la valeur de celui-ci
            if root.jeton.valeur == c.Operateur.ADDITION:
              # Si l'opérateur est l'addition, on vérifie qu'il y ait un fils gauche et un fils droit.
              # Pour éviter les erreurs de syntaxe du type : "f(x) = 3*2+" (opérateur isolé) : :
                if root.fils_gauche is None :
                  return 'fonctionvide'
                if root.fils_droit is None :
                  return 'fonctionvide'
                fg = postorderTraversal(root.fils_gauche,x)
                fd = postorderTraversal(root.fils_droit,x)
                # Test qui sert à propager une erreur trouvée dans un des fils :
                # En l'occurence, un problème de domaine de définition (division par 0,
                # racine négative, etc.) :
                if fg == 'erreurdef':
                  return 'erreurdef'
                if fd == 'erreurdef':
                  return 'erreurdef'
                #test d'une erreur de syntaxe (fonction vide, ou opérateur isolé) : :
                if fg == 'fonctionvide':
                  return 'fonctionvide'
                if fd == 'fonctionvide':
                  return 'fonctionvide'
                return fg + fd # On retourne la somme du fils gauche et du fils droit, dans le cas de l'addition
            # Les mêmes tests sont faits pour chaque type d'opération.
            elif root.jeton.valeur == c.Operateur.MULTIPLICATION:
                if root.fils_gauche is None :
                  return 'fonctionvide'
                if root.fils_droit is None :
                  return 'fonctionvide'
                fg = postorderTraversal(root.fils_gauche,x)
                fd = postorderTraversal(root.fils_droit,x)
                # Test qui sert à propager une erreur trouvée dans un des fils :
                if fg == 'erreurdef':
                  return 'erreurdef'
                if fd == 'erreurdef':
                  return 'erreurdef'
                #test d'une erreur de syntaxe (fonction vide, ou opérateur isolé) :
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
                # Test qui sert à propager une erreur trouvée dans un des fils :
                if fg == 'erreurdef':
                  return 'erreurdef'
                if fd == 'erreurdef':
                  return 'erreurdef'
                #test d'une erreur de syntaxe (fonction vide, ou opérateur isolé) :
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
                # Test qui sert à propager une erreur trouvée dans un des fils :
                if fg == 'erreurdef':
                  return 'erreurdef'
                if fd == 'erreurdef':
                  return 'erreurdef'
                #test d'une erreur de syntaxe (fonction vide, ou opérateur isolé) :
                if fg == 'fonctionvide':
                  return 'fonctionvide'
                if fd == 'fonctionvide':
                  return 'fonctionvide'
                if root.fils_droit.jeton.lexeme == c.Lexeme.VARIABLE and x == 0 :
                  return 'erreurdef'
                if root.fils_droit.jeton.valeur == 0:
                  return 'erreurdef'
                return fg/fd
            elif root.jeton.valeur == c.Operateur.PUISSANCE:
                if root.fils_gauche is None :
                  return 'fonctionvide'
                if root.fils_droit is None :
                  return 'fonctionvide'
                fg = postorderTraversal(root.fils_gauche,x)
                fd = postorderTraversal(root.fils_droit,x)
                if isinstance(fg, complex) :
                  return 'erreurdef'
                if isinstance(fd, complex) :
                  return 'erreurdef'
                # Test qui sert à propager une erreur trouvée dans un des fils :
                if fg == 'erreurdef':
                  return 'erreurdef'
                if fd == 'erreurdef':
                  return 'erreurdef'
                #test d'une erreur de syntaxe (fonction vide, ou opérateur isolé) :
                if fg == 'fonctionvide':
                  return 'fonctionvide'
                if fd == 'fonctionvide':
                  return 'fonctionvide'
                return pow(fg, fd)
        elif root.jeton.lexeme == c.Lexeme.FONCTION:
            if root.jeton.valeur == c.Fonction.ABS:
                if root.fils_droit is None :
                  return 'fonctionvide'
                fd = postorderTraversal(root.fils_droit,x)
                # Test qui sert à propager une erreur trouvée dans un des fils :
                if fd == 'erreurdef':
                  return 'erreurdef'
                #test d'une erreur de syntaxe (fonction vide, ou opérateur isolé) :
                if fd == 'fonctionvide':
                  return 'fonctionvide'
                return abs(fd)
            elif root.jeton.valeur == c.Fonction.SIN:
                if root.fils_droit is None :
                  return 'fonctionvide'
                fd = postorderTraversal(root.fils_droit,x)
                # Test qui sert à propager une erreur trouvée dans un des fils :
                if fd == 'erreurdef':
                  return 'erreurdef'
                #test d'une erreur de syntaxe (fonction vide, ou opérateur isolé) :
                if fd == 'fonctionvide':
                  return 'fonctionvide'
                return math.sin(fd)
            elif root.jeton.valeur == c.Fonction.SQRT:
                if root.fils_droit is None :
                  return 'fonctionvide'
                fd = postorderTraversal(root.fils_droit,x)
                # Test qui sert à propager une erreur trouvée dans un des fils :
                if fd < 0:
                  fd = 'erreurdef'
                if fd == 'erreurdef':
                  return 'erreurdef'
                #test d'une erreur de syntaxe (fonction vide, ou opérateur isolé) :
                if fd == 'fonctionvide':
                  return 'fonctionvide'
                return math.sqrt(fd)
            elif root.jeton.valeur == c.Fonction.COS:
                if root.fils_droit is None :
                  return 'fonctionvide'
                fd = postorderTraversal(root.fils_droit,x)
                # Test qui sert à propager une erreur trouvée dans un des fils :
                if fd == 'erreurdef':
                  return 'erreurdef'
                #test d'une erreur de syntaxe (fonction vide, ou opérateur isolé) :
                if fd == 'fonctionvide':
                  return 'fonctionvide'
                return math.cos(fd)
            elif root.jeton.valeur == c.Fonction.EXP:
                if root.fils_droit is None :
                  return 'fonctionvide'
                fd = postorderTraversal(root.fils_droit,x)
                # Test qui sert à propager une erreur trouvée dans un des fils :
                if fd == 'erreurdef':
                  return 'erreurdef'
                #test d'une erreur de syntaxe (fonction vide, ou opérateur isolé) :
                if fd == 'fonctionvide':
                  return 'fonctionvide'
                return math.exp(fd)
            elif root.jeton.valeur == c.Fonction.LOG:
                if root.fils_droit is None :
                  return 'fonctionvide'
                fd = postorderTraversal(root.fils_droit,x)
                if isinstance(fd, complex) :
                  return 'erreurdef'
                if fd <=0 :
                  fd = 'erreurdef'
                # Test qui sert à propager une erreur trouvée dans un des fils :
                if fd == 'erreurdef':
                  return 'erreurdef'
                #test d'une erreur de syntaxe (fonction vide, ou opérateur isolé) :
                if fd == 'fonctionvide':
                  return 'fonctionvide'
                return math.log(fd)
        elif root.jeton.lexeme == c.Lexeme.VARIABLE:
            return x




def evaluateur(arbre,nomb, xmin, xmax):
    if nomb < 2 :
      return er.ErreurEval.ITERATIONS_INSUFFISANTES
    res = [[0] * nomb, [0] * nomb] # Initialisation du tableau de sortie
    if xmin > xmax : # Vérification de l'intervalle 
      return er.ErreurEval.XMIN_SUPERIEUR_A_XMAX, res
    # Les erreurs liées à l'entrée des valeurs sont vérifiées
    for i in range(nomb):
       res[0][i] = xmin + i*(xmax-xmin)/(nomb-1) # On génère la liste des x en fonction des valeurs rentrées (nombre d'itérations, xmin et xmax)
    for i in range(nomb):
        res[1][i] = postorderTraversal(arbre,res[0][i]) # Pour chaque calcul d'image de x dans la première ligne de la liste, on fait appel à la fonction postorderTraversal, et on stocke la valeur dans la dexuième ligne, à la même colonne que l'antécédent.
        if res[1][i] == 'fonctionvide': # Si l'erreur de fonction vide s'est propagée, on retourne le code d'erreur correspondant, ainsi qu'une liste remplie de 0.
          res = [[0] * nomb, [0] * nomb]
          return er.ErreurEval.FONCTION_VIDE, res
        if res[1][i] == 'erreurdef': # Si le x n'a pas d'image par la fonction entrée, alors son image est un None.
            res[1][i] = None
        if isinstance(res[1][i], complex): # S'il a une image mais qu'elle est complexe, alors son image est un None.
            res[1][i] = None
    return er.ErreurEval.PAS_D_ERREUR, res # On retourne le code qui dit qu'il n'y a pas d'erreur et on retourne la liste contenant en première ligne les antécédants, et en seconde les images