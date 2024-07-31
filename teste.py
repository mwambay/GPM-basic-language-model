from nltk.tokenize import word_tokenize

tokens = []
def Tokenization(sequence):
    sequence = word_tokenize(sequence)
    token_probable = ''
    for token in range(len(sequence) - 1):
        recurence = 0
        temp = sequence[token]

        
        for ind in range(len(sequence)-1):
            print(token, ind)
            if token_probable in sequence[ind] and sequence[ind] != sequence[token]:
                recurence += 1
                
        if recurence > 2:
            tokens.append(token_probable)
    print(tokens)
    
texte = """
Il était une fois un petit garçon nommé Tom, qui adorait les histoires de pirates. Chaque soir, sa mère lui racontait une histoire différente de batailles en mer, de trésors cachés et de pirates légendaires.
Tom était fasciné par ces histoires et il rêvait de devenir un pirate lui-même. Il passe des heures à dessiner des cartes au trésor et à fabriquer des épées en carton pour jouer avec ses amis.
Un jour, alors qu'il se promenait sur la plage, Tom a trouvé une bouteille contenant une carte au trésor. Il a été tellement excité qu'il a couru chez lui pour montrer la carte à sa mère.
Ils ont étudié la carte ensemble et ont réalisé que le trésor était caché sur une île lointaine, au-delà des mers inconnues. Tom a décidé de partir à l'aventure pour trouver le trésor lui-même.
Il a préparé son sac à dos, a fait des provisions pour le voyage et a embarqué sur un petit bateau avec quelques amis. Ils ont navigué pendant des jours, bravant les tempêtes et les vagues déchaînées.
Finalement, ils ont atteint l'île et ont commencé à chercher le trésor. Ils ont dû traverser des jungles épaisses, éviter les pièges et les ennemis, mais finalement, ils ont trouvé le trésor.
Le trésor était rempli de pièces d'or, de bijoux étincelants et de pierres précieuses. Tom et ses amis ont partagé le butin, mais ce qui était le plus important pour Tom, c'était l'expérience de l'aventure et la réalisation de son rêve de devenir un vrai pirate.
De retour chez lui, Tom a raconté son aventure à sa mère, qui était fière de lui et heureuse de voir son fils si courageux et déterminé.
Et ainsi, Tom est devenu une légende dans son petit village, un pirate intrépide qui avait navigué au-delà des mers pour trouver le trésor caché. Et chaque soir, avant de s'endormir, il repensait à cette aventure incroyable et se préparait pour de nouvelles aventures à venir.
end"""  
Tokenization(texte)