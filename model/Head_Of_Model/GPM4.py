# !!/usr/bin/python
# -*- coding: latin -*-
import os
import sys
chemin_parent = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(chemin_parent)
import random
import os
import json
import difflib
from nltk.tokenize import word_tokenize
from threading import Thread
from Neural_layers.probEngine import ProbEngineNeural
from Neural_layers.Troughts_Neural import Thoughts
from Neural_layers.training_neural import Training_on_prompt
from Training.Training_GPM import TeDS_Training
from Neural_layers.logical_neuron import logicalFunction
from Neural_layers.logic_math import LogicAgent
from icecream import ic

comp_itera = 0

historique_prob                     = {}
compteur_sequence                   = 0
verbs                               = ["est","ai", "es", "a"]
probability_temp                    = {}
input_word_help                     = ""
top                                 = 0
orientation_vers_prompt             = True
data_of_live_training               = ""
data_of_training_on_prompt          = []
compteur_des_recompences_negatives  = 0
history_prompt                      = []
elementDeRecursion                  = {}
predict                             = False
tokens_vector                       = []
classe                              = None
operation                           = ['+', '-', '/', '*']


def GPM4_Head(setups):

    def reset_op():
        global historique_prob, compteur_sequence, probability_temp, input_word_help, top, orientation_vers_prompt, data_of_live_training, data_of_training_on_prompt, compteur_des_recompences_negatives, history_prompt,\
            elementDeRecursion, predict, tokens_vector, classe, operation
        historique_prob                     = {}
        compteur_sequence                   = 0
        verbs                               = ["est","ai", "es", "a"]
        probability_temp                    = {}
        input_word_help                     = ""
        top                                 = 0
        orientation_vers_prompt             = True
        data_of_live_training               = ""
        data_of_training_on_prompt          = []
        compteur_des_recompences_negatives  = 0
        history_prompt                      = []
        elementDeRecursion                  = {}
        predict                             = False
        tokens_vector                       = []
        classe                              = None
        operation                           = ['+', '-', '/', '*']

    
    
    global compteur_des_recompences_negative, tokens_vector, classe, comp_itera
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
    reinforcement_learning = setups["RL"]
    recursivite = setups["recursivite"]
    EngineState = setups["EngineState"]  
    fenetre_context = setups['fenetre_context']

    if input_word.split() == []:
                vecteur_temporaire = "Hello i am GPM ! write something here before to call me <ignore> "
                Model_results = {}
                classe = "Error"
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
                Model_results['Class'] = classe

                return Model_results

    path_temp = chemin_parent.replace("\model", "")
    with open(rf"{path_temp}\config\setups", "w") as f:
        json.dump(setups, f, indent=4)
        f.close()
    
    def RewardsManager():
        global compteur_des_recompences_negatives
        if reinforcement_learning == True:
            if reward == 0:
                compteur_des_recompences_negatives += 1
                if compteur_des_recompences_negatives > 2:
                    if history_prompt[-1] == 0 and history_prompt[-2] == 0:
                        thread8 = Thread(target=lambda: TeDS_Training() )
                        thread8.start()
        history_prompt.append(reward)
                   
    RewardsManager()

    global input_word_help
    global data_of_training_on_prompt
    global data_of_live_training
    global top
    global orientation_vers_prompt
    #print("AMORCAGE...")
    
    text_add = word_tokenize(str(text_add))

    if top == 0:
        input_word_help = input_word
        top += 1

    
    input_word = input_word.split()
    
    def fenetre_de_context(fenetre):
        if len(input_word) <= fenetre:
            return input_word
        temp = []
        for i in range(len(input_word) - 1, 0, -1):
            temp.append(input_word[i])
            if len(temp) == fenetre:
                break
        return temp[::-1]
    
    input_word = fenetre_de_context(fenetre_context)
    
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
    
    with open(rf'{chemin_parent}\vectors\GP-Model.json', encoding='utf-8-sig') as file:
       sequence_encode =  json.load(file)
       base_sequences = sequence_encode
       file.close()

    with open(rf'{chemin_parent}\vectors\vecteur_multi_dimentionnel.json', 'r') as file:
        relation_sequence_forward_propagation = json.load(file)
        base_vectors = relation_sequence_forward_propagation
        file.close()
        
    liste_sequence = []
    if orientation_vers_prompt == True and training_on_context == False:
        if text_add != data_of_live_training:
            data_of_training_on_prompt = Training_on_prompt(context, 22, [])
        sequence_encode = data_of_training_on_prompt['sequence_encode']
        relation_sequence_forward_propagation = data_of_training_on_prompt['vecteurs_forward']
    if training_on_context == True:
        if text_add != data_of_live_training:
            data_of_training_on_prompt = Training_on_prompt(text_add, 22, [])
        #print(data_of_training_on_prompt)
        sequence_encode = data_of_training_on_prompt['sequence_encode']
        relation_sequence_forward_propagation = data_of_training_on_prompt['vecteurs_forward']
        
    if text_add != data_of_live_training:
        data_of_live_training = text_add
    try:
        input_word = input_word[-1]
    except IndexError:
                vecteur_temporaire = "Hello i am GPM ! write something here before to call me <ignore> "
                Model_results = {}
                classe = "Error"
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
                Model_results['Class'] = classe

                return Model_results
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
                Model_results['Class'] = classe

                return Model_results
        else:
            pass
        
        
    
    # Tokenisation avancée pour Le module logique.
    def Advenced_tokenization(context):
        liste = []
        last_token = context[-1]
        comp = 0
        result_after_equal = False
        temp = ''

        for token in last_token:
            comp += 1
            if token in operation or token == '=':
                liste.append(temp)
                temp = ''
                
            temp += token
            if temp in operation:
                liste.append(temp)
                temp = ''
                
            if token == '=':
                liste.append(token)
                result_after_equal = True
                break
            
        if result_after_equal and comp < len(last_token):  
            liste_temp = last_token[comp:]
            temp = ''
            #print("liste temp : ", liste_temp)
            for char in liste_temp:
                temp += char
            
            liste.append(temp)
        #print("Advenced_tokenization : ", liste)
        try:
            if str(last_token[-1]).isdigit() and str(last_token[-2]) in operation:
                liste.append(last_token[-1])

            if liste[-1] != '=' and str(liste[-1]).isdigit() and str(liste[-1]).isdigit() and str(liste[-2]) in operation and str(liste[-3]).isdigit():
                liste.append('=')
        except IndexError:
            pass
        #print("Advenced_tokenization : ", liste)

        return liste


    # Tenter d'appeler la fonction Logic
    # fonction qui  va tenter un appel à la fonction logique en testant différentes possibilités pour faire effectuer les calculs .    
    def Call_logical_function(context):
        try:
            agent = LogicAgent(context)
            resultat = agent.solve_math()
                    ##print(logicalFunction(context[-1], context))
            vecteur_temporaire =  resultat
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
            Model_results["Sequence retained"] = str(vecteur_temporaire) + " <ignore> "
            Model_results["Predictions"] =     [
                    "nothing",
                    "nothing"
                ]
            classe = 'Reasoning'
            Model_results['Class'] = classe
                    #ic(Model_results)
            #print("FIN ET RENVOI : ", vecteur_temporaire)
            
            if vecteur_temporaire:
                return Model_results
        
        except:
            pass
        
        
        try:
            int(context[-1])
            validation = True
        except ValueError:
            try:
                float(context[-1])
                validation = True
            except:
                validation = False
        except:
            validation = False
        try:
            if context[-1] == '=' or list(context[-1])[-1] == '=' or context[-1].isdigit() or validation == True:
                ##print(context[-1], context)
                if context[0] in operation :
                    del context[0]
                if str(context[0]).isdigit() and context[1].isdigit():
                    del context[0]
                
                try:result_logic =  logicalFunction(context[-1], context, validation)
                except SyntaxError: return False
                if not result_logic:
                    return False
                else:
                    
                    ##print(logicalFunction(context[-1], context))
                    vecteur_temporaire =  result_logic
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
                    Model_results["Sequence retained"] = str(vecteur_temporaire)
                    Model_results["Predictions"] =     [
                    "nothing",
                    "nothing"
                ]
                    classe = 'Logic Math'
                    Model_results['Class'] = classe
                    #ic(Model_results)
                    #print("FIN ET RENVOI : ", vecteur_temporaire)
                    return Model_results
        except IndexError:
            return False
            
    # Si appel reussi renvoyer le reultat
    result_of_call = Call_logical_function(context)
    if type(result_of_call) is dict:
        return result_of_call
    else:
        result_of_tokenization = Advenced_tokenization(context)
        result_of_call = Call_logical_function(result_of_tokenization)
        if type(result_of_call) is dict:
            
            result_of_call['Sequence retained'] = result_of_call['Sequence retained'].strip(' ')
            #print(result_of_tokenization, "ld")
            if context[-1][-1].isdigit() and context[-1][-2] in operation:
                result_of_call['Sequence retained'] = '=' +  result_of_call['Sequence retained'].strip(' ')

            return result_of_call
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
            tokens_vector = liste_temp
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
    with open(rf'{chemin_parent}\Reasoning\Prompt.json','w') as file:
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
        Model_results['Class'] = classe
        #print("RENVOI : ", vecteur_temporaire)

        return Model_results
    if last_word != context[context.__len__() - 1] and last_word in context[context.__len__() - 1]:
        return_word = context[context.__len__() - 1].replace(last_word, "")
        return return_word.strip(" ")


    
    # Generer la sortie
    MAXIMUM_LENGTH            = max_parameter
    nombre_recursion          = 0
    RAPPORT                   = 0
    output_2                  = ""
    random_list               = []
    observer                  = ''
    observer_2                = ""
    observer_antecedant       = ""
    limitateur                = 0
    removing                  = ""
    elements_predict_by_model = []
    antecedant_du_mot         = []  
    stop_compteur             = 0
    last_word                 = ""   
    output_remember           = []
    stationnement             = 0
    classe = 'Text'
    temp_input_code = input_code

    try:
        def Generer_la_sortie(input_code, MAXIMUM_LENGTH_in_fuct):
                    nonlocal RAPPORT
                    global comp_itera
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
                        nonlocal output_2
                        
                        antecedant_du_mot         = []  
                        observer                  = ''
                        removing                  = ""
                        observer_2                = ""
                        random_list               = []
                        elements_predict_by_model = []
                        #output_2 = ""
                    indice_context = 0
                                
                    if RAPPORT == 0:
                        output = input_word
                    max_word = 0
                    for index, vecteur in enumerate(relation_sequence_forward_propagation):
                        if MAXIMUM_LENGTH_in_fuct == max_word:
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
                            
                        with open(rf'{chemin_parent}\Reasoning\random_list.json', 'w') as file:
                                                    json.dump(random_list, file, indent=4)
                                                    file.close()
                        with open(rf'{chemin_parent}\Reasoning\antecedant.json', 'w') as file:
                                                    json.dump(antecedant_du_mot, file, indent=4)
                                                    file.close()
                    if random_list == [] and recursion <=1 and recursion == "back":
                        if recursion == 0:
                            GPM4_Head(setups)
                            recursion += 1
                        else:
                            recursion += 1
                            setups = {   "prompt": "",
                        "temperature" : temperature,
                        "maximum lenght" : MAXIMUM_LENGTH,
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
                            GPM4_Head(setups)
                            
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
                                        ##print(random_list)
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
                                                    if  EngineState == True:                                             
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

                                                    with open(rf'{chemin_parent}\Reasoning\Probability.json', 'w') as file:
                                                            json.dump(probability, file, indent=4)
                                                            file.close()
                                                    with open(rf"{chemin_parent}\Reasoning\vecteurs_comp.json", 'w') as file:
                                                            json.dump(vecteur_comptabilises, file, indent=4)
                                                            file.close()
                                                            
                                                    # Calculer les probabilites liees a chaque mot identifie et selectioner le plus probable        
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
                                                            with open(rf'{chemin_parent}\Reasoning\Probability_number.json', 'w') as file:
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
                                                                    with open(rf'{chemin_parent}\Reasoning\Probability_number.json', 'w') as file:
                                                                        json.dump(dict_of_probability, file, indent=4)
                                                                        file.close()
                                                                    
                                                                
                                                            result_of_analyse = Analyse_subject.jugement(Analyse_subject.Analyse_appronfodie_du_contexte())       
                                                            
                                                            def FeedBack_Analysis():
                                                                if reward == 0:
                                                                    pass
                                                            

                                                            if EngineState == False:
                                                                score_des_mots = ProbEngineNeural(context, dict_of_probability, sequence_encode, random_list)
                                                                with open(rf'{chemin_parent}\Reasoning\Probability_number.json', 'w') as file:
                                                                    json.dump(score_des_mots, file, indent=4)
                                                                    file.close()
                                                                dict_of_probability = score_des_mots
                                                                #print("TENTATIVE DE PREDICTION")
                                                                with open(rf'{chemin_parent}\Reasoning\Word_score.json', 'w') as file:
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
                                                                
                                                                with open(rf'{chemin_parent}\Reasoning\output.json', 'w') as file:
                                                                    json.dump(output_vecteur, file)
                                                                    file.close()
                                                            select_word()
                                                    except:
                                                        pass      
                                                    Calcul_des_probabilites()
                                                    
                                                    # Fonction qui reparti les mots selon leurs niveaux de pertinence // repartition_des_mots //
                                                    def repartition_des_mots():
                                                        global classe
                                                        final_distribution = {}
                                                        nonlocal output_vecteur
                                                        cont = 0
                                                        try:
                                                            first_value = output_vecteur[0][1]
                                                        except IndexError:
                                                            try:
                                                                for i in range(3):
                                                                    output_vecteur.append([
                                                                        tokens_vector[
                                                                            random.randint(0, len(tokens_vector))
                                                                        ], random.randint(0,10)
                                                                    ]
                                                                                        )
                                                                    classe = 'Uncertainty'
                                                                    first_value = output_vecteur[0][1]
                                                            except:
                                                                first_value = random_list[0]
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
                                                        with open(rf'{chemin_parent}\Reasoning\distribution.json', 'w') as file:
                                                            json.dump(final_distribution, file, indent=4)
                                                            file.close()
                                                        if len(final_distribution['les plus probables']) == 0:
                                                            sortie = [random_list[0]]
                                                        else:
                                                            sortie = final_distribution['les plus probables']
                                                            #sortie_2 = final_distribution['moyennement probables']
                                                        
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
                                        with open(rf'{chemin_parent}\Reasoning\distribution.json', 'r') as file:
                                            possibilites = json.load(file)
                                            

                                        
                                        
                                        try:
                                            # Selection en fonction de la distribution faite par les 3 agents
                                            def Reference_a_la_distribution_thinking():
                                                nonlocal stop_compteur
                                                nonlocal final_decision
          
                                                with open(rf'{chemin_parent}\Reasoning\distribution.json') as file_output:
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
                                                                try:
                                                                    final_decision = words_probable[tirer_au_sort]
                                                                except:
                                                                    final_decision = random_list[0]

                                                            else:
                                                                final_decision = words_probable[0]
                                            Reference_a_la_distribution_thinking()
                                            
                                        except IndexError: 
                                            
                                            # Selection en fonction des calculs du Thoughts \\ si la fonction thinking ne repond pas
                                            def Selection_fonction_du_thoughts():  
                                                selection_in_Thoughts = Thoughts(possibilites, sequence_encode, context)
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
                                            
                                        if observer_2 != final_decision and limitateur == 0 and context[context.__len__() - 1] != final_decision:
                                            if final_decision !='<stop>':
                                                last_word = final_decision
                                                if final_decision == ".":
                                                    output_2 = output_2+ final_decision
                                                else:
                                                    output_2 = output_2 + " " + final_decision
                                                if automatic_space == False:
                                                    output_2 = str(output_2).strip(" ")
                                                    output_2 += " "
                                                #print("SORTIE : ", output_2)
                                        
                                        #output_2 =" " +final_decision
                                                
                                                
                                        observer_2 = final_decision
                                        output = output + " " +  final_decision
                                        def find_embeding():
                                            nonlocal input_code
                                            input_word = final_decision
                                            for embeding in sequence_encode:
                                                if embeding[0] == input_word:
                                                    input_code = embeding[1]
                                                    break
                                                elementDeRecursion["embeding"] = input_code
                                        find_embeding()
                                        return output
                                    self.word = Agent_random(word)

                    except IndexError:
                            stationnement += 1
                            if stationnement < 5:
                                Generer_la_sortie(input_code, MAXIMUM_LENGTH)
                    complete_output = Agent_master(random_list)
                    add_word = complete_output.word
                    nombre_recursion += 1
                    """                for i in random_list:
                        random_list.remove(i)"""
                    reference_stop = output_2.split()
                    #print("reference : ", reference_stop)
                    reference_stop = reference_stop[len(reference_stop) - 1]
                    

                        
                    if nombre_recursion < MAXIMUM_LENGTH and last_word != "." and recursivite == True:
                        reset_settings()
                        out = output_2.split()
                        if out.__len__() < 2:
                            out = out[0]
                        else:
                            out = out[out.__len__() - 1]
                            
                        context.append(out)
                        stationnement = 0
                        Generer_la_sortie(input_code, MAXIMUM_LENGTH)
                    if limitateur != 1:
                        limitateur += 1
                        stationnement = 0
                        if predict == True:
                            Generer_la_sortie(input_code, MAXIMUM_LENGTH)
                    word_retained =output_2
                    Model_results = {}
                    liste_des_probabilites = []
                    with open(rf'{chemin_parent}\Reasoning\Probability_number.json') as file:
                        probabilite_des_mots_possible = json.load(file)
                    if os.path.exists(rf"{chemin_parent}\Reasoning\Thoughts.json"):
                        with open(rf'{chemin_parent}\Reasoning\Thoughts.json') as file:
                            elements_du_thoughts = json.load(file)
                            file.close()
                    else:
                        elements_du_thoughts = ["none"]
                    for i , j in probabilite_des_mots_possible.items():
                        liste_des_probabilites.append(i + " " + str(j))
                        
                    Model_results["Probability"] = liste_des_probabilites
                    Model_results["Thoughts"] = elements_du_thoughts
                    Model_results["Sequence retained"] = word_retained
                    Model_results["Predictions"] = elements_predict_by_model
                    Model_results["Supposition"] = context
                    elementDeRecursion["mot"] = word_retained
                    Model_results["Recursion"] = elementDeRecursion
                    Model_results['Class'] = classe
                    output_remember.append(output_2)
                    with open(rf"{path_temp}\Labs\Model results.json", 'w') as file:
                        json.dump(Model_results, file, indent=4)
                        file.close()
                    orientation_vers_prompt = True
                    
                    #print("FIN ET RENVOIE SEQUENCE")
                    print("Sortie : ", output_2)
                    if comp_itera < 1:
                        reset_settings()
                        reset_op()
                        sequence_encode = base_sequences
                        relation_sequence_forward_propagation = base_vectors
                        comp_itera = 19919
                        stationnement = 1
                        #Generer_la_sortie(temp_input_code, MAXIMUM_LENGTH)
                        temp_setup = setups
                        output_2 = ""
                        if setups["training_on_context"]:
                            temp_setup["training_on_context"] = False
                            GPM4_Head(temp_setup)
                            
                    comp_itera = 0
                    
                    return Model_results

        Generer_la_sortie(input_code, MAXIMUM_LENGTH)
        
        # Fonction de deviation
        print("jisdjcd", output_2)
        def Deviation():
            global compteur_sequence
            nonlocal output_2
            nonlocal stop_compteur
            with open(rf"{chemin_parent}\Reasoning\Probability_number.json") as file:
                data_probability = json.load(file)
                file.close()
            historique_prob[f"sequence {compteur_sequence}"] = data_probability
            compteur_sequence += 1
            if compteur_sequence > 1:
                probability_temp = historique_prob[f"sequence {compteur_sequence - 2}"]

                with open(rf"{chemin_parent}\Reasoning\Probability_number_temp.json", 'w') as file:
                        json.dump(probability_temp, file, indent=4)
                        file.close()
                with open(rf"{chemin_parent}\Reasoning\historique_prob.json", 'w') as file:
                        json.dump(historique_prob, file, indent=4)
                        file.close()

            if compteur_sequence > 1:
                try:
                    data_probability_temp = probability_temp
  
                    class Agent_of_deviation:
                        with open(rf"{chemin_parent}\Reasoning\Probability_number.json") as file:
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
                        pass
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
        word_retained =output_2
        if '.' in word_retained:
            word_retained += '\n'
        Model_results = {}
        liste_des_probabilites = []
        with open(rf'{chemin_parent}\Reasoning\Probability_number.json') as file:
            probabilite_des_mots_possible = json.load(file)
        if os.path.exists(rf"{chemin_parent}\Reasoning\Thoughts.json"):
            with open(rf'{chemin_parent}\Reasoning\Thoughts.json') as file:
                elements_du_thoughts = json.load(file)
                file.close()
        else:
            elements_du_thoughts = ["none"]
        for i , j in probabilite_des_mots_possible.items():
            liste_des_probabilites.append(i + " " + str(j))
            
        Model_results["Probability"] = liste_des_probabilites
        Model_results["Thoughts"] = elements_du_thoughts
        Model_results["Sequence retained"] = word_retained
        Model_results["Predictions"] = elements_predict_by_model
        Model_results["Supposition"] = context
        elementDeRecursion["mot"] = word_retained
        Model_results["Recursion"] = elementDeRecursion
        Model_results['Class'] = classe
        output_remember.append(output_2)
        with open(rf"{path_temp}\Labs\Model results.json", 'w') as file:
            json.dump(Model_results, file, indent=4)
            file.close()
        orientation_vers_prompt = True
        #print("FIN ET RENVOIE SEQUENCE", word_retained)
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
        Model_results['Class'] = classe
        
        #print( f" Erreur rencontree lors du traitement, code 001 : (" + str(error_sending) + f") Unknown this word '{word_unknown}' <ignore> {texte_contexte} ")
        return Model_results

