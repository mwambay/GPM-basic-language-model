import customtkinter
from PIL import Image, ImageTk
from tkinter import*
import tkinter as tk
import customtkinter
import time
import json
import random
from PIL import Image, ImageTk
from random import randint
from threading import Thread
from GPM_3 import TeDS_execution
from Reward_Model import Fonction_Optimisation
from Training_GPM import TeDS_Training
import multiprocessing
theme = "dark" 
customtkinter.set_appearance_mode(theme)

window = customtkinter.CTk()
window.geometry("960x600")

canvas = customtkinter.CTkCanvas(window, bd=0, highlightthickness=0)
canvas.configure(background=window.cget("background") )
frame_scrollable = customtkinter.CTkFrame(canvas, fg_color='transparent')

if theme == 'light':
    image = Image.open(r'C:\Users\Jenovic Mwambay\Documents\Model GPM\images\GPM_2_vierge.png')
else:
    image = Image.open(r'C:\Users\Jenovic Mwambay\Documents\Model GPM\images\GPM_dark_2.png')
image.thumbnail((140, 140), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(image)
label_image = customtkinter.CTkLabel(window, image=photo, compound='left', text = 'Master', font=("arial", 9, 'italic'))
label_image.pack()
frame_resultat = customtkinter.CTkFrame(window, fg_color='transparent')
frame_resultat.pack()
label_positif = customtkinter.CTkLabel(frame_resultat, text= "positive Reward :    ", text_color='green')
label_positif.grid(row=0, column=0)  
label_p = customtkinter.CTkLabel(frame_resultat, text= str("rwp"))
label_p.grid(row=0, column=1)  
label_negative = customtkinter.CTkLabel(frame_resultat, text= "negative Reward :    ", text_color='red')
label_negative.grid(row=1, column=0)  
label_n = customtkinter.CTkLabel(frame_resultat, text= str("rwn"))
label_n.grid(row=1, column=1) 

text_widget_GPM3 = customtkinter.CTkTextbox(frame_scrollable, width=938, height=35, fg_color='transparent', border_width=2, wrap=WORD,insertwidth=8 , corner_radius=0, font=("courier", 12, 'italic'))
text_widget_GPM3.pack(pady=5)
text_widget_pred = customtkinter.CTkTextbox(frame_scrollable, width=938, height=135, fg_color='transparent', border_width=2, wrap=WORD,insertwidth=8 , corner_radius=0, font=("courier", 12, 'italic'))
text_widget_pred.pack()

scroll = customtkinter.CTkScrollbar(window, orientation='vertical', command=canvas.yview)
scroll.pack(side = 'right', fill='y')
canvas.configure(yscrollcommand=scroll.set)
canvas.pack(expand=True, fill='both')
canvas.bind_all("<MouseWheel>", lambda event: canvas.yview_scroll(int(-1 *(event.delta / 120)), "units"))
frame_scrollable.bind("<Configure>", lambda event: canvas.configure(scrollregion=canvas.bbox("all")))
canvas.create_window((0,0), window=frame_scrollable,anchor='nw' )

window.mainloop()