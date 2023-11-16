import pygame as pg
from sys import exit

def display_time():
    current_time = int(pg.time.get_ticks()/1000) - start_time
    score_surface = test_font.render(f'Score: {current_time}', False, (64,64,64))
    score_rect = score_surface.get_rect(center = (400,50))
    screen.blit(score_surface, score_rect)
    return current_time

pg.init()
screen = pg.display.set_mode((800,400))
pg.display.set_caption("FlappyAstro")
clock = pg.time.Clock()
test_font = pg.font.Font("font/Pixeltype.ttf", 50)

sky_surface = pg.image.load("graphics/Sky.png").convert()
ground_surface = pg.image.load("graphics/ground.png").convert()

snail_surface = pg.image.load("graphics/snail/snail1.png").convert_alpha()
snail_rect = snail_surface.get_rect(midbottom = (600,300))


player_surf = pg.image.load("graphics/Player/player_walk_1.png").convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80,300))

player_stand_surf = pg.image.load("graphics/Player/player_stand.png").convert_alpha()
player_stand_rect = player_stand_surf.get_rect(center = (400,200))

game_start_text = test_font.render('Welcome, start or you\'re racist', False, 'white')
game_start_text_rect = game_start_text.get_rect(center = (400, 125))

game_start_text2 = test_font.render('press R to start.', False, 'white')
game_start_text_rect2 = game_start_text.get_rect(center = (500, 275))

player_gravity = 0
start_time = 0
score = 0

game_active = False

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
        if game_active:
            if event.type == pg.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos) and player_rect.bottom >= 300:
                    player_gravity = -20
            if event.type == pg.KEYDOWN:
                if (event.key == pg.K_SPACE) and player_rect.bottom >= 300:
                    player_gravity = -20
        else:
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_r:
                    game_active = True
                    snail_rect.left = 800
                    start_time = int(pg.time.get_ticks()/1000)


    if (game_active):
        screen.blit(sky_surface, (0,0))
        screen.blit(ground_surface, (0,300))
        # pg.draw.rect(screen, '#c0e8ec', score_rect)
        # pg.draw.rect(screen, '#c0e8ec', score_rect, 10)
        # screen.blit(score_surface, score_rect)
        score = display_time()

        snail_rect.left -= 4
        if snail_rect.right == 0 : snail_rect.left = 800
        screen.blit(snail_surface, snail_rect)

        #Player 
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 300:
            player_rect.bottom = 300
        screen.blit(player_surf, player_rect)
        display_time()

        #Collision
        if snail_rect.colliderect(player_rect):
            game_active = False
    else: 
        screen.fill((94,129,162))
        screen.blit(player_stand_surf, player_stand_rect)
        score_message = test_font.render(f'Your score: {score}', False, (111,196,196))
        score_message_rect = score_message.get_rect(center = (400,50))
        if score == 0:
            screen.blit(game_start_text, game_start_text_rect)
            screen.blit(game_start_text2, game_start_text_rect2)
        else : 
            screen.blit(score_message, score_message_rect)
            screen.blit(game_start_text2, game_start_text_rect2)

    pg.display.update()
    clock.tick(60)
