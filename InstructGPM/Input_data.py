import customtkinter
from tkinter import*
from PIL import Image, ImageTk
import json
import io
root = customtkinter.CTk()

root.geometry('950x610')
root.title("ITG")
"""frame= customtkinter.CTkFrame(root, corner_radius=70, fg_color = 'transparent')
frame.pack()

frame_glm = customtkinter.CTkFrame(frame, corner_radius=70, fg_color = 'transparent')
frame_glm.pack()
image = Image.open('images\instructGPM.png')
image.thumbnail((340, 340), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(image)
label_image = customtkinter.CTkLabel(frame_glm, image=photo, text = '')
label_image.grid(row=1, column=1, pady = 5)
label_image_text = customtkinter.CTkLabel(frame_glm, text = ' ' *210)
label_image_text.grid(row=1, column=2)
def submit():
    texte = text.get('1.0', END)
    texte = texte.split()
    ref = 0
    with open('instructGMP.json', 'a+') as file:
        data = json.load(file)
    for mot in texte:
        if mot == 'humain':
            data
"""
"""text = customtkinter.CTkTextbox(frame, width=590, height=309, wrap=WORD,insertwidth=8, font=("courier", 12, 'italic'), corner_radius= 10, border_color='#969696', border_width=0)
text.pack(pady=10)"""
"""button = customtkinter.CTkButton(frame, text='Submit')
button.pack()
"""
tets = customtkinter.CTkTabview(root, width=40)
tets.pack()
tets.add("Tab 1")
tets.add("Tab 2")
tets.add("Tab 3")
tets.tab("Tab 1").grid_columnconfigure(0, weight=1)
tets.tab("Tab 2").grid_columnconfigure(0, weight=1)
tets.tab("Tab 3").grid_columnconfigure(0, weight=1)

text = customtkinter.CTkTextbox(tets.tab("Tab 1"))
text.pack()
progress = customtkinter.CTkProgressBar(root, orientation=HORIZONTAL)
progress.pack()
def stop_progress():
    progress.stop()
    progress.set(100)
progress.start()
root.after(5000, stop_progress)


with Image.open("images\loading.gif") as gif:
    gif_red = gif.resize((30, 30), Image.ANTIALIAS)

    frames = []
    try:
        for frame in range(0, gif_red.n_frames):
            gif_red.seek(frame)
            frame_image = gif_red.copy().convert("RGBA")
            frames.append(ImageTk.PhotoImage(frame_image)
            )
    except:
        pass
label = customtkinter.CTkLabel(root)
label.pack()
def afficher_image(frame):
    image = frames[frame]
    label.configure(image=image)
    root.after(gif_red.info["duration"], lambda: afficher_image((frame + 1) % len(frames)))
afficher_image(0)
root.mainloop()