from nltk import word_tokenize
import random

memoire = ""
last_word = ""
def Fonction_Optimisation(texte, prediction):
    global memoire
    global last_word
    data = {}
    texte = word_tokenize(texte)   
    def Generer_prompt():
        global memoire
        global last_word
        taille_texte = len(texte)
        choix_aleatoire = taille_texte -1
        while taille_texte - choix_aleatoire < 9:
            choix_aleatoire = random.randint(0, taille_texte)
        prompt = ""
        for i in range(choix_aleatoire, choix_aleatoire + 9):
            prompt += texte[i] + " "
        memoire = prompt + " " + texte[i+1]
        last_word = texte[i+1]
        return prompt
    
    if memoire == "":
        data["reward"] = 1
        data["prompt"] = Generer_prompt()
        data["token"] = last_word
        return data
    else:
        if prediction == last_word:
            data["reward"] = 1
            data["prompt"] = Generer_prompt()
            data["token"] = last_word
            return data
        else:
            data["reward"] = 0
            data["prompt"] = memoire.replace(last_word, "")
            data["token"] = last_word
            return data
