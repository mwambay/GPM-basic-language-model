import sys
import os
chemin_parent = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(chemin_parent)
import json
                                                            # Attention portée sur les mots et calculs des probabilités
def ProbEngineNeural(context, dict_of_probability,sequence_encode, random_list):
                                                                
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
                                                                    
                                                                    with open(rf'{chemin_parent}\Reasoning\Context_vecteurs.json', 'w') as file:
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
                                                                                        
                                                                                        
                                                                        with open(rf'{chemin_parent}\Reasoning\Nouveau_vecteurs.json', 'w') as file:
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
                                                                                
                                                                        with open(rf'{chemin_parent}\Reasoning\Nouveau_vecteurs.json', 'w') as file:
                                                                            json.dump(vecteur_context, file, indent=4)
                                                                            file.close()
                                                                Self_Attention()
                                                                
                                                                with open(rf"{chemin_parent.replace('model', '')}training data\RL\Poids.json", 'r') as file:
                                                                    poids = json.load(file)
                                                                    file.close()
                                                                
                                                                distribution = {}
                                                                if use_context_illusoire == True:
                                                                    pass
                                                                else:
                                                                    context_illusoire = context
                                                                for unite in random_list:
                                                                    distribution[unite] = 1
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
                                                            