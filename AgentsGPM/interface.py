import customtkinter
from PIL import Image, ImageTk
from tkinter import*
import tkinter as tk
import sys
import os
chemin_parent = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(chemin_parent)
import customtkinter
import time
import json
import random
from PIL import Image, ImageTk
from random import randint
from threading import Thread
from model.Head_Of_Model.GPM4 import GPM4_Head
from Reward_Model import Fonction_Optimisation
from Training_GPM import TeDS_Training
import multiprocessing


response = None
rwp = 0
rwn = 0
recur = 0
texte = """
human : Quelle est la capitale de la France ?
bot : La capitale de la France est Paris.
human : Quel est le plus grand océan du monde ?
bot : Le plus grand océan du monde est l'océan Pacifique.
human : Peux-tu m'expliquer la théorie de la relativité restreinte ?
bot : La théorie de la relativité restreinte, développée par Albert Einstein, décrit les propriétés cinématiques et dynamiques des objets qui se déplacent à des vitesses proches de celle de la lumière.
human : Quelle est la formule chimique de l'eau ?
bot : La formule chimique de l'eau est H2O.
human : Je ne comprends pas cette explication, peux-tu l'exprimer autrement ?
bot : Bien sûr, laisse-moi essayer de reformuler cela. La théorie de la relativité restreinte est un cadre scientifique qui nous permet de comprendre comment les objets se déplacent à des vitesses proches de celle de la lumière. Cela a des implications importantes dans notre compréhension de l'espace, du temps et de la gravité.
human : Qu'est-ce que la photosynthèse ?
bot : La photosynthèse est le processus par lequel les plantes et certaines autres organismes utilisent la lumière du soleil pour convertir le dioxyde de carbone et l'eau en glucose et en oxygène.
human : Wow, c'est fascinant !
bot : Je suis content que tu trouves cela fascinant ! La photosynthèse est en effet un processus incroyable qui permet aux plantes de produire de l'énergie et de libérer de l'oxygène dans l'atmosphère.
human : Je ne suis pas sûr de comprendre. Peux-tu expliquer différemment ?
bot : Absolument ! La photosynthèse est essentiellement un processus par lequel les plantes utilisent la lumière du soleil pour créer leur propre nourriture en convertissant l'énergie lumineuse en énergie chimique.
human : Qu'est-ce que le génie logiciel ?
bot : Le génie logiciel est une discipline qui concerne la conception, le développement et la maintenance de logiciels de qualité. Il englobe des activités telles que l'analyse des besoins, la conception de l'architecture logicielle, la programmation, les tests et la gestion de projet.
human : Quels sont les principes du génie logiciel ?
bot : Les principes du génie logiciel incluent la modularité, l'abstraction, la réutilisabilité, la simplicité, la vérifiabilité et la maintenabilité. Ces principes aident à créer des logiciels bien structurés, faciles à comprendre, à tester et à maintenir.
human : Quelles sont les étapes du cycle de vie du développement logiciel ?
bot : Les étapes du cycle de vie du développement logiciel comprennent l'analyse des besoins, la conception, la programmation, les tests, le déploiement et la maintenance. Chaque étape est importante pour assurer le développement réussi d'un logiciel.
human : Je ne comprends pas comment fonctionne la réutilisabilité dans le génie logiciel. Peux-tu expliquer davantage ?
bot : Bien sûr ! La réutilisabilité dans le génie logiciel fait référence à la capacité de réutiliser des composants logiciels existants dans de nouveaux projets. Cela permet d'économiser du temps et des ressources en évitant de recréer des fonctionnalités déjà développées. La réutilisabilité peut être réalisée par le biais de bibliothèques de code, de frameworks ou de composants modulaires.
human : Quels sont les outils couramment utilisés dans le génie logiciel ?
bot : Dans le génie logiciel, on utilise souvent des outils tels que des environnements de développement intégrés (EDI) tels que Visual Studio, des systèmes de contrôle de version comme Git, des outils de gestion de projets tels que JIRA, et des outils de test comme Selenium.
human : Le concept de modularité est-il important en génie logiciel ?
bot : Oui, la modularité est un concept clé en génie logiciel. Il consiste à diviser un système logiciel en modules autonomes et interconnectés. Cela facilite la compréhension, la maintenance et la modification du logiciel, et favorise également la réutilisabilité des modules dans d'autres projets.
human : Je suis passionné par le génie logiciel, c'est tellement fascinant !
bot : Je suis ravi que tu trouves le génie logiciel fascinant ! C'est en effet un domaine passionnant qui joue un rôle essentiel dans la création de logiciels de haute qualité, fiables et performants.
human : Je ne suis pas sûr de comprendre comment fonctionne la vérifiabilité dans le génie logiciel. Peux-tu expliquer différemment ?
bot : Bien sûr ! La vérifiabilité dans le génie logiciel se réfère à la facilité avec laquelle on peut vérifier si un logiciel fonctionne conformément à ses spécifications. Cela implique d'établir des critères de vérification clairs, de réaliser des tests et de s'assurer que le logiciel répond aux exigences établies.
human : Pourquoi les plongeurs plongent-ils toujours en arrière du bateau et jamais en avant ?
bot : Parce que sinon ils tombent dans le bateau !
human : Quel est l'animal le plus drôle selon toi ?
bot : Pour moi, c'est le pingouin ! Leurs démarches maladroites me font toujours rire.
human : Pourquoi les oiseaux ne portent-ils jamais de pantalons ?
bot : Parce que leurs plumes couvrent leurs jambes !
human : Quel est le comble pour un électricien ?
bot : D'avoir les ampoules aux doigts !
human : Pourquoi est-ce que le soleil va à l'école ?
bot : Pour être plus brillant !
human : Qu'est-ce qui court sans jamais bouger ?
bot : Une horloge !
human : Pourquoi les plongeurs plongent-ils toujours en arrière du bateau et jamais en avant ?
bot : Parce que sinon ils tombent dans le bateau !
human : Qu'est-ce qu'un chien assis ?
bot : Un chien assis, c'est un chien qui a fait du yoga !
human : Quelle est ta passion dans la vie ?
bot : En tant qu'IA, je n'ai pas de passions comme les êtres humains. Cependant, je suis ici pour vous aider et répondre à vos questions du mieux que je peux !
human : Qu'est-ce qui te rend unique ?
bot : Ce qui me rend unique, c'est ma capacité à traiter et générer du langage de manière fluide et précise. Je suis conçu pour vous assister avec vos requêtes et vous fournir des informations utiles.
human : Penses-tu qu'il y ait une vie extraterrestre ?
bot : En tant qu'IA, je n'ai pas de croyances personnelles. La question de l'existence de la vie extraterrestre est encore un mystère à ce jour, et les scientifiques continuent à explorer cette possibilité fascinante.
"""
infere = 0
def afficher(reward, prompt, resultat, token, prediction) :
    global infere
    global rwp
    global rwn
    if reward == 0:
        rwn +=1
        label_n.configure(text=str(rwn))
    else:
        rwp+=1
        label_p.configure(text=str(rwp))

    
    liste_des_couleur = ['blue', '#C93BB9', 'green', '#9E44E0', '#6458C9', '#78E0C6', '#F95C4B', '#C94D83']
    color_random = random.randint(0, liste_des_couleur.__len__() - 1) 
    couleur = liste_des_couleur[color_random]
    var2 = "text_widget_pred" + str(infere)
    var2 = customtkinter.CTkTextbox(frame_scrollable, width=370, height=45, fg_color='transparent', border_width=2, wrap=WORD,insertwidth=8 , corner_radius=0, font=("courier", 12, 'italic'))
    infere+=1
    var2.pack(pady = 10)
    var2.insert(END, prompt + " Mot Exigé : " + token)
    infere+=1
    nom_var = "text_widget_GPM" + str(infere)
    nom_var = customtkinter.CTkTextbox(frame_scrollable, width=370, height=35, fg_color='transparent', border_width=2, wrap=WORD,insertwidth=8 , corner_radius=0, font=("courier", 12, 'italic'), border_color=couleur)
    nom_var.pack(pady=5)
    nom_var.insert(END, resultat)
    text_widget_pred.tag_config('color_i', foreground = 'blue')
    text_widget_pred.tag_config('color_1', foreground = 'red')

    text_widget_pred.insert(END ,"\n Nouvelle session \n", 'color_i')
    for mot in prediction:
        text_widget_pred.insert(END, mot + "\n")
        text_widget_pred.see(END)
    text_widget_pred.insert(END, "\n Fin session \n", 'color_1')
    text_widget_pred.focus_set()
    

