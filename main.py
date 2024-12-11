import tkinter as tk
from os import listdir
import json,bcrypt
import accounts_handling as acc



def clear_canvas(canvas):
    """Efface tous les widgets du canvas."""
    canvas.delete("all")


def display_main_menu(canvas, length, width, wallpaper):
    """Affiche le menu principal."""
    clear_canvas(canvas)

    # Réafficher le wallpaper
    canvas.create_image(0, 0, image=wallpaper, anchor="nw")

    # Widgets du menu principal
    title = tk.Label(canvas, text="Password Vault", font=('Arial', 28), bg="#000000", fg="#FFFFFF")
    connection_btn = tk.Button(canvas, text="Connexion", font=('Arial', 15), command=lambda: display_connection_menu(canvas, length, width, wallpaper))
    sign_up_btn = tk.Button(canvas, text="Inscription", font=('Arial', 15), command=lambda: display_inscritpion_menu(canvas, length, width, wallpaper))

    # Placement des widgets
    canvas.create_window(length / 2, 100, window=title)
    canvas.create_window(length / 2, 250, window=connection_btn)
    canvas.create_window(length / 2, 300, window=sign_up_btn)


def display_inscritpion_menu(canvas, length, width, wallpaper):
    """Affiche le menu de connexion."""
    clear_canvas(canvas)

    # Réafficher le wallpaper
    canvas.create_image(0, 0, image=wallpaper, anchor="nw")

    # Widgets pour la connexion
    title = tk.Label(canvas, text="Inscription", font=('Arial', 22), bg="#000000", fg="#FFFFFF")
    login_entry = tk.Entry(canvas)
    password_entry = tk.Entry(canvas, show="*") 
    confirm_password = tk.Entry(canvas, show="*")
    result_label = tk.Label(canvas, text="", font=('Arial', 12), bg="#000000", fg="#FFFFFF")

    create_btn = tk.Button(canvas, text="Créer un compte", font=('Arial', 12),
                          command=lambda: acc.handle_sign_up(login_entry, password_entry, confirm_password, result_label))
    back_btn = tk.Button(canvas, text="Retour", font=('Arial', 12),
                         command=lambda: display_main_menu(canvas, length, width, wallpaper))

    # Placement des widgets
    canvas.create_window(length / 2, 50, window=title)
    canvas.create_window(length / 2, 150, window=login_entry)
    canvas.create_window(length / 2, 200, window=password_entry)
    canvas.create_window(length / 2, 250, window=confirm_password)
    canvas.create_window(length / 2, 300, window=create_btn)
    canvas.create_window(length / 2, 350, window=back_btn)
    canvas.create_window(length / 2, 400, window=result_label)

def display_connection_menu(canvas, length, width, wallpaper):
    """Affiche le menu de connexion."""
    clear_canvas(canvas)

    # Réafficher le wallpaper
    canvas.create_image(0, 0, image=wallpaper, anchor="nw")

    # Widgets pour la connexion
    title = tk.Label(canvas, text="Connexion", font=('Arial', 22), bg="#000000", fg="#FFFFFF")
    login_entry = tk.Entry(canvas)
    password_entry = tk.Entry(canvas, show="*")
    result_label = tk.Label(canvas, text="", font=('Arial', 12), bg="#000000", fg="#FFFFFF")

    login_btn = tk.Button(canvas, text="Se connecter", font=('Arial', 12),
                        command=lambda: acc.handle_sign_in(login_entry, password_entry, result_label))
    back_btn = tk.Button(canvas, text="Retour", font=('Arial', 12),
                        command=lambda: display_main_menu(canvas, length, width, wallpaper))

    # Placement des widgets
    canvas.create_window(length / 2, 50, window=title)
    canvas.create_window(length / 2, 200, window=login_entry)
    canvas.create_window(length / 2, 250, window=password_entry)
    canvas.create_window(length / 2, 300, window=login_btn)
    canvas.create_window(length / 2, 350, window=back_btn)
    canvas.create_window(length / 2, 380, window=result_label)


def main_window(width=450, length=800):
    """Crée la fenêtre principale."""
    root = tk.Tk()
    width = width
    length = length
    root.geometry(f"{length}x{width}")
    root.title("Password Vault")

    # Chargement du wallpaper
    wallpaper = tk.PhotoImage(file="assets/blackwhite.png")

    # Création du canvas
    canvas = tk.Canvas(root, width=length, height=width)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=wallpaper, anchor="nw")

    # Afficher le menu principal
    display_main_menu(canvas, length, width, wallpaper)

    # Lancement de la boucle principale
    root.mainloop()


# Exécuter l'application
main_window()



