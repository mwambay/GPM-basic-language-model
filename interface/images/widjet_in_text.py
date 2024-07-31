import tkinter as tk
from tkinter import font

def on_button_click():
    text.insert("insert", "Button Clicked!\n")

root = tk.Tk()
root.geometry("300x200")

# Création du widget Text
text = tk.Text(root, height=8, width=30)
text.pack()

# Création d'un style pour le bouton simulé
button_style = font.Font(weight="bold", underline=True)

# Insertion du texte avec des balises de style
text.insert("insert", "Ceci est un texte avec un bouton simulé.\n")
text.insert("insert", "Cliquez sur le ", "")
text.insert("insert", "bouton", "button")
text.insert("insert", " pour effectuer une action.\n")

# Ajout d'une balise de style pour le bouton simulé
text.tag_configure("button", font=button_style)
text.tag_bind("button", "<Button-1>", lambda event: on_button_click())

root.mainloop()
