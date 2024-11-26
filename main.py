import json, bcrypt, os


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
    username = input("Veuillez entrer votre nom d'utilisateur : ").strip()
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
        connection()
    else:
        print("Le nom d'utilisateur et le mot de passe ne doivent pas être vides.")


# Fonction de connexion
def connection():
    print("Connexion au PassWordManager")
    username = input("Nom d'utilisateur : ").strip()
    main_password = input("Mot de passe principal : ").strip()

    # Vérifie si le fichier de l'utilisateur existe
    user_file = f"{username}.json"
    if user_file not in get_json_files():
        print("Utilisateur introuvable.")
        return

    # Charge les données de l'utilisateur
    user_data = file_read(user_file)
    if not user_data:
        print("Impossible de lire les données de l'utilisateur.")
        return

    # Vérifie le mot de passe
    stored_hash = user_data["pwd"]
    if bcrypt.checkpw(main_password.encode(), stored_hash.encode()):
        print(f"Bienvenue, {username} !")
    else:
        print("Mot de passe incorrect.")

# Fonction pour afficher les choix principaux
def choice():
    print("1. Connexion \n2. Création de compte")
    while True:
        user_choice = input("1? 2? ").strip()
        if user_choice == "1":
            connection()
            break
        elif user_choice == "2":
            user_creation()
            break
        else:
            print("Veuillez choisir 1 ou 2.")

# Fonction principale
def main():
    users = get_json_files()
    if not users:
        print("Aucun compte n'existe. Créons un compte !")
        user_creation()
    else:
        choice()

# Lancement du programme
if __name__ == "__main__":
    main()
