import pygame
import sys
from bullet import Bullet
from alien import Alien
from explosion import Explosion
import time


def events(game):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                game.gun.mright = True
            elif event.key == pygame.K_LEFT:
                game.gun.mleft = True
            elif event.key == pygame.K_SPACE:
                new_bullet = Bullet(game.screen, game.gun)
                game.bullets.add(new_bullet)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                game.gun.mright = False
            elif event.key == pygame.K_LEFT:
                game.gun.mleft = False


def update(game):
    game.screen.fill(game.bg_color)
    game.sc.show_score()
    for bullet in game.bullets.sprites():
        bullet.draw_bullet()
    game.gun.output()
    game.aliens.draw(game.screen)
    game.expls.update()
    game.expls.draw(game.screen)
    pygame.display.flip()


def update_bullets(game):
    game.bullets.update()
    for bullet in game.bullets.copy():
        if bullet.rect.bottom <= 0:
            game.bullets.remove(bullet)
    collisions = pygame.sprite.groupcollide(game.bullets, game.aliens, True,
                                            True)
    if collisions:
        for col_aliens in collisions.values():
            game.stats.score += len(col_aliens)
            for col_alien in col_aliens:
                expl = Explosion(col_alien.rect.center, 'sm',
                                 game.explosion_anim)
                game.expls.add(expl)
        game.sc.image_score()
        check_high_score(game.stats, game.sc)
        game.sc.image_guns()
    if len(game.aliens) == 0:
        game.bullets.empty()
        create_army(game.screen, game.aliens)


def update_aliens(game):
    game.aliens.update()
    if pygame.sprite.spritecollideany(game.gun, game.aliens):
        gun_kill(game)
    aliens_check(game)


def create_army(screen, aliens):
    alien = Alien(screen)
    alien_width = alien.rect.width
    number_alien_x = int((700 - 2 * alien_width) / alien_width)
    alien_height = alien.rect.height
    number_alien_y = int((800 - 100 - 2 * alien_height) / alien_height)

    for row_n in range(number_alien_y - 2):
        for column in range(number_alien_x):
            alien = Alien(screen)
            alien.x = alien_width + (alien_width * column)
            alien.y = alien_height + (alien_height * row_n)
            alien.rect.x = alien.x
            alien.rect.y = alien.rect.height + (alien.rect.height * row_n)
            aliens.add(alien)


def gun_kill(game):

    if game.stats.guns_left > 0:
        game.stats.guns_left -= 1
        game.sc.image_guns()
        game.aliens.empty()
        game.bullets.empty()
        create_army(game.screen, game.aliens)
        game.gun.create_gun()
        time.sleep(1)
    else:
        game.stats.run_game = False
        sys.exit()


def aliens_check(game):
    screen_rect = game.screen.get_rect()
    for alien in game.aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            gun_kill(game)
            break


def check_high_score(stats, sc):
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sc.image_high_score()
        with open('highscore.txt', 'w') as f:
            f.write(str(stats.high_score))
