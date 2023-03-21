from erreurs import ErreurLex
from common import *


      
# Debut de la fonction lex_analyser 
# Entrées : chaine de caractère avec espace, la liste de sortie vide 
# Sorties : nom de l'erreur, la liste de sortie sous forme de lexème
def lex_analyser(chaine_entree_avec_espace, liste_sortie):
# Suppresion des espaces dans la chaine d'entrées et Création d'une nouvelle chaine d'entree sans l'espace
  chaine_entree = "" #Variable de la nouvelle chaine d'entree sans les espaces 
  i_espace = 0 #Variable d'itération pour la suppression des espaces 
  while i_espace < len(chaine_entree_avec_espace):
    if chaine_entree_avec_espace[i_espace] != ' ':
      chaine_entree = chaine_entree + chaine_entree_avec_espace[i_espace]
    i_espace = i_espace + 1
# Ajout d'un espace à la fin de la chaine
  chaine_entree = chaine_entree + ' '
  i = 0 # Variable d'iteration de la chaine d'entree
# Tant que la chaine d'entrée n'est pas fini lire les caractères 
  while i < len(chaine_entree):  
# Variable pour tester pour savoir si l'utilisateur n'a rien tapé ou a tapé un caractère non reconnu
    test_caractere = 0 
    match chaine_entree[i]:   
# Ajout dans la liste de sortie des opérateurs et des parenthèses
        case '(': 
          liste_sortie.append(Jeton(Lexeme.PARENTHESE_OUV)) 
          test_caractere = 1
        case ')': 
          liste_sortie.append(Jeton(Lexeme.PARENTHESE_FERM))
          test_caractere = 1  
        case '+': 
          liste_sortie.append(Jeton(Lexeme.OPERATEUR, Operateur.ADDITION))
          test_caractere = 1
        case '*':    
          liste_sortie.append(Jeton(Lexeme.OPERATEUR, Operateur.MULTIPLICATION))
          test_caractere = 1
        case '/': 
          liste_sortie.append(Jeton(Lexeme.OPERATEUR, Operateur.DIVISION))
          test_caractere = 1
        case '^': 
          liste_sortie.append(Jeton(Lexeme.OPERATEUR, Operateur.PUISSANCE))
          test_caractere = 1
        case '-':
          liste_sortie.append(Jeton(Lexeme.OPERATEUR, Operateur.SOUSTRACTION))  
          test_caractere = 1             
        case _: 
# Si il y a un caractère entre a et z, ajouter les caractères dans la chaine appelée "chaine intermédiaire pour fonction"
          test_fonction = 0 # Variable de test qui va être utile pour savoir si la fonction est bien écrite ou non 
          chaine_intermediare_pour_fonction = "" # Variable qui va récupérer la fonction caractère par caractère
          i_deb_fonction = -1 # Variable iterative qui recupère la variable itérative "i" du debut de la fonction
          while chaine_entree[i] >= "a" and chaine_entree[i] <= "z":
            test_caractere = 1
            if i_deb_fonction == -1: i_deb_fonction = i
            test_fonction = 1
            chaine_intermediare_pour_fonction = chaine_intermediare_pour_fonction + chaine_entree[i]
            i = i + 1
# Ajout dans la liste de sortie les différentes fonctions         
          match chaine_intermediare_pour_fonction:            
            case 'cos': 
# S'il y a un réel avant la fonction mettre une multiplication entre la fonction et le réel
                if chaine_entree[i_deb_fonction-1] >= '0' and chaine_entree[i_deb_fonction-1] <= '9':
                  liste_sortie.append(Jeton(Lexeme.OPERATEUR, Operateur.MULTIPLICATION))                
                liste_sortie.append(Jeton(Lexeme.FONCTION, Fonction.COS))  
                chaine_intermediare_pour_fonction = ""
                i = i - 1
            case 'sin':
# S'il y a un réel avant la fonction mettre une multiplication entre la fonction et le réel              
                if chaine_entree[i_deb_fonction-1] >= '0' and chaine_entree[i_deb_fonction-1] <= '9':
                  liste_sortie.append(Jeton(Lexeme.OPERATEUR, Operateur.MULTIPLICATION))                     
                liste_sortie.append(Jeton(Lexeme.FONCTION, Fonction.SIN))
                chaine_intermediare_pour_fonction = ""
                i = i - 1
            case 'tan':
# S'il y a un réel avant la fonction mettre une multiplication entre la fonction et le réel   
                if chaine_entree[i_deb_fonction-1] >= '0' and chaine_entree[i_deb_fonction-1] <= '9':
                  liste_sortie.append(Jeton(Lexeme.OPERATEUR, Operateur.MULTIPLICATION))              
                liste_sortie.append(Jeton(Lexeme.FONCTION, Fonction.TAN))
                chaine_intermediare_pour_fonction = ""
                i = i - 1
            case 'log':
# S'il y a un réel avant la fonction mettre une multiplication entre la fonction et le réel   
                if chaine_entree[i_deb_fonction-1] >= '0' and chaine_entree[i_deb_fonction-1] <= '9':
                  liste_sortie.append(Jeton(Lexeme.OPERATEUR, Operateur.MULTIPLICATION))
                liste_sortie.append(Jeton(Lexeme.FONCTION, Fonction.LOG))
                chaine_intermediare_pour_fonction = ""      
                i = i - 1
            case 'exp':
