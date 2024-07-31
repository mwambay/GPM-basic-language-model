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
        while taille_texte - choix_aleatoire < 4:
            choix_aleatoire = random.randint(0, taille_texte)
        prompt = ""
        for i in range(choix_aleatoire, choix_aleatoire + 4):
            prompt += texte[i] + " "
        memoire = prompt + " " + texte[i+1]
        last_word = texte[i+1]
        return prompt
    
    if memoire == "":
        data["reward"] = 1
        data["prompt"] = Generer_prompt()
        return data
    else:
        if prediction == last_word:
            data["reward"] = 1
            data["prompt"] = Generer_prompt()
            return data
        else:
            data["reward"] = 0
            data["prompt"] = memoire.replace(last_word, "")
            return data
human = None
        
for i in range(19):
    resultat = Fonction_Optimisation("salut je suis jenovic, et je suis ingenieur logiciel, actuellement je suis a salama, et j'y poursuit mon cursus scolaire. je suis fier d'etre dans cette institution depuis maintenant 2 ans et j'enchaines les reussites. je suis fiere de moi !", human)
    print("Prompt : ", resultat['prompt'])
    print("Reward", resultat["reward"])
    human = input("reponse : ")