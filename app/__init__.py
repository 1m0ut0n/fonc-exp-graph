from flask import Flask

#on importe le framework flask qui va permettre d'utiliser un serveur python sur un site web

app = Flask(__name__) #on définit la localisation des ressources de l'application

from app import views

#on importe le fichier python qui va définir les fonctions exécutées lors d'interactions avec le serveur
