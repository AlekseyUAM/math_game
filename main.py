import pygame
import controls
from gun import Gun
from pygame.sprite import Group
from stats import Stats
from scores import Scores


def get_explosion_anim():
    explosion_anim = {'lg': [], 'sm': [], 'gun': []}
    for i in range(1, 13):
        img = pygame.image.load(f'images/exp1_{i}.png').convert()
        img.set_colorkey((0, 0, 0))
        img_lg = pygame.transform.scale(img, (150, 150))
        explosion_anim['lg'].append(img_lg)
        img_sm = pygame.transform.scale(img, (75, 75))
        explosion_anim['sm'].append(img_sm)
        img = pygame.image.load(f'images/exp3_{i}.png').convert()
        img.set_colorkey((0, 0, 0))
        img_gun = pygame.transform.scale(img, (200, 200))
        explosion_anim['gun'].append(img_gun)

    return explosion_anim


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('space invaders')
        self.screen = pygame.display.set_mode((700, 800))
        self.bg_color = (0, 0, 0)
        self.gun = Gun(self.screen)
        self.bullets = Group()
        self.aliens = Group()
        self.expls = Group()
        controls.create_army(self.screen, self.aliens)
        self.stats = Stats()
        self.sc = Scores(self.screen, self.stats)
        self.explosion_anim = get_explosion_anim()

def run():

    game = Game()
    while True:
        controls.events(game)
        if game.stats.run_game:
            game.gun.update_gun()
            controls.update(game)
            controls.update_bullets(game)
            controls.update_aliens(game)


run()
