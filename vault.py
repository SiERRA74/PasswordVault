import tkinter as tk
import wallpaper as wp
import pwd_management as pwd
import vignere
import accounts_handling as acc


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

    title = tk.Label(canvas, text=f"Bienvenue, {username}", font=('Arial', 22), bg="#000000", fg="#FFFFFF")
    canvas.create_window(width / 2, 50, window=title)

    user_data = pwd.file_read(username)
    passwords = user_data["PWD"]

    y_pos = 100
    for alias, details in passwords.items():
        login = details["login"]
        login = vignere.decryptage_vignere(master_password, login)
        encrypted_password = details["password"]
        decrypted_password = vignere.decryptage_vignere(master_password, encrypted_password)

        alias_label = tk.Label(canvas, text=f"{alias} ({login}): {decrypted_password}", font=('Arial', 12), bg="#000000", fg="#FFFFFF")
        canvas.create_window(width / 2, y_pos, window=alias_label)
        y_pos += 30

    add_password_btn = tk.Button(canvas, text="Ajouter un mot de passe", font=('Arial', 15), bg='#000000', fg="#FFFFFF", activebackground="#fa4902",
                                 command=lambda: password_add_screen(canvas, width, height, wallpaper, username, master_password))
    canvas.create_window(width / 2, height - 50, window=add_password_btn)



"""############################################################################################################################
####################################### PARTIE 3 : ADDING AND SAVING PASSWORDS ################################################
############################################################################################################################"""


def password_add_screen(canvas, width, height, wallpaper, username, master_password):
    """Affiche l'écran d'ajout de mot de passe."""
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
    result_label = tk.Label(canvas, text="", font=('Arial', 13), bg="#000000", fg="#FFFFFF")
    canvas.create_window(width / 2, 370, window=result_label)

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
        pwd.add_password(username, alias, {
            "identifiant": encrypted_login,
            "password": encrypted_password,
            "link": link
        })
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

    canvas.create_window(width / 2, height -50, window=save_btn)
    canvas.create_window(width / 2, height - 30, window=back_btn)



"""############################################################################################################################
######################################## PARTIE 4 : GENERATING SAFE PASSWORDS #################################################
############################################################################################################################"""


def generate_password(canvas, width, height, wallpaper):
    pass