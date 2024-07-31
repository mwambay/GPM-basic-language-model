data = ["je", "suis", "jenovic", "et", "je", "peux", "voler", "je", "peux", "aussi", "marcher"]
mot = "je"
vecteur = []
for index in range(len(data)):
    token = data[index]
    if token == mot:
        if data[:index].__len__() == 1:
            if data[index:].__len__() == 1:  
                vecteur.append(token)
            else:
                vecteur.append(data[index : index + 3])
        else:
            vecteur.append(data[index-2:index+3])
print(vecteur)