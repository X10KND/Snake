import pygame
import random
import sys

pygame.init()

score = 0

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

width = 800
height = 600

size = (width, height)

screen = pygame.display.set_mode(size)

def out_box(a,b):
    if a < 0 or a > width - block:
        return True
    if b < 0 or b > height - block:
        return True
    return False

def on_body(s):
    a = s[0][0]
    b = s[0][1]

    i = 1
    while i < len(s):
        if s[i][0] == a and s[i][1] == b:
            return True
        i += 1

    return False

block = 20
food_size = 20

x = width / 2
y = height / 2

snake_len = 10
snake = []

for i in range(snake_len):
    snake.append([x - i * block, y],)

no_food = False
in_body = True
while in_body:
    food = [random.randrange(0, width - food_size, food_size),
            random.randrange(0, height - food_size, food_size)]
    for body in snake:
        in_body = False
        if body[0] == food[0] and body[1] == food[1]:
            in_body = True
            break

add_x = 1
add_y = 0

speed = block

game_over = False
clock = pygame.time.Clock()

while not game_over:

    clock.tick(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("Score:", score)
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and add_x != 1:
                add_x = -1
                add_y = 0
                break
            elif event.key == pygame.K_RIGHT and add_x != -1:
                add_x = 1
                add_y = 0
                break
            elif event.key == pygame.K_UP and add_y != 1:
                add_x = 0
                add_y = -1
                break
            elif event.key == pygame.K_DOWN and add_y != -1:
                add_x = 0
                add_y = 1
                break

    
    x += add_x * speed
    y += add_y * speed

    if out_box(x,y):
        print("Score:", score)
        sys.exit()

    if x == food[0] and y == food[1]:
        no_food = True
        score += 1

    snake.insert(0,[x, y])

    if not no_food:
        snake.pop()

    if on_body(snake):
        print("Score:", score)
        sys.exit()

    screen.fill(black)

    for body in snake:
        pygame.draw.rect(screen, white, (body[0],body[1], block, block))

    if no_food:
        no_food = False
        in_body = True
        while in_body:
            food = [random.randrange(0, width - food_size, food_size),
                    random.randrange(0, height - food_size, food_size)]
            for body in snake:
                in_body = False
                if body[0] == food[0] and body[1] == food[1]:
                    in_body = True
                    break

    pygame.draw.rect(screen, red, (food[0],food[1], food_size, food_size))

    pygame.display.update()