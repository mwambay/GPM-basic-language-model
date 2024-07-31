

data = {
    "pain": 0.0,
    "chat": 61.53846153846154,
    "predateur": 0.0,
    "paresseux": 15.384615384615385,
    "python": 23.076923076923077
}
data_2 = {
    "pain": 0.0,
    "chat": 57.14285714285714,
    "predateur": 0.0,
    "paresseux": 14.285714285714285,
    "python": 28.57142857142857
}
class Agent_of_master:
    
    def __init__(self, data, probability) -> None:
        self.probability = probability
        self.data = data
    def Reflechir():
        temp = {}
        if len(data) == len(data_2):
            for element in data:
                if data[element] != data_2[element]:
                    if data_2[element] > data[element]:
                        temp[element] = data_2[element]
        return temp
    def Conclure():
        data_of_action_precedent = Agent_of_master.Reflechir()
        temp_value = 0
        for cle, value in data_of_action_precedent.items():
            if value > temp_value:
                temp_value = value
        valeur_retenu = ""
        for element, prob in data_of_action_precedent.items():
            if prob == temp_value:
                valeur_retenu = prob
        for cle, valeur in data_2.items():
            if valeur == valeur_retenu:   
                return cle
agent_action = Agent_of_master.Conclure()
print(agent_action)

                        
                
    
