import pygame


class AnimateSprite(pygame.sprite.Sprite):

    # definir les choses a faire a la creation
    def __init__(self, sprite_name, size=(200, 200)):
        super().__init__()
        self.size = size
        self.image = pygame.image.load(f'assets/{sprite_name}.png')
        self.image = pygame.transform.scale(self.image, size)
        self.currant_image = 0 # commencer l'annimation a l'image 0
        self.images = animations.get(sprite_name)
        self.animation = False

    # methode qui demarre l'animation (players)
    def start_animation(self):
        self.animation = True

    def animate(self, loop=False):
        #verifier si l'animation est actibver
        if self.animation:
            # passer a l'image suivante
            self.currant_image += 1

            # v"rifier si on a atteint la fin
            if self.currant_image >= len(self.images):
                # remettre l'animation au départ
                self.currant_image = 0

                # si l'animation n'est pas en mode boucle
                if loop is False:
                    #desacivation de l'animation
                    self.animation = False

            # modifier l'image precedente par la suivant
            self.image = self.images[self.currant_image]
            self.image = pygame.transform.scale(self.image, self.size)


# definir une fonction pour charger les images d'un sprite
def load_animation_images(sprite_name):
    # charger les 244 images de ce sprite dans le dossier correspondants
    images =[]
    # recuperer le chmin
    path = f'assets/{sprite_name}/{sprite_name}'

    # boucler sur chaque images
    for num in range(1, 24):
        image_path = path + str(num) + '.png'
        images.append(pygame.image.load(image_path))

    return images


# definir un dictionnaire des images chargées
animations = {
    'mummy' : load_animation_images('mummy'),
    'player' : load_animation_images('player'),
    'alien' : load_animation_images('alien')
}