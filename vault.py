import tkinter as tk
import wallpaper as wp
import pwd_management as pwd
import vignere
import accounts_handling as acc
from tkinter.scrolledtext import ScrolledText


"""############################################################################################################################
############################################ PARTIE 2 : LISTING PASSWORDS #####################################################
############################################################################################################################"""

def clear_canvas(canvas):
    canvas.delete("all")

def go_back(canvas, width, height, wallpaper, username, master_password):
    """Retour à l'écran précédent."""
    display_vault(canvas, width, height, wallpaper, username, master_password)


def display_vault(canvas, width, height, wallpaper, username, master_password):
    """Affiche les mots de passe de l'utilisateur."""
    clear_canvas(canvas)
    canvas.create_image(0, 0, image=wallpaper, anchor="nw")

    # Titre de la page
    title = tk.Label(canvas, text=f"Bienvenue, {username}", font=('Arial', 20), bg="#000000", fg="#FFFFFF")
    canvas.create_window(width / 2, 30, window=title)

    # Charger les mots de passe depuis le fichier
    user_data = pwd.file_read(username)
    passwords = user_data["PWD"]

    # ScrolledText pour afficher les mots de passe
    scrolled_text = ScrolledText(canvas, width=80, height=15, wrap=tk.WORD, bg="#000000", fg="#FFFFFF", font=('Arial', 12))
    scrolled_text.place(x=40, y=80)

    # Création d'une frame dans le ScrolledText
    frame = tk.Frame(scrolled_text, bg="#000000")
    scrolled_text.window_create(tk.END, window=frame)

    # Ajouter les mots de passe
    for alias, details in passwords.items():
        # Décryptage des champs
        login = vignere.decryptage_vignere(master_password, details["login"])
        decrypted_password = vignere.decryptage_vignere(master_password, details["password"])

        # Frame horizontale pour chaque mot de passe
        row_frame = tk.Frame(frame, bg="#000000")
        row_frame.pack(fill="x", pady=5)

        # Alias
        alias_label = tk.Label(row_frame, text=alias, font=('Arial', 12), bg="#000000", fg="#FFFFFF", width=15, anchor="w")
        alias_label.pack(side="left", padx=5)

        # Identifiant
        login_label = tk.Label(row_frame, text=login, font=('Arial', 12), bg="#000000", fg="#FFFFFF", width=20, anchor="w")
        login_label.pack(side="left", padx=5)

        # Mot de passe
        password_label = tk.Label(row_frame, text=decrypted_password, font=('Arial', 12), bg="#000000", fg="#FFFFFF", width=20, anchor="w")
        password_label.pack(side="left", padx=5)

        # Bouton d'action
        action_button = tk.Button(row_frame, text="X", font=('Arial', 12), bg='#fa4902', fg="#FFFFFF",
                                command=lambda alias=alias: delete_password(alias, canvas, width, height, wallpaper, username, master_password))
        action_button.pack(side="left", padx=5)


    # Bouton pour ajouter un mot de passe
    add_password_btn = tk.Button(canvas, text="Ajouter un mot de passe", font=('Arial', 14), bg='#000000', fg="#FFFFFF",
                                 activebackground="#fa4902",
                                 command=lambda: password_add_screen(canvas, width, height, wallpaper, username, master_password,scrolled_text))
    canvas.create_window(width / 2, height - 50, window=add_password_btn)


"""############################################################################################################################
####################################### PARTIE 3 : ADDING AND SAVING PASSWORDS ################################################
############################################################################################################################"""




