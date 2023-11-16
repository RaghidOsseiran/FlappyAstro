import pygame as pg
from sys import exit

pg.init()
screen = pg.display.set_mode((800,400))
pg.display.set_caption("FlappyAstro")
clock = pg.time.Clock()
test_font = pg.font.Font("font/Pixeltype.ttf", 50)

sky_surface = pg.image.load("graphics/Sky.png").convert()
ground_surface = pg.image.load("graphics/Ground.png").convert()
text_surface = test_font.render('My game', False, 'black')

snail_surface = pg.image.load("graphics/snail/snail1.png").convert_alpha()
snail_rect = snail_surface.get_rect(midbottom = (600,300))


player_surf = pg.image.load("graphics/Player/player_walk_1.png").convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80,300))

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()

    screen.blit(sky_surface, (0,0))
    screen.blit(ground_surface, (0,300))
    screen.blit(text_surface, (325,0))

    snail_rect.left -= 2
    if snail_rect.right == 0 : snail_rect.left = 800

    screen.blit(snail_surface, snail_rect)

    player_rect.left += 1
    screen.blit(player_surf, player_rect)
    pg.display.update()
    clock.tick(60)