import tkinter as tk
from accounts_handling import connection, get_json_files

# Création de la fenêtre principale
wndw = tk.Tk()
wndw_width = 450
wndw_lenght = 800
wndw.geometry(f"{wndw_lenght}x{wndw_width}")
wndw.title("Password Vault")

# Chargement de l'image de fond
wallpaper = tk.PhotoImage(file="assets/blackwhite.png")

# Création d'un Canvas pour afficher l'image de fond
canvas1 = tk.Canvas(wndw, width=wndw_lenght, height=wndw_width)
canvas1.pack(fill="both", expand=True)
canvas1.create_image(0, 0, image=wallpaper, anchor="nw")


#####################################################################
def handle_sign_in():
    username_ui = login.get().strip()
    password_ui = password.get().strip()

    if not username_ui or not password_ui:
        result_label.config(text="Nom d'utilisateur ou mot de passe vide.", fg="red")
        return

    # Appel à la fonction de connexion
    error_message = connection(password_ui, username_ui)

    if error_message:
        result_label.config(text=error_message, fg="red")
    else:
        result_label.config(text=f"Bienvenue, {username_ui} !", fg="green")
#####################################################################


# Création des widgets
title = tk.Label(wndw, text="Password Vault", font=('Arial', 18), bg="#000000", fg="#FFFFFF")
author = tk.Label(wndw, text="by Sierra74", font=('Arial', 10), bg="#000000", fg="#FFFFFF")
login = tk.Entry(wndw)
password = tk.Entry(wndw, show="*")
result_label = tk.Label(wndw, text="", font=('Arial', 10), bg="#000000", fg="#FFFFFF")  # Affiche les messages d'erreur ou de succès
login_btn = tk.Button(wndw, text="Sign in", font=('Arial', 10), bg="#000000", fg="#FFFFFF", command=handle_sign_in)
sign_up = tk.Button(wndw, text="Sign up", font=('Arial', 10), fg="#000000", bg="#FFFFFF")  # À compléter pour l'inscription

# Placement des widgets dans le Canvas
canvas1.create_window(wndw_lenght / 2, 50, window=title)  # Centré en haut
canvas1.create_window(wndw_lenght / 2, 80, window=author)
canvas1.create_window(wndw_lenght / 2, 150, window=login)  # Champ login
canvas1.create_window(wndw_lenght / 2, 200, window=password)  # Champ mot de passe
canvas1.create_window(wndw_lenght / 2, 250, window=login_btn)  # Bouton de connexion
canvas1.create_window(wndw_lenght / 2, 280, window=sign_up)  # Bouton d'inscription
canvas1.create_window(wndw_lenght / 2, 320, window=result_label)  # Message d'erreur ou succès

# Lancement de la boucle principale
wndw.mainloop()
