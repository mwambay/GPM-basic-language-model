import customtkinter
customtkinter.set_appearance_mode('dark')

root = customtkinter.CTk()

canvas = customtkinter.CTkCanvas(root)
frane_master = customtkinter.CTkFrame(root)
frane_master.pack()
canvas.configure(background=root.cget("background"))
frame = customtkinter.CTkFrame(canvas, fg_color='transparent')
"""frame_2 = customtkinter.CTkFrame(frame)
frame_2.pack()"""
for i in range(100):
    label = customtkinter.CTkLabel(frame, text=f'label{i}')
    label.pack(side = 'top', fill='x')
scroll = customtkinter.CTkScrollbar(root, orientation='vertical', command=canvas.yview)
scroll.pack(side = 'right', fill='y')
canvas.configure(yscrollcommand=scroll.set)
canvas.pack(expand=True, fill='both')
canvas.bind_all("<MouseWheel>", lambda event: canvas.yview_scroll(int(-1 *(event.delta / 120)), "units"))
frame.bind("<Configure>", lambda event: canvas.configure(scrollregion=canvas.bbox("all")))
canvas.create_window((0,0), window=frame,anchor='nw' )
root.mainloop()
