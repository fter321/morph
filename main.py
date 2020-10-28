import pygame as pg
import sys

SIZE = WIDTH, HEIGHT = 640, 480
speed_x, speed_y = 5, 5
BLACK = (0, 0, 0)
FPS = 120

pg.init()
pg.display.set_caption('Ball')
screen = pg.display.set_mode(SIZE)
clock = pg.time.Clock()

ball = pg.image.load('ball.png')
ball_rect = ball.get_rect()
#print(ball_rect)

while True:
    for e in pg.event.get():
        if e.type == pg.QUIT or \
                e.type == pg.KEYDOWN and e.key == pg.K_ESCAPE:
            sys.exit(0)

    ball_rect = ball_rect.move(speed_x, speed_y)      
    if ball_rect.left < 0 or ball_rect.right > WIDTH:
        speed_x = -speed_x
    if ball_rect.top < 0 or ball_rect.bottom > HEIGHT:
        speed_y = -speed_y

    screen.fill(BLACK)
    screen.blit(ball, ball_rect)
    pg.display.update()
    clock.tick(FPS)
    pg.display.set_caption(f'Ball  FPS: {int(clock.get_fps())}')
