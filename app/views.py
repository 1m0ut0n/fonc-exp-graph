from app import app, main

#on importe l'application qui est définie dans le fichier "__init__.py" et le fichier python qui va gérer toutes les fonctions de calcul

from flask import request, render_template, jsonify

#on importe des modules qui vont permettre de gérer les requêtes, afficher la page web ou encore convertir des données au format JSON

import json

#on importe la bibliothèque json qui permet d'utiliser des données structurées de façon semblable aux objets Javascript 


#---------------------------------------------------------------------------------------------------------------------
#
#                  Ci-dessous, nous allons assigner une fonction précise à chaque url que l'on va créer
#
#---------------------------------------------------------------------------------------------------------------------


@app.route('/') #'/' correspond à l'url de la page d'accueil
def index():
    return render_template('public/accueil.html') #on exécute alors une fonction qui permet d'afficher la page

@app.route('/mainpage') #'/mainpage' correspond à l'url par défaut de la page de calcul
def mainpage():
    return render_template('public/mainpage.html') #on exécute alors une fonction qui permet d'afficher la page
    
@app.route('/mainpage/calculate', methods=['POST']) # lorsque l'url est '/mainpage/calculate', on veut poster des données sur le serveur, on exécute la fonction suivante
def calculate():
    output = request.get_json() #on récupère la requête au format JSON
    result = json.loads(output) #on convertit la donnée JSON en un dictionnaire Python
    return main.analyse_complete(result) #on renvoie les données calculées
