import pygame
import random
import animation


class Monster(animation.AnimateSprite):
    def __init__(self, game, name, size, offset = 0):
        super().__init__(name, size)
        self.health = 100
        self.game = game
        self.max_health = 100
        self.attack = 0.3
        self.rect = self.image.get_rect()
        self.velocity = random.randint(1,1)
        self.rect.x = 1000 + random.randint(0, 300)
        self.rect.y = 540 - offset
        self.start_animation()
        self.loot_amount = 10

    def set_speed(self, speed):
        self.default_speed = speed
        self.velocity = random.randint(1,1)


    def damage(self, amount):
        # infliger les degats
         self.health -= amount

        # Verifier si son niveau de vie est nulle
         if self.health <= 0:
             # Reapparaitre comme un nouveau monstre
             self.rect.x = 1000 + random.randint(0, 300)
             self.velocity = random.randint(1, self.default_speed)
             self.health = self.max_health
             # ajouter le score
             self.game.add_score(self.loot_amount)

             # si la barre du jeu est charger
             if self.game.comet_event.is_full_loaded():
                 # retirer du jeu
                 self.game.all_monsters.remove(self)

                 # appel de la méthode pour essayer de declencher la pluie
                 self.game.comet_event.attempt_full()

    def update_animation(self):
        self.animate(loop= True)

    def update_health_bar(self, surface):

        #dessiner la barre de vie
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 10, self.rect.y - 20, self.max_health, 5])
        pygame.draw.rect(surface, (0, 115, 255), [self.rect.x + 10, self.rect.y - 20, self.health, 5])

    def set_loot_amount(self, amount):
        self.loot_amount = amount

    def forward(self):
        # le deplacement ce fait que si ya pas de joueur
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity
        # si le monste en collision
        else :
            #infliger des degats
            self.game.player.damage(self.attack)


# definie une classe pour la momie
class Mummy(Monster):

    def __init__(self, game):
        super().__init__(game, "mummy", (130, 130))
        self.set_speed(2)
        self.set_loot_amount(20)
class Alien(Monster):

    def __init__(self,game):
        super().__init__(game, "alien", (300, 300), 130)
        self.health = 250
        self.max_health = 250
        self.attack = 0.8
        self.set_speed(1)
        self.set_loot_amount(80)