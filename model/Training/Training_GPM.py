import random
from random import randint
import json
from nltk.tokenize import word_tokenize
import difflib


file = open(r"C:\Users\mwamb\Documents\Engineering\Engineering\GPM4\training data\texte_representatif.txt", encoding='utf-8')
vecteurs = file.readlines()
file.close()
tableau_partiel = ""
for token in vecteurs:
    tableau_partiel += "" + token
vectorisation = []
tableau_partiel = tableau_partiel.split()
nouvelle_donnees = []
for token in tableau_partiel:
    if token == "<text_stop>":
            vectorisation.append(token)
            nouvelle_donnees.append(vectorisation)
            vectorisation = []
    else:
        vectorisation.append(token)
file = open(r"C:\Users\mwamb\Documents\Engineering\Engineering\GPM4\training data\training_data.json", 'w', encoding='utf-8')
json.dump(nouvelle_donnees, file, indent=4)
file.close()
history = []
exeprience__par_feedback = [['sur', 'une', 'f�te'], ['suis', 'homme', 'nous', 0], ['je', 'vous', 'aider', 0], ['faire', 'des', 'mers', 0], ['aire', 'des', 'dangers', 0], ['pendant', 'des', 'provisions', 0], ['pendant', 'des', 'cha�nes', 0], ["n'ai", 'vous', 'je', 0], ['courait', 'ont', 'était', 0], ['l', 'rêvait', 'de', 0], ['semblaient', 'ont', 'signifie', 0], ['glissé', 'sur', 'le', 'trésor', 0], ["j'ai", 'glissé', 'sur', "l'île", 0], ['glissé', 'sur', 'un', 'message', 0], ['glissé', 'sur', 'la', 'gestion', 0], ['glissé', 'sur', 'le', 'développement', 0], ['glissé', 'sur', 'le', 'voyage', 0], ['glissé', 'sur', 'une', 'vaste', 0], ['glissé', 'sur', 'une', 'fois', 0], ['glissé', 'sur', 'une', 'nouvelle', 0], ['glissé', 'sur', 'ses', 'aventures', 0], ['glissé', 'sur', 'ses', 'aventures', 0], ['glissé', 'sur', 'une', 'légende', 0], ['glissé', 'sur', 'une', 'légende', 0], ['glissé', 'sur', 'mon', 'compte', 0], ['glissé', 'sur', 'une', 'intelligence', 0], ['glissé', 'sur', 'la', 'ramassa', 0], [0], ['glissé', 'sur', 'ses', 'journées', 0], ['sur', 'un', 'peu', 'maladroit', 0], ['glissé', 'sur', 'la', 'programmation', 0], ['glissé', 'sur', 'la', 'maison', 0], ['glissé', 'sur', 'ses', 'rêves', 0], [0], ['glissé', 'sur', 'un', 'homme', 0], ['glissé', 'sur', 'le', 'lendemain', 0], ['échouée', 'sur', 'une', 'intelligence', 0]]
def TeDS_Training():
    with open(r'C:\Users\mwamb\Documents\Engineering\Engineering\GPM4\training data\training_data.json', 'r', encoding="utf-8") as file:
        corpus_de_text = json.load(file)
        file.close()
    CHARSET = [1,2,3,4,5,6,7,8,9,0,8,98,34,5,2,4,5,6,4,3]
    sequence_encode = []
    relation_sequence_forward_propagation = []
    relation_sequence_back_propagation = []

    code_length = 20
    liste_temporaire_des_codes_generes = []

    # Encodage des sequences
    def encoder_sequences(text):
            liste_insertion = []
            compteur = 0
            chaine_tokken = ""
            tableau_temporaire_des_tokken = []
            list_tokken = []
            tab_temp = text
            for sentence in text:
                compteur += 1
                if sentence != "<text_start>" and  sentence != "<text_stop>":
                    print(compteur, "token assembly" + " " + sentence)
                    chaine_tokken += sentence + ' '
            tableau_temporaire_des_tokken = word_tokenize(chaine_tokken)
            list_tokken = tableau_temporaire_des_tokken
                    #print('sentence', compteur, sentence, compteur)
            compteur = 0
      
            
            for token in range(list_tokken.__len__()):
                temp = 0
                compteur += 1
                code = ''.join(map(str, random.sample(CHARSET, code_length)))
                while code in liste_temporaire_des_codes_generes:
                    code = ''.join(map(str, random.sample(CHARSET, code_length)))
                liste_temporaire_des_codes_generes.append(code)
                print(f'Tokens embeding :  {list_tokken[token]}  {code} + {compteur}')
                liste_insertion.append(list_tokken[token])
                
                for i in sequence_encode:
                    if i[0] == list_tokken[token]:
                        code = i[1]
                        
                liste_insertion.append(code)
                
                try:
                    liste_insertion.append(list_tokken[token + 1])
                except IndexError:
                    pass
                try:
                    liste_insertion.append(list_tokken[token + 2])
                except IndexError:
                    pass
                try:liste_insertion.append(list_tokken[token + 3])
                except IndexError:pass
                try:liste_insertion.append(list_tokken[token + 4])
                except IndexError:pass
                try:liste_insertion.append(list_tokken[token + 5])
                except IndexError:pass
                #try:liste_insertion.append(list_tokken[token + 6])
                #except IndexError:pass
                    #try:liste_insertion.append(list_tokken[token + 6])
                    #except IndexError:pass
                if list_tokken[token] == ".":
                    liste_insertion.append("<stop>")
                
                # Decouverte des relation entre les mots
                def self_attention():
                    self_attention_by_word = []
                    ponctuation = ['.', ',', ':', ';', '!']
                    if list_tokken[token] not in ponctuation:
                        for vector in sequence_encode:
                            try:
                                if list_tokken[token] in vector and list_tokken[token - 1] in vector:
                                    self_attention_by_word.append(vector[0])
                            except IndexError:
                                pass
                    if self_attention_by_word.__len__() != 0:
                        for word in self_attention_by_word:
                            if word not in liste_insertion:
                                liste_insertion.append(word)
                #self_attention()
                sequence_encode.append(liste_insertion)
                liste_insertion = []
                
                def chain_of_understanding(compteur):
                    for index, vecteur in enumerate(sequence_encode):
                        try:
                            for sous_vecteur in range(index+1, len(sequence_encode)):
                                if sequence_encode[index].__len__() < 13 and "<text_stop>" not in sequence_encode[index]:
                                    print(f"{vecteur} operation : {compteur}//")
                                    compteur+=1
                                    for embeding in sequence_encode[sous_vecteur]:
                                        if embeding in sequence_encode[index]:
                                            if embeding == "<border>" :
                                                break
                                            
                                            for element in sequence_encode[sous_vecteur]:
                                                if element not in sequence_encode[index]:
                                                    if "<border>" not in sequence_encode[index]:
                                                        if str(element).isdigit():
                                                            pass
                                                        else:
                                                            if sequence_encode[index].__len__() < 13 and element != "<text_stop>":
                                                                sequence_encode[index].append("<border>")
                                                                sequence_encode[index].append(element)
                                                    else:
                                                        if str(element).isdigit():
                                                            pass
                                                        else:
                                                            if sequence_encode[index].__len__() < 13 and element != "<text_stop>":
                                                                sequence_encode[index].append(element)
                        except:
                            pass
                #chain_of_understanding(0)

            sequence_encode[len(sequence_encode) - 1].append("<text_stop>")
    for vecteur in corpus_de_text:
        encoder_sequences(vecteur)
        
    with open(r'C:\Users\mwamb\Documents\Engineering\Engineering\GPM4\model\vectors\GP-Model.json', 'w',encoding= 'utf-8') as file:
        json.dump(sequence_encode, file, indent=1)
    liste_des_vecteur = []

    # Vectorisation // list Embeding
    def Vecteur_sequences():
        for vecteur in sequence_encode:
            liste_des_vecteur.append(int(vecteur[1]))
            print('Extraction Vecteurs : ' ,vecteur)
    Vecteur_sequences()

    # Calcul des relations entre sequences
    def relations_entre_sequences():
        for element in range(len(liste_des_vecteur) - 1):
            liste_d_integration = []
            liste_d_integration_forward = []
            liste_d_integration_forward.append(int(liste_des_vecteur[element] - int(liste_des_vecteur[element + 1])))
            print('Relation sequence : ' + str(element))
            for token_vecteur in sequence_encode:
                if int(token_vecteur[1]) == int(liste_des_vecteur[element]):
                    liste_d_integration_forward.append(token_vecteur[0])
                    break
            
            reference_propa = element
            reference_propa += 2
            
            for i in range(5):
                try:
                    for x in sequence_encode:
                        if str(x[1]) == str(liste_des_vecteur[reference_propa]):
                            liste_d_integration_forward.append(x[0])
                            reference_propa += 1
                            break
                except IndexError:
                    pass
            
            relation_sequence_forward_propagation.append(liste_d_integration_forward)
            
            liste_d_integration.append(int(liste_des_vecteur[element + 1]) - int(liste_des_vecteur[element]))
            reference_propa = element
            reference_propa += 2
            
            for i in range(5):
                try:
                    liste_d_integration.append(liste_des_vecteur[reference_propa])
                    reference_propa += 1
                except IndexError:
                    pass
            relation_sequence_back_propagation.append(liste_d_integration)
    relations_entre_sequences()
    
    with open(r'C:\Users\mwamb\Documents\Engineering\Engineering\GPM4\model\vectors\vecteur_multi_dimentionnel_back.json', 'w') as file:
        json.dump(relation_sequence_back_propagation, file)
        file.close()
    with open(r'C:\Users\mwamb\Documents\Engineering\Engineering\GPM4\model\vectors\vecteur_multi_dimentionnel.json', 'w') as file:
        json.dump(relation_sequence_forward_propagation, file)
        file.close()
        
        
    def attention():
        liste_vide = []
        dictionnaire = {}
        for vecteur in sequence_encode:
            for vec in sequence_encode:
                try:
                    if vecteur[1] == vec[1] and vecteur[3] == vec[3]:
                        if vecteur[2] not in liste_vide and vec[2] not in liste_vide:
                            if vecteur[2] not in liste_vide:
                                liste_vide.append(vecteur[2])
                            liste_vide.append(vec[2])
                            nouvelle_liste = []
                            for element in liste_vide:
                                if element not in nouvelle_liste:
                                    nouvelle_liste.append(element)
                            dictionnaire[vecteur[1]] = nouvelle_liste
                except IndexError:
                    pass


        with open(r"C:\Users\mwamb\Documents\Engineering\Engineering\GPM4\model\vectors\element_synonyme.json", 'w') as file:
            json.dump(dictionnaire, file, indent=4)
    attention()
if __name__ == '__main__':
    TeDS_Training()