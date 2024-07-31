import random
import json
from nltk.tokenize import word_tokenize

file_path = r"C:\Users\Jenovic Mwambay\Documents\Model GPM\training data\texte_representatif.txt"
output_file_path = r"C:\Users\Jenovic Mwambay\Documents\Model GPM\training data\training_data.json"
vectors_output_file_path = r"C:\Users\Jenovic Mwambay\Documents\Model GPM\model\vectors\GP-Model.json"
back_vectors_output_file_path = r"C:\Users\Jenovic Mwambay\Documents\Model GPM\model\vectors\vecteur_multi_dimentionnel_back.json"
forward_vectors_output_file_path = r"C:\Users\Jenovic Mwambay\Documents\Model GPM\model\vectors\vecteur_multi_dimentionnel.json"
synonym_output_file_path = r"C:\Users\Jenovic Mwambay\Documents\Model GPM\model\vectors\element_synonyme.json"

CHARSET = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 8, 98, 34, 5, 2, 4, 5, 6, 4, 3]
code_length = 20

def TeDS_Training():
    with open(file_path, 'r', encoding="utf-8") as file:
        corpus_de_text = file.readlines()
    
    sequence_encode = []
    liste_temporaire_des_codes_generes = []

    def encoder_sequences(text):
        liste_insertion = []
        chaine_tokken = ""
        list_tokken = []
        
        for sentence in text:
            if sentence != "<text_start>" and sentence != "<text_stop>":
                chaine_tokken += sentence + ' '
        
        tableau_temporaire_des_tokken = word_tokenize(chaine_tokken)
        list_tokken = tableau_temporaire_des_tokken
        
        for token in list_tokken:
            code = ''.join(map(str, random.sample(CHARSET, code_length)))
            while code in liste_temporaire_des_codes_generes:
                code = ''.join(map(str, random.sample(CHARSET, code_length)))
            liste_temporaire_des_codes_generes.append(code)
            
            liste_insertion.append(token)
            liste_insertion.append(code)
            
            try:
                liste_insertion.append(list_tokken[list_tokken.index(token) + 1])
            except IndexError:
                pass
            try:
                liste_insertion.append(list_tokken[list_tokken.index(token) + 2])
            except IndexError:
                pass
            try:
                liste_insertion.append(list_tokken[list_tokken.index(token) + 3])
            except IndexError:
                pass
            try:
                liste_insertion.append(list_tokken[list_tokken.index(token) + 4])
            except IndexError:
                pass
            try:
                liste_insertion.append(list_tokken[list_tokken.index(token) + 5])
            except IndexError:
                pass
            
            if token == ".":
                liste_insertion.append("<stop>")
            
            sequence_encode.append(liste_insertion)
            liste_insertion = []
    
    for vecteur in corpus_de_text:
        encoder_sequences(vecteur)
    
    with open(output_file_path, 'w', encoding='utf-8') as file:
        json.dump(sequence_encode, file, indent=4)
    
    liste_des_vecteur = []
    
    def Vecteur_sequences():
        for vecteur in sequence_encode:
            liste_des_vecteur.append(int(vecteur[1]))
            print('Extraction Vecteurs : ', vecteur)
    
    Vecteur_sequences()
    
    relation_sequence_forward_propagation = []
    relation_sequence_back_propagation = []
    
    def relations_entre_sequences():
        for element in range(len(liste_des_vecteur) - 1):
            liste_d_integration_forward = []
            liste_d_integration_forward.append(int(liste_des_vecteur[element]) - int(liste_des_vecteur[element + 1]))
            
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
            
            liste_d_integration = []
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
    
    with open(forward_vectors_output_file_path, 'w') as file:
        json.dump(relation_sequence_forward_propagation, file)
    
    with open(back_vectors_output_file_path, 'w') as file:
        json.dump(relation_sequence_back_propagation, file)
    
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
        
        with open(synonym_output_file_path, 'w') as file:
            json.dump(dictionnaire, file, indent=4)
    
    attention()

TeDS_Training()