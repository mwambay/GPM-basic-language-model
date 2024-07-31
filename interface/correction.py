from nltk.tokenize import word_tokenize
import tkinter as tk

def correction_de_saisie(output_model, text_widget, champ_rapport):
    output_model = output_model["Sequence retained"]
    texte = text_widget.get('1.0', tk.END)
    texte = word_tokenize(texte)
    temp = ""
    for mot in output_model.split():
        if mot != "<ignore>":
            temp+=" " + mot
    output_model = temp

    ponctuation = ['.', ':', ';', '!', '?']  
    output_model = word_tokenize(output_model)
    for indice, token in enumerate(texte):
        if token.strip(" ") in output_model or token.strip(" ") in ponctuation:
            del texte[indice]
            del output_model[indice]

    def inserer(champ_rapport):
        champ_rapport.configure(state = "normal")
        champ_rapport.insert("end", "nouvelle session\n\n")
        for indice, mot in enumerate(texte):
            try:
                #liste_des_couleur = ['blue', '#C93BB9', 'green', '#9E44E0', '#6458C9', '#78E0C6', '#F95C4B', '#C94D83', '#8F8E42']
                #color_random = random.randint(0, liste_des_couleur.__len__() - 1) 
                #couleur = liste_des_couleur[color_random]
                couleur = 'gray'
                champ_rapport.tag_config(couleur, foreground = couleur)
                champ_rapport.insert(tk.END, f"pour {mot} essayez avec {output_model[indice]} \n\n", couleur)
            except:
                pass
        champ_rapport.insert("end", "\nfin session\n")
    inserer(champ_rapport)

    def rechercher_occurrences(mot, support, color, tag_, define_foreground):
        # Efface toutes les balises de mise en surbrillance précédentes
        #text_widget.tag_remove("highlight", "1.0", tk.END)

        texte = support.get("1.0", "end-1c")  # Obtient le texte du widget texte
        mot_a_rechercher = mot  # Obtient le mot à rechercher
        occurrences = []

        # Recherche toutes les occurrences du mot dans le texte
        index = 1.0
        if mot.__len__() != 0:
            while True:
                index = support.search(mot_a_rechercher, index, stopindex=tk.END)
                if not index:
                    break
                occurrences.append(index)
                index = support.index(f"{index}+{len(mot_a_rechercher)}c")

            # Met en surbrillance les occurrences trouvées
            for index in occurrences:
                support.tag_add(tag_, index, f"{index}+{len(mot_a_rechercher)}c")
            if define_foreground:
                support.tag_config(tag_, underline=True, foreground=color)
            else:
                support.tag_config(tag_, underline=True)

    for mot in texte:
        rechercher_occurrences(mot, text_widget, 'red', 'prime', True)
    for mot in output_model:
        rechercher_occurrences(mot, champ_rapport, 'black', 'out', False)
    for mot in texte:
        rechercher_occurrences(mot, champ_rapport, 'red', 'prob', True)