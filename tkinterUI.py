import tkinter as tk
from accounts_handling import *




# Création de la fenêtre principale
wndw = tk.Tk()
wndw_width = 450
wndw_lenght = 800
wndw.geometry(str(wndw_lenght)+"x"+str(wndw_width))
wndw.title("Password Vault")

# Chargement de l'image de fond
wallpaper = tk.PhotoImage(file="assets/blackwhite.png")


# Création d'un Canvas pour afficher l'image de fond
canvas1 = tk.Canvas(wndw, width=800, height=400)
canvas1.pack(fill="both", expand=True)
canvas1.create_image(0, 0, image=wallpaper, anchor="nw")


##########################################################
def handle_sign_in():
    username_ui = login.get()
    password_ui = password.get()
    connection(username_ui,password_ui)

##########################################################


# Création des widgets
title = tk.Label(wndw, text="Password Vault", font=('Arial', 18), bg="#000000", fg="#FFFFFF")
author = tk.Label(wndw, text="by Sierra74", font=('Arial', 10), bg="#000000", fg="#FFFFFF")
login = tk.Entry(wndw)
password = tk.Entry(wndw, show="*")
login_btn = tk.Button(wndw, text="Sign in", font=('Arial', 10),bg="#000000", fg="#FFFFFF", command="handle_sign_in")
sign_up = tk.Button(wndw, text="Sign up", font=('Arial', 10),fg="#000000", bg="#FFFFFF", command="handle_sign_up")


# Placement des widgets dans le Canvas
canvas1.create_window(wndw_lenght/2, 50, window=label)  # Centré en haut
canvas1.create_window(wndw_lenght/2, 80, window=author)
canvas1.create_window(wndw_lenght/2, 150, window=login)  # Champ login
canvas1.create_window(wndw_lenght/2, 200, window=password)  # Champ mot de passe
canvas1.create_window(wndw_lenght/2, 250, window=login_btn)  # Bouton de connexion
canvas1.create_window(wndw_lenght/2, 280, window=sign_up)  # Bouton de connexion


# Lancement de la boucle principale
wndw.mainloop()
