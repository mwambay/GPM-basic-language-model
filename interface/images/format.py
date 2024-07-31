import json
def simulation():
                                            liste_provisoire = ['kinshasa', 'kigali']   
                                            context = ['je', 'parle', 'anglais', 'parceque', 'je', 'suis', 'a']   
                                            sequence_encode = [ ['je', '586969469', 'parle', 'francais', 'parceque', 'je', 'suis', 'a', 'kinshasa'],
                                                               ['francais', '5521144155', 'kinshasa'],
                                                               ['parle', '4095959', 'francais', 'parceque', 'je' , 'suis', 'a', 'kinshasa' ],
                                                               ['je', '586969469', 'parle', 'anglais', 'parceque', 'je', 'suis', 'a', 'kigali'],
                                                               ['anglais', '52255232', 'kigali'],
                                                               ['parle', '4095959', 'anglais', 'parceque', 'je' , 'suis', 'a', 'kigali' ]]
          
                                            liste_prob = {}
                                            lis = []
                                            if liste_provisoire.__len__() != 100:
                                                for word_context in context:
                                                    for vector in range(sequence_encode.__len__()):
                                                        lis = []
                                                        if sequence_encode[vector][0] == word_context:
                                                            lis.append(sequence_encode[vector][0])
                                                            
                                                            for token in liste_provisoire:
                                                                if token in sequence_encode[vector]:
                                                                    if token not in liste_prob:
                                                                        print(token)
                                                                        liste_prob[token] = 1
                                                                        lis.append(token)
                                                                        lis.append(word_context)
                                                                        break
                                                                        
                                                                    else:
                                                                        indice = liste_prob[token]
                                                                        liste_prob[token] = int(indice) + 1
                                                                        print(token, "googotot")
                                                                        break
                                                                      
                                                                        
                                            with open('file.json', 'w') as file:
                                                    json.dump(liste_prob, file, indent=4)
                                                    file.close()
simulation()