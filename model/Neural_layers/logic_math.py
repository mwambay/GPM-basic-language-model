import difflib
from random import randint




# j'ai 940 plus 3 et puis moins 89 divise par 2


class LogicAgent:
    def __init__(self, context) -> None:
        self.context = context
        self.texte_de_reference = {
                    "plus" : '+',
                    "moins" : '-',
                    "divisé" : '/',
                    'multiplié' : '*',
                    "ajoute" : '+',
                    "addition" : "+",
                    "soustrait" : "-",
                    "retranche" : "-",
                    "sommes" : '+',
                    "produit" : '*',
                    "division" : '/',
                    "font" : '*',
                    "soustraction" : '-'
                    #"egale" : '=',
                    #'vaut' : "="
                    
                    
                }
        self.text_to_operation = ['plus', 'moins', 'divisé', 'multiplié', 'sommes', "produit", "division", "addition", "font", "soustraction", "ajoute"]
        self.number = {
            '1' : 'un',
            '2' : 'deux',
            '3' : 'trois',
            '4' : 'quatre',
            '5' : 'cinq',
            '6' : 'six',
            '7' : 'sept',
            '8' : 'huit',
            '9' : 'neuf',
            '0' : 'zero'
        }
        self.replique = ["cela donne", "le resultat est", "reprise", None]


    #  Calcul de la distance entre sequence \\ Fonction
    def levenshtein_distance(self, str1, str2):                                                            
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
                
    
    def find_closest_match(self, data_use, file_data):
        closest_match = difflib.get_close_matches(data_use, file_data, n=1,  cutoff=0.0)
        return closest_match[0] if closest_match else None


    def find_math_operations(self):
        liste = []
        for token in self.context:
            result = self.find_closest_match(token, self.text_to_operation)
            if result:
                diff = self.levenshtein_distance(result, token)
                if diff <= 45.0:
                    liste.append(result)
        print(liste)
        return liste
    
    
    def decoder(self):
        operations = []
        op = self.find_math_operations()
        
        for operation in op:
            for cle, valeur in self.texte_de_reference.items():
                if cle == operation:
                    operations.append(valeur)
                    
        return operations
            
    def extract_numbers(self):
        digits = []
        for token in self.context:
            if str(token).isdigit():
                digits.append(token)
        print(digits)
        return digits
    
    def format_result(self, resultat, equation):
        texte = ""
        resultat = str(resultat)
        for char in equation:
            if char == '*':
                texte += " " + 'x'
            else:
                texte += " " + char
        equation = texte
            
        nombre_replique = len(self.replique) - 1
        replique = self.replique[randint(0, nombre_replique)]
        if replique == "reprise":
            resultat = equation + " = " + resultat
        elif replique == None:
            resultat = " : " + resultat
        else:
            resultat = replique + " " + resultat
        
        return " " + resultat
         
        
    def solve_math(self):
        try:
            equation = ""
            operations = self.decoder()
            digits = self.extract_numbers()
            print(operations)
            for indice, digit in enumerate(digits):
                if indice < len(digits)-1:
                    equation += digit
                    equation += operations[indice]
                else:
                    equation += digit
        except IndexError:
            return False
        try: 
            resultat = eval(equation)
            resultat = self.format_result(resultat, equation)
            return resultat
        except ZeroDivisionError:
            return False
            
            
if __name__ == '__main__':
    agent = LogicAgent("combien font 4 multiplie par 4")
    print(agent.solve_math())

