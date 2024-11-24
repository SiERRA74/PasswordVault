import json
import bcrypt
import os

# État initial du fichier
empty_data = {
    "user": {},
    "PWD": {}
}

# Fonction pour initialiser et/ou créer le fichier JSON
def file_init(data):
    with open("user_data.json", "w+") as file: 
        json.dump(data, file, indent=4)


# Fonction pour lire les données du fichier JSON
def file_read():
    # Si le fichier n'existe pas, initialise-le
    if not os.path.exists("user_data.json"):
        file_init(empty_data)

    # Ouvre le fichier pour lecture
    with open("user_data.json", "r") as file:
        try:
            data = json.load(file)  
            return data
        except json.JSONDecodeError:  # Si le fichier est vide ou corrompu
            print("Fichier JSON vide ou corrompu. Réinitialisation...")
            file_init(empty_data) 
            return data


# Fonction pour écrire dans le fichier JSON
def file_write(data):
    with open("user_data.json", "w") as file:
        json.dump(data, file, indent=4)


# Fonction pour créer un nouvel utilisateur
def user_creation():
    print("Création de compte pour PassWordManager")
    username = input("Veuillez entrer votre nom d'utilisateur : ").strip()
    main_password = str(input(
        "Veuillez entrer le mot de passe principal de votre PWM\n"
        "(ce dernier doit être sécurisé car il donne accès à tous les autres mots de passe) : "
    ).strip())

    if username and main_password: 
        user_data = file_read()

        # Vérifie si l'utilisateur existe déjà
        for user in user_data["user"]:
            if user["username"] == username:
                print("Cet utilisateur existe déjà. Veuillez choisir un autre nom.")
                return

        # Hashage
        hashed_password = bcrypt.hashpw(main_password.encode(), bcrypt.gensalt()).decode()

        # Ajoute l'utilisateur au .json
        user_data["user"][username] = hashed_password
        file_write(user_data)
        print("Utilisateur créé avec succès !")

        # Lancement de la connexion après création
        connection()

    else:
        print("Le nom d'utilisateur et le mot de passe ne doivent pas être vides.")

# Fonction de connexion
def connection():
    user_data = file_read()

    if not user_data["user"]:  # Si aucun utilisateur n'est enregistré
        print("Aucun utilisateur trouvé. Créons un compte !")
        user_creation()
    else:
        print("Connexion au PassWordManager")
        username = str(input("Nom d'utilisateur : ").strip())
        main_password = str(input("Mot de passe principal : ").strip())

        for user in user_data["user"]:
            if username in user_data["user"]:
            # Récupère le hash du mot de passe associé
                stored_hash = user_data["user"][username]


                # Vérifie si le mot de passe fourni correspond au hash stocké
                if bcrypt.checkpw(main_password.encode(), stored_hash.encode()):
                    print(f"Bienvenue, {username} !")
                    return  # Connexion réussie
                else:
                    print("Mot de passe incorrect.")
        else:
            print("Utilisateur introuvable.")

# Fonction principale
def main():
    connection()

# Lancement du programme
main()
