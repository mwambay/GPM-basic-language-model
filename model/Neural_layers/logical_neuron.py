from icecream import ic
import random

def logicalFunction(input_w, context, valide):
    def isString(var):
        try:
            int(var)
            return False
        except ValueError:
            try:
                float(var)
                return False
            except ValueError : return True
        
    if context[-1] == '=' and isString(context[-2]):
        return False
    if not isString(context[0]) and not isString(context[1]):
        del context[0]
    
    operation = ['+', '-', '/', '*']
    compteur = 0
    repere = 0
    indexs = []
    
    
    for j, i in enumerate(context):
        if i == '=':
            compteur = j
            indexs.append(j)
            repere += 1
    
    
    if repere > 1:
        nouveau_context = []
        indice_debut = indexs[-2]
        for i in range(indice_debut + 2, len(context) - 1):
            if context[i].isdigit() or context[i] in operation or context[i] == '=':
                nouveau_context.append(context[i])
        if valide:
            nouveau_context.append(context[-1])
        if '=' == context[-1] and '=' not in nouveau_context:
            nouveau_context.append('=')
        context = nouveau_context
    #print(context, "nouveau")
            
    try:
        if valide and context[-2] == '='\
            and context[-3].isdigit() and context[-4] in operation and\
                context[-5].isdigit():
                new_cont = []
                for i in context:
                    try:
                        j = int(i)
                        passe = True
                    except:
                        try:
                            j = float(i)
                            passe = True
                        except:
                            passe = False
                    if i.isdigit() or i in operation or passe or i == '=':
                        new_cont.append(i)
                context = new_cont
                quotient = len(context) / 4
                quotient = round(quotient, 0)
                quotient = int(quotient)
                #print(quotient, "sdjhb", context)
                data = ''
                rep = context[-1]
                context = context[:-2]
                chaine = ' '.join(context)
                try:
                    rep = int(rep)
                except:
                    rep = float(rep)
                
                est_decimal = rep != round(rep)
                
                if est_decimal and str(round(eval(chaine), 3)) != str(rep):
                    return f'\n{chaine} = {round(eval(chaine), 3)}'
                elif not est_decimal and str(eval(chaine)) != str(rep):
                    return f'\n{chaine} = {eval(chaine)}'
                else:
                    for i in range(quotient):
                        data += str(random.randint(1, 100))
                        
                        data += ' ' + operation[
                            random.randint(0, len(operation)-1)
                        ] + ' '
                        data += str(random.randint(1, 50)) + ' '
                        
                        if quotient > 1 and i < quotient - 1:
                            data += ' ' + operation[
                                random.randint(0, len(operation)-1)
                            ] + ' '

                    resultat = eval(data)
                    est_decimal = resultat != round(resultat)
                    
                    if est_decimal:
                        resultat = round(resultat, 3)
                    
                    return f'\n{data} = {str(resultat)}'
    except ValueError:
        pass
    
    
    try:   
        if input_w == '=' and context[-2].isdigit() and context[-3] in operation\
            and context[-4].isdigit():
                data = ''
                for indice, token in enumerate(context):
                    if token == '=':
                        break
                    if token.isdigit() or token in operation:
                        data+= ' ' + token
                resultat = eval(data)
                est_decimal = resultat != round(resultat)
                    
                if est_decimal:
                    resultat = round(resultat, 3)
                    
                return f' {str(resultat)}'
            

    except ZeroDivisionError:
        if list(context[-1])[-1] == '=':
            context = list(context[-1])
            input_w = context[-1]
            ic(context)
            ic(input_w)
            
            try:
                if input_w == '=' and context[-2].isdigit() and context[-3] in operation\
                    and context[-4].isdigit():
                        data = ''
                        for indice, token in enumerate(context):
                            if token == '=':
                                break
                            if token.isdigit() or token in operation:
                                data+=token
                        resultat = eval(data)
                        est_decimal = resultat != round(resultat)
                        
                        if est_decimal:
                            resultat = round(resultat, 3)
                        
                        return f'\n{data} = {str(resultat)}'
            except :
                return False
        else :
            return False