import tkinter as tk
import sys
import os
chemin_parent = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(chemin_parent)
from model.Head_Of_Model.GPM4 import GPM4_Head
import customtkinter
import time
import json
import random
from PIL import Image, ImageTk
from threading import Thread
from correction import correction_de_saisie
from nltk.tokenize import word_tokenize

def rechercher_occurrences(mot):
        # Efface toutes les balises de mise en surbrillance précédentes
        champ_rapport.tag_remove("highlight", "1.0", customtkinter.END)

        texte = champ_rapport.get("1.0", "end-1c")  # Obtient le texte du widget texte
        mot_a_rechercher = mot  # Obtient le mot à rechercher
        occurrences = []

        # Recherche toutes les occurrences du mot dans le texte
        index = 1.0
        if mot.__len__() != 0:
            while True:
                index = champ_rapport.search(mot_a_rechercher, index, stopindex=customtkinter.END)
                if not index:
                    break
                occurrences.append(index)
                index = champ_rapport.index(f"{index}+{len(mot_a_rechercher)}c")
            # Met en surbrillance les occurrences trouvées
            for index in occurrences:
                champ_rapport.tag_add("highlight", index, f"{index}+{len(mot_a_rechercher)}c")
                
            if occurrences:
                champ_rapport.see(occurrences[0])
            champ_rapport.tag_config("highlight", background="yellow")


with open(rf"{chemin_parent}\config\configuration.json") as file:
    data_settings = json.load(file)
    file.close()
rapport = 'None'
autoSave = data_settings['Auto preference']
theme = "dark" 
customtkinter.set_appearance_mode(theme)
max_word = 1
texte_temp = ""
prediction_text = ""
stop_calling = False
attente_flag = True
bascule_engine_state = True
bascule_swiche = 0
bascule_swiche_recur = 0
def affiche_resultat(resultat):
    global rapport
    output = resultat
    try:
        rapport = output['Class']
    except:
        pass
    global texte_temp
    global completion_done
    # Récupérer le texte saisi par l'utilisateur
    if indice_mode != 10e000:
        current_text = text_widget.get("1.0", "end-1c")
        try:
            probability = output["Probability"]
            x_reference = output["Sequence retained"]
            for valeur in probability:
                tem = valeur.split()
                if tem[0] == x_reference.strip(" "):
                    big_value = tem[1]
        except:
            probability = [""]
        
        champ_rapport.configure(state = "normal")
        champ_rapport.insert("end", "nouvelle session\n\n")
        for mot in probability:
            try:
                liste_des_couleur = ['blue', '#C93BB9', 'green', '#9E44E0', '#6458C9', '#78E0C6', '#F95C4B', '#C94D83', '#8F8E42']
                color_random = random.randint(0, liste_des_couleur.__len__() - 1) 
                couleur = liste_des_couleur[color_random]
                temp = mot.split()
                if x_reference.strip(" ") == temp[0] or temp[1] == big_value:
                    champ_rapport.tag_config("yellow", background =  'gray' )# "#BE82CF")
                    
                    champ_rapport.insert(customtkinter.END, mot + "\n", "yellow")

                else:
                    champ_rapport.tag_config(couleur, foreground = couleur)
                    champ_rapport.insert(customtkinter.END, mot + "\n", couleur)
            except:
                pass
        champ_rapport.insert("end", "\nfin session\n")
        
        try:
            comp = 0
            prediction_du_model.insert(customtkinter.END, 'New Process\n')
            for mot in output["Predictions"]:
                comp += 1
                liste_des_couleur = ['blue', '#C93BB9', 'green', '#9E44E0', '#6458C9', '#78E0C6', '#F95C4B', '#C94D83']
                color_random = random.randint(0, liste_des_couleur.__len__() - 1) 
                couleur = liste_des_couleur[color_random]
                prediction_du_model.tag_config(couleur, foreground = couleur)
                prediction_du_model.insert(customtkinter.END, f' {comp}. {mot} \n' , couleur)
                prediction_du_model.see(customtkinter.END)
            prediction_du_model.insert(customtkinter.END, '\nProcessing finish\n')
            text_insert ='_'*24
            prediction_du_model.insert(customtkinter.END, text_insert + '\n')
        except:pass
        try:
            
            output = output["Sequence retained"]
            
            texte_temp += " " + output.rstrip("\n")
        except:pass
        completed_text = str(current_text) + str(output)
            # Mettre à jour le widget texte avec le texte complété
        try:
            def typing_effect1(string1, label):
                for char in string1:
                    text_widget.tag_config('color_i', foreground = '#666666')
                    if char == ":" :
                        text_widget.insert("end",  char   , "color_i")
                    elif char == '\n' or char == ' \n':
                        text_widget.insert("end",  '\n'   , "color_i")
                    elif char == '\t' or char == ' \t':

                        text_widget.insert("end",  '\t'   , "color_i")
                    else:
                        text_widget.insert("end",char , "color_i")
                    def on_clic(event):
                        rechercher_occurrences(text_widget.get('0.1', customtkinter.END).split()[-1])
                    text_widget.tag_bind("color_i", "<Button-1>", on_clic)
                    text_widget.update()
                    text_widget.see("end")
                    time.sleep(0.001)
            typing_effect1(output, completed_text)
        except TypeError:
            pass
        prediction_du_model.see("end")
        champ_rapport.see("end")
        text_widget_3.configure(state = 'normal')
        text_widget_3.delete(1.0, customtkinter.END)
        taille = len(word_tokenize(text_widget.get('1.0', customtkinter.END)))
        text_widget_3.tag_config("len_texte", foreground = "blue")
        text_widget_3.insert('1.0', 'Token(s) : ')
        text_widget_3.insert('1.14', str(taille) + "   " , 'len_texte')
        
        if rapport == 'Logic Math':
            text_widget_3.tag_config("Class", foreground = "green")
            text_widget_3.insert('1.23', 'Class : ')
            text_widget_3.insert('1.29', rapport, 'Class')
        elif rapport == 'Text':
            text_widget_3.tag_config("Class", foreground = "#EB1DB6")
            text_widget_3.insert('1.23', 'Class : ')
            text_widget_3.insert('1.29', rapport, 'Class')
        elif rapport == 'Uncertainty':
            text_widget_3.tag_config("Class", foreground = "red")
            text_widget_3.insert('1.23', 'Class : ')
            text_widget_3.insert('1.29', rapport, 'Class')
        elif rapport == 'Reasoning':
            text_widget_3.tag_config("Class", foreground = "#7020A6")
            text_widget_3.insert('1.23', 'Class : ')
            text_widget_3.insert('1.29', rapport, 'Class')
        else:
            text_widget_3.tag_config("Class", foreground = "black")
            text_widget_3.insert('1.23', 'Class : ')
            text_widget_3.insert('1.29', rapport, 'Class')
        text_widget_3.configure(state = 'disable')
        prediction_du_model.configure(state = "disable")
        progress.configure(progress_color = "#672DF2")
        progress.set(20)
        progress.stop()
        
    champ_rapport.configure(state = "disable")

