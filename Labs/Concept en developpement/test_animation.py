import customtkinter as ctk
from tkinter import *
import time
import random
from random import randint
root = ctk.CTk()

root.geometry('480x234')

label = ctk.CTkLabel(root, text='', compound='left')
label.pack()
label_2 = ctk.CTkLabel(root, text='')
label_2.pack()
def teste():
    indice = " "*100
    label.configure(text='')
    p=0
    liste = ['#99D9EA', '#403BBA', '#7DB1BF', '#55528C', '#918DF0']
    beta = liste.__len__() - 1
    nb = random.randint(0, beta)
    def typing_effect1(string1, label, labell):
            o = 0
            for char in string1:
                o+=1
                nb = random.randint(0, beta)
                if o < 51:
                    labell.configure(text= label.cget("text") + char, fg_color=liste[nb],height=4, corner_radius=3)
                label.configure(text= label.cget("text") + char, fg_color=liste[nb],height=4, corner_radius=3)
                label.update()
                time.sleep(0.001)
    typing_effect1(indice, label, label_2)
    indice = " "*50
    p=0
    def typing_effect1(string1, label):
            for char in string1:
                label.configure(text= label.cget("text") + char, fg_color='green',height=4, corner_radius=3)
                label.update()
                time.sleep(0.001)
    typing_effect1(indice, label_2)
button = ctk.CTkButton(root, text='Click me', command=teste)
button.pack()

root.mainloop()