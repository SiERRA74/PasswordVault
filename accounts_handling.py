from bcrypt import *
import pwd_management as pwd


def checkIFexist(user):
    # Vérifie si l'utilisateur existe déjà
    all_users = pwd.get_json_files()
    existing_users = [file.split(".")[0] for file in all_users]
    if user in existing_users:
        return True
    else: 
        return False


def handle_sign_in(login_entry, password_entry, result_label):
    """Gère la connexion de l'utilisateur."""
    username_ui = login_entry.get().strip()
    password_ui = password_entry.get().strip()

    if not username_ui or not password_ui:
        result_label.config(text="Nom d'utilisateur ou mot de passe vide.", fg="red")
        return

    if not checkIFexist(username_ui):
        result_label.config(text="Identifiant innéxistant", fg="red")
    else:
        data = pwd.file_read(username_ui)
        hashed_password = data["pwd"]
        is_same_password = checkpw(password_ui.encode(), hashed_password.encode())
        if not is_same_password:
            result_label.config(text="Mot de passe incorrect", fg="red")
        else:
            result_label.config(text=f"Bienvenue, {username_ui} !", fg="green")


def handle_sign_up(login_entry, password_entry, confirm_password, result_label):
    """Gère l'inscription d'un utilisateur."""
    username_ui = login_entry.get().strip()
    password_ui = password_entry.get().strip()
    confirm_ui = confirm_password.get().strip()

    # Vérification des champs vides
    if not username_ui or not password_ui or not confirm_ui:
        result_label.config(text="Veuillez remplir tous les champs.", fg="red")
        return


    if checkIFexist(username_ui):
        result_label.config(text="Un compte avec ce nom existe déjà.", fg="red")
        return

    # Vérification de la correspondance des mots de passe
    if password_ui != confirm_ui:
        result_label.config(text="Les mots de passe ne correspondent pas.", fg="red")
        return

    # Hashage du mot de passe
    hashed_password = hashpw(password_ui.encode(), gensalt()).decode()
    # Création des données de l'utilisateur
    user_file_data = {
        "user": username_ui,
        "pwd": hashed_password,
        "PWD": {}
    }

    # Sauvegarde des données utilisateur
    try:
        pwd.file_write(user_file_data, username_ui)
        result_label.config(text=f"Compte créé avec succès ! Bienvenue, {username_ui} !", fg="green")
        
    except Exception as e:
        result_label.config(text=f"Erreur lors de la création du compte : {str(e)}", fg="red")


