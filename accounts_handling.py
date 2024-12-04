import json, bcrypt, os
from colors import Colors as cl

def clean_console():
    os.system('cls')


# Fonction pour lire les données d'un fichier JSON
def file_read(filename):
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

# Fonction pour récupérer les fichiers JSON dans le dossier courant
def get_json_files():
    files = os.listdir(".")
    json_files = [file for file in files if file.endswith(".json")]
    return json_files

# Fonction pour écrire dans un fichier JSON
def file_write(data, filename):
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)

# Fonction pour créer un nouvel utilisateur
def user_creation():
    print("Création de compte pour PassWordManager")
    username = input("Veuillez entrer votre nom d'utilisateur : ").strip().lower
    existing_users = [file.split(".")[0] for file in get_json_files()]  # Liste des noms d'utilisateur existants (sans l'extension .json)

    # Vérifie si l'utilisateur existe déjà
    if username in existing_users:
        print("Ce nom d'utilisateur existe déjà. Veuillez en choisir un autre.")
        return

    main_password = input(
        "Veuillez entrer le mot de passe principal de votre PWM\n"
        "(ce dernier doit être sécurisé car il donne accès à tous les autres mots de passe) : "
    ).strip()

    if username and main_password:
        # Hashage du mot de passe
        hashed_password = bcrypt.hashpw(main_password.encode(), bcrypt.gensalt()).decode()

        # Création des données de l'utilisateur
        user_file_data = {
            "user": username,
            "pwd": hashed_password,
            "PWD": {}
        }

        # Sauvegarde dans un fichier spécifique
        file_write(user_file_data, f"{username}.json")
        print(f"Utilisateur '{username}' créé avec succès !")
        
    else:
        print("Le nom d'utilisateur et le mot de passe ne doivent pas être vides.")


# Fonction de connexion
def connection(main_password,username, msg=""):
    clean_console()
    print(cl.RED+msg+cl.END)
    print("Connexion en cours...")

    # Vérifie si le fichier de l'utilisateur existe
    user_file = f"{username}.json"
    if user_file not in get_json_files():
        return("Utilisateur introuvable.")

    # Charge les données de l'utilisateur
    user_data = file_read(user_file)
    if not user_data:
        return("Fichier vide...")

    # Vérifie le mot de passe
    stored_hash = user_data["pwd"]
    if bcrypt.checkpw(main_password.encode(), stored_hash.encode()):
        clean_console()
        print(f"Bienvenue, {username} !")
        render_creds(username)
    else:
        return("Mot de passe incorrect.")

# Fonction pour afficher les choix principaux
def user_choice():

    print("1. Connexion \n2. Création de compte")
    while True:
        user_choice = input("1? 2?").strip()
        if user_choice == "1":
            connection()
            break
        elif user_choice == "2":
            user_creation()
            break
        else:
            clean_console()
            print("Veuillez choisir 1 ou 2.")

# Fonction principale
def launch():
    users = get_json_files()
    if not users:
        print(cl.ITALIC + "Aucun compte n'existe. Créons un compte !" + cl.END)
        user_creation()
    else:
        user_choice()

def render_creds(login):
    user_data = file_read(f"{login}.json")  # Charge le fichier JSON de l'utilisateur actuel
    columns = ["Alias", "Identifiant", "Mot de passe"]  # En-têtes des colonnes

    # Affiche les en-têtes
    print(f"{columns[0]:<20}{columns[1]:<20}{columns[2]:<20}")
    print("-" * 60)

    # Parcourt et affiche les entrées de "PWD"
    for alias, creds in user_data["PWD"].items():
        identifiant = creds.get("identifiant", "N/A")
        mot_de_passe = creds.get("password", "N/A")
        print(f"{alias:<20}{identifiant:<20}{mot_de_passe:<20}")

    # Si aucune donnée n'existe
    if not user_data["PWD"]:
        print("Aucune donnée enregistrée.")


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