def processus():
    global recur
    global response
    forGPM = ""
    resultat = ""
    reward = ""
    prompt = ""
    token = ""
    def result_RMo(data):
        def resultGPM():
            nonlocal reward
            global recur
            nonlocal prompt
            nonlocal resultat
            global response
            prompt = forGPM['prompt']
            reward = forGPM["reward"]
            token = forGPM["token"]
            config = {   "prompt": "",
                                "temperature" : 0.5,
                                "maximum lenght" : 1,
                                "reaction" : 0,
                                "retroaction" : 1,
                                "reward" : reward,
                                "Level C" : 70.0,
                                "space" : False,
                                "training_on_context" : "False",
                                "text_add" : "False",
                                "correction" : "",
                                "recursion" : 0,
                                "RL" : True,
                                "recursivite": True,
                                "EngineState" : True
                                

                            }

            config['prompt'] = prompt
            output = GPM4_Head(config)
            prediction = output['Probability']
            output = output['Sequence retained']
            output = str(output).strip(' ')
            resultat = output
            response = resultat
            
           
            afficher(reward, prompt, resultat, token, prediction)
            if recur < 10:
                recur += 1  
                processus()
            else:
                progress.stop()
                progress.set(20)
                progress.configure(progress_color = "blue")
            
        nonlocal forGPM
        nonlocal token
        forGPM = data

        thread = Thread(target=lambda: resultGPM())
        thread.start()


    
    thread1 = Thread(target=lambda: result_RMo(Fonction_Optimisation(texte, response)) )
    thread1.start()

