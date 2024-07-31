import tkinter as tk

def on_key_release(event):
    global completion_done
    # Récupérer le texte saisi par l'utilisateur
    current_text = text_widget.get("1.0", "end-1c")
    
    # Vérifier si le texte contient le mot "bonjour" et si la complétion n'a pas encore été faite
    if "bonjour" in current_text.lower() and not completion_done:
        # Compléter automatiquement avec "comment allez-vous ?"
        completed_text = current_text + " comment allez-vous ?"
        # Mettre à jour le widget texte avec le texte complété
        text_widget.delete("1.0", "end")
        text_widget.insert("1.0", completed_text)
        # Marquer la complétion comme étant déjà faite
        completion_done = True
    else:
        # Réinitialiser la variable de complétion si le mot "bonjour" est supprimé
        if "bonjour" not in current_text.lower():
            completion_done = False

# Créer la fenêtre principale
window = tk.Tk()

# Créer le widget texte
text_widget = tk.Text(window)
text_widget.pack()

# Initialiser la variable de complétion
completion_done = False

# Associer l'événement de relâchement de touche à la fonction on_key_release
text_widget.bind("<KeyRelease>", on_key_release)
def my_fonction(event):
    print("hello")
text_widget.tag_config("my_tag", foreground = "yellow")
text_widget.tag_bind("my_tag", "<Button-1>", my_fonction)
text_widget.insert("1.0", "salut", "my_tag" )
text_widget.configure(state="disabled")
# Lancer la boucle principale de la fenêtre
window.mainloop()
