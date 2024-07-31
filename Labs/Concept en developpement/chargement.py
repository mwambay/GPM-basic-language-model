import json
file = open('texte_representatif.txt', 'r', encoding='utf-8')
data = file.readlines()
file.close()
file = open('training_data.json', 'w', encoding='utf-8')
json.dump(data, file, indent = 4)
#quit_programme = input("Tapez 'Enter' pour fermer le programme")