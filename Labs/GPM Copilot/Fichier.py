import tkinter as tk
from tkinter import ttk

def on_key_release(event):
    # Récupérer le texte saisi par l'utilisateur
    current_text = text_widget.get("1.0", "end-1c")
    
    # Vérifier si le texte contient le mot "bonjour"
    if "bonjour" in current_text.lower():
        # Proposer un menu de suggestions
        suggested_words = ["comment allez-vous ?", "bienvenue", "salut"]
        show_suggestions(suggested_words)
    else:
        # Effacer le menu de suggestions s'il est affiché
        hide_suggestions()

def show_suggestions(suggested_words):
    # Effacer le menu de suggestions s'il est déjà affiché
    hide_suggestions()
    
    # Créer un menu déroulant pour les suggestions
    global suggestions_menu
    suggestions_menu = tk.Menu(window, tearoff=0)
    
    # Ajouter les suggestions au menu
    for word in suggested_words:
        suggestions_menu.add_command(label=word, command=lambda w=word: complete_with_suggestion(w))
    
    # Afficher le menu de suggestions sous le curseur
    x, y, _, _ = text_widget.bbox("insert")
    x += text_widget.winfo_rootx() + 2
    y += text_widget.winfo_rooty() + text_widget.winfo_height() + 2
    suggestions_menu.post(x, y)

def hide_suggestions():
    # Cacher le menu de suggestions s'il est affiché
    global suggestions_menu
    if suggestions_menu:
        suggestions_menu.delete(0, "end")
        suggestions_menu.unpost()
        suggestions_menu = None

def complete_with_suggestion(suggestion):
    # Récupérer le texte saisi par l'utilisateur
    current_text = text_widget.get("1.0", "end-1c")
    
    # Trouver la position du mot "bonjour"
    index = current_text.lower().index("bonjour")
    
    # Compléter le mot avec la suggestion sélectionnée
    completed_text = current_text[:index] + suggestion
    
    # Mettre à jour le widget texte avec le texte complété
    text_widget.delete("1.0", "end")
    text_widget.insert("1.0", completed_text)
    
    # Effacer le menu de suggestions
    hide_suggestions()

def handle_enter(event):
    # Vérifier si le menu de suggestions est affiché
    if suggestions_menu:
        # Récupérer la suggestion sélectionnée dans le menu
        selected_suggestion = suggestions_menu.entrycget(0, "label")
        complete_with_suggestion(selected_suggestion)

# Créer la fenêtre principale
window = tk.Tk()

# Créer le widget texte
text_widget = tk.Text(window)
text_widget.pack()

# Créer le menu de suggestions
suggestions_menu = None

# Associer l'événement de relâchement de touche à la fonction on_key_release
text_widget.bind("<KeyRelease>", on_key_release)

# Associer l'événement d'appui sur la touche Entrée à la fonction handle_enter
text_widget.bind("<Return>", handle_enter)

# Lancer la boucle principale de
window.mainloop()