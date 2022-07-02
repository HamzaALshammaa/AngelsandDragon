import pygame
class Settings:
    def __init__(self):
        self.speed = 1.0
        self.bullets_allowed = 10
        self.screen_width = 1800
        self.speed = 1.5
        self.screen_height = 800
        self.fleet_drop_speed = 10
        self.fleet_dir = 1
        self.enemies_point = 5
        self.player_limit = 3
        self.speed_up = 1.5
        self.player_speed = 1
        self.bullet_speed = 1
        self.enemies_speed = 1


        #self.initialize_dynamic_sittings()

    def initialize_dynamic_sittings(self):
        self.player_speed = 1.1
        self.bullet_speed = 0.9
        self.enemies_speed = 0.9
        self.fleet_dir = 1
        self.enemies_point = 5

    def increase_speed(self):
        self.player_speed *= self.speed_up
        self.bullet_speed *= self.speed_up
        self.enemies_speed *= self.speed_up
