import json
with open(r"C:\Users\Jenovic Mwambay\Documents\Swift GPM\Labs\MedGPM\data.json", 'r', encoding='utf-8') as file:
    data = json.load(file)
data = {
  "fièvre, maux de tête, fatigue": "malaria",
  "toux, essoufflement, fièvre": "covid-19",
  "nausées, vomissements, diarrhée": "gastro-entérite",
  "rougeur, gonflement, douleur": "infection",
  "perte de poids, soif excessive, miction fréquente": "diabète",
  "douleur thoracique, essoufflement, sueurs froides": "infarctus du myocarde",
  "maux de gorge, difficulté à avaler, ganglions enflés": "angine",
  "vertiges, troubles de l'équilibre, acouphènes": "ménière",
  "démangeaisons, sécheresse, rougeur": "eczéma",
  "saignements anormaux, douleurs pelviennes, fatigue": "cancer du col de l'utérus",
  "toux, congestion nasale, éternuements": "rhume",
  "douleurs articulaires, raideur matinale, fatigue": "arthrite",
  "douleur abdominale, ballonnements, constipation": "syndrome du côlon irritable",
  "saignements de nez, fatigue, pâleur": "anémie",
  "douleur lombaire, difficulté à uriner, fièvre": "infection urinaire",
  "douleur oculaire, vision floue, sensibilité à la lumière": "conjonctivite",
  "douleur musculaire, fatigue, fièvre": "grippe",
  "douleur thoracique, toux sèche, fatigue": "pneumonie"
}

liste = []
trainset = {}
for i, j in data.items():

    trainset["human"] = i
    trainset["bot"] = j.replace(" ", "-")
    liste.append(trainset)
    print(liste)
    trainset = {}
print(trainset)

file = open("trainset_MedGPM.json", 'w', encoding="utf-8")
json.dump(liste,file,indent=1)