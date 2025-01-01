import tkinter as tk

def wallpaper(root, width, height, mod="dark"):
    """Crée un canvas avec un wallpaper."""
    if mod == "dark":
        mod = "assets/blackwhite.png"
    else:
        mod = "assets/whiteblack.png"

    # Création du canvas
    canvas = tk.Canvas(root, width=width, height=height)
    canvas.pack(fill="both", expand=True)

    wallpaper_image = tk.PhotoImage(file=mod)
    
    canvas.create_image(0, 0, image=wallpaper_image, anchor="nw")

    # Associe l'image à l'objet canvas pour éviter le garbage collector
    canvas.wallpaper_image = wallpaper_image

    # Retourne le canvas et l'image
    return canvas, wallpaper_image



"""
def change_theme(DayNight):
    if DayNight == 1:
        wallpaper(root, 450, 800, "assets/blackwhite.png")

"""