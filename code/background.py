import pygame


class Background:
    def __init__(self, ag):
        self.screen = ag.screen
        self.width = self.screen.get_width()
        self.hight = self.screen.get_height()

        self.settings = ag.settings
        self.screen_rect = ag.screen.get_rect()
        self.backgroundImages = []
        image1 = pygame.image.load('./images/bachground/The Big Pixel Art Gallery (presented by PixelArtus)-0.png')
        image1 = pygame.transform.scale(image1, (self.width, self.hight))
        image2 = pygame.image.load('./images/bachground/The Big Pixel Art Gallery (presented by PixelArtus)-1.png')
        image2 = pygame.transform.scale(image2, (self.width, self.hight))
        image3 = pygame.image.load('./images/bachground/The Big Pixel Art Gallery (presented by PixelArtus)-2.png')
        image3 = pygame.transform.scale(image3, (self.width, self.hight))
        image4 = pygame.image.load('./images/bachground/The Big Pixel Art Gallery (presented by PixelArtus)-3.png')
        image4 = pygame.transform.scale(image4, (self.width, self.hight))
        image5 = pygame.image.load('./images/bachground/The Big Pixel Art Gallery (presented by PixelArtus)-4.png')
        image5 = pygame.transform.scale(image5, (self.width, self.hight))
        image6 = pygame.image.load('./images/bachground/The Big Pixel Art Gallery (presented by PixelArtus)-5.png')
        image6 = pygame.transform.scale(image6, (self.width, self.hight))
        image7 = pygame.image.load('./images/bachground/The Big Pixel Art Gallery (presented by PixelArtus)-6.png')
        image7 = pygame.transform.scale(image7, (self.width, self.hight))
        image8 = pygame.image.load('./images/bachground/The Big Pixel Art Gallery (presented by PixelArtus)-7.png')
        image8 = pygame.transform.scale(image8, (self.width, self.hight))
        self.backgroundImages.append(image1)
        self.backgroundImages.append(image2)
        self.backgroundImages.append(image3)
        self.backgroundImages.append(image4)
        self.backgroundImages.append(image5)
        self.backgroundImages.append(image6)
        self.backgroundImages.append(image7)
        self.backgroundImages.append(image8)

        self.current_background = 0
        self.image = self.backgroundImages[self.current_background]

        pygame.mixer.Channel(0).play(pygame.mixer.Sound("./images/player/sounds/bachground sound.wav"), -1)
        pygame.mixer.Channel(0).set_volume(0.3)
        # pygame.mixer.music.set_volume(1.0)
        # mixer.music.play(-1)

    def update(self):
        self.current_background += 0.006
        if self.current_background >= len(self.backgroundImages):
            self.current_background = 0
        self.image = self.backgroundImages[int(self.current_background)]