def invite_GPM():
    global texte_temp
    global press_button
    global bascule
    press_button = "def"
    texte_temp = ""
    if mode_model_2.get() == "GPM completion" or mode_model_2.get() == 'Chat' :
        bascule = 0
    if mode_model_2.get() == "GPM correction" or mode_model_2.get() == "live correction":
        bascule = 1
    if bascule_swiche_recur == 0:
        recursivite = False
    else:
        recursivite  = True
    prediction_du_model.configure(state = "normal")
    maximum_length_model = maximum_length.get()
    maximum_length_model = int(maximum_length_model)
    maximum_comprehension_para = maximum_comprehension.get()
    mode_model_para = mode_model.get()
    if mode_model_para == "Passive":
        add_space.set("Automatic space") 
    add_space_para = add_space.get()
    if add_space_para == "Automatic space":
        add_space_para = True
    else:
        add_space_para = False
    reaction = bascule
    long_memory = 'LONG'
    long_memory_large = ""
    retroaction = 0
    recompence = 1
    temperature_para = temperature.get()
    if recursivite == True:
        taille = 1
    else:
        taille = maximum_length_model
    temp = None
    for i in range(taille):
        progress.start()
        progress.configure(progress_color = "#F27085")
        if enable_completion == True:
            text_widget.insert(customtkinter.END, "\n bot : ")
        final_prompt =  text_widget.get("1.0", customtkinter.END)
        text_training = text_widget_2.get("1.0", customtkinter.END)
        if bascule_swiche == 0:
            tot = False
        else:
            tot = True
        configure_GPM = {   "prompt": "",
                        "temperature" : 0.3,
                        "maximum lenght" : 1,
                        "reaction" : 0,
                        "retroaction" : 1,
                        "reward" : 1,
                        "Level C" : 70.0,
                        "space" : "True",
                        "training_on_context" : "False",
                        "text_add" : "False",
                        "correction" : "",
                        "recursion" : 0,
                        "RL" : False
                        
                        

                    }
        configure_GPM["prompt"] = final_prompt
        configure_GPM["Level C"] = maximum_comprehension_para
        configure_GPM["training_on_context"] = tot
        configure_GPM["temperature"] = temperature_para
        configure_GPM["text_add"] = text_training
        configure_GPM["space"] = add_space_para
        configure_GPM["maximum lenght"] = maximum_length_model
        configure_GPM["reaction"] = reaction
        configure_GPM["reward"] = recompence
        configure_GPM["recursivite"] = recursivite
        configure_GPM["EngineState"] = bascule_engine_state
        configure_GPM["fenetre_context"] = int(fenetre_contexte.get())

        
        
        #text_widget.insert(customtkinter.END, ' ' + prompt.get(1.0, customtkinter.END))
        with open(rf"{chemin_parent}\config\configure_model.json", 'w') as file:
            json.dump(configure_GPM, file, indent=4)
            file.close()
        
        output =  GPM4_Head(configure_GPM)
        #affiche_resultat(output)
        if mode_model_2.get() != "live correction":
            affiche_resultat(output)
        else:
            correction_de_saisie(output, text_widget, champ_rapport)
        try:
            if output["Sequence retained"] == "." or output["Sequence retained"] == " ." or stop_calling == True:
                break
        except:
            pass
        prompt.delete(1.0, customtkinter.END)
def on_key_release(event):
    prediction_du_model.see(customtkinter.END)
    prediction_du_model.configure(state = "disable")
    progress.start()
    progress.configure(progress_color = "#F27085")
    thread = Thread(target=lambda: affiche_resultat(invite_GPM()))
    thread.start()

window = customtkinter.CTk()

longeur_fenetre = "1179"
largeur_fenetre = "660"
window.geometry(f"{longeur_fenetre}x{largeur_fenetre}")
window.title("GPM4")
canvas = customtkinter.CTkCanvas(window, bd=0, highlightthickness=0)
canvas.configure(background=window.cget("background") )
frame_scrollable = customtkinter.CTkFrame(canvas, fg_color='transparent')

frame_glm = customtkinter.CTkFrame(frame_scrollable,fg_color='transparent')
frame_glm.pack(side="top")
if theme == 'light':
    image = Image.open(rf'{chemin_parent}\interface\images\GPM_dark_2.png')
else:
    image = Image.open(rf'{chemin_parent}\interface\images\GPM_2_vierge.png')
image.thumbnail((160, 160), Image.Resampling.LANCZOS)
photo = ImageTk.PhotoImage(image)
label_image = customtkinter.CTkLabel(frame_glm, image=photo, text = '  Foundation model and copilot', compound='left', text_color='blue', font=("arial", 9, 'italic'))
label_image.grid(row=1, column=1, pady = 5)
label_image_text = customtkinter.CTkLabel(frame_glm, text = ' ' *260)
label_image_text.grid(row=1, column=2)


frame_master = customtkinter.CTkFrame(frame_scrollable,fg_color='transparent')
frame_master.pack(expand= True)

frame_option_2 = customtkinter.CTkFrame(frame_master,fg_color='transparent')
frame_option_2.grid(row=1, column=1, padx = 10)


tabview = customtkinter.CTkTabview(frame_option_2, width=20, height=220)
tabview.grid(row=1, column = 1, pady=10)
tabview.add("Reasoning")
tabview.tab("Reasoning").grid_columnconfigure(0, weight=1)
tabview.add("RLHF")
tabview.tab("RLHF").grid_columnconfigure(0, weight=1)

champ_rapport =  customtkinter.CTkTextbox(tabview.tab("Reasoning"), width=250, height=230, fg_color='transparent', border_width=2, wrap=customtkinter.WORD,insertwidth=8 , font=("courier", 12, 'italic'))
champ_rapport.grid(row=1, column = 1, pady=5)

def search_occurences():
    dialog_box = customtkinter.CTkInputDialog(title="search occurence", text = "Saisissez le mot recherché ")
    mot = dialog_box.get_input()
    

    def rechercher_occurrences():
        # Efface toutes les balises de mise en surbrillance précédentes
        champ_rapport.tag_remove("highlight", "1.0", customtkinter.END)

        texte = champ_rapport.get("1.0", "end-1c")  # Obtient le texte du widget texte
        mot_a_rechercher = mot  # Obtient le mot à rechercher
        occurrences = []

        # Recherche toutes les occurrences du mot dans le texte
        index = 1.0
        if mot.__len__() != 0:
            while True:
                index = champ_rapport.search(mot_a_rechercher, index, stopindex=customtkinter.END)
                if not index:
                    break
                occurrences.append(index)
                index = champ_rapport.index(f"{index}+{len(mot_a_rechercher)}c")

            # Met en surbrillance les occurrences trouvées
            for index in occurrences:
                champ_rapport.tag_add("highlight", index, f"{index}+{len(mot_a_rechercher)}c")
            champ_rapport.tag_config("highlight", background="yellow")
    rechercher_occurrences()
    
         

button_search = customtkinter.CTkButton(tabview.tab("Reasoning"), text="Search", command = search_occurences, width=10, fg_color='gray')
button_search.grid(row = 2, column = 1, pady = 5)


prediction_du_model = customtkinter.CTkTextbox(tabview.tab("Reasoning"), width=250, height=170, wrap=customtkinter.WORD,insertwidth=8, font=("courier", 12, 'italic'), corner_radius= 0, border_width=2, fg_color='transparent')
prediction_du_model.grid(row=3, column = 1, pady=10)
enable_completion = False
bascule_save_pref = data_settings["Auto preference"]
def settings():
    window_settings = customtkinter.CTkToplevel(window)
    window_settings.title("Settings")
    window_settings.geometry("580x340")
    #window_settings.resizable(False, False)
    
    frame_settings = customtkinter.CTkFrame(master=window_settings)
    frame_settings.pack(expand = True, side = 'left')
    
    frame_image = customtkinter.CTkFrame(master=window_settings, fg_color='transparent')
    frame_image.pack(expand = True, side = 'right')
    
    image_info = Image.open(rf"{chemin_parent}\interface\images\st.png")
    image_info.thumbnail((120, 120), Image.Resampling.LANCZOS)
    photo_info = ImageTk.PhotoImage(image_info)
    
    label_img = customtkinter.CTkLabel(frame_image, text="", image=photo_info)
    label_img.pack()
    basc = data_settings["Auto Role"]
    
    
    
    def auto_save():
        with open(rf"{chemin_parent}\config\configuration.json") as file:
            data_settings = json.load(file)
            file.close()
        global bascule_save_pref
        if bascule_save_pref == False:
            bascule_save_pref = True
        else:
            bascule_save_pref = False
        data_settings["Auto preference"] = bascule_save_pref

    def enable_def():
        global enable_completion
        nonlocal basc
        if basc == False:
            basc = True
            role1.configure(state = "normal")
            role1.set("human")
            role2.configure(state = "normal")
            role2.set("bot")
            enable_completion = True
            data_settings["Auto Role"] = True
            role1.configure(state = "normal")
            role2.configure(state = "normal")
        else:
            basc = False
            enable_completion = False
            data_settings["Auto Role"] = False
            role1.configure(state = "disable")
            role2.configure(state = "disable")
    
    enable_comp = customtkinter.CTkSwitch(frame_settings, text="Auto completion de role", command=enable_def, )
    enable_comp.grid(row=0, column=0)
    role1 = customtkinter.CTkComboBox(frame_settings, values= ["human"], state="disable")
    role1.grid(row = 1, column = 0, pady = 10)
    role2 = customtkinter.CTkComboBox(frame_settings, values= ["bot"], state="disable")
    role2.grid(row = 2, column = 0, pady = 10)
    if data_settings["Auto Role"] == True:    
        enable_comp.select()
        role1.configure(state = "normal", values = ["human"])
        role2.configure(state = "normal", values= ["bot"])
    else:
        enable_comp.deselect()
        role1.configure(state = "disable")
        role2.configure(state = "disable")
        
    
    enable_auta_save = customtkinter.CTkSwitch(frame_settings, text="Enregistrer les preferences ", command=auto_save )
    enable_auta_save.grid(row=3, column=0, pady = 10)
    if bascule_save_pref == True:
        enable_auta_save.select()
    else:
        enable_auta_save.deselect()
    def close_win():
        window_settings.destroy()
    save_settings = customtkinter.CTkButton(frame_settings, text="Sauvegarder", command=close_win, height=30, corner_radius=20)
    save_settings.grid(row = 4, column = 0)
    window_settings.mainloop()

photo_settings = Image.open(rf"{chemin_parent}\interface\images\icons8_settings_32.png")
photo_settings.thumbnail((26, 26), Image.Resampling.LANCZOS)
my_image = ImageTk.PhotoImage(photo_settings)
buton_settings = customtkinter.CTkButton(tabview.tab("Reasoning"), text = "        ", command=settings, width=10, fg_color="transparent", bg_color="transparent", hover_color = "pink")
buton_settings.grid(row=4, column=1)
label_settings = customtkinter.CTkLabel(tabview.tab("Reasoning"), image=my_image, text="")
label_settings.grid(row=4, column=1)

def swiche_def_recur():
    global bascule_swiche_recur
    if bascule_swiche_recur == 0:
        bascule_swiche_recur = 1
    else:
        bascule_swiche_recur = 0
def swiche_def_engine():
    global bascule_engine_state
    if bascule_engine_state == True:
        bascule_engine_state = False
    else:
        bascule_engine_state = True
champ_rapport_simule =  customtkinter.CTkTextbox(tabview.tab("RLHF"), width=190, height=200, fg_color='transparent', border_width=2, wrap=customtkinter.WORD,insertwidth=8 , font=("courier", 12, 'italic'))
champ_rapport_simule.grid(row=0, column = 1, pady=10)
swicher_recursivite = customtkinter.CTkSwitch(tabview.tab("RLHF"), text="recursivite du model", command=swiche_def_recur)
swicher_recursivite.grid(row=1, column=1, pady=5, padx = 3)
swicher_engine = customtkinter.CTkSwitch(tabview.tab("RLHF"), text="        light prediction", command=swiche_def_engine)
swicher_engine.grid(row=2, column=1, pady=5, padx = 3)

frame_option = customtkinter.CTkFrame(frame_master,fg_color='transparent')
frame_option.grid(row=1, column=3, padx=10)
frame_maximum_lenght = customtkinter.CTkFrame(frame_option, corner_radius=0, fg_color='transparent')
frame_maximum_lenght.grid(row = 3, column = 1)
mode_model = customtkinter.CTkComboBox(frame_maximum_lenght, values=['Copilot trace', "Passive"], width=176, bg_color='transparent', border_width=1)
mode_model.grid(row=0, column = 1, pady = 10)
mode_model.set("Passive")

def change_mode(self):
    if mode_model_2.get() == 'Chat':
        text_widget.configure(height=280)
        frame_prompt.grid(row = 1, column = 1, pady = 5)
    else:
        text_widget.configure(height=350)
        frame_prompt.grid_forget()

mode_model_2 = customtkinter.CTkOptionMenu(frame_maximum_lenght, values=['GPM completion', "GPM correction", "live correction", "Chat"], width=176, bg_color='transparent', command = change_mode)
mode_model_2.grid(row=1, column = 1, pady = 10)
add_space = customtkinter.CTkComboBox(frame_maximum_lenght, values=['Automatic space', "Manuel space"], width=176, bg_color='transparent', border_width = 1)
add_space.grid(row=2, column = 1, pady = 10)


    
def max_length(value):
    global max_word
    value = int(value)
    max_word = value
    maximum_length_select.configure(text=str(value))

maximum_length_label = customtkinter.CTkLabel(frame_maximum_lenght, text = "Maximum_length" + " "*15 , corner_radius=20, fg_color='transparent')
maximum_length_label.grid(row=3, column = 1)
maximum_length_select = customtkinter.CTkLabel(frame_maximum_lenght, text = "1" , corner_radius=40, fg_color='transparent',bg_color='gray')
maximum_length_select.grid(row=4, column = 2)
maximum_length = customtkinter.CTkSlider(frame_maximum_lenght, to=99, command=max_length, width=166, height=16, progress_color="blue")
maximum_length.grid(row=4, column = 1, pady = 10)
maximum_length.set(1)

def max_comp(value):
    global max_word
    value = int(value)
    max_word = value
    maximum_comp_label.configure(text=str(value))
    
maximum_comp_label = customtkinter.CTkLabel(frame_maximum_lenght, text = "Level C" + " "*35 , corner_radius=20, fg_color='transparent')
maximum_comp_label.grid(row=5, column = 1, pady = 0)
maximum_comp_label = customtkinter.CTkLabel(frame_maximum_lenght, text = "70" , corner_radius=20, fg_color='transparent',bg_color='gray')
maximum_comp_label.grid(row=6, column = 2)
maximum_comprehension = customtkinter.CTkSlider(frame_maximum_lenght, to=99, command=max_comp, width=166, height=16, progress_color="blue")
maximum_comprehension.grid(row=6, column = 1, pady = 15)

temperature_label = customtkinter.CTkLabel(frame_maximum_lenght, text = "temperature" + " "*25 , corner_radius=20, fg_color='transparent')
temperature_label.grid(row=7, column = 1, pady = 0)

def max_temp(value):
    global max_word
    value = round(value, 1)
    max_word = value
    temperature_label_show.configure(text=str(value))
temperature_label_show = customtkinter.CTkLabel(frame_maximum_lenght, text = "0.3" , corner_radius=20, fg_color='transparent',bg_color='gray')
temperature_label_show.grid(row=8, column = 2, pady = 0)
temperature = customtkinter.CTkSlider(frame_maximum_lenght, command=max_temp, width=166, height=16, progress_color="blue")
temperature.grid(row=8, column = 1, pady = 15, rowspan=1)
temperature.set(0.3)
maximum_comprehension.set(70)


def fenetre_cont(value):
    value = int(value)
    fenetre_label_show.configure(text=str(value))

fenetre_label_show = customtkinter.CTkLabel(frame_maximum_lenght, text = "10" , corner_radius=20, fg_color='transparent' ,bg_color='gray')
fenetre_label_show.grid(row=10, column = 2, pady = 0)
fenetre_contexte = customtkinter.CTkSlider(frame_maximum_lenght, command=fenetre_cont, width=166, height=16, progress_color="blue", to=200)
fenetre_contexte.grid(row=10, column = 1, pady = 15, rowspan=1)
fenetre_contexte.set(10)
  
def new_command():
    text_widget.tag_config('color_ig', foreground = 'red')
    text_widget.insert(customtkinter.END, " <ignore> ", "color_ig")  
    text_widget.focus_set()

button_add_trans = customtkinter.CTkButton(frame_maximum_lenght, text='Add', command=new_command, width=5, border_width=0, fg_color='#91BFBB', corner_radius=20, text_color='black')
button_add_trans.grid(row = 12, column = 1, pady = 10)
press_button = "def"

def action():
    global press_button
    if press_button == "def":
        add_space.set("Automatic space") 
    global texte_temp
    global nb_action_2
    global nb_action
    nb_action_2 = 0
    nb_action = 0
    texte_temp = ""
    on_key_release("self")
    
def reset_check_box():
    global stop_calling
    button_stop.deselect()
    stop_calling = False
    
def stop_generating():
    global stop_calling
    stop_calling = True
    window.after(2000, reset_check_box)
button_stop = customtkinter.CTkCheckBox(frame_maximum_lenght, text='stop', command=stop_generating)
button_stop.grid(row = 11, column = 1, columnspan = 3, pady=5)

def regenerate():
    global press_button
    global texte_temp
    
    texte = text_widget.get("1.0", customtkinter.END)
    if texte_temp != "":
        press_button = True
        add_space.set("Manuel space")
        text_widget.delete("1.0","end")
        texte = texte.replace(texte_temp.rstrip("\n"), "")
        text_widget.insert("end", texte.rstrip("\n"))
        texte_temp = ""
        action()



frame_of_buttons = customtkinter.CTkFrame(frame_maximum_lenght,fg_color='transparent')
frame_of_buttons.grid(row = 13, column = 1)


button = customtkinter.CTkButton(frame_of_buttons, text=' Submit ', command=action, width=10, corner_radius=5)
button.grid(row = 1, column = 1, padx = 10)
button_ragenerate = customtkinter.CTkButton(frame_of_buttons, text=' Regenerate ', command=regenerate, width=10, corner_radius=5, fg_color="pink", text_color="black")
button_ragenerate.grid(row = 1, column = 2)

indice_mode = 1
nb_action = 0
nb_action_2 = 0
def on_key_press(events):
    global indice_mode
    global nb_action_2
    global nb_action
    if mode_model.get() == "Copilot trace":
        indice_mode = 1
    else:
        indice_mode = 0
    if events.keysym == "Left" and nb_action == 0:
        text  = text_widget.get("1.0", customtkinter.END)
        text = text.split()
        g_text = text[len(text)-1]
        g_text = len(texte_temp)
        index_text = text_widget.index("insert")
        last_index = index_text[:-1] + str(int(index_text[-1]))
        last_index = list(last_index)
        index_debut = last_index[0]
        index_fin = last_index[2:]
        temp = ""
        for i in index_fin:
            temp += i
        index_fin = temp
        delete_index = int(index_fin) - g_text
        delete_index = str(index_debut) + "." + str(delete_index)
            
        
        new_text = ""
        nb_action += 1
        nb_action_2 += 1
        for mot in text:
            new_text += mot +" "
        text_widget.delete(delete_index, customtkinter.END)
    elif events.keysym == "Right" and nb_action_2 == 0:
        text  = text_widget.get("1.0", customtkinter.END)
        text_widget.delete("1.0", customtkinter.END)
        text_widget.insert(customtkinter.END, text.rstrip("\n") )
        nb_action_2 += 1
        nb_action += 1
#window.bind("<KeyPress>", on_key_press)

# Créer le widget texte

frame_widget = customtkinter.CTkFrame(frame_master, fg_color='transparent')
frame_widget.grid(row=1, column = 2, padx = 10)
text_widget = customtkinter.CTkTextbox(frame_widget, width=600, height=350, fg_color='transparent', border_width=2, wrap=customtkinter.WORD,insertwidth=8 , corner_radius=0, font=("courier", 12, 'italic'))
text_widget.grid(row=0, column = 1, padx = 10, pady = 5)

frame_prompt = customtkinter.CTkFrame(frame_widget, fg_color='transparent')
frame_prompt.grid(row = 1, column = 1, pady = 5)

prompt_label = customtkinter.CTkLabel(frame_prompt, text='Prompt   ')
prompt_label.grid(row = 0, column = 0, pady = 20)

taille_ajustable = 30
prompt = customtkinter.CTkTextbox(frame_prompt, width=500, height= taille_ajustable, corner_radius=5, fg_color='transparent', border_width=1)
prompt.grid(row = 0, column = 1, pady = 20)

def on_get(event):
    prompt.configure(border_color='blue', border_width = 2)
def out_get(event):
    global taille_ajustable
    taille_ajustable = 30
    prompt.configure(border_color='#969696', border_width = 1, height = taille_ajustable)
prompt.bind("<FocusIn>", on_get)
prompt.bind("<FocusOut>", out_get)

def resize_w(event):
    global taille_ajustable
    if taille_ajustable < 80:
        taille_ajustable += 10
    prompt.configure(height = taille_ajustable )
prompt.bind('<Return>', resize_w)

frame_prompt.grid_forget()

if autoSave:
    text_widget.insert(customtkinter.END, data_settings['text'])
separateur = ""

def swiche_def():
    
    global bascule_swiche
    bascule_swiche = data_settings['live t']

    if bascule_swiche == False:
        bascule_swiche = True
    else:
        bascule_swiche = False
    data_settings['live t'] = bascule_swiche
        
    if bascule_swiche == False :
        bascule_swiche = 0
    else : 
        bascule_swiche = 1
    
def load_instructGPM(self):
    text_widget_2.delete("1.0", customtkinter.END)
    comp = 0
    personalised_instruct = False
    if buton_load.get() == "load ChatGPM":
        with open(rf"{chemin_parent}\InstructGPM\Data_of_instruct.json", "r") as f:
            dataGPM = json.load(f)
            f.close()
            
    elif buton_load.get() == "load MedGPM":
        with open(rf"{chemin_parent}\trainset_MedGPM.json", "r") as f:
            dataGPM = json.load(f)
            f.close()

    else:
        with open(rf"{chemin_parent}\config\configuration.json") as file:
            dataGPM = json.load(file)
            file.close()
            text_widget_2.delete(1.0, customtkinter.END)
            personalised_instruct = True
    if not personalised_instruct:
        for i in dataGPM:
                comp += 1
                if comp == 2222   :
                    break
                text_widget_2.insert(customtkinter.END, "human : " + i['human'] + "\n")
                text_widget_2.insert(customtkinter.END, "bot : " +  i['bot'] + "\n")
    else:
        text_widget_2.insert(customtkinter.END, str("human : .... \nbot : ...") + "\n\n")
        text_widget_2.tag_add('sel', '1.0', customtkinter.END)
        text_widget_2.tag_config('sel', background='gray')
        text_widget_2.focus_set()
    text_widget_2.insert(customtkinter.END, "ENDGPM@")
    progress.configure(progress_color = "#672DF2")
    progress.set(20)
    progress.stop()

    data_settings["data instruct"] = text_widget_2.get("1.0", customtkinter.END)
    data_settings["instruct"] = buton_load.get()



            
def thread_instructGPM():
    progress.start()
    progress.configure(progress_color = "#F27085")
    thread_2 = Thread(target=lambda: load_instructGPM())
    thread_2.start()
frame_manipulation_model = customtkinter.CTkFrame(frame_widget, fg_color="transparent")
frame_manipulation_model.grid(row=3, column=1, pady=5)
swicher = customtkinter.CTkSwitch(frame_manipulation_model, text="live training", command=swiche_def)
swicher.grid(row=1, column=1, pady=5, padx = 3)
photo_load = Image.open(rf"{chemin_parent}\interface\images\load.png")
photo_load.thumbnail((35, 35), Image.Resampling.LANCZOS)
my_image = ImageTk.PhotoImage(photo_load)
label_load = customtkinter.CTkLabel(frame_manipulation_model, image=my_image, text="")
label_load.grid(row=1, column=2, pady=5, padx=3)
buton_load = customtkinter.CTkOptionMenu(frame_manipulation_model, values=["","load ChatGPM", "load MedGPM", "personalized"], fg_color="gray", command=load_instructGPM)
buton_load.grid(row=1, column=3, padx = 5)


def on_get_2(event):
    text_widget_2.configure(border_color='green')
    text_widget_2.configure(width = 600, height=120)
    text_widget.configure(width = 600, height=310)
def out_get_2(event):
    text_widget_2.configure(border_color="#969696")
    text_widget_2.configure(width = 600, height=20)


text_widget_2 = customtkinter.CTkTextbox(frame_widget, width=600, height=20, fg_color='transparent', border_width=2, wrap=customtkinter.WORD,insertwidth=2 , corner_radius=0, font=("courier", 12, 'italic'))
text_widget_2.grid(row=2, column = 1, padx = 10, pady=5)

text_widget_3 = customtkinter.CTkTextbox(frame_widget, width=600, height=20, fg_color='transparent', border_width=1, wrap=customtkinter.WORD,insertwidth=8 , corner_radius=0, font=("courier", 12, 'italic'))
text_widget_3.grid(row=5, column = 1, padx = 10, pady=5)

taille = len(word_tokenize(text_widget.get('1.0', customtkinter.END)))
text_widget_3.tag_config("len_texte", foreground = "blue")
text_widget_3.insert('1.0', 'Token(s) : ')
text_widget_3.insert('1.14', str(taille) + "   ", 'len_texte')


text_widget_3.tag_config("Class", foreground = "black")
text_widget_3.insert('1.23', 'Class : ')
text_widget_3.insert('1.29', 'None', 'Class')
text_widget_3.configure(state = 'disable')

progress = customtkinter.CTkProgressBar(frame_widget, orientation=customtkinter.HORIZONTAL, width=600, determinate_speed=5, corner_radius=0, height=3, progress_color= "blue")
text_widget_2.bind("<FocusIn>", on_get_2)
text_widget_2.bind("<FocusOut>", out_get_2)
progress.grid(row=4, column = 1)
progress.set(0)



if data_settings["Auto preference"] == True:
    text_widget_2.insert(customtkinter.END, data_settings['data instruct'])
    buton_load.set(data_settings['instruct'])
    
    if data_settings['live t'] == True:
        swicher.select()
        bascule_swiche = 1
        
    else:
        swicher.deselect()


def on_get(event):
    if mode_model_2.get() != 'Chat':
        text_widget.configure(border_color='blue', height=400)
        text_widget_2.configure(width = 600, height=20)
def out_get(event):
    text_widget.configure(border_color='#969696')
text_widget.bind("<FocusIn>", on_get)
text_widget.bind("<FocusOut>", out_get)


# Initialiser la variable de complétion
completion_done = False

# Associer l'événement de relâchement de touche à la fonction on_key_release
text_widget.see(customtkinter.END)
def action_on_space(event):
    global nb_action_2
    global nb_action
    beta = mode_model.get()
    
    def rapp():
        text_widget_3.configure(state = 'normal')
        text_widget_3.delete(1.0, customtkinter.END)
        taille = len(word_tokenize(text_widget.get('1.0', customtkinter.END)))
        text_widget_3.tag_config("len_texte", foreground = "blue")
        text_widget_3.insert('1.0', 'Token(s) : ')
        text_widget_3.insert('1.14', str(taille) + "   " , 'len_texte')
        
        if rapport == 'Logic Math':
            text_widget_3.tag_config("Class", foreground = "green")
            text_widget_3.insert('1.23', 'Class : ')
            text_widget_3.insert('1.29', rapport, 'Class')
        elif rapport == 'Text':
            text_widget_3.tag_config("Class", foreground = "#EB1DB6")
            text_widget_3.insert('1.23', 'Class : ')
            text_widget_3.insert('1.29', rapport, 'Class')
        if rapport == 'Reasoning':
            text_widget_3.tag_config("Class", foreground = "#45521D")
            text_widget_3.insert('1.23', 'Class : ')
            text_widget_3.insert('1.29', rapport, 'Class')
        else:
            text_widget_3.tag_config("Class", foreground = "black")
            text_widget_3.insert('1.23', 'Class : ')
            text_widget_3.insert('1.29', rapport, 'Class')
        text_widget_3.configure(state = 'disable')
    rapp()
    if beta == "Copilot trace":
        nb_action = 0
        nb_action_2 = 0
        if mode_model.get() == "Copilot trace":
            add_space.set("Manuel space")
        else:
            add_space.set("Automatic space")
        on_key_release("self")
