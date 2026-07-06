from pygame import *
from random import choice

init()

WIDTH, HEIGHT = 800, 600
screen = display.set_mode((WIDTH, HEIGHT))
display.set_caption('Пинг-понг')

WHITE = (255, 255, 255)
GREEN = (0, 100, 0)
GOLD = (255, 215, 0)

try:
    bg_image = image.load('backgrounds.jpg')
    bg_image = transform.scale(bg_image, (WIDTH, HEIGHT))
except:
    bg_image = Surface((WIDTH, HEIGHT))
    bg_image.fill(GREEN)

try:
    ball_img = image.load('ball.png')
    ball_img = transform.scale(ball_img, (65, 65))
except:
    ball_img = Surface((65, 65))
    ball_img.fill(GOLD)


class Player1:
    def __init__(self, x, y, width, height, speed):
        self.rect = Rect(x, y, width, height)
        self.speed = speed

    def update(self, keys):
        if keys[K_w] and self.rect.top > 0:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.bottom < HEIGHT:
            self.rect.y += self.speed

    def draw(self, surface):
        draw.rect(surface, WHITE, self.rect)


class Player2:
    def __init__(self, x, y, width, height, speed):
        self.rect = Rect(x, y, width, height)
        self.speed = speed

    def update(self, keys):
        if keys[K_UP] and self.rect.top > 0:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.bottom < HEIGHT:
            self.rect.y += self.speed

    def draw(self, surface):
        draw.rect(surface, WHITE, self.rect)


BALL_SIZE = 65
PAD_WIDTH, PAD_HEIGHT = 15, 100
PAD_SPEED = 7

player1 = Player1(30, HEIGHT // 2 - PAD_HEIGHT // 2, PAD_WIDTH, PAD_HEIGHT, PAD_SPEED)
player2 = Player2(WIDTH - 30 - PAD_WIDTH, HEIGHT // 2 - PAD_HEIGHT // 2, PAD_WIDTH, PAD_HEIGHT, PAD_SPEED)

ball = Rect(WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)
ball_speed_x = 6 * choice((1, -1))
ball_speed_y = 6 * choice((1, -1))

clock = time.Clock()
running = True

while running:
    for e in event.get():
        if e.type == QUIT:
            running = False

    keys = key.get_pressed()

    player1.update(keys)
    player2.update(keys)

    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed_y *= -1

    if ball.colliderect(player1.rect) and ball_speed_x < 0:
        ball_speed_x *= -1
    if ball.colliderect(player2.rect) and ball_speed_x > 0:
        ball_speed_x *= -1

    if ball.left <= 0 or ball.right >= WIDTH:
        ball.x = WIDTH // 2 - BALL_SIZE // 2
        ball.y = HEIGHT // 2 - BALL_SIZE // 2
        ball_speed_x = 6 * choice((1, -1))
        ball_speed_y = 6 * choice((1, -1))

    screen.blit(bg_image, (0, 0))
    screen.blit(ball_img, (ball.x, ball.y))
    player1.draw(screen)
    player2.draw(screen)

    display.update()
    clock.tick(60)

quit()