# S'il y a un réel avant la fonction mettre une multiplication entre la fonction et le réel   
                if chaine_entree[i_deb_fonction-1] >= '0' and chaine_entree[i_deb_fonction-1] <= '9':
                  liste_sortie.append(Jeton(Lexeme.OPERATEUR, Operateur.MULTIPLICATION))           
                liste_sortie.append(Jeton(Lexeme.FONCTION, Fonction.EXP))
                chaine_intermediare_pour_fonction = "" 
                i = i - 1
            case 'sqrt':
# S'il y a un réel avant la fonction mettre une multiplication entre la fonction et le réel   
                if chaine_entree[i_deb_fonction-1] >= '0' and chaine_entree[i_deb_fonction-1] <= '9':
                  liste_sortie.append(Jeton(Lexeme.OPERATEUR, Operateur.MULTIPLICATION))            
                liste_sortie.append(Jeton(Lexeme.FONCTION, Fonction.SQRT))
                chaine_intermediare_pour_fonction = ""   
                i = i - 1
            case 'abs':
# S'il y a un réel avant la fonction mettre une multiplication entre la fonction et le réel                 
                if chaine_entree[i_deb_fonction-1] >= '0' and chaine_entree[i_deb_fonction-1] <= '9':
                  liste_sortie.append(Jeton(Lexeme.OPERATEUR, Operateur.MULTIPLICATION))
                liste_sortie.append(Jeton(Lexeme.FONCTION, Fonction.ABS))
                chaine_intermediare_pour_fonction = ""
                i = i - 1
            case 'x' : 
# S'il y a un réel avant la fonction mettre une multiplication entre la fonction et le réel   
                if chaine_entree[i_deb_fonction-1] >= '0' and chaine_entree[i_deb_fonction-1] <= '9':
                  liste_sortie.append(Jeton(Lexeme.OPERATEUR, Operateur.MULTIPLICATION))    
                liste_sortie.append(Jeton(Lexeme.VARIABLE, None)) 
# S'il y a un réel après la fonction mettre une multiplication entre la fonction et le réel   
                if chaine_entree[i] >= '0' and chaine_entree[i] <= '9':
                  liste_sortie.append(Jeton(Lexeme.OPERATEUR, Operateur.MULTIPLICATION))
                i = i - 1
                chaine_intermediare_pour_fonction = ""
# Erreur si la fonction est mal écrite, c'est à dire qu'il a réconnu aucune fonction 
            case _: 
                if test_fonction == 1 : 
                  return ErreurLex.FONCTION_MAL_ECRITE, liste_sortie                 
# Ajout dans la liste de sortie le réel à la suite
          i_reel = 0 # Variable d'itération du réels
          reel_test = 0 # Variable de test 
          chaine_intermediare_pour_reel_sep = "" # Chaine qui va récupérer le réel, élement par élement
          chaine_intermediare_pour_reel = "" # Chaine qui va récuperer tout les élements de val dans une seule variable
          valeur_string = 0 # Variable qui va récuperer le réel en string
          valeur_float = 0 # Variable qui va récuperer le réel en float
# S'il y a entier ou un "." , ajouter les caractères dans la chaine appelée "chaine intermédiaire pour reel sep"
          while chaine_entree[i] >= '0' and chaine_entree[i] <= '9' or chaine_entree[i] == '.':
            test_caractere = 1
            chaine_intermediare_pour_reel_sep = chaine_intermediare_pour_reel_sep + chaine_entree[i]
            i = i + 1
            i_reel = i_reel + 1
            reel_test = 1          
          if reel_test == 1:
# S'il y a une parenthèse après le réel mettre une multiplication *
            if chaine_entree[i] == '(':
              valeur_string = chaine_intermediare_pour_reel.join(chaine_intermediare_pour_reel_sep) 
              valeur_float = float(valeur_string)
              liste_sortie.append(Jeton(Lexeme.REEL, valeur_float))
              liste_sortie.append(Jeton(Lexeme.OPERATEUR, Operateur.MULTIPLICATION))
              i = i - 1
            else : 
              valeur_string = chaine_intermediare_pour_reel.join(chaine_intermediare_pour_reel_sep) 
              valeur_float = float(valeur_string)
              liste_sortie.append(Jeton(Lexeme.REEL, valeur_float))
              i = i - 1
# Erreur si le caractère est inconnu             
    if test_caractere == 0: 
     if chaine_entree[i] != ' ':
      return ErreurLex.CARACTERE_NON_RECONNU, liste_sortie
# Erreur si l'utilisateur ne tape rien 
     if chaine_entree[0] == ' ':
      return ErreurLex.RIEN_EST_TAPE_PAR_UTILISATEUR, liste_sortie    
# Incrémentation "générale"           
    i = i + 1     
# Fin de l fonction s'il n'y a pas d'erreur 
  return ErreurLex.PAS_D_ERREUR, liste_sortie