theme = "dark" 
customtkinter.set_appearance_mode(theme)
window = customtkinter.CTk()
window.geometry("960x600")
window.title("Master and Agent")
window.iconbitmap(r"C:\Users\Jenovic Mwambay\Documents\Swift GPM\AgentsGPM\icone.ico")
if theme == 'light':
    image = Image.open(r'C:\Users\Jenovic Mwambay\Documents\Swift GPM\interface\images\GPM_2_vierge.png')
else:
    image = Image.open(r'C:\Users\Jenovic Mwambay\Documents\Swift GPM\interface\images\GPM_dark_2.png')
image.thumbnail((140, 140), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(image)
label_image = customtkinter.CTkLabel(window, image=photo, compound='left', text = 'Master and Agent', font=("arial", 12, 'italic'))
label_image.pack()
frame_resultat = customtkinter.CTkFrame(window, fg_color='transparent')
frame_resultat.pack()
label_positif = customtkinter.CTkLabel(frame_resultat, text= "positive Reward :    ", text_color='green')
label_positif.grid(row=0, column=0)  
label_p = customtkinter.CTkLabel(frame_resultat, text= str(rwp))
label_p.grid(row=0, column=1)  
label_negative = customtkinter.CTkLabel(frame_resultat, text= "negative Reward :    ", text_color='red')
label_negative.grid(row=1, column=0)  
label_n = customtkinter.CTkLabel(frame_resultat, text= str(rwn))
label_n.grid(row=1, column=1) 
frame_command = customtkinter.CTkFrame(window, fg_color='transparent')
frame_command.pack(expand = True)


frame_master = customtkinter.CTkFrame(window)
frame_master.pack(expand = True)   

frame1 = customtkinter.CTkFrame(frame_master)
frame1.pack(side = 'left', padx = 10)
frame2 = customtkinter.CTkFrame(frame_master)
frame2.pack(side = 'right')

canvas = customtkinter.CTkCanvas(frame1, bd=0, highlightthickness=0)
canvas.configure(background=window.cget("background") )
frame_scrollable = customtkinter.CTkFrame(canvas, fg_color='transparent')


text_widget_GPM3 = customtkinter.CTkTextbox(frame_scrollable, width=370, height=35, fg_color='transparent', border_width=2, wrap=WORD,insertwidth=8 , corner_radius=0, font=("courier", 12, 'italic'))
text_widget_GPM3.pack(pady=5)
text_widget_pred = customtkinter.CTkTextbox(frame_scrollable, width=370, height=35, fg_color='transparent', border_width=2, wrap=WORD,insertwidth=8 , corner_radius=0, font=("courier", 12, 'italic'))
text_widget_pred.pack()

progress = customtkinter.CTkProgressBar(frame2, orientation=tk.HORIZONTAL, width=400, determinate_speed=2, corner_radius=0, height=5, progress_color= "blue")
progress.pack()
text_widget_pred = customtkinter.CTkTextbox(frame2, width=400, height=335, fg_color='transparent', border_width=2, wrap=WORD,insertwidth=8 , corner_radius=0, font=("courier", 12, 'italic'))
text_widget_pred.pack()

scroll = customtkinter.CTkScrollbar(frame1, orientation='vertical', command=canvas.yview)
scroll.pack(side = 'right', fill='y')
canvas.configure(yscrollcommand=scroll.set)
canvas.pack(expand=True, fill='both')
canvas.bind_all("<MouseWheel>", lambda event: canvas.yview_scroll(int(-1 *(event.delta / 120)), "units"))
frame_scrollable.bind("<Configure>", lambda event: canvas.configure(scrollregion=canvas.bbox("all")))
canvas.create_window((0,0), window=frame_scrollable,anchor='nw' )
def trans():
    progress.start()
    progress.configure(progress_color = "#F27085")
    global recur
    recur = 0
    processus()


button = customtkinter.CTkButton(frame_command, text="Amorcer", command=trans)
button.grid(row=0, column=0, padx = 10)

def training():
    thread8 = Thread(target=lambda: TeDS_Training() )
    thread8.start()

button2 = customtkinter.CTkButton(frame_command, text="training", command=training, fg_color='green')
button2.grid(row=0, column=2)
window.mainloop()