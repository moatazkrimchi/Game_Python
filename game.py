import pygame
from player import Player
from monster import Monster, Mummy, Alien
from comet_event import CometFallEvent

class Game:
    def __init__(self):
        # commencemant du jeu
        self.is_playing = False
        #generer notre joueur
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        # groupe de monstres
        self.all_monsters = pygame.sprite.Group()
        self.pressed = {}
        # generer l'evenement
        self.comet_event = CometFallEvent(self)
        # score a zero
        self.score = 0
        self.font = pygame.font.Font("assets/font.ttf", 25)



    def update(self, screen):
        # afficher notre score
        score_text = self.font.render(f"Score : {self.score}", 1, (31, 5, 5))
        screen.blit(score_text, (20, 20))

        # appliquer l'image de notre joueur
        screen.blit(self.player.image, self.player.rect)

        # actualise rla barre de vie du joueur
        self.player.update_health_bar(screen)

        #animation du joueur
        self.player.update_animation()

        # acctualiser la bare de l'evenement
        self.comet_event.update_bar(screen)

        # recuperer les projectiles de jouueur
        for projectile in self.player.all_projectiles:
            projectile.move()

        # recuperer les monstes de notre jeu
        for monster in self.all_monsters:
            monster.forward()
            monster.update_health_bar(screen)
            monster.update_animation()

        # recuperer les comets
        for comet in self.comet_event.all_comets:
            comet.fall()

        # appliquer projectiles
        self.player.all_projectiles.draw(screen)

        # appliquer  l'ensemble des monstres
        self.all_monsters.draw(screen)

        # appliquer les comets
        self.comet_event.all_comets.draw(screen)

        # verifier si gauche ou droite
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x < screen.get_width() - self.player.rect.width:
            self.player.move_right()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
            self.player.move_left()

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def spawn_monster(self, monster_class_name):
        self.all_monsters.add(monster_class_name.__call__(self))

    def game_over(self):
        # remetre le jeu a zero (retirer les monstres, remetre le joeur a 100 vie et jeu en attente)
        self.all_monsters = pygame.sprite.Group()
        self.comet_event.all_comets = pygame.sprite.Group()
        self.comet_event.reset_percent()
        self.player.health = self.player.max_health
        self.is_playing = False
        self.player.rect.x = 400
        self.score = 0



    def start(self):
        self.is_playing = True
        self.spawn_monster(Mummy)
        self.spawn_monster(Mummy)
        self.spawn_monster(Alien)

    def add_score(self, points):
        self.score += points




