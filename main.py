import pygame as pg
from sys import exit

pg.init()
screen = pg.display.set_mode((800,400))
pg.display.set_caption("FlappyAstro")
clock = pg.time.Clock()
test_font = pg.font.Font("font/Pixeltype.ttf", 50)

sky_surface = pg.image.load("graphics/Sky.png").convert()
ground_surface = pg.image.load("graphics/ground.png").convert()

score_surface = test_font.render('My game', False, (64,64,64))
score_rect = score_surface.get_rect(center = (400,50))

snail_surface = pg.image.load("graphics/snail/snail1.png").convert_alpha()
snail_rect = snail_surface.get_rect(midbottom = (600,300))


player_surf = pg.image.load("graphics/Player/player_walk_1.png").convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80,300))

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
        # if event.type == pg.MOUSEMOTION:
        #     if (player_rect.collidepoint(event.pos)): print("collision")

    screen.blit(sky_surface, (0,0))
    screen.blit(ground_surface, (0,300))
    pg.draw.rect(screen, '#c0e8ec', score_rect)
    pg.draw.rect(screen, '#c0e8ec', score_rect, 10)
    screen.blit(score_surface, score_rect)

    snail_rect.left -= 2
    if snail_rect.right == 0 : snail_rect.left = 800

    screen.blit(snail_surface, snail_rect)
    screen.blit(player_surf, player_rect)

    # check for collisions between my player rectangle and the snail rectangle

    # if (player_rect.colliderect(snail_rect)):
    #     print("collision")

    # mouse_pos = pg.mouse.get_pos()
    # if player_rect.collidepoint(mouse_pos):
    #     print(pg.mouse.get_pressed())

    pg.display.update()
    clock.tick(60)
