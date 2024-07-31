from keras.models import Sequential
from keras.layers import Embedding, LSTM, Dense
import numpy as np

# Liste des verbes d'entrée et leurs formes conjuguées correspondantes
verbes_entree = ["aimer", "appeler", "arriver"]
formes_conjuguees = ["j'aime", "j'appelle", "j'arrive"]

# Créez un vocabulaire manuellement
vocabulaire = list("abcdefghijklmnopqrstuvwxyzàâçéèêëîïôûùüÿ'")

# Créez un dictionnaire de correspondance de caractères à indices
char_indices = {char: index for index, char in enumerate(vocabulaire)}
indices_char = {index: char for index, char in enumerate(vocabulaire)}

# Convertissez les verbes et les formes conjuguées en séquences d'indices
sequences_entree = [[char_indices[char] for char in verb] for verb in verbes_entree]
sequences_sortie = [[char_indices[char] for char in forme] for forme in formes_conjuguees]

# Convertissez les verbes et les formes conjuguées en séquences d'indices
sequences_entree = [[char_indices[char] for char in verb] for verb in verbes_entree]
sequences_sortie = [[char_indices[char] for char in forme] for forme in formes_conjuguees]

# Paramètres du modèle
longueur_sequence = max(len(seq) for seq in sequences_entree)
vocabulaire_size = len(vocabulaire)

# Remplissez les séquences avec des zéros pour qu'elles aient toutes la même longueur
sequences_entree = np.array([seq + [0] * (longueur_sequence - len(seq)) for seq in sequences_entree])
sequences_sortie = np.array([seq + [0] * (longueur_sequence - len(seq)) for seq in sequences_sortie])

# Créez le modèle RNN
model = Sequential()
model.add(Embedding(vocabulaire_size, 8, input_length=longueur_sequence))
model.add(LSTM(32, return_sequences=True))
model.add(Dense(vocabulaire_size, activation='softmax'))

# Compilez le modèle
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Entraînez le modèle sur les données d'entraînement
model.fit(sequences_entree, sequences_sortie, epochs=1000)

# Utilisez le modèle pour prédire la forme conjuguée d'un nouveau verbe
nouveau_verbe = "chanter"
sequence_nouveau_verbe = np.array([[char_indices[char] for char in nouveau_verbe]])
forme_conjuguee_predite = model.predict(sequence_nouveau_verbe)
forme_conjuguee_predite = [indices_char[np.argmax(char_probs)] for char_probs in forme_conjuguee_predite[0]]

print("Verbe original:", nouveau_verbe)
print("Forme conjuguée prédite:", "".join(forme_conjuguee_predite))
