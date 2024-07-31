mon_dictionnaire = {'Nom': ['Alice', 'Bob', 'Charlie'],
                   'Âge': [25, 30, 35],
                   'Ville': ['Paris', 'New York', 'Londres']}
import pandas as pd

# Convertir le dictionnaire en DataFrame
mon_dataframe = pd.DataFrame(mon_dictionnaire)

# Afficher le DataFrame
print(mon_dataframe)
