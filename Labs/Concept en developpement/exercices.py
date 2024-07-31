import pprint
"""liste = [4,7,6,4,6,8,3,6,1,4,5]
nombre_paire = []
resultat = 0
for nombre in liste:
    resultat = nombre % 2
    if int(resultat) == 0:
        nombre_paire.append(nombre)
print(nombre_paire)"""

"""word = "bonjour"
word = list(word)
temp = ""
for j in range(len(word)):
    for i in range(len(word)-1):
        try:
            temp = word[i]
            print(temp, word[i + 1])
            word[i] = word[i + 1]
            word[i+1] = temp
            print(word)
        except IndexError as e:
            pass
            print(e)
print(word)"""

"""listo = []
i = 0
def nombre(liste, i):
    total = len(liste) - 1
    if int(liste[i] % 2) == 0:
        listo.append(liste[i])
    i+=1
    if i <= total:
        nombre(liste, i)
    return listo
element = [7,8,9,5,3,2, 6]
print(nombre( element,i))"""

"""voyelle = ["a", "e", "i", "o", "u"]
texte = "je suis une personne"
compteurteur = 0
for lettre in texte:
    if lettre in voyelle:
        compteurteur += 1
print(compteurteur)"""

"""texte = "je suis une personne et j'ai des embitions "
liste = []
temp = ""
for caractere in texte:
    if caractere != " ":
        temp += caractere
    if caractere == " ":
        print("ok")
        liste.append(temp)
        temp = ""
print(liste)
"""
"""liste_des_nombre = []
for i in range(5):
    nombre = input(f"saisissez le nombre {i} : " )
    liste_des_nombre.append(nombre)
temp = 0
for i in range(len(liste_des_nombre)):
    for j in range(len(liste_des_nombre)-1):
        if liste_des_nombre[i] < liste_des_nombre[j]:
            temp = liste_des_nombre[i]
            liste_des_nombre[i] = liste_des_nombre[j]
            liste_des_nombre[j] = temp
print(liste_des_nombre)
print(f"Nombre le plus petit [{liste_des_nombre[0]}] \nPlus grand nombre [{liste_des_nombre[len(liste_des_nombre)-1]}]")"""
"""
try:
    nombre = 5/0
    print(nombre)
except:
    print("Error")"""
"""    
mes_nombres = []
for i in range(3):
    take_nombers = int(input("saisir le nombre " + str(i+1)+ " : "))
    mes_nombres.append(take_nombers)
resultat = (mes_nombres[0] + mes_nombres[1]) * mes_nombres[2]
print("le resultat est egale à : " + str(resultat ))
"""
"""

for i in range(3):
    nombre = int(input("saisir le nombre : "))
    if i < 2:
        if i == 1:    
            nombre += nombre
    if i > 1:
        nombre *= nombre
print(nombre)
print("bonjour".__len__())"""

"""Ma_galerie_des_voitures = [[1,0],
                            [1,1,0],
                            [1,0,0,0,0],
                            [1,1,0,0],
                            [1,0,0],
                            [1,0,0],
                            [1,1,1]
                            ]
sieges_par_vehicule = []
Vecteur_de_remplissage = []
Passagers_et_sieges = []

for index, voiture in enumerate(Ma_galerie_des_voitures):
    sieges_par_vehicule.append(voiture.__len__())
    for i in voiture:
        Passagers_et_sieges.append(i)

Passagers_et_sieges = sorted(Passagers_et_sieges, reverse=True)
compteur = 1
indice_incrementation = 0
Nouvelle_repartition = []

for element in Passagers_et_sieges:
    Vecteur_de_remplissage.append(element)
    if compteur == sieges_par_vehicule[indice_incrementation]:
        Nouvelle_repartition.append(Vecteur_de_remplissage)
        Vecteur_de_remplissage = []
        compteur = 0
        indice_incrementation += 1
    compteur += 1
    
pprint.pprint(Nouvelle_repartition)
            
                """
"""liste = ["u", 3,3,2,1]
print(liste)
liste.remove(all)
liste = []
print(liste)
  
                    """
li = [5,2,5,2,2]
for i in range(li[0]):
    print("x")