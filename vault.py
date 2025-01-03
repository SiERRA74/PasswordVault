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
        identifiant = details["identifiant"]
        encrypted_password = details["password"]
        decrypted_password = vignere.decryptage_vignere(master_password, encrypted_password)

        alias_label = tk.Label(canvas, text=f"{alias} ({identifiant}): {decrypted_password}", font=('Arial', 12), bg="#000000", fg="#FFFFFF")
        canvas.create_window(width / 2, y_pos, window=alias_label)
        y_pos += 30

    add_password_btn = tk.Button(canvas, text="Ajouter un mot de passe", font=('Arial', 15), bg='#000000', fg="#FFFFFF", activebackground="#fa4902",
                                 command=lambda: password_add_screen(canvas, width, height, wallpaper, username, master_password))
    canvas.create_window(width / 2, height - 50, window=add_password_btn)

def password_add_screen(canvas, width, height, wallpaper, username, master_password):
    """Affiche l'écran d'ajout de mot de passe."""
    clear_canvas(canvas)
    canvas.create_image(0, 0, image=wallpaper, anchor="nw")


    title = tk.Label(canvas, text="Ajout d'un nouveau mot de passe", font=('Arial', 20), bg="#000000", fg="#FFFFFF")
    canvas.create_window(width / 2, 50, window=title)

    alias_entry = tk.Entry(canvas)
    alias_entry.insert(0, "Alias")
    canvas.create_window(width / 2, 150, window=alias_entry)

    login_entry = tk.Entry(canvas)
    login_entry.insert(0, "Identifiant")
    canvas.create_window(width / 2, 200, window=login_entry)

    password_entry = tk.Entry(canvas)
    canvas.create_window(width / 2, 250, window=password_entry)

    result_label = tk.Label(canvas, text="", font=('Arial', 12), bg="#000000", fg="#FFFFFF")
    canvas.create_window(width / 2, 350, window=result_label)

    def save_password():
        alias = alias_entry.get()
        login = login_entry.get()
        password = password_entry.get()

        if not alias or not login or not password:
            result_label.config(text="Tous les champs doivent être remplis.", fg="red")
            return

        encrypted_password = vignere.vignere_cryptage(master_password, password)
        pwd.add_password(username, alias, login, encrypted_password)
        result_label.config(text="Mot de passe ajouté avec succès !", fg="green")

    save_btn = tk.Button(canvas, text="Sauvegarder", font=('Arial', 12), bg='#000000', fg="#FFFFFF", activebackground="#fa4902",
                         command=save_password)
    back_btn = tk.Button(canvas, text="Retour", font=('Arial', 12), bg='#000000', fg="#FFFFFF", activebackground="#fa4902",
                         command=lambda: go_back(canvas, width, height, wallpaper, username, master_password))

    canvas.create_window(width / 2, 300, window=save_btn)
    canvas.create_window(width / 2, height - 50, window=back_btn)
