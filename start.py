import tkinter as tk
import accounts_handling as acc
import wallpaper as wp
import vault

"""############################################################################################################################
########################################  PARTIE 1 : CHOIX INSCRIPTION / CONNEXION ############################################ 
############################################################################################################################"""

connected_to = None

def clear_canvas(canvas):
    """Efface tous les widgets du canvas."""
    canvas.delete("all")



def display_main_menu(canvas, width, height, wallpaper):
    """Affiche le menu principal."""
    clear_canvas(canvas)
    canvas.create_image(0, 0, image=wallpaper, anchor="nw")

    title = tk.Label(canvas, text="Password Vault", font=('Arial', 28, 'bold'), bg="#000000", fg="#fa4902")
    connection_btn = tk.Button(canvas, text="Connexion", font=('Arial', 18), bg='#000000', fg="#FFFFFF", activebackground="#fa4902",
                                command=lambda: display_connection_menu(canvas, width, height, wallpaper))
    sign_up_btn = tk.Button(canvas, text="Inscription", font=('Arial', 18), bg='#000000', fg="#FFFFFF", activebackground="#fa4902",
                             command=lambda: display_inscritpion_menu(canvas, width, height, wallpaper))

    canvas.create_window(width/2, 100, window=title)
    canvas.create_window(width/2, 200, window=connection_btn)
    canvas.create_window(width/2, 265, window=sign_up_btn)

def display_inscritpion_menu(canvas, width, height, wallpaper):
    """Affiche le menu d'inscription."""
    clear_canvas(canvas)
    canvas.create_image(0, 0, image=wallpaper, anchor="nw")

    # Titre
    title = tk.Label(canvas, text="Inscription", font=('Arial', 22), bg="#000000", fg="#FFFFFF")
    canvas.create_window(width / 2, 50, window=title)

    # Alias (Nom d'utilisateur)
    login_label = tk.Label(canvas, text="Nom d'utilisateur", font=('Arial', 14), bg="#000000", fg="#FFFFFF")
    canvas.create_window(width / 2, 120, window=login_label)
    login_entry = tk.Entry(canvas,width=15, font=('Arial 14'))
    canvas.create_window(width / 2, 150, window=login_entry)

    # Mot de passe
    password_label = tk.Label(canvas, text="Mot de passe", font=('Arial', 14), bg="#000000", fg="#FFFFFF")
    canvas.create_window(width / 2, 180, window=password_label)
    password_entry = tk.Entry(canvas,width=15, font=('Arial 14'), show="*")
    canvas.create_window(width / 2, 210, window=password_entry)

    # Confirmation du mot de passe
    confirm_label = tk.Label(canvas, text="Confirmer le mot de passe", font=('Arial', 14), bg="#000000", fg="#FFFFFF")
    canvas.create_window(width / 2, 240, window=confirm_label)
    confirm_password = tk.Entry(canvas,width=15, font=('Arial 14'), show="*")
    canvas.create_window(width / 2, 270, window=confirm_password)

    # Boutons
    result_label = tk.Label(canvas, text="", font=('Arial', 12), bg="#000000", fg="#FFFFFF")
    canvas.create_window(width / 2, 430, window=result_label)

    create_btn = tk.Button(canvas, text="Créer un compte", font=('Arial', 14), bg='#000000', fg="#FFFFFF", activebackground="#fa4902",
                           command=lambda: acc.handle_sign_up(login_entry, password_entry, confirm_password, result_label))
    back_btn = tk.Button(canvas, text="Retour", font=('Arial', 14), bg='#000000', fg="#FFFFFF", activebackground="#fa4902",
                         command=lambda: display_main_menu(canvas, width, height, wallpaper))
    canvas.create_window(width / 2, 335, window=create_btn)
    canvas.create_window(width / 2, 380, window=back_btn)


def display_connection_menu(canvas, width, height, wallpaper):
    """Affiche le menu de connexion."""
    clear_canvas(canvas)
    canvas.create_image(0, 0, image=wallpaper, anchor="nw")

    # Titre
    title = tk.Label(canvas, text="Connexion", font=('Arial', 22), bg="#000000", fg="#FFFFFF")
    canvas.create_window(width / 2, 50, window=title)

    # Nom d'utilisateur
    login_label = tk.Label(canvas, text="Nom d'utilisateur", font=('Arial', 14), bg="#000000", fg="#FFFFFF")
    canvas.create_window(width / 2, 180, window=login_label)
    login_entry = tk.Entry(canvas, width=15, font=('Arial', 14))
    canvas.create_window(width / 2, 210, window=login_entry)

    # Mot de passe
    password_label = tk.Label(canvas, text="Mot de passe", font=('Arial', 14), bg="#000000", fg="#FFFFFF")
    canvas.create_window(width / 2, 240, window=password_label)
    password_entry = tk.Entry(canvas, width=15, font=('Arial', 14), show="*")
    canvas.create_window(width / 2, 270, window=password_entry)

    # Résultat
    result_label = tk.Label(canvas, text="", font=('Arial', 12), bg="#000000", fg="#FFFFFF")
    canvas.create_window(width / 2, 430, window=result_label)

    # Fonction pour gérer la connexion
    def handle_login():
        username, master_password = acc.handle_sign_in(login_entry, password_entry, result_label)
        if username and master_password:  # Si connexion réussie
            vault.display_vault(canvas, width, height, wallpaper, username, master_password)

    # Boutons
    login_btn = tk.Button(canvas, text="Se connecter", font=('Arial', 16), bg='#000000', fg="#FFFFFF", activebackground="#fa4902",
                          command=handle_login)
    back_btn = tk.Button(canvas, text="Retour", font=('Arial', 16), bg='#000000', fg="#FFFFFF", activebackground="#fa4902",
                         command=lambda: display_main_menu(canvas, width, height, wallpaper))

    canvas.create_window(width / 2, 335, window=login_btn)
    canvas.create_window(width / 2, 380, window=back_btn)





###############################################################################################################################
###############################################################################################################################

def main(mod="dark"):
    width, height = 800, 450
    root = tk.Tk()
    root.geometry(f"{width}x{height}")
    root.resizable(0, 0)
    root.title("Password Vault")

    # Charger le wallpaper et créer le canvas
    canvas, wallpaper_image = wp.wallpaper(root, width, height)

    # Afficher le menu principal
    display_main_menu(canvas, width, height, wallpaper_image)

    # Lancement de la boucle principale
    root.mainloop()

if __name__ == "__main__":
    main()

