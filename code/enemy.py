import pygame
from pygame.sprite import Sprite


class Enemie(Sprite):
    def __init__(self, sj_game):
        super().__init__()
        self.screen = sj_game.screen
        self.settings = sj_game.settings
        self.image = pygame.image.load("images/enemy/enemie-unscreen-0.png")
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.image = pygame.transform.rotate(self.image, 0)
        self.rect = self.image.get_rect()
        self.screen_rect = sj_game.screen.get_rect()
        self.rect.midright = self.screen_rect.midright
        self.rect.y = self.rect.width
        self.rect.y = self.rect.height
        self.y = float(self.rect.y)
        self.x = float(self.rect.x)

    def update(self):
        self.y -= (self.settings.enemies_speed * self.settings.fleet_dir)
        self.rect.y = self.y

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.bottom >= screen_rect.bottom or self.rect.top <= 0:
            return True


# import pygame
# from player import Player
# from pygame.sprite import Sprite
#
#
# class Enemy(Sprite):
#     def __init__(self, ag):
#         super().__init__()
#         self.screen = ag.screen
#         self.settings = ag.settings
#         self.screen_rect = ag.screen.get_rect()
#         self.enemy = []
#         self.image1 = pygame.image.load('images/enemy/enemie-unscreen-0.png')
#         self.image1 = pygame.transform.scale(self.image1, (80, 80))
#         self.image2 = pygame.image.load('images/enemy/enemie-unscreen-1.png')
#         self.image2 = pygame.transform.scale(self.image2, (80, 80))
#         self.image3 = pygame.image.load('images/enemy/enemie-unscreen-2.png')
#         self.image3 = pygame.transform.scale(self.image3, (80, 80))
#         self.image4 = pygame.image.load('images/enemy/enemie-unscreen-3.png')
#         self.image4 = pygame.transform.scale(self.image4, (80, 80))
#         self.image5 = pygame.image.load('images/enemy/enemie-unscreen-4.png')
#         self.image5 = pygame.transform.scale(self.image5, (80, 80))
#         self.image6 = pygame.image.load('images/enemy/enemie-unscreen-5.png')
#         self.image6 = pygame.transform.scale(self.image6, (80, 80))
#         self.image7 = pygame.image.load('images/enemy/enemie-unscreen-6.png')
#         self.image7 = pygame.transform.scale(self.image7, (80, 80))
#         self.image8 = pygame.image.load('images/enemy/enemie-unscreen-7.png')
#         self.image8 = pygame.transform.scale(self.image8, (80, 80))
#         self.image9 = pygame.image.load('images/enemy/enemie-unscreen-8.png')
#         self.image9 = pygame.transform.scale(self.image9, (80, 80))
#         self.image10 = pygame.image.load('images/enemy/enemie-unscreen-9.png')
#         self.image10 = pygame.transform.scale(self.image10, (80, 80))
#
#         self.enemy.append(self.image1)
#         self.enemy.append(self.image2)
#         self.enemy.append(self.image3)
#         self.enemy.append(self.image4)
#         self.enemy.append(self.image5)
#         self.enemy.append(self.image6)
#         self.enemy.append(self.image7)
#         self.enemy.append(self.image8)
#         self.enemy.append(self.image9)
#         self.enemy.append(self.image10)
#
#         self.current_enemy = 0
#         self.enemyImage = self.enemy[self.current_enemy]
#         self.rect = self.enemyImage.get_rect()
#         self.rect.midleft = self.rect.bottomleft
#
#     def check_edges(self):
#         screen_rect = self.screen.get_rect()
#         if self.rect.bottom >= screen_rect.bottom or self.rect.top <= 0:
#             return True
#
#     def update(self):
#         self.current_enemy += 0.01
#         if self.current_enemy >= len(self.enemy):
#             self.current_enemy = 0
#         self.enemyImage = self.enemy[int(self.current_enemy)]
