import customtkinter

root = customtkinter.CTk()
root.geometry("1080x520")
longeur = 600
largeur = 400
text = customtkinter.CTkTextbox(root, width=longeur, height=largeur)
text.pack(expand = True)

def max_length(value):
    global longeur
    global largeur
    value = int(value)
    text.configure(width = longeur + value, height = largeur + value )
    root.update()
    print(value)
maximum_length = customtkinter.CTkSlider(root, to=200, command=max_length, width=165, height=15)
maximum_length.pack(side = "right")
root.mainloop()