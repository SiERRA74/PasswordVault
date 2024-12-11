import tkinter as tk
from accounts_handling import connection


def handle_sign_in(login_entry, password_entry, result_label):
    """Gère la connexion de l'utilisateur."""
    username_ui = login_entry.get().strip()
    password_ui = password_entry.get().strip()

    if not username_ui or not password_ui:
        result_label.config(text="Nom d'utilisateur ou mot de passe vide.", fg="red")
        return

    # Appel à la fonction de connexion
    error_message = connection(password_ui, username_ui)

    if error_message:
        result_label.config(text=error_message, fg="red")
    else:
        result_label.config(text=f"Bienvenue, {username_ui} !", fg="green")


def handle_sign_up(login_entry, password_entry, confirm_password, result_label):
    """Gère la connexion de l'utilisateur."""
    username_ui = login_entry.get().strip()
    password_ui = password_entry.get().strip()
    confirm_ui = confirm_password.get().strip()


    if not username_ui or not password_ui:
        result_label.config(text="Nom d'utilisateur ou mot de passe vide.", fg="red")
        return
    if not confirm_ui == password_ui:
        result_label.config(text="Les mots de passes ne conresspondent pas", fg="red")

    # Appel à la fonction de connexion
    error_message = connection(password_ui, username_ui)

    if error_message:
        result_label.config(text=error_message, fg="red")
    else:
        result_label.config(text=f"Bienvenue, {username_ui} !", fg="green")


def clear_canvas(canvas):
    """Efface tous les widgets du canvas."""
    canvas.delete("all")


def display_main_menu(canvas, length, width, wallpaper):
    """Affiche le menu principal."""
    clear_canvas(canvas)

    # Réafficher le wallpaper
    canvas.create_image(0, 0, image=wallpaper, anchor="nw")

    # Widgets du menu principal
    title = tk.Label(canvas, text="Password Vault", font=('Arial', 18), bg="#000000", fg="#FFFFFF")
    connection_btn = tk.Button(canvas, text="Connexion", font=('Arial', 10), command=lambda: display_connection_menu(canvas, length, width, wallpaper))
    sign_up_btn = tk.Button(canvas, text="Inscription", font=('Arial', 10), command=lambda: display_inscritpion_menu(canvas, length, width, wallpaper))

    # Placement des widgets
    canvas.create_window(length / 2, 50, window=title)
    canvas.create_window(length / 2, 150, window=connection_btn)
    canvas.create_window(length / 2, 200, window=sign_up_btn)


def display_inscritpion_menu(canvas, length, width, wallpaper):
    """Affiche le menu de connexion."""
    clear_canvas(canvas)

    # Réafficher le wallpaper
    canvas.create_image(0, 0, image=wallpaper, anchor="nw")

    # Widgets pour la connexion
    title = tk.Label(canvas, text="Inscription", font=('Arial', 18), bg="#000000", fg="#FFFFFF")
    login_entry = tk.Entry(canvas)
    password_entry = tk.Entry(canvas, show="*")
    confirm_password = tk.Entry(canvas, show="*")
    result_label = tk.Label(canvas, text="", font=('Arial', 10), bg="#000000", fg="#FFFFFF")

    login_btn = tk.Button(canvas, text="Créer un compte", font=('Arial', 10),
                          command=lambda: handle_sign_up(login_entry, password_entry, result_label))
    back_btn = tk.Button(canvas, text="Retour", font=('Arial', 10),
                         command=lambda: display_main_menu(canvas, length, width, wallpaper))

    # Placement des widgets
    canvas.create_window(length / 2, 50, window=title)
    canvas.create_window(length / 2, 150, window=login_entry)
    canvas.create_window(length / 2, 200, window=password_entry)
    canvas.create_window(length / 2, 200, window=confirm_password)
    canvas.create_window(length / 2, 250, window=login_btn)
    canvas.create_window(length / 2, 300, window=back_btn)
    canvas.create_window(length / 2, 350, window=result_label)

def display_connection_menu(canvas, length, width, wallpaper):
    """Affiche le menu de connexion."""
    clear_canvas(canvas)

    # Réafficher le wallpaper
    canvas.create_image(0, 0, image=wallpaper, anchor="nw")

    # Widgets pour la connexion
    title = tk.Label(canvas, text="Connexion", font=('Arial', 18), bg="#000000", fg="#FFFFFF")
    login_entry = tk.Entry(canvas)
    password_entry = tk.Entry(canvas, show="*")
    result_label = tk.Label(canvas, text="", font=('Arial', 10), bg="#000000", fg="#FFFFFF")

    login_btn = tk.Button(canvas, text="Se connecter", font=('Arial', 10),
                          command=lambda: handle_sign_in(login_entry, password_entry, result_label))
    back_btn = tk.Button(canvas, text="Retour", font=('Arial', 10),
                         command=lambda: display_main_menu(canvas, length, width, wallpaper))

    # Placement des widgets
    canvas.create_window(length / 2, 50, window=title)
    canvas.create_window(length / 2, 150, window=login_entry)
    canvas.create_window(length / 2, 200, window=password_entry)
    canvas.create_window(length / 2, 250, window=login_btn)
    canvas.create_window(length / 2, 300, window=back_btn)
    canvas.create_window(length / 2, 350, window=result_label)


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
