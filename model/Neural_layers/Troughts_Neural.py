import os
import sys
chemin_parent = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(chemin_parent)
import json
def Thoughts(enter_possibilites, sequence_encode, context):
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

                                                        
                                            with open(rf'{chemin_parent}\Reasoning\Thoughts.json', 'w') as file:
                                                    json.dump(liste_provisoire, file, indent=4)
                                                    file.close()
                                            with open(rf'{chemin_parent}\Reasoning\output.json') as file:
                                                distribution = json.load(file)
                                                file.close()
                                            return liste_provisoire