from app import app

# On importe l'application qui est définie dans le fichier "__init__.py"

if __name__ == "__main__":
    app.run(host='0.0.0.0') # Quand le programme est lancé, on lance le serveur sur l'adresse IP locale

# http://127.0.0.1/
