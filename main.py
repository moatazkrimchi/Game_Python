import pygame
import math
from game import Game
pygame.mixer.init(44100, -16, 2, 2048)
pygame.init()

# definir une clock
clock = pygame.time.Clock()
FPS = 60



# generer la fenetre de notre jeu

pygame.display.set_caption("Game Moataz")
screen = pygame.display.set_mode((1080, 720))

# Premiere page
background = pygame.image.load('assets/bg.jpg')

# importer banniere
banner = pygame.image.load('assets/banner.png')
banner = pygame.transform.scale(banner, (500,500))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width() / 3.5)


# importer button
play_button = pygame.image.load('assets/button.png')
play_button = pygame.transform.scale(play_button, (400,150))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width() / 3)
play_button_rect.y = math.ceil(screen.get_height() / 2)

# charger notre jeu
game = Game()



running = True

# cree une boucle pour que notre fenetre reste ouverte
while running:

    # appliquer background
    screen.blit(background, (0, -200))

    # verifier si le jeu commence
    if game.is_playing:
        # declencher les instruction de la partie
        game.update(screen)
    # verifier si notre jeu n'a pas commencer
    else:
        # ajouter mon ecran de bienvenue
        screen.blit(play_button, play_button_rect)
        screen.blit(banner, banner_rect)




    #mettre a jour l'ecran
    pygame.display.flip()
    # si le joueur ferme cette fenetre
    for event in pygame.event.get():
        # que l'evenement est fermeture de fenetre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("fermeture du Games")
        # detecter les touches claviers
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            # si la touche espace est selectionne
            if event.key == pygame.K_SPACE:
                game.player.launch_projectile()


        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            # verifier si le button est cliquer
            if play_button_rect.collidepoint(event.pos):
                #mettre le jeu en mode "lancé"
                game.start()

    # ficer le nombre fps sur clock
    clock.tick(FPS)
