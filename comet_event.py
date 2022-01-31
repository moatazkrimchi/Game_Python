import pygame
from comet import Comet

# cree une classe pour gerer cet evenement
class CometFallEvent:

    # lors du chargement cree un compteur
    def __init__(self, game):
        self.percent = 0
        self.percent_speed = 10
        self.game = game
        self.fall_mode = False
        # groupe de comet
        self.all_comets = pygame.sprite.Group()

    def add_percent(self):
        self.percent += self.percent_speed / 100

    def is_full_loaded(self):
        return self.percent >=100

    def reset_percent(self):
        self.percent = 0

    def meteor_fall(self):
        # boucle de comets
        for i in range(1, 10):
            # apprataitre une boule de feu
            self.all_comets.add(Comet(self))


    def attempt_full(self):
        # la jauge max
        if self.is_full_loaded() and len(self.game.all_monsters) == 0:
            print("pluie de cometes !! ")
            self.meteor_fall()
            self.fall_mode = True # activer evenement


    def update_bar(self, surface):
        # ajouter le porcentage a la barre
        self.add_percent()



        # barre noir (en arriere plan)
        pygame.draw.rect(surface, (0, 0, 0), [
            0, # axe x
            surface.get_height() - 20, # axe y
            surface.get_width(), # longeur de la fenetre
            10 # epaisseur de la barre

        ])
        # la barre rouge de l'event
        pygame.draw.rect(surface, (187, 11, 11), [
            0,  # axe x
            surface.get_height() - 20,  # axe y
            (surface.get_width() / 100) * self.percent,  # longeur de la fenetre
            10  # epaisseur de la barre

        ])
