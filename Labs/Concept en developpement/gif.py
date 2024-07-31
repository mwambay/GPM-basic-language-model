
from tkinter import Tk, Label
from PIL import Image, ImageTk


# Création de la fenêtre principale
fenetre = Tk()

# Chargement du fichier GIF
gif = Image.open("Labs\loading-50 (1).gif")

# Création d'une liste contenant chaque image du GIF
frames = []
for frame in range(0, gif.n_frames):
    gif.seek(frame)
    frame_image = gif.copy().convert("RGBA")
    frames.append(ImageTk.PhotoImage(frame_image))

# Création du widget Label pour afficher les images du GIF
label = Label(fenetre)
label.pack()

# Fonction pour afficher les images successivement
def afficher_image(frame):
    image = frames[frame]
    label.configure(image=image)
    fenetre.after(gif.info['duration'], lambda: afficher_image((frame + 1) % len(frames)))

# Lancement de l'affichage de l'animation
afficher_image(0)

# Lancement de la boucle principale
fenetre.mainloop()