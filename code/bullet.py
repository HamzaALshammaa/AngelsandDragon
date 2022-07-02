import pygame
from pygame.sprite import Sprite
import random


class Bullet(Sprite):
    def __init__(self, ag):
        super().__init__()
        self.screen = ag.screen
        self.setting = ag.settings
        self.bullet_image = pygame.image.load('images/player/player fireball/ezgif-frame-001-removebg-preview.png')
        self.bullet_image = pygame.transform.scale(self.bullet_image, (60, 60))
        self.rect = self.bullet_image.get_rect()
        self.rect.midright = ag.player.rect.midright
        self.x = float(self.rect.x)

    def update(self):
        self.x += self.setting.bullet_speed
        self.rect.x = self.x
        return self.rect.x

    def draw_bullet(self):
        self.screen.blit(self.bullet_image, self.rect)
        # pygame.draw.rect(self.screen, self.bullet_image, self.rect)

    def bullet_sound(self):
        x = random.randint(0, 12)
        if x == 6:
            x = 5
        elif x == 7:
            x = 4
        elif x == 8:
            x = 3
        elif x == 9:
            x = 2
        elif x == 10:
            x = 1
        elif x == 11:
            x = 0
        elif x == 12:
            x = 1

        sound = ["./images/player/sounds/really_bullet_sound/Clash Royale Wizard Sounds (mp3cut (mp3cut.net).mp3",
                 "./images/player/sounds/really_bullet_sound/Clash Royale Wizard Sounds (mp3cut (mp3cut.net) (1).mp3",
                 "./images/player/sounds/really_bullet_sound/Clash Royale Wizard Sounds (mp3cut (mp3cut.net) (2).mp3",
                 "./images/player/sounds/really_bullet_sound/Clash Royale Wizard Sounds (mp3cut (mp3cut.net) (3).mp3",
                 "./images/player/sounds/really_bullet_sound/Clash Royale Wizard Sounds (mp3cut (mp3cut.net) (4).mp3",
                 './images/player/sounds/really_bullet_sound/Clash Royale Wizard Sounds (mp3cut.net).mp3',
                 ]
        pygame.mixer.Channel(1).play(pygame.mixer.Sound(sound[x]))
        pygame.mixer.Channel(1).set_volume(0.5)
