
import json,os
from vignere import *

def add_password(username, alias, login, password,link):
    user_data = file_read(f"{username}")  # Charge les données du fichier JSON de l'utilisateur

    if alias in user_data["PWD"]:
        print("Cet alias existe déjà. Choisissez un alias unique.")
        return

    login = login.strip()

    if alias and login and password and link:
        # Ajoute les informations au JSON
        user_data["PWD"][alias] = {
            "login": login,
            "password": password,
            "link": link
        }
        file_write(user_data, user_data["user"])  # Sauvegarde dans le fichier JSON
        print(f"Mot de passe ajouté sous l'alias '{alias}' avec succès !")

    elif alias and login and password:
        # Ajoute les informations au JSON (sans le lien)
        user_data["PWD"][alias] = {
            "login": login,
            "password": password,
        }
        file_write(user_data, user_data["user"])  # Sauvegarde dans le fichier JSON
        print(f"Mot de passe ajouté sous l'alias '{alias}' avec succès !")

    else:
        print("Tous les champs (alias, identifiant, mot de passe) doivent être remplis.")




def clean_console():
    os.system('cls')


# Fonction pour lire les données d'un fichier JSON
def file_read(username):
    filename = "users/"+username+".json"
    if not os.path.exists(filename):
        print(f"Le fichier {filename} n'existe pas.")
        return None

    with open(filename, "r") as file:
        try:
            data = json.load(file)
            return data
        except json.JSONDecodeError:
            print(f"Le fichier {filename} est vide ou corrompu.")
            return None

# Fonction pour écrire dans un fichier JSON
def file_write(data, username):
    filename = "users/"+username+".json"
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)

# Fonction pour récupérer les fichiers JSON dans le dossier courant
def get_json_files():
    files = os.listdir("users/")
    json_files = [file for file in files if file.endswith(".json")]
    return json_files