text_widget.bind("<space>", action_on_space)
def on_backspace(event):
        text_widget_3.configure(state = 'normal')
        text_widget_3.delete(1.0, customtkinter.END)
        taille = len(word_tokenize(text_widget.get('1.0', customtkinter.END)))
        text_widget_3.tag_config("len_texte", foreground = "blue")
        text_widget_3.insert('1.0', 'Token(s) : ')
        text_widget_3.insert('1.14', str(taille) + "   " , 'len_texte')
        
        if rapport == 'Logic Math':
            text_widget_3.tag_config("Class", foreground = "green")
            text_widget_3.insert('1.23', 'Class : ')
            text_widget_3.insert('1.29', rapport, 'Class')
        elif rapport == 'Text':
            text_widget_3.tag_config("Class", foreground = "#EB1DB6")
            text_widget_3.insert('1.23', 'Class : ')
            text_widget_3.insert('1.29', rapport, 'Class')
        elif rapport == 'Reasoning':
            text_widget_3.tag_config("Class", foreground = "#45521D")
            text_widget_3.insert('1.23', 'Class : ')
            text_widget_3.insert('1.29', rapport, 'Class')
        else:
            text_widget_3.tag_config("Class", foreground = "black")
            text_widget_3.insert('1.23', 'Class : ')
            text_widget_3.insert('1.29', rapport, 'Class')
        text_widget_3.configure(state = 'disable')
            
text_widget.bind("<BackSpace>", on_backspace)

scroll = customtkinter.CTkScrollbar(window, orientation='vertical', command=canvas.yview)
scroll.pack(side = 'right', fill='y')
canvas.configure(yscrollcommand=scroll.set)
canvas.pack(expand=True, fill='both')
canvas.bind_all("<MouseWheel>", lambda event: canvas.yview_scroll(int(-1 *(event.delta / 120)), "units"))
frame_scrollable.bind("<Configure>", lambda event: canvas.configure(scrollregion=canvas.bbox("all")))
canvas.create_window((0,0), window=frame_scrollable,anchor='nw' )

def colorize_prompt(event):
    text_widget.tag_remove("prompt", customtkinter.END)
    start_index = "1.0"
    while True:
        start_index = text_widget.search("<prompt>", start_index, customtkinter.END)
        if not start_index:
            break
        end_index = f"{start_index}+{len('<prompt>')}c"
        text_widget.tag_add("prompt", start_index, end_index)
        text_widget.tag_config("prompt", foreground = "green")
        start_index = end_index

def colorize_end(event):
    text_widget.tag_remove("end", customtkinter.END)
    start_index = "1.0"
    while True:
        start_index = text_widget.search("<end>", start_index, customtkinter.END)
        if not start_index:
            break
        end_index = f"{start_index}+{len('<end>')}c"
        text_widget.tag_add("end", start_index, end_index)
        text_widget.tag_config("end", foreground = "blue")
        start_index = end_index

text_widget.bind("<KeyRelease>", colorize_prompt)
text_widget.bind("<KeyRelease>", colorize_end)


def on_resize(event):
    width = event.width  # Nouvelle largeur de la fenêtre
    height = event.height  # Nouvelle hauteur de la fenêtre
    x = event.x  # Nouvelle position X de la fenêtre
    y = event.y  # Nouvelle position Y de la fenêtre

    # Insérez ici le code pour réagir aux changements de taille ou de position
    print(f"Largeur: {width}, Hauteur: {height}, Position X: {x}, Position Y: {y}")
    
    if width == 1350:
        text_widget.configure(width = 750 )
        text_widget_2.configure(width = 750 )
        champ_rapport.configure(width = 300 )
        prediction_du_model.configure(width = 300 )
        
    elif width == int(longeur_fenetre):
        text_widget.configure(width = 600 )
        text_widget_2.configure(width = 600 )
        champ_rapport.configure(width = 250 )
        prediction_du_model.configure(width = 250 )
    elif width == 681:
        text_widget.configure(width = 500 )
        text_widget_2.configure(width = 500 )
        champ_rapport.configure(width = 150 )
        prediction_du_model.configure(width = 150 )
        frame_option_2.grid_forget()
#window.bind('<Configure>', on_resize)
# Lancer la boucle principale de la fenêtre

if autoSave:
    mode_model_2.set(data_settings['mode model'])
    mode_model.set(data_settings['mode int'])
    add_space.set(data_settings['space'])
    temp = round(data_settings['level c'], 1)
    maximum_comprehension.set(temp)
    maximum_comp_label.configure(text = str(temp))
    temperature.set(data_settings['temperature'])
    temp = round(data_settings['temperature'], 1)
    temperature_label_show.configure(text = str(temp))
    maximum_length.set(int(data_settings['ml']))
    temp = int(data_settings['ml'])
    maximum_length_select.configure(text = str(temp))
    fenetre_contexte.set(int(data_settings['fenetre context']))
    fenetre_label_show.configure(text = str(data_settings['fenetre context']))
    
    
def save_data_on_exit():
    data_settings['text'] = text_widget.get('1.0', customtkinter.END)
    data_settings['mode model'] = mode_model_2.get()
    data_settings['mode int'] = mode_model.get()  
    data_settings['space'] = add_space.get()
    data_settings['level c'] = maximum_comprehension.get()
    data_settings['temperature'] = temperature.get()  
    data_settings['ml'] = maximum_length.get()
    data_settings["data instruct"] = text_widget_2.get("1.0", customtkinter.END)
    data_settings["instruct"] = buton_load.get()
    data_settings["fenetre context"] = int(fenetre_contexte.get())

    


    
    with open(rf"{chemin_parent}\config\configuration.json", 'w') as file:
        json.dump(data_settings, file,  indent=2 )
        file.close()
        print("Enregistrement des données avant la fermeture")
        window.quit()

window.protocol("WM_DELETE_WINDOW", save_data_on_exit)


window.mainloop()