def password_add_screen(canvas, width, height, wallpaper, username, master_password, scroll):
    """Affiche l'écran d'ajout de mot de passe."""
    scroll.destroy()
    clear_canvas(canvas)
    canvas.create_image(0, 0, image=wallpaper, anchor="nw")

    # Titre de la page
    title = tk.Label(canvas, text="Ajout d'un nouveau mot de passe", font=('Arial', 20), bg="#000000", fg="#FFFFFF")
    canvas.create_window(width / 2, 50, window=title)

    # Alias
    alias_label = tk.Label(canvas, text="Alias (Nom du site/service)", font=('Arial', 14), bg="#000000", fg="#FFFFFF")
    canvas.create_window(width / 2, 100, window=alias_label)
    alias_entry = tk.Entry(canvas, width=25, font=('Arial 14'))
    canvas.create_window(width / 2, 130, window=alias_entry)

    # Identifiant
    login_label = tk.Label(canvas, text="Identifiant", font=('Arial', 14), bg="#000000", fg="#FFFFFF")
    canvas.create_window(width / 2, 170, window=login_label)
    login_entry = tk.Entry(canvas,width=25, font=('Arial 14'))
    canvas.create_window(width / 2, 200, window=login_entry)

    # Mot de passe
    password_label = tk.Label(canvas, text="Mot de passe", font=('Arial', 14), bg="#000000", fg="#FFFFFF")
    canvas.create_window(width / 2, 240, window=password_label)
    password_entry = tk.Entry(canvas,width=25, font=('Arial 14'))
    canvas.create_window(width / 2, 270, window=password_entry)

    # Lien/URL
    link_label = tk.Label(canvas, text="Lien (facultatif)", font=('Arial', 14), bg="#000000", fg="#FFFFFF")
    canvas.create_window(width / 2, 310, window=link_label)
    link_entry = tk.Entry(canvas,width=25, font=('Arial 14'))
    canvas.create_window(width / 2, 340, window=link_entry)

    # Résultat
    result_label = tk.Label(canvas, text="", font=('Arial', 12), bg="#000000", fg="#FFFFFF")
    canvas.create_window(width / 2, 430, window=result_label)

    # Fonction pour sauvegarder
    def save_password():
        alias = alias_entry.get()
        login = login_entry.get()
        password = password_entry.get()
        link = link_entry.get()

        if not alias or not login or not password:
            result_label.config(text="Tous les champs obligatoires doivent être remplis.", fg="red")
            return

        encrypted_login = vignere.vignere_cryptage(master_password, login)
        encrypted_password = vignere.vignere_cryptage(master_password, password)

        # Ajouter les données au gestionnaire
        pwd.add_password(username, alias, encrypted_login, encrypted_password, link)

        result_label.config(text="Mot de passe ajouté avec succès !", fg="green")

        # Effacer les champs après la sauvegarde
        alias_entry.delete(0, 'end')
        login_entry.delete(0, 'end')
        password_entry.delete(0, 'end')
        link_entry.delete(0, 'end')

    # Boutons
    save_btn = tk.Button(canvas, text="Sauvegarder", font=('Arial', 14), bg='#000000', fg="#FFFFFF", activebackground="#fa4902",
                         command=save_password)
    back_btn = tk.Button(canvas, text="Retour", font=('Arial', 14), bg='#000000', fg="#FFFFFF", activebackground="#fa4902",
                         command=lambda: go_back(canvas, width, height, wallpaper, username, master_password))

    canvas.create_window(width / 2, 380, window=save_btn)
    canvas.create_window(width / 2, 420, window=back_btn)


def delete_password(alias, canvas, width, height, wallpaper, username, master_password):
    """Supprime le mot de passe associé à l'alias."""
    user_data = pwd.file_read(username)  # Charge les données utilisateur
    if alias in user_data["PWD"]:
        del user_data["PWD"][alias]  # Supprime l'entrée
        pwd.file_write(user_data, username)  # Sauvegarde les changements
        print(f"Mot de passe pour {alias} supprimé avec succès.")
        go_back(canvas, width, height, wallpaper, username, master_password)
    else:
        print(f"Alias {alias} introuvable.")


"""############################################################################################################################
######################################## PARTIE 4 : GENERATING SAFE PASSWORDS #################################################
############################################################################################################################"""


def generate_password(canvas, width, height, wallpaper):
    pass
    """TODO"""