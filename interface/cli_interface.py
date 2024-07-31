import sys
import os
chemin_parent = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(chemin_parent)
import json
from model.Head_Of_Model.GPM4 import GPM4_Head
import pprint

with open(rf"{chemin_parent}\trainset_MedGPM.json", "r") as f:
    dataGPM = json.load(f)
    f.close()
    dataGPM = """
    human : fièvre, maux de tête, fatigue
bot : malaria
human : toux, essoufflement, fièvre
bot : covid-19
human : nausées, vomissements, diarrhée
bot : gastro-entérite
human : rougeur, gonflement, douleur
bot : infection
human : perte de poids, soif excessive, miction fréquente
bot : diabète
human : douleur thoracique, essoufflement, sueurs froides
bot : infarctus-du-myocarde
human : maux de gorge, difficulté à avaler, ganglions enflés
bot : angine
human : vertiges, troubles de l'équilibre, acouphènes
bot : ménière
human : démangeaisons, sécheresse, rougeur
bot : eczéma
human : saignements anormaux, douleurs pelviennes, fatigue
bot : cancer-du-col-de-l'utérus
human : toux, congestion nasale, éternuements
bot : rhume
human : douleurs articulaires, raideur matinale, fatigue
bot : arthrite
human : douleur abdominale, ballonnements, constipation
bot : syndrome-du-côlon-irritable
human : saignements de nez, fatigue, pâleur
bot : anémie
human : douleur lombaire, difficulté à uriner, fièvre
bot : infection-urinaire
human : douleur oculaire, vision floue, sensibilité à la lumière
bot : conjonctivite
human : douleur musculaire, fatigue, fièvre
bot : grippe
human : douleur thoracique, toux sèche, fatigue
bot : pneumonie
ENDGPM@
"""

configure_GPM = {   "prompt": "",
                        "temperature" : 0.3,
                        "maximum lenght" : 1,
                        "reaction" : 0,
                        "retroaction" : 1,
                        "reward" : 1,
                        "Level C" : 70.0,
                        "space" : "True",
                        "training_on_context" : "True",
                        "text_add" : dataGPM,
                        "correction" : "",
                        "recursion" : 0,
                        "RL" : False,
                        "recursivite" : True,
                        "EngineState" : False
                    }

while True:
    x = "human : "
    x += input("Prompt : ")
    try:    
        configure_GPM['prompt'] = x
        resultat = GPM4_Head(configure_GPM)
        print("Bot : " ,resultat['Sequence retained'])
        pprint.pprint("Brut Result", resultat)
    except:
        continue
    