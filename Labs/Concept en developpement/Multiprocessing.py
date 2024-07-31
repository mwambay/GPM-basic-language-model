"""import multiprocessing
num_cores = multiprocessing.cpu_count()
print(num_cores)
import multiprocessing

def my_function():
    # Code de votre fonction à exécuter en parallèle
    for i in range(10):
        print("Process ID:", multiprocessing.current_process().name, "Value:", i)

if __name__ == "__main__":
    num_cores = multiprocessing.cpu_count()  # Récupère le nombre de cœurs disponibles
    print(num_cores, "iuyfdfghjkloiuyfh")
    processes = []

    for _ in range(num_cores):
        p = multiprocessing.Process(target=my_function)
        p.start()
        processes.append(p)

    for p in processes:
        p.join()"""

import multiprocessing
from tkinter import *
from GPM_3 import TeDS_execution
def my_function(note):
    # Code de votre fonction à exécuter en parallèle
    model_result =  TeDS_execution("souris", 1, 0, 0, "long_memory", 1, "long_memory_large", 70, False, 0.3)
    print(model_result , note)
    texte.insert(END, str(model_result) + note)


def processus():
    p = multiprocessing.Process(target=my_function)
    p.start()
    p2 = multiprocessing.Process(target=my_function)
    p2.start()
    p3 = multiprocessing.Process(target=my_function)
    p3.start()
    p4 = multiprocessing.Process(target=my_function)
    p4.start()
    
root = Tk()
root.geometry("800x400")
button = Button(root, text = "Executer", command=processus)
button.pack()
texte = Text(root, width=200, height=200)
texte.pack()


root.mainloop()