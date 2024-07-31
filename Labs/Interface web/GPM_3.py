# !!/usr/bin/python
# -*- coding: latin -*-
import random
from random import randint
import os
import json
import difflib
from nltk.tokenize import word_tokenize

history = []
historique_prob = {}
compteur_sequence = 0
verbs = ["est","ai", "es", "a"]
probability_temp = {}
input_word_help = ""
top = 0
orientation_vers_prompt = True
data_of_live_training = ""
data_of_training_on_prompt = []
experience__par_feedback = [['sur', 'une', 'f�te'], ['suis', 'homme', 'nous', 0], ['je', 'vous', 'aider', 0], ['faire', 'des', 'mers', 0], ['aire', 'des', 'dangers', 0], ['pendant', 'des', 'provisions', 0], ['pendant', 'des', 'cha�nes', 0], ["n'ai", 'vous', 'je', 0], ['courait', 'ont', 'était', 0], ['l', 'rêvait', 'de', 0], ['semblaient', 'ont', 'signifie', 0], ['glissé', 'sur', 'le', 'trésor', 0], ["j'ai", 'glissé', 'sur', "l'île", 0], ['glissé', 'sur', 'un', 'message', 0], ['glissé', 'sur', 'la', 'gestion', 0], ['glissé', 'sur', 'le', 'développement', 0], ['glissé', 'sur', 'le', 'voyage', 0], ['glissé', 'sur', 'une', 'vaste', 0], ['glissé', 'sur', 'une', 'fois', 0], ['glissé', 'sur', 'une', 'nouvelle', 0], ['glissé', 'sur', 'ses', 'aventures', 0], ['glissé', 'sur', 'ses', 'aventures', 0], ['glissé', 'sur', 'une', 'légende', 0], ['glissé', 'sur', 'une', 'légende', 0], ['glissé', 'sur', 'mon', 'compte', 0], ['glissé', 'sur', 'une', 'intelligence', 0], ['glissé', 'sur', 'la', 'ramassa', 0], [0], ['glissé', 'sur', 'ses', 'journées', 0], ['sur', 'un', 'peu', 'maladroit', 0], ['glissé', 'sur', 'la', 'programmation', 0], ['glissé', 'sur', 'la', 'maison', 0], ['glissé', 'sur', 'ses', 'rêves', 0], [0], ['glissé', 'sur', 'un', 'homme', 0], ['glissé', 'sur', 'le', 'lendemain', 0], ['échouée', 'sur', 'une', 'intelligence', 0]]
def TeDS_execution(setups):
    input_word = setups["prompt"]
    max_parameter = setups["maximum lenght"]
    reaction = setups["reaction"]
    reward = setups["reward"]
    niveau_comprehension = setups["Level C"]
    automatic_space = setups["space"]
    temperature = setups["temperature"]
    text_add = setups["text_add"]
    training_on_context = setups["training_on_context"]
    recursion = setups["recursion"] 

    global input_word_help
    global data_of_training_on_prompt
    global data_of_live_training
    global top
    global orientation_vers_prompt
    print(text_add)
    
    text_add = word_tokenize(str(text_add))

    print(input_word, "au premier niveia inpit word")
    if top == 0:
        input_word_help = input_word
        top += 1

        
    # Fonction permettant au modele d'apprendre constament sur le texte
    def Training_on_prompt(list_tokken, code_length, liste_des_vecteur):
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
            with open(r"C:\Users\Jenovic Mwambay\Documents\Model GPM\model\vectors\result_of_training.json", 'w') as file:
                json.dump(result_of_training, file, indent=4)
                file.close()
            return result_of_training
    

    
    input_word = input_word.split()
    last_word = input_word[len(input_word)-1]
    def reset_file():
        with open('Reasoning\distribution.json', 'w') as file:
            json.dump([""], file, indent=4)
            file.close()
        with open('Reasoning\Probability.json', 'w') as file:
            json.dump([""], file, indent=4)
            file.close()
        with open('Reasoning\Probability_number.json', 'w') as file:
            json.dump([""], file, indent=4)
            file.close()
        with open('Reasoning\output.json', 'w') as file:
            json.dump([""], file)
            file.close()
        with open('Reasoning\Throughts.json', 'w') as file:
            json.dump([""], file)
            file.close()
    
            

    context = input_word
    
    # "<ignore>" prise en charge
    def Non_prise_des_before_ignore():
        nonlocal context
        if "<ignore>" in context:
            index_sequence = []
            for index, word in enumerate(context):
                if word == "<ignore>":
                    index_sequence.append(index)
            new_context = []
            index_de_depart = index_sequence[index_sequence.__len__() - 1] + 1
            index_self = context.__len__()
            for indice in range(index_de_depart, index_self):
                new_context.append(context[indice])
            context = []
            context = new_context  
    Non_prise_des_before_ignore()  
    print(context, "apres ignore")
    
    # Identification de l'instruction dans le prompt
    def identifier_prompt(context):
        global orientation_vers_prompt
        if "<prompt>" in context:
            index_sequence = []
            for index, word in enumerate(context):
                if word == "<prompt>":
                    index_sequence.append(index)
            new_context = []
            index_de_depart = index_sequence[index_sequence.__len__() - 1] + 1
            index_self = context.__len__()
            for indice in range(index_de_depart, index_self):
                new_context.append(context[indice])
                
            if "<end>" in new_context:
                orientation_vers_prompt = False
            else:
                orientation_vers_prompt = True
        else:
            orientation_vers_prompt = False
    identifier_prompt(context)


    # Reconstruction du prompt apres extraction <ignore>
    caractere = ""
    def Reconstruction_prompt(caractere):
        caractere = ""
        for token in context:
            if token == "<prompt>" or token == "<end>":
                pass
            else:  
                caractere += " " + token
        caractere = caractere.strip(" ")
        return caractere
    
    caractere = Reconstruction_prompt(caractere)
    caractere = word_tokenize(caractere)
    context = caractere
    input_word = caractere
    print(context, input_word, "contexte et input word apres reconstitutionm")
    
    with open(r'C:\Users\Jenovic Mwambay\Documents\Model GPM\model\vectors\GP-Model.json', encoding='utf-8-sig') as file:
       sequence_encode =  json.load(file)

    with open(r'C:\Users\Jenovic Mwambay\Documents\Model GPM\model\vectors\vecteur_multi_dimentionnel.json', 'r') as file:
        relation_sequence_forward_propagation = json.load(file)
    liste_sequence = []
    if orientation_vers_prompt == True and training_on_context == False:
        if text_add != data_of_live_training:
            data_of_training_on_prompt = Training_on_prompt(context, 22, [])
        sequence_encode = data_of_training_on_prompt['sequence_encode']
        relation_sequence_forward_propagation = data_of_training_on_prompt['vecteurs_forward']
    if training_on_context == True:
        if text_add != data_of_live_training:
            data_of_training_on_prompt = Training_on_prompt(text_add, 22, [])
        sequence_encode = data_of_training_on_prompt['sequence_encode']
        relation_sequence_forward_propagation = data_of_training_on_prompt['vecteurs_forward']
        
    if text_add != data_of_live_training:
        data_of_live_training = text_add
        
    input_word = input_word[len(input_word) - 1]
    word_unknown = input_word
    input_code = 0
    for embedding in sequence_encode:
        if embedding[0] == input_word:
            input_code = embedding[1]
            break
        
    for i in sequence_encode:
                liste_sequence.append(i[0])
    
    if input_code == 0:
        liste_temp = []
        if reaction == 1  and context.__len__() == 1:
            for i in sequence_encode:
                liste_temp.append(i[0])
            def find_closest_match(data_use, file_data):
                closest_match = difflib.get_close_matches(data_use, file_data, n=1,  cutoff=0.0)
                return closest_match[0] if closest_match else None
            result = find_closest_match(input_word, liste_temp)
            
            if result:
                vecteur_temporaire = " <ignore> " + result
                Model_results = {}
                Model_results["Probability"] =         [
                    "None 0.0",
                    "None 0",
                    "nothing 0.0",
                    "nothing 0.0",
                    "nothing 0.0",
                    "nothing 0.0",
                    "nothing 0.0",
                    "nothing 0.0",
                    "nothing 0.0",
                    "nothing 0.0"
                ]
                Model_results["Thoughts"] =         [
                    "None"
                ]
                Model_results["Sequence retained"] = vecteur_temporaire
                Model_results["Predictions"] =     [
                "nothing",
                "nothing"
            ]

                return Model_results
        else:
            pass
        
    #  Calcul de la distance entre sequence \\ Fonction
    def levenshtein_distance(str1, str2):                                                            
                    m = len(str1)
                    n = len(str2)
                    dp = [[0 for x in range(n + 1)] for x in range(m+1)]
                    for i in range (m+1):
                        for j in range(n+1):
                            if i ==0:
                                dp[i][j] = j
                            elif j == 0:
                                dp[i][j] = i
                            elif str1[i-1] == str2[j-1]:
                                dp[i][j] = dp[i-1][j-1]
                            else:
                                dp[i][j] = 1+ min(dp[i][j-1],
                                dp[i-1][j],
                                dp[i-1][j-1])
                        pourcentag = (dp[m][n]/max(m,n)*100)
                        return pourcentag
    if input_code == 0:
            liste_temp = []
            for i in sequence_encode:
                liste_temp.append(i[0])
            def find_closest_match(data_use, file_data):
                closest_match = difflib.get_close_matches(data_use, file_data, n=1,  cutoff=0.0)
                return closest_match[0] if closest_match else None
            result = find_closest_match(input_word, liste_temp)
            if result:
                if levenshtein_distance(input_word, result ) < niveau_comprehension:
                    input_word = result
                    for embedding in sequence_encode:
                        if embedding[0] == input_word:
                            input_code = embedding[1]
                            break
    
    primitive_context = context
    
    # Formatage du prompt
    for index, token in enumerate(context):
        if token not in liste_sequence:
            def find_closest_match(data_use, file_data):
                closest_match = difflib.get_close_matches(data_use, file_data, n=1,  cutoff=0.0)
                return closest_match[0] if closest_match else None
            result = find_closest_match(token, liste_sequence)
            if result:
                if levenshtein_distance(token, result ) < niveau_comprehension:
                    context[index] = result
    if_context_as_changed = 0
    if primitive_context != context:
        if_context_as_changed += 1
    else:
        if_context_as_changed = 0
    with open(r'C:\Users\Jenovic Mwambay\Documents\Model GPM\Reasoning\Prompt.json','w') as file:
        json.dump(context, file)
        file.close()
    if reaction == 1 and context.__len__() > 1:
        temp = ''
        for mot in context:
            temp += " " + mot
        vecteur_temporaire = ""
        vecteur_temporaire = " <ignore> " + temp
        Model_results = {}
        Model_results["Probability"] =         [
            "None 0.0",
            "None 0",
            "nothing 0.0",
            "nothing 0.0",
            "nothing 0.0",
            "nothing 0.0",
            "nothing 0.0",
            "nothing 0.0",
            "nothing 0.0",
            "nothing 0.0"
        ]
        Model_results["Thoughts"] =         [
            "None"
        ]
        Model_results["Sequence retained"] = vecteur_temporaire
        Model_results["Predictions"] =     [
        "nothing",
        "nothing"
    ]

        return Model_results
    if last_word != context[context.__len__() - 1] and last_word in context[context.__len__() - 1]:
        return_word = context[context.__len__() - 1].replace(last_word, "")
        return return_word.strip(" ")
    # Generer la sortie
    maximum_length = max_parameter
    nombre_recursion = 0
    rapport = 0
    output_2 = ""
    random_list = []
    observer = ''
    observer_2 = ""
    observer_antecedant = ""
    limitateur = 0
    removing = ""
    elements_predict_by_model = []
    antecedant_du_mot = []  
    stop_compteur = 0
    last_word = ""

        
    output_remember = []
    
    stationnement = 0
    try:
        def Generer_la_sortie(input_code, maximum_length_in_fuct):
                    nonlocal rapport
                    nonlocal setups
                    nonlocal recursion
                    nonlocal nombre_recursion
                    nonlocal output_2
                    nonlocal observer
                    nonlocal limitateur
                    nonlocal context
                    nonlocal stationnement
                    nonlocal last_word
                    nonlocal antecedant_du_mot
                    nonlocal observer_antecedant
                    nonlocal sequence_encode
                    nonlocal relation_sequence_forward_propagation
                    global orientation_vers_prompt
                    
                    def reset_settings():
                        nonlocal observer_2
                        nonlocal observer
                        nonlocal removing
                        nonlocal random_list
                        nonlocal elements_predict_by_model
                        nonlocal antecedant_du_mot
                        antecedant_du_mot = []  
                        observer = ''
                        removing = ""
                        observer_2 = ""
                        random_list = []
                        elements_predict_by_model = []
                    indice_context = 0
                                
                    
                    if rapport == 0:
                        output = input_word
                    max_word = 0
                    for index, vecteur in enumerate(relation_sequence_forward_propagation):
                        if maximum_length_in_fuct == max_word:
                            pass
                        reste = int(input_code) - int(vecteur[0]) 
                        for indice ,element in enumerate(sequence_encode):
                            
                            if element[1] == str(reste):
                                max_word += 1
                                if observer != element[0]:
                                    if limitateur == 1:
                                            elements_predict_by_model.append(element[0])

                                    if limitateur == 0: 
                                        if element[0] != input_word:  
                                            random_list.append(element[0])

                                    observer = element[0]
                            
                            def Find_antecedants(observer_antecedant):
                                nonlocal indice_context
                                nonlocal index
                                try:
                                    if element[0] == context[indice_context]  and element[0] not in antecedant_du_mot \
                                        and indice_context < len(context) and len(antecedant_du_mot) <= len(context):
                                        if observer_antecedant != element[0]:
                                            temp_vect = []
                                            if limitateur == 0:
                                                if indice_context <= len(context) - 1:
                                                    indice_context += 1
                                                temp_vect.append(sequence_encode[indice-1][0])
                                                temp_vect.append(context[indice_context - 1])
                                                antecedant_du_mot.append(temp_vect)
                                                observer_antecedant = element[0]
                                except IndexError:
                                    pass
                            Find_antecedants(observer_antecedant)
                            
                        with open(r'C:\Users\Jenovic Mwambay\Documents\Model GPM\Reasoning\random_list.json', 'w') as file:
                                                    json.dump(random_list, file, indent=4)
                                                    file.close()
                        with open(r'C:\Users\Jenovic Mwambay\Documents\Model GPM\Reasoning\antecedant.json', 'w') as file:
                                                    json.dump(antecedant_du_mot, file, indent=4)
                                                    file.close()
                    if random_list == [] and recursion <=1 and recursion == "back":
                        if recursion == 0:
                            TeDS_execution(setups)
                            recursion += 1
                        else:
                            recursion += 1
                            setups = {   "prompt": "",
                        "temperature" : temperature,
                        "maximum lenght" : maximum_length,
                        "reaction" : reaction,
                        "retroaction" : 1,
                        "reward" : 1,
                        "Level C" : niveau_comprehension,
                        "space" : automatic_space,
                        "training_on_context" : training_on_context,
                        "text_add" : text_add + "gpm",
                        "correction" : "",
                        "recursion" : recursion
                        

                    }
                            TeDS_execution(setups)
                            
                    # Creation d'un agent se chargeant de devier la generation lineaire
                    try:
                            class Agent_master:
                                def __init__(self, word) :
                                    self.word = word
                                    def Agent_random(word_parameter):
                                        nonlocal output
                                        nonlocal output_2
                                        nonlocal observer_2
                                        nonlocal removing
                                        recessivity = "pass"
                                        nonlocal last_word
                                        #print(random_list)
                                        int_number = random_list.__len__() - 1
                                        try: choice_word = random.randint(0, int_number)
                                        except ValueError :choice_word = random.randint(0, int_number + 1 )
                                        try:
                                            temporary = random_list[choice_word]
                                        except IndexError:
                                            temporary = element[0]
                                        if random_list.__len__() == 0:
                                            random_list == elements_predict_by_model
                                        try:
                                        # Predictionn en fonction du context
                                            def Thinking():
                                                    nonlocal context
                                                    vecteur_comptabilises = []
                                                    variable_comptablilisee = []
                                                    class Agent_de_verification:
                                                        def Module_de_verification(vecteur, indice_token, top, variable_comptablilisee ):
                                                            variable_comptablilisee.append(context[top])
                                                            variable_comptablilisee.append(vecteur[indice_token])
                                                            vecteur_comptabilises.append(variable_comptablilisee)
                                                            variable_comptablilisee = []
                                                            variable_comptablilisee.append(context[top-1])
                                                            variable_comptablilisee.append(vecteur[indice_token])
                                                            vecteur_comptabilises.append(variable_comptablilisee)
                                                            variable_comptablilisee = []
                                                            

                                                    element_integres = random_list
                                                    probability = {}
                                                    vecteurs_integres = []
                                                    if element_integres.__len__() != 100:
                                                        for word_context in context:
                                                            for vector in sequence_encode:
                                                                if vector[0] == word_context:
                                                                    vecteurs_integres.append(vector)
                                                    top = len(context)
                                                    top -= 1 
                                                    vad = False     
                                                    if  vad == True:                                             
                                                        for vecteur in vecteurs_integres:
                                                            for token in element_integres:

                                                                if token in vecteur:
                                                                    indice_token = vecteur.index(token)
                                                                    try:
                                                                        if str(vecteur[indice_token-2]).isdigit():
                                                                            if context[top] == vecteur[indice_token-1] and context[top-1] == vecteur[indice_token-3]:
                                                                                        if token not in probability:
                                                                                            probability[token] = 1
                                                                                            vecteurs_integres.append(token)
                                                                                            vecteurs_integres.append(word_context)
                                                                                        else:
                                                                                            
                                                                                            if context[top] and token not in vecteur_comptabilises:
                                                                                                    indice = probability[token]
                                                                                                    probability[token] = int(indice) + 1
                                                                                            Agent_de_verification.Module_de_verification(vecteur, indice_token, top, variable_comptablilisee)
                                                                                            
                                                                        else:       
                                                                            if context[top] == vecteur[indice_token-1] and context[top-1] == vecteur[indice_token-2]:
                                                                                        if token not in probability:
                                                                                            probability[token] = 1
                                                                                            vecteurs_integres.append(token)
                                                                                            vecteurs_integres.append(word_context)
                                                                                            
                                                                                        else:
                                                                                            if context[top] and token not in vecteur_comptabilises:
                                                                                                indice = probability[token]
                                                                                                probability[token] = int(indice) + 1
                                                                                            Agent_de_verification.Module_de_verification(vecteur, indice_token, top, variable_comptablilisee)
                                                                    except IndexError:
                                                                        try:
                                                                            if context[top] == vecteur[indice_token-1] and context[top-1] == vecteur[indice_token-2]:
                                                                                        if token not in probability:
                                                                                            probability[token] = 1
                                                                                            vecteurs_integres.append(token)
                                                                                            vecteurs_integres.append(word_context)
                                                                                        else:
                                                                                            if context[top] and token not in vecteur_comptabilises:
                                                                                                indice = probability[token]
                                                                                                probability[token] = int(indice) + 1
                                                                                            Agent_de_verification.Module_de_verification(vecteur, indice_token, top, variable_comptablilisee)
                                                                        except:
                                                                            pass
                                                                    finally:
                                                                            pass        
                                                                else:                   
                                                                    if token not in probability:
                                                                        probability[token] = 0
                                                    if probability == {}:
                                                        pass

                                                    with open(r'C:\Users\Jenovic Mwambay\Documents\Model GPM\Reasoning\Probability.json', 'w') as file:
                                                            json.dump(probability, file, indent=4)
                                                            file.close()
                                                    with open(r"C:\Users\Jenovic Mwambay\Documents\Model GPM\Reasoning\vecteurs_comp.json", 'w') as file:
                                                            json.dump(vecteur_comptabilises, file, indent=4)
                                                            file.close()
                                                            
                                                    # Calculer les probabilites liees a chaque mot identifier et selectioner le plus probable        
                                                    output_vecteur = []  
                                                    try:     
                                                        def Calcul_des_probabilites():
                                                            nonlocal output_vecteur
                                                            def Formule(cas_favorable, cas_possible):
                                                                probability_of = (cas_favorable / cas_possible) * 100
                                                                probability_of = round(probability_of, 2)
                                                                return probability_of
                                                                
                                                            all_are_possible = 0
                                                            dict_of_probability = {}
                                                            
                                                            # Trouver les cas possibles
                                                            for word, value in probability.items():
                                                                all_are_possible += value
                                                            if all_are_possible == 0:
                                                                all_are_possible += 1
                                                                
                                                            # Cas Fovorables
                                                            for word, value in probability.items():
                                                                dict_of_probability[word] = Formule(value, all_are_possible)
                                                            with open(r'C:\Users\Jenovic Mwambay\Documents\Model GPM\Reasoning\Probability_number.json', 'w') as file:
                                                                json.dump(dict_of_probability, file, indent=4)
                                                                file.close()
                                                                
                                                            # Analyse du contexte pour trouver des elements plus complexe  || Sujets, verbes...      
                                                            class Analyse_subject:
                                        
                                                                def Analyse_appronfodie_du_contexte():
                                                                    try:
                                                                        for mot, prob in dict_of_probability.items():
                                                                            for vecteur in sequence_encode :
                                                                                if mot == vecteur[0]:
                                                                                    if vecteur[2] in verbs:
                                                                                        for verb in verbs:
                                                                                            if verb == vecteur[2]:
                                                                                                if verb in context:
                                                                                                    for indice, word in enumerate(context):
                                                                                                        if word == verb:
                                                                                                            try:
                                                                                                                for vector in sequence_encode: # Couche supplementaure de confirmation du sujet
                                                                                                                    if vector[0] == context[indice-2]: # Mot precedent le supposé sujet = context[indice-2]
                                                                                                                        if vector[2] == mot:
                                                                                                                            liste_elements = []
                                                                                                                            liste_elements.append(context[indice-1])
                                                                                                                            liste_elements.append(mot)
                                                                                                                            return liste_elements
                                                                                                            except IndexError:
                                                                                                                return context[indice-1]
                                                                    except:
                                                                        pass
                                                                def jugement(resultat):
                                                                    if resultat != None:
                                                                        Analyse_subject.Action(resultat)
                                                                    else:
                                                                        return "Zero"
                                                                def Action(result_of_ana):
                                                                    temp = 0
                                                                    for cle, valeur in dict_of_probability.items():
                                                                        if cle == result_of_ana[1]:
                                                                            temp = valeur
                                                                            break
                                                                    del dict_of_probability[result_of_ana[1]]
                                                                    dict_of_probability[result_of_ana[0]] = temp
                                                                    with open(r'C:\Users\Jenovic Mwambay\Documents\Model GPM\Reasoning\Probability_number.json', 'w') as file:
                                                                        json.dump(dict_of_probability, file, indent=4)
                                                                        file.close()
                                                                    
                                                                
                                                            result_of_analyse = Analyse_subject.jugement(Analyse_subject.Analyse_appronfodie_du_contexte())       
                                                            
                                                            def FeedBack_Analysis():
                                                                if reward == 0:
                                                                    pass
                                                            
                                                            # Attention portée sur les mots et calculs des probabilités
                                                            def somme_des_probabilite():
                                                                
                                                                result_somme = []
                                                                somme = 0
                                                                for cle, value in dict_of_probability.items():
                                                                    somme+=value
                                                                if context.__len__() > 1:
                                                                    score_vecteur = {}
                                                                    indexVecteur = []
                                                                    vecteur_context = []
                                                                    for index, vect in enumerate(sequence_encode):
                                                                        if vect[0] == context[0]:
                                                                            indexVecteur.append(index)
                                                                    
                                                                    for indice in indexVecteur:
                                                                        score_vecteur[indice] = 0
                                                                        
                                                                    for indice in indexVecteur:
                                                                        for word in context:
                                                                            if word in sequence_encode[indice]:
                                                                                for cle, valeur in score_vecteur.items():
                                                                                    if cle == indice:
                                                                                        score_vecteur[cle] = valeur+1
                                                                    grande_valeur = 0
                                                                    position_retenu = 0
                                                                    for cle, valeur in score_vecteur.items():
                                                                        if valeur > grande_valeur:
                                                                            grande_valeur = valeur
                                                                    for cle, valeur in score_vecteur.items():
                                                                        if valeur == grande_valeur:
                                                                            position_retenu = cle
                                                                    
                                                                    with open(r'C:\Users\Jenovic Mwambay\Documents\Model GPM\Reasoning\Context_vecteurs.json', 'w') as file:
                                                                        json.dump(sequence_encode[position_retenu], file, indent=4)
                                                                        file.close()
                                                                        
                                                                    # Trouver toutes les representations des tokens du context si le prompt est correctement saisi      
                                                                    def Trouver_les_vecteurs_context():        
                                                                        for ind, mot in enumerate(context):
                                                                            for indice, vecteur in enumerate(sequence_encode):
                                                                                try:
                                                                                    if mot == vecteur[0] and context[ind+1] == vecteur[2] and context[ind+2] == vecteur[3] and context[ind+3] == vecteur[4] and  context[ind+4] == vecteur[5] and context[ind+5] == vecteur[6] and context[ind+6] == vecteur[7]:
                                                                                        for i in range(context.__len__()):  
                                                                                            vecteur_context.append(sequence_encode[indice])
                                                                                            indice+=1
                                                                                except:
                                                                                    try:
                                                                                        if mot == vecteur[0] and context[ind+1] == vecteur[2] and context[ind+2] == vecteur[3] and context[ind+3] == vecteur[4] and context[ind+4] == vecteur[5] and context[ind+5] == vecteur[6]:
                                                                                            for i in range(context.__len__()):  
                                                                                                vecteur_context.append(sequence_encode[indice])
                                                                                                indice+=1
                                                                                    except:
                                                                                        try:
                                                                                            if mot == vecteur[0] and context[ind+1] == vecteur[2] and context[ind+2] == vecteur[3] and context[ind+3] == vecteur[4] and context[ind+4] == vecteur[5]:
                                                                                                for i in range(context.__len__()):  
                                                                                                    vecteur_context.append(sequence_encode[indice])
                                                                                                    indice+=1
                                                                                        except:
                                                                                            try:
                                                                                                if mot == vecteur[0] and context[ind+1] == vecteur[2] and context[ind+2] == vecteur[3] and context[ind+3] == vecteur[4]:
                                                                                                    for i in range(context.__len__()):  
                                                                                                        vecteur_context.append(sequence_encode[indice])
                                                                                                        indice+=1
                                                                                            except:
                                                                                                try:
                                                                                                    if mot == vecteur[0] and context[ind+1] == vecteur[2] and context[ind+2] == vecteur[3]:
                                                                                                        for i in range(context.__len__()):  
                                                                                                            vecteur_context.append(sequence_encode[indice])
                                                                                                            indice+=1
                                                                                                except:
                                                                                                    try:                                                                                        
                                                                                                        if mot == vecteur[0] and context[ind+1] == vecteur[2]:
                                                                                                            for i in range(context.__len__()):  
                                                                                                                vecteur_context.append(sequence_encode[indice])
                                                                                                                indice+=1
                                                                                                    except:
                                                                                                        try:
                                                                                                            if mot == vecteur[0]:
                                                                                                                for i in range(context.__len__()):  
                                                                                                                    vecteur_context.append(sequence_encode[indice])
                                                                                                                    indice+=1
                                                                                                        except:
                                                                                                            pass
                                                                                        
                                                                            break
                                                                                        
                                                                                        
                                                                        with open(r'C:\Users\Jenovic Mwambay\Documents\Model GPM\Reasoning\Nouveau_vecteurs.json', 'w') as file:
                                                                            json.dump(vecteur_context, file, indent=4)
                                                                            file.close()
                                                                Trouver_les_vecteurs_context()
                                                                use_context_illusoire = False
                                                                # Si Le prompt n'est pas correctement saisi la fonction self attention entre en jeu pour construire un 
                                                                # Context illusoire à partir des mots cles
                                                                def Self_Attention():
                                                                    comp = 0
                                                                    if vecteur_context == []:
                                                                        use_context_illusoire = True
                                                                        for i in range(position_retenu, len(sequence_encode)):
                                                                            comp += 1
                                                                            vecteur_context.append(sequence_encode[i])
                                                                            if sequence_encode[i][0] == context[-1] and comp >= len(context):
                                                                                break
                                                                            
                                                                        def Creation_du_context_illusoire():
                                                                            context_illusoire = []
                                                                            for vecteur in vecteur_context:
                                                                                context_illusoire.append(vecteur_context[0])
                                                                            return context_illusoire
                                                                                
                                                                        with open(r'C:\Users\Jenovic Mwambay\Documents\Model GPM\Reasoning\Nouveau_vecteurs.json', 'w') as file:
                                                                            json.dump(vecteur_context, file, indent=4)
                                                                            file.close()
                                                                Self_Attention()
                                                                
                                                                with open(r"C:\Users\Jenovic Mwambay\Documents\Model GPM\training data\RL\Poids.json", 'r') as file:
                                                                    poids = json.load(file)
                                                                    file.close()
                                                                
                                                                distribution = {}
                                                                if use_context_illusoire == True:
                                                                    pass
                                                                else:
                                                                    context_illusoire = context
                                                                for unite in random_list:
                                                                    distribution[unite] = 0
                                                                for mot in random_list:
                                                                    ref = 2
                                                                    compteur = 0
                                                                    for i in range(len(vecteur_context)-1, 0, -1):
                                                                        if compteur == 0:
                                                                            compteur+=1
                                                                            poid = 0
                                                                            if mot in vecteur_context[i]:
                                                                                poid += poids["layer1"]
                                                                                if vecteur_context[i][2] == mot or mot !="jhgfds":
                                                                                    poid+=  poids["layer2"]
                                                                                    if vecteur_context[i-1][3] == mot:
                                                                                        poid+= poids["layer3"]
                                                                                        if vecteur_context[i-2][4] == mot:
                                                                                            poid+= poids["layer4"]
                                                                                            if vecteur_context[i-3][5] == mot:
                                                                                                poid+= poids["layer5"]
                                                                                                if vecteur_context[i-4][6] == mot:
                                                                                                    poid+= poids["layer6"]
                                                                            for cle, valeur in distribution.items():
                                                                                if cle == mot:
                                                                                    distribution[cle] = valeur + poid
                                                                                    
                                                                        else:
                                                                            if mot in vecteur_context[i]:
                                                                                if vecteur_context[i][ref] == mot:
                                                                                    for cle, valeur in distribution.items():
                                                                                        if cle == mot:
                                                                                            distribution[cle] = valeur + ref
                                                                                            ref+=1
                                                                                            
                                                                                else:
                                                                                    for cle, valeur in distribution.items():
                                                                                        if cle == mot:
                                                                                            distribution[cle] = valeur + 0.5  
                                                                                            ref+=1   
                                                                            if ref == 6:
                                                                                break     
                                                                                                                                 
                                                                return distribution
                                                            score_des_mots = somme_des_probabilite()
                                                            with open(r'C:\Users\Jenovic Mwambay\Documents\Model GPM\Reasoning\Probability_number.json', 'w') as file:
                                                                json.dump(score_des_mots, file, indent=4)
                                                                file.close()
                                                            dict_of_probability = score_des_mots
                                                            print("\n\n\n\n", score_des_mots,context, "\n\n\n\n\n")
                                                            with open(r'C:\Users\Jenovic Mwambay\Documents\Model GPM\Reasoning\Word_score.json', 'w') as file:
                                                                json.dump(score_des_mots, file, indent=4)
                                                                file.close()

                                                                                    
                                                            def select_word():
                                                                big_value = 0
                                                                for word, valeur in dict_of_probability.items():
                                                                    if valeur > big_value:
                                                                        big_value = valeur
                                                                secand_valeur = 0
                                                                for word, valeur in dict_of_probability.items():
                                                                    if valeur > secand_valeur and valeur != big_value and valeur > 5.0:
                                                                        secand_valeur = valeur
                                                                        
                                                                valeur_3_sortie = 0 
                                                                for word, valeur in dict_of_probability.items():
                                                                    if valeur > valeur_3_sortie and valeur != big_value and valeur != secand_valeur:
                                                                        valeur_3_sortie = valeur
                                                                
                                                                list_integration = []
                                                                                            
                                                                
                                                                # Agent de tri numero 1
                                                                def Agent_de_tri_1():
                                                                    nonlocal output_vecteur
                                                                    nonlocal list_integration
                                                                    for word, value in dict_of_probability.items():
                                                                        if value == big_value:
                                                                            list_integration.append(word)
                                                                            list_integration.append(big_value)
                                                                            output_vecteur.append(list_integration)
                                                                            list_integration = []
                                                                            break
                                                                        
                                                                    for word, value in dict_of_probability.items():
                                                                        if value == big_value and word not in output_vecteur[0]:
                                                                                    list_integration.append(word)
                                                                                    list_integration.append(value)
                                                                                    output_vecteur.append(list_integration)
                                                                                    list_integration = []
                                                                Agent_de_tri_1()

                                                                # Agent de tri numero 2
                                                                def Agent_de_tri_2():
                                                                    nonlocal output_vecteur
                                                                    nonlocal list_integration       
                                                                    for word, value in dict_of_probability.items():
                                                                        if value == secand_valeur:
                                                                            list_integration.append(word)
                                                                            list_integration.append(secand_valeur)
                                                                            output_vecteur.append(list_integration)
                                                                            list_integration = []
                                                                            break
                                                                        
                                                                    for word, value in dict_of_probability.items():
                                                                        if value == secand_valeur and word not in output_vecteur[1]:
                                                                                    list_integration.append(word)
                                                                                    list_integration.append(value)
                                                                                    output_vecteur.append(list_integration)
                                                                                    list_integration = []
                                                                Agent_de_tri_2()

                                                                # Agent de tri numero 3
                                                                def Agent_de_tri_3():
                                                                    nonlocal output_vecteur
                                                                    nonlocal list_integration
                                                                    
                                                                    for word, value in dict_of_probability.items():
                                                                        if value == valeur_3_sortie:
                                                                            list_integration.append(word)
                                                                            list_integration.append(value)
                                                                            output_vecteur.append(list_integration)
                                                                            list_integration = []
                                                                
                                                                    for word, value in dict_of_probability.items():
                                                                        if value == valeur_3_sortie and word not in output_vecteur[2]:
                                                                                    list_integration.append(word)
                                                                                    list_integration.append(value)
                                                                                    output_vecteur.append(list_integration)
                                                                                    list_integration = []
                                                                #Agent_de_tri_3()
                                                                
                                                                with open(r'C:\Users\Jenovic Mwambay\Documents\Model GPM\Reasoning\output.json', 'w') as file:
                                                                    json.dump(output_vecteur, file)
                                                                    file.close()
                                                            select_word()
                                                    except:
                                                        pass      
                                                    Calcul_des_probabilites()
                                                    
                                                    # Fonction qui reparti les mots selon leurs niveaux de pertinence // repartition_des_mots //
                                                    def repartition_des_mots():
                                                        final_distribution = {}
                                                        nonlocal output_vecteur
                                                        cont = 0
                                                        first_value = output_vecteur[0][1]
                                                        temp_1 = []
                                                        temp_2 = []
                                                        temp_3 = []
                                                        for unite in output_vecteur:
                                                            if int(unite[1]) == int(first_value):
                                                                temp_1.append(unite[0])
                                                            if unite[1] !=  first_value and unite[1] > 2:
                                                                cont = unite[1]
                                                                temp_2.append(unite[0])
                                                            if unite[1] <3:
                                                                temp_3.append(unite[0])
                                                        final_distribution['les plus probables'] = temp_1
                                                        final_distribution['moyennement probables'] = temp_2
                                                        final_distribution['les moins probables'] = temp_3 
                                                        with open(r'C:\Users\Jenovic Mwambay\Documents\Model GPM\Reasoning\distribution.json', 'w') as file:
                                                            json.dump(final_distribution, file, indent=4)
                                                            file.close()
                                                        
                                                        sortie = final_distribution['les plus probables']
                                                        sortie_2 = final_distribution['moyennement probables']
                                                        
                                                        if len(sortie) > 1:
                                                            nombre_de_sortie = sortie.__len__()
                                                            nombre_de_sortie -= 1
                                                            nombre_aleatoire = random.randint(0, nombre_de_sortie)
                                                            sortie_aleatoire = sortie[nombre_aleatoire]
                                                        if len(sortie) > 1:
                                                            return sortie_aleatoire
                                                        else:
                                                            return sortie[0]
                                                        
                                                    return repartition_des_mots()
                                        except (ZeroDivisionError, IndexError) as e:
                                            pass
                                        if context.__len__() > 1:
                                            final_decision = Thinking()
                                        else:
                                            final_decision = random_list[choice_word]
                                        with open(r'C:\Users\Jenovic Mwambay\Documents\Model GPM\Reasoning\distribution.json', 'r') as file:
                                            possibilites = json.load(file)
                                            
                                        def Thoughts(enter_possibilites):
                                            for partition, word in enter_possibilites.items():
                                                if partition == 'les plus probables':
                                                    alpha = word
                                                if partition == 'moyennement probables':
                                                    beta = word
                                            context_of_thoughts = context
                                            try:
                                                pas_1 = context_of_thoughts[len(context_of_thoughts) - 2]
                                            except:pass
                                            try:
                                                pas_2 = context_of_thoughts[len(context_of_thoughts) - 3]
                                            except: pass
                                            liste_provisoire = []
                                            for i in sequence_encode:
                                                for j in alpha:
                                                    if i[0] == pas_2 and i[2] == pas_1 and i[3] == context_of_thoughts[len(context_of_thoughts) - 1]  and i[4] == j:
                                                        if j not in liste_provisoire:
                                                            liste_provisoire.append(j)
                                                    if i[0] == pas_1 and i[2] == context_of_thoughts[len(context_of_thoughts) - 1] and i[3] == j :
                                                        if j not in liste_provisoire:
                                                            liste_provisoire.append(j)
                                                        
                                                for j in beta:
                                                    if i[0] == pas_2 and i[2] == pas_1 and i[3] == context_of_thoughts[len(context_of_thoughts) - 1]  and i[4] == j:
                                                        if j not in liste_provisoire:
                                                            liste_provisoire.append(j)
                                                    if i[0] == pas_1 and i[2] == context_of_thoughts[len(context_of_thoughts) - 1] and i[3] == j :
                                                        if j not in liste_provisoire:
                                                            liste_provisoire.append(j)
                                                
                                                def probability_function():
                                                    probability = {}
                                                    if liste_provisoire.__len__() > 1:
                                                        for word_context in context:
                                                            for vector in range(sequence_encode.__len__()):
                                                                if sequence_encode[vector][0] == word_context:
                                                                    for token in liste_provisoire:
                                                                        if token in sequence_encode[vector] and context[context.__len__() - 1] in sequence_encode[vector] and  context[context.__len__() - 2] in sequence_encode[vector]:
                                                                            if token not in probability:
                                                                                probability[token] = 1
                                                                                
                                                                            else:
                                                                                indice = probability[token]
                                                                                probability[token] = int(indice) + 1
                                                                    vector = sequence_encode.__len__()

                                                        
                                            with open(r'C:\Users\Jenovic Mwambay\Documents\Model GPM\Reasoning\Thoughts.json', 'w') as file:
                                                    json.dump(liste_provisoire, file, indent=4)
                                                    file.close()
                                            with open(r'C:\Users\Jenovic Mwambay\Documents\Model GPM\Reasoning\output.json') as file:
                                                distribution = json.load(file)
                                                file.close()
                                            return liste_provisoire
                                        
                                        
                                        try:
                                            # Selection en fonction de la distribution faite par les 3 agents
                                            def Reference_a_la_distribution_thinking():
                                                nonlocal stop_compteur
                                                nonlocal final_decision
          
                                                with open(r'C:\Users\Jenovic Mwambay\Documents\Model GPM\Reasoning\distribution.json') as file_output:
                                                            words_probable = json.load(file_output)
                                                            if temperature > 0.5 and words_probable["moyennement probables"].__len__() > 0 and temperature < 0.8:
                                                                words_probable = words_probable["moyennement probables"]
                                                            elif temperature >= 0.8 and words_probable["les moins probables"].__len__() > 0:
                                                                words_probable = words_probable["les moins probables"]
                                                            else:
                                                                if temperature > 0.5 and temperature < 0.8 and words_probable["moyennement probables"].__len__() == 0:
                                                                    if words_probable["les moins probables"].__len__() > 0:
                                                                        words_probable = words_probable["les moins probables"]
                                                                elif temperature >= 0.8 and words_probable["les moins probables"].__len__() == 0:
                                                                    if ["moyennement probables"].__len__() > 0:
                                                                        words_probable = words_probable["moyennement probables"]
                                                                else:
                                                                    words_probable = words_probable["les plus probables"]
                                                            file_output.close()
                                                            if words_probable.__len__() > 1:
                                                                tirer_au_sort = random.randint(0, words_probable.__len__()-1)
                                                                final_decision = words_probable[tirer_au_sort]
                                                            else:
                                                                final_decision = words_probable[0]
                                            Reference_a_la_distribution_thinking()
                                            
                                        except IndexError: 
                                            
                                            # Selection en fonction des calculs du Thoughts \\ si la fonction thinking ne repond pas
                                            def Selection_fonction_du_thoughts():  
                                                selection_in_Thoughts = Thoughts(possibilites)
                                                try:
                                                    index_au_sort = selection_in_Thoughts.__len__() - 1
                                                    index_au_sort = random.randint(0, index_au_sort)
                                                    tire_au_sort = selection_in_Thoughts[index_au_sort]
                                                    selection_in_Thoughts = tire_au_sort
                                                except:
                                                    selection_in_Thoughts = selection_in_Thoughts[0]
                                                return selection_in_Thoughts
                                            
                                            final_decision = Selection_fonction_du_thoughts()
                                            
                                        except:
                                            final_decision = random_list[choice_word]
                                            
                                        if context.__len__() == 1:
                                            final_decision = random_list[choice_word] 
                                        
                                        Reference_a_la_distribution_thinking()
                                        if context.__len__() == 1:
                                            final_decision = random_list[choice_word] 
                                            print(final_decision)
                                            
                                        if observer_2 != final_decision and limitateur == 0 and context[context.__len__() - 1] != final_decision:
                                            if final_decision !='<stop>':
                                                last_word = final_decision
                                                if final_decision == ".":
                                                    output_2 = output_2+ final_decision
                                                else:
                                                    print(output_2, "avant")
                                                    output_2 = output_2 + " " + final_decision
                                                if automatic_space == False:
                                                    output_2 = str(output_2).strip(" ")
                                                    output_2 += " "
                                                print(output_2, "apres")
                                        print(output_2, "premier level", final_decision)
                                        output_2 = " " +final_decision
                                                
                                                
                                        observer_2 = final_decision
                                        output = output + " " +  final_decision
                                        def find_embeding():
                                            nonlocal input_code
                                            input_word = final_decision
                                            for embeding in sequence_encode:
                                                if embeding[0] == input_word:
                                                    input_code = embeding[1]
                                                    break
                                        find_embeding()
                                        return output
                                    self.word = Agent_random(word)
                                    print(output_2, "deuxieme level")

                    except IndexError:
                            stationnement += 1
                            if stationnement < 5:
                                Generer_la_sortie(input_code, maximum_length)
                    complete_output = Agent_master(random_list)
                    add_word = complete_output.word
                    nombre_recursion += 1
                    """                for i in random_list:
                        random_list.remove(i)"""
                    reference_stop = output_2.split()
                    reference_stop = reference_stop[len(reference_stop) - 1]
                    if nombre_recursion < maximum_length and last_word != "." and nombre_recursion == 2345:
                        reset_settings()
                        out = output_2.split()
                        if out.__len__() < 2:
                            out = out[0]
                        else:
                            out = out[out.__len__() - 1]
                        context.append(out)
                        stationnement = 0
                        Generer_la_sortie(input_code, maximum_length)
                    if limitateur != 1:
                        limitateur += 1
                        stationnement = 0
                        Generer_la_sortie(input_code, maximum_length)
                        print(output_2, "troisieme level")

        Generer_la_sortie(input_code, maximum_length)
        
        # Fonction de deviation
        def Deviation():
            global compteur_sequence
            nonlocal output_2
            nonlocal stop_compteur
            with open(r"C:\Users\Jenovic Mwambay\Documents\Model GPM\Reasoning\Probability_number.json") as file:
                data_probability = json.load(file)
                file.close()
            historique_prob[f"sequence {compteur_sequence}"] = data_probability
            compteur_sequence += 1
            if compteur_sequence > 1:
                probability_temp = historique_prob[f"sequence {compteur_sequence - 2}"]

                with open(r"C:\Users\Jenovic Mwambay\Documents\Model GPM\Reasoning\Probability_number_temp.json", 'w') as file:
                        json.dump(probability_temp, file, indent=4)
                        file.close()
                with open(r"C:\Users\Jenovic Mwambay\Documents\Model GPM\Reasoning\historique_prob.json", 'w') as file:
                        json.dump(historique_prob, file, indent=4)
                        file.close()

            if compteur_sequence > 1:
                try:
                    data_probability_temp = probability_temp
  
                    class Agent_of_deviation:
                        with open(r"C:\Users\Jenovic Mwambay\Documents\Model GPM\Reasoning\Probability_number.json") as file:
                            data_probability = json.load(file)
                            file.close()
                        def __init__(self, data, probability) -> None:
                            self.probability = probability
                            self.data = data
                            
                        def Reflechir():                               
                            temp = {}
                            if len(data_probability) == len(data_probability_temp):
                                for element in data_probability:
                                    if int(data_probability[element]) > int(data_probability_temp[element]):
                                        temp[element] = data_probability[element]
                                                                            
                            return temp
                        
                        def Argumenter():
                            data_of_action_precedent = Agent_of_deviation.Reflechir()
                            temp_value = 0
                            for cle, value in data_of_action_precedent.items():
                                if value > temp_value:
                                    temp_value = value
                            valeur_retenu = ""
                            for element, prob in data_of_action_precedent.items():
                                if prob == temp_value:
                                    valeur_retenu = element  
                                    return valeur_retenu

                        def Verdict(argument):
                            if argument != None:
                                return argument
                            else:
                                return "Nothing"
                except (KeyError, IndexError):
                    pass
                try:
                    agent_action = Agent_of_deviation.Argumenter()
                    agent_verdict = Agent_of_deviation.Verdict(agent_action)
                    if agent_verdict != "Nothing":
                        output_2 = agent_verdict
                        print(agent_verdict)
                except:
                    pass
        Deviation()
        
        stationnement = 0
        word_retained = ""
        try : 
                if removing != "" :
                    random_list.remove(removing)  
        except: 
                pass
        history.append(output_2)
        word_retained =output_2
        print(output_2)
        Model_results = {}
        liste_des_probabilites = []
        with open(r'C:\Users\Jenovic Mwambay\Documents\Model GPM\Reasoning\output.json') as file:
            probabilite_des_mots_possible = json.load(file)
        if os.path.exists(r"C:\Users\Jenovic Mwambay\Documents\Model GPM\Reasoning\Thoughts.json"):
            with open(r'C:\Users\Jenovic Mwambay\Documents\Model GPM\Reasoning\Thoughts.json') as file:
                elements_du_thoughts = json.load(file)
        else:
            elements_du_thoughts = ["none"]
            for i in probabilite_des_mots_possible:
                liste_des_probabilites.append(i[0] + " " + str(i[1]))
            file.close()
        
        
        Model_results["Probability"] = liste_des_probabilites
        Model_results["Thoughts"] = elements_du_thoughts
        Model_results["Sequence retained"] = word_retained
        Model_results["Predictions"] = elements_predict_by_model
        Model_results["Supposition"] = context
        output_remember.append(output_2)
        with open(r"C:\Users\Jenovic Mwambay\Documents\Model GPM\Labs\Model results.json", 'w') as file:
            json.dump(Model_results, file, indent=4)
            file.close()
        orientation_vers_prompt = True
        return Model_results
    
    except TabError as error_sending:
        texte_contexte = ""
        index = len(context) - 1
        i = -1
        for mot in context:
            i +=1
            if mot != word_unknown and i != index:
                texte_contexte += " " + mot
            
        Model_results = {}
        Model_results["Probability"] =         [
            "None 0.0",
            "None 0",
            "nothing 0.0",
            "nothing 0.0",
            "nothing 0.0",
            "nothing 0.0",
            "nothing 0.0",
            "nothing 0.0",
            "nothing 0.0",
            "nothing 0.0"
        ]
        Model_results["Thoughts"] =         [
            "None"
        ]
        Model_results["Sequence retained"] = " "
    
        Model_results["Predictions"] =     [
        "nothing",
        "nothing"
    ]
        print( f" Erreur rencontree lors du traitement, code 001 : (" + str(error_sending) + f") Unknown this word '{word_unknown}' <ignore> {texte_contexte} ")
        return Model_results

