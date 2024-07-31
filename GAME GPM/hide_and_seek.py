import pygame
import random

# Initialisation de Pygame
pygame.init()

# Dimensions de la fenêtre de jeu
largeur = 800
hauteur = 600

# Couleurs
BLANC = (255, 255, 255)
ROUGE = (255, 0, 0)
VERT = (0, 255, 0)
NOIR = (0, 0, 0)

# Création de la fenêtre de jeu
fenetre = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("Jeu de cache-cache")

# Classe pour représenter les avatars
class Avatar(pygame.sprite.Sprite):
    def __init__(self, couleur, taille, position):
        super().__init__()
        self.image = pygame.Surface([taille, taille])
        self.image.fill(couleur)
        self.rect = self.image.get_rect()
        self.rect.x = position[0]
        self.rect.y = position[1]

    def deplacer(self, dx, dy, labyrinthe):
        future_rect = self.rect.move(dx, dy)
        if labyrinthe.est_valide(future_rect):
            self.rect = future_rect

# Classe pour représenter le labyrinthe
class Labyrinthe:
    def __init__(self, largeur_case, hauteur_case):
        self.largeur_case = largeur_case
        self.hauteur_case = hauteur_case
        self.grille = [
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
            [1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 1, 0, 1, 1, 1, 1, 0, 1],
            [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
            [1, 0, 1, 0, 1, 1, 1, 1, 0, 1],
            [1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
            [1, 0, 0, 0, 1, 1, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        ]

    def dessiner(self):
        for y in range(len(self.grille)):
            for x in range(len(self.grille[y])):
                if self.grille[y][x] == 1:
                    pygame.draw.rect(fenetre, NOIR, (x * self.largeur_case, y * self.hauteur_case, self.largeur_case, self.hauteur_case))

    def est_valide(self, rect):
        x = rect.x // self.largeur_case
        y = rect.y // self.hauteur_case
        return rect.x >= 0 and rect.y >= 0 and x < len(self.grille[0]) and y < len(self.grille) and self.grille[y][x] == 0

# Création des avatars
avatar1 = Avatar(ROUGE, 30, (60, 60))
avatar2 = Avatar(VERT, 30, (60, 42))

avatars = pygame.sprite.Group()
avatars.add(avatar1)
avatars.add(avatar2)

# Création du labyrinthe
largeur_case = largeur // len(Labyrinthe(0, 0).grille[0])
hauteur_case = hauteur // len(Labyrinthe(0, 0).grille)
labyrinthe = Labyrinthe(largeur_case, hauteur_case)

# Boucle principale du jeu
fin_jeu = False
horloge = pygame.time.Clock()

while not fin_jeu:
    for evenement in pygame.event.get():
        if evenement.type == pygame.QUIT:
            fin_jeu = True

    # Déplacement de l'avatar contrôlé par le clavier
    dx = 0
    dy = 0
    touches = pygame.key.get_pressed()
    if touches[pygame.K_LEFT]:
        dx = -30
    elif touches[pygame.K_RIGHT]:
        dx = 30
    elif touches[pygame.K_UP]:
        dy = -30
    elif touches[pygame.K_DOWN]:
        dy = 30
    avatar1.deplacer(dx, dy, labyrinthe)
    print("dx : " + str(dx), 'dy : ' + str(dy))
    print(avatar1.rect.x)
    # Déplacement de l'avatar2 pour fuir l'avatar1
    dx = 0
    dy = 0
    if avatar1.rect.x < avatar2.rect.x:
        dx = -30
    elif avatar1.rect.x > avatar2.rect.x:
        dx = 30
    if avatar1.rect.y < avatar2.rect.y:
        dy = -30
    elif avatar1.rect.y > avatar2.rect.y:
        dy = 30
    avatar2.deplacer(dx, dy, labyrinthe)

    # Vérification des collisions entre les avatars
    if pygame.sprite.collide_rect(avatar1, avatar2):
        # Les avatars se sont trouvés, on génère une nouvelle position pour avatar2
        x = random.randint(0, 9)
        y = random.randint(0, 9)
        while not labyrinthe.est_valide(pygame.Rect(x * 40, y * 40, 30, 30)):
            x = random.randint(0, 9)
            y = random.randint(0, 9)
        avatar2.rect.x = x * 40
        avatar2.rect.y = y * 40

    # Effacement de l'écran
    fenetre.fill(BLANC)

    # Dessin du labyrinthe
    labyrinthe.dessiner()

    # Dessin des avatars
    avatars.draw(fenetre)

    # Rafraîchissement de l'écran
    pygame.display.flip()

    # Limitation du nombre d'images par seconde
    horloge.tick(30)

# Fermeture de Pygame
pygame.quit()
