import pygame
import controls
from gun import Gun
from pygame.sprite import Group
from stats import Stats
from scores import Scores


def run():

    pygame.init()
    screen = pygame.display.set_mode((700, 800))
    pygame.display.set_caption('space invaders')
    bg_color = (0, 0, 0)
    gun = Gun(screen)
    bullets = Group()
    aliens = Group()
    expls = Group()
    controls.create_army(screen, aliens)
    stats = Stats()
    sc = Scores(screen, stats)
    explosion_anim = get_explosion_anim()

    while True:
        controls.events(screen, gun, bullets)
        if stats.run_game:
            gun.update_gun()
            controls.update(bg_color, screen, stats, sc, gun, aliens, bullets, expls)
            controls.update_bullets(screen, stats, sc, aliens, bullets, explosion_anim, expls)
            controls.update_aliens(stats, screen, sc, gun, aliens, bullets)


def get_explosion_anim():
    explosion_anim = {'lg': [], 'sm': []}
    for i in range(1, 13):
        img = pygame.image.load(f'images/exp1_{i}.png').convert()
        img.set_colorkey((0, 0, 0))
        img_lg = pygame.transform.scale(img, (75, 75))
        explosion_anim['lg'].append(img_lg)
        img_sm = pygame.transform.scale(img, (32, 32))
        explosion_anim['sm'].append(img_sm)
    return explosion_anim


run()
