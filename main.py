import tkinter as tk
import accounts_handling as acc


""" PARTIE 1 : CHOIX INSCRIPTION / CONNEXION """
###############################################################################################################################
###############################################################################################################################

def clear_canvas(canvas):
    """Efface tous les widgets du canvas."""
    canvas.delete("all")

def wallpaper(root, width, height, mod="assets/whiteblack.png"):
    """Crée un canvas avec un wallpaper."""
    
    wallpaper = tk.PhotoImage(file=mod)

    # Création du canvas
    canvas = tk.Canvas(root, width=width, height=height)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=wallpaper, anchor="nw")

    # Retourne le canvas et l'image pour éviter le garbage collector
    return canvas, wallpaper

"""
def change_theme(DayNight):
    if DayNight == 1:
        wallpaper(root, 450, 800, "assets/blackwhite.png")

"""


def display_main_menu(canvas, width, height, wallpaper):
    """Affiche le menu principal."""
    clear_canvas(canvas)

    # Réafficher le wallpaper
    canvas.create_image(0, 0, image=wallpaper, anchor="nw")

    # Widgets du menu principal
    title = tk.Label(canvas, text="Password Vault", font=('Arial', 28), bg="#000000", fg="#fa4902")
    connection_btn = tk.Button(canvas, text="Connexion", font=('Arial', 15), bg='#000000', fg="#FFFFFF", activebackground="#fa4902",command=lambda: display_connection_menu(canvas, width, height, wallpaper))
    sign_up_btn = tk.Button(canvas, text="Inscription", font=('Arial', 15), bg='#000000', fg="#FFFFFF", activebackground="#fa4902", command=lambda: display_inscritpion_menu(canvas, width, height, wallpaper))

    # Placement des widgets
    canvas.create_window(width/2, 100, window=title)
    canvas.create_window(width/2, 250, window=connection_btn)
    canvas.create_window(width/2, 300, window=sign_up_btn)


def display_inscritpion_menu(canvas, width, height, wallpaper):
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

    create_btn = tk.Button(canvas, text="Créer un compte", font=('Arial', 12), bg='#000000', fg="#FFFFFF", activebackground="#fa4902",
                          command=lambda: acc.handle_sign_up(login_entry, password_entry, confirm_password, result_label))
    back_btn = tk.Button(canvas, text="Retour", font=('Arial', 12), bg='#000000', fg="#FFFFFF", activebackground="#fa4902",
                         command=lambda: display_main_menu(canvas, width, height, wallpaper))

    # Placement des widgets
    canvas.create_window(width / 2, 50, window=title)
    canvas.create_window(width / 2, 150, window=login_entry)
    canvas.create_window(width / 2, 200, window=password_entry)
    canvas.create_window(width / 2, 250, window=confirm_password)
    canvas.create_window(width / 2, 300, window=create_btn)
    canvas.create_window(width / 2, 350, window=back_btn)
    canvas.create_window(width / 2, 430, window=result_label)

def display_connection_menu(canvas, width, height, wallpaper):
    """Affiche le menu de connexion."""
    clear_canvas(canvas)

    # Réafficher le wallpaper
    canvas.create_image(0, 0, image=wallpaper, anchor="nw")

    # Widgets pour la connexion
    title = tk.Label(canvas, text="Connexion", font=('Arial', 22), bg="#000000", fg="#FFFFFF")
    login_entry = tk.Entry(canvas)
    password_entry = tk.Entry(canvas, show="*")
    result_label = tk.Label(canvas, text="", font=('Arial', 12), bg="#000000", fg="#FFFFFF")

    login_btn = tk.Button(canvas, text="Se connecter", font=('Arial', 12), bg='#000000', fg="#FFFFFF", activebackground="#fa4902",
                        command=lambda: acc.handle_sign_in(login_entry, password_entry, result_label))
    back_btn = tk.Button(canvas, text="Retour", font=('Arial', 12), bg='#000000', fg="#FFFFFF", activebackground="#fa4902",
                        command=lambda: display_main_menu(canvas, width, height, wallpaper))

    # Placement des widgets
    canvas.create_window(width / 2, 50, window=title)
    canvas.create_window(width / 2, 200, window=login_entry)
    canvas.create_window(width / 2, 250, window=password_entry)
    canvas.create_window(width / 2, 300, window=login_btn)
    canvas.create_window(width / 2, 350, window=back_btn)
    canvas.create_window(width / 2, 430, window=result_label)

###############################################################################################################################
###############################################################################################################################

def main_window(width=800,height=450 ):
    """Crée la fenêtre principale."""
    root = tk.Tk()
    root.geometry(f"{width}x{height}")
    root.resizable(0, 0)
    root.title("Password Vault")

    # Charger le wallpaper et créer le canvas
    canvas, wallpaper_image = wallpaper(root, width, height)

    # Afficher le menu principal
    display_main_menu(canvas, width, height, wallpaper_image)  # Corrigé : width, puis height

    # Lancement de la boucle principale
    root.mainloop()


# Exécuter l'application
main_window()



