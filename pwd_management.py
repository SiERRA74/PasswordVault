
import json,os

def add_password(login):
    user_data = file_read(f"{login}.json")  # Charge les données du fichier JSON de l'utilisateur

    # Demande des informations à l'utilisateur
    alias = input("Entrez un alias pour ce mot de passe (ex. 'email_gmail') : ").strip()
    if alias in user_data["PWD"]:
        print("Cet alias existe déjà. Choisissez un alias unique.")
        return

    identifiant = input("Entrez l'identifiant ou le login associé : ").strip()
    password = input("Entrez le mot de passe : ").strip()

    if alias and identifiant and password:
        # Ajoute les informations au JSON
        user_data["PWD"][alias] = {
            "identifiant": identifiant,
            "password": password
        }
        file_write(user_data, user_data["user"])  # Sauvegarde dans le fichier JSON
        print(f"Mot de passe ajouté sous l'alias '{alias}' avec succès !")
    else:
        print("Tous les champs (alias, identifiant, mot de passe) doivent être remplis.")



def render_creds(login):
    user_data = file_read(f"{login}.json")  # Charge le fichier JSON de l'utilisateur actuel
    columns = ["Alias", "Identifiant", "Mot de passe"]  # En-têtes des colonnes


    # Parcourt et affiche les entrées de "PWD"
    for alias, creds in user_data["PWD"].items():
        identifiant = creds.get("identifiant", "N/A")
        mot_de_passe = creds.get("password", "N/A")
        print(f"{alias:<20}{identifiant:<20}{mot_de_passe:<20}")

    # Si aucune donnée n'existe
    if not user_data["PWD"]:
        print("Aucune donnée enregistrée.")

def clean_console():
    os.system('cls')


# Fonction pour lire les données d'un fichier JSON
def file_read(name):
    filename = "users/"+name+".json"
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
def file_write(data, filename):
    filename = "users/"+filename+".json"
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)

# Fonction pour récupérer les fichiers JSON dans le dossier courant
def get_json_files():
    files = os.listdir("users/")
    json_files = [file for file in files if file.endswith(".json")]
    return json_files


