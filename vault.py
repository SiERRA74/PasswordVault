import tkinter as tk
import wallpaper as wp
import pwd_management as pwd



"""############################################################################################################################
############################################ PARTIE 2 : LISTING PASSWORDS #####################################################
############################################################################################################################"""

def clear_canvas(canvas):
    canvas.delete("all")


def display_vault(canvas, width, height, wallpaper, username):
    """Affiche les mots de passe pour l'utilisateur connecté."""
    clear_canvas(canvas)
    canvas.create_image(0, 0, image=wallpaper, anchor="nw")

    title = tk.Label(canvas, text=f"Bienvenue, {username}", font=('Arial', 22), bg="#000000", fg="#FFFFFF")
    canvas.create_window(width / 2, 50, window=title)

    passwords = pwd.get_json_files(username)  # Obtenir les mots de passe pour l'utilisateur
    y_pos = 100
    for site, pwd_info in passwords.items():
        site_label = tk.Label(canvas, text=f"{site}: {pwd_info}", font=('Arial', 12), bg="#000000", fg="#FFFFFF")
        canvas.create_window(width / 2, y_pos, window=site_label)
        y_pos += 30

    back_btn = tk.Button(canvas, text="Retour", font=('Arial', 12), bg='#000000', fg="#FFFFFF", activebackground="#fa4902",
                         command=lambda: display_main_menu(canvas, width, height, wallpaper))
    canvas.create_window(width / 2, height - 50, window=back_btn)

