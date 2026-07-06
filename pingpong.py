from pygame import *
from random import choice

init()
WIDTH, HEIGHT = 800, 600
screen = display.set_mode((WIDTH, HEIGHT))
display.set_caption('Пинг-понг')

try:
    bg_image = image.load('backgrounds.jpg')
    bg_image = transform.scale(bg_image, (WIDTH, HEIGHT))
except:
    bg_image = Surface((WIDTH, HEIGHT))
    bg_image.fill((0, 100, 0))

BALL_SIZE = 25
try:
    ball_img = image.load('ball.jpg')
    ball_img = transform.scale(ball_img, (BALL_SIZE, BALL_SIZE))
except:
    ball_img = Surface((BALL_SIZE, BALL_SIZE))
    ball_img.fill((255, 215, 0))

WHITE = (255, 255, 255)
PAD_WIDTH, PAD_HEIGHT = 15, 100
PAD_SPEED = 7

ball = Rect(WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)
ball_speed_x = 6 * choice((1, -1))
ball_speed_y = 6 * choice((1, -1))

left_pad = Rect(30, HEIGHT // 2 - PAD_HEIGHT // 2, PAD_WIDTH, PAD_HEIGHT)
right_pad = Rect(WIDTH - 30 - PAD_WIDTH, HEIGHT // 2 - PAD_HEIGHT // 2, PAD_WIDTH, PAD_HEIGHT)

clock = time.Clock()
running = True

while running:
    for e in event.get():
        if e.type == QUIT:
            running = False

    keys = key.get_pressed()
    if keys[K_w] and left_pad.top > 0:
        left_pad.y -= PAD_SPEED
    if keys[K_s] and left_pad.bottom < HEIGHT:
        left_pad.y += PAD_SPEED
    if keys[K_UP] and right_pad.top > 0:
        right_pad.y -= PAD_SPEED
    if keys[K_DOWN] and right_pad.bottom < HEIGHT:
        right_pad.y += PAD_SPEED

    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed_y *= -1

    if ball.colliderect(left_pad) and ball_speed_x < 0:
        ball_speed_x *= -1
    if ball.colliderect(right_pad) and ball_speed_x > 0:
        ball_speed_x *= -1

    if ball.left <= 0 or ball.right >= WIDTH:
        ball.x = WIDTH // 2 - BALL_SIZE // 2
        ball.y = HEIGHT // 2 - BALL_SIZE // 2
        ball_speed_x = 6 * choice((1, -1))
        ball_speed_y = 6 * choice((1, -1))

    screen.blit(bg_image, (0, 0))
    screen.blit(ball_img, (ball.x, ball.y))
    draw.rect(screen, WHITE, left_pad)
    draw.rect(screen, WHITE, right_pad)
    
    display.update()
    clock.tick(60)

quit()
