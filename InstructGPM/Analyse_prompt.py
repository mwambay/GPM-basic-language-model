import pprint
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

def remove(text):
    tokens = word_tokenize(text)
    stop_words = set(stopwords.words('french'))
    filtre = [word for word in tokens if word.lower() not  in stop_words]
    filtre_text = ' '.join(filtre)
    return filtre_text
prompt = "la programmation est avant tout un ensemble des techiques permettant de communuquer avec une machine, la programmation se fait avec un language de programmation comme le python ou le javascript."
prompt = remove(prompt)
print(prompt)
prompt = prompt.split()
output = "bien-sur la programmation imperative est un ensemble de techniques qui permettent a l'homme imperative de transmettre des instructions a une machine pour que elle puisse les executer"
output = output.split()
frequency = {}
for word in output:
    if word in prompt:
        if word not in frequency:
            frequency[word] = 1
        else:
            for cle, value in frequency.items():
                if cle == word:
                    frequency[word] = int(value) + 1
term_probable = {}
def Neural_Network():
    recurent_term = []  
    memoire_temp = []
    global term_probable
    if frequency.__len__() > 1:
        for word, frequence in frequency.items():
            grande_valeur = 0
            if int(frequence) > int(grande_valeur):
                grande_valeur = int(frequence)
        for mot, valeur in frequency.items():
            if valeur == grande_valeur:    
                memoire_temp.append(word)
                memoire_temp.append(grande_valeur)
        term_probable['first'] = memoire_temp
        memoire_temp = []
        for word, frequence in frequency.items():
            autre_valeur = 0
            if frequence > autre_valeur and frequence != grande_valeur:
                autre_valeur = frequence 
                memoire_temp.append(word)
                memoire_temp.append(autre_valeur)
        term_probable['secand'] = memoire_temp
    else:
        pass
    def Analysis_of_exemples():
        pass
Neural_Network()
pprint.pprint(term_probable) 
    
pprint.pprint(frequency)