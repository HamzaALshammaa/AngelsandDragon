import pygame
from pygame import mixer


class Player:
    def __init__(self, ag):
        mixer.init()
        self.screen = ag.screen
        self.settings = ag.settings
        self.screen_rect = ag.screen.get_rect()
        self.player = []
        self.image1 = pygame.image.load('images/player/fatais-0.png')
        self.image1 = pygame.transform.scale(self.image1, (150, 150))
        self.image2 = pygame.image.load('images/player/fatais-1.png')
        self.image2 = pygame.transform.scale(self.image2, (150, 150))
        self.image3 = pygame.image.load('images/player/fatais-2.png')
        self.image3 = pygame.transform.scale(self.image3, (150, 150))
        self.image4 = pygame.image.load('images/player/fatais-3.png')
        self.image4 = pygame.transform.scale(self.image4, (150, 150))
        self.image5 = pygame.image.load('images/player/fatais-3.png')
        self.image5 = pygame.transform.scale(self.image5, (150, 150))
        self.image6 = pygame.image.load('images/player/fatais-4.png')
        self.image6 = pygame.transform.scale(self.image6, (150, 150))
        self.image7 = pygame.image.load('images/player/fatais-5.png')
        self.image7 = pygame.transform.scale(self.image7, (150, 150))
        self.image8 = pygame.image.load('images/player/fatais-6.png')
        self.image8 = pygame.transform.scale(self.image8, (150, 150))
        self.image9 = pygame.image.load('images/player/fatais-7.png')
        self.image9 = pygame.transform.scale(self.image9, (150, 150))
        self.image10 = pygame.image.load('images/player/fatais-8.png')
        self.image10 = pygame.transform.scale(self.image10, (150, 150))
        self.image11 = pygame.image.load('images/player/fatais-9.png')
        self.image11 = pygame.transform.scale(self.image11, (150, 150))
        self.image12 = pygame.image.load('images/player/fatais-10.png')
        self.image12 = pygame.transform.scale(self.image12, (150, 150))
        self.image13 = pygame.image.load('images/player/fatais-11.png')
        self.image13 = pygame.transform.scale(self.image13, (150, 150))
        self.player.append(self.image1)
        self.player.append(self.image2)
        self.player.append(self.image3)
        self.player.append(self.image4)
        self.player.append(self.image5)
        self.player.append(self.image6)
        self.player.append(self.image7)
        self.player.append(self.image8)
        self.player.append(self.image9)
        self.player.append(self.image10)
        self.player.append(self.image11)
        self.player.append(self.image12)
        self.player.append(self.image13)

        self.current_player = 0
        self.playerImage = self.player[self.current_player]
        self.rect = self.playerImage.get_rect()
        self.rect.midleft = self.screen_rect.midleft
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.moving_top = False
        self.moving_down = False
        self.moving_foreword = False
        self.moving_backward = False

    def update(self):
        if self.moving_top and self.rect.top > 0:
            self.y -= self.settings.player_speed
        if self.moving_down and self.rect.bottom < self.screen.get_height():
            self.y += self.settings.player_speed
        if self.moving_foreword and self.rect.right < self.screen.get_width():
            self.x += self.settings.player_speed
        if self.moving_backward and self.rect.left > 0:
            self.x -= self.settings.player_speed

        self.rect.x = self.x
        self.rect.x -= 1
        self.rect.y = self.y
        self.rect.y += 1

        self.current_player += 0.1
        if self.current_player >= len(self.player):
            self.current_player = 0
        self.playerImage = self.player[int(self.current_player)]

    def blitme(self):
        self.screen.blit(self.image1, self.rect)

    def center_ship(self):
        self.rect.midleft = self.screen_rect.midleft
        self.x = float(self.rect.x)

    # def blitme(self):
    #     self.screen.blit(self.image, self.rect.midleft)
