import pygame
import random

class Comet(pygame.sprite.Sprite):

    def __init__(self, comet_event):
        super().__init__()
        # definir l'image
        self.image = pygame.image.load('assets/comet.png')
        self.rect = self.image.get_rect()
        self.velocity = random.randint(3,4)
        self.rect.x = random.randint(20,800)
        self.rect.y = - random.randint(0, 800)
        self.comet_event = comet_event

    def remove(self):
        self.comet_event.all_comets.remove(self)

        # verifier nombre de comets
        if len(self.comet_event.all_comets) == 0:
            # remetre la barre a zerp
            self.comet_event.reset_percent()
            # apparaitre les 2 monstres
            self.comet_event.game.start()

    def fall(self):
        self.rect.y += self.velocity

        # si elle tombe au sol
        if self.rect.y >= 500:
            # retirer la boule feu
            self.remove()
            # si il n'ya plus de boule de feu
            if len(self.comet_event.all_comets) == 0 :
                # remetre la jauge au depart
                self.comet_event.reset_percent()
                self.comet_event.fall_mode = False
        # verifier si la boule de feu touche le joeur
        if self.comet_event.game.check_collision(self, self.comet_event.game.all_players):
            # retirer la boule
            self.remove()
            # degats
            self.comet_event.game.player.damage(20)