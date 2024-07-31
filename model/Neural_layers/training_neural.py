import os
import sys
chemin_parent = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(chemin_parent)
import random
import json

# Fonction permettant au modele d'apprendre constament sur le texte
def Training_on_prompt(list_tokken, code_length, liste_des_vecteur):
            memoire_token = []
            sequence_encode = []
            liste_temporaire_des_codes_generes = []
            CHARSET = [1,2,3,4,5,6,7,8,9,0,32,56,23,65,33,22,34,66,77,66,544,665]
            liste_insertion = []
            compteur = 0
            for token in range(list_tokken.__len__()):
                temp = 0
                compteur += 1
                code = ''.join(map(str, random.sample(CHARSET, code_length)))
                while code in liste_temporaire_des_codes_generes:
                    code = ''.join(map(str, random.sample(CHARSET, code_length)))
                liste_temporaire_des_codes_generes.append(code)
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
                try:liste_insertion.append(list_tokken[token + 6])
                except IndexError:pass
                try:liste_insertion.append(list_tokken[token + 7])
                except IndexError:pass
                sequence_encode.append(liste_insertion)
                liste_insertion = []
            # Vectorisation // list Embeding
            def Vecteur_sequences():
                for vecteur in sequence_encode:
                    liste_des_vecteur.append(int(vecteur[1]))
            Vecteur_sequences()

            # Calcul des relations entre sequences
            def relations_entre_sequences(sequence_encode):
                relation_sequence_forward_propagation =[]
                for element in range(len(liste_des_vecteur) - 1):
                    liste_d_integration = []
                    liste_d_integration_forward = []
                    relation_sequence_back_propagation =[]
                    
                    liste_d_integration_forward.append(int(liste_des_vecteur[element] - int(liste_des_vecteur[element + 1])))
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
                return relation_sequence_forward_propagation
            
            
            result_of_training = {}
            result_of_training["sequence_encode"] = sequence_encode
            result_of_training["vecteurs_forward"] = relations_entre_sequences(sequence_encode)
            with open(rf"{chemin_parent}\vectors\result_of_training.json", 'w') as file:
                json.dump(result_of_training, file, indent=4)
                file.close()
            return result_of_training