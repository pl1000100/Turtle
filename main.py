import pygame
import os
import random

pygame.font.init();

WIDTH, HEIGHT = 960, 540
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Turtle")

GREY = (127, 127, 127)
GREEN = (0, 63, 0)

FPS = 60
STRAWBERRY_VEL = 1

TURTLE_WIDTH, TURTLE_HEIGHT = 85, 115  # 120, 80     85, 115

TURTLE_IMAGE = pygame.image.load(os.path.join('Assets', 'turtle2.png'))
TURTLE = pygame.transform.scale(TURTLE_IMAGE, (TURTLE_WIDTH, TURTLE_HEIGHT))

STRAWBERRY_WIDTH, STRAWBERRY_HEIGHT = 30, 30

STRAWBERRY_IMAGE = pygame.image.load(os.path.join('Assets', 'strawberry.png'))
STRAWBERRY = pygame.transform.scale(STRAWBERRY_IMAGE, (STRAWBERRY_WIDTH, STRAWBERRY_HEIGHT))

BACKGROUND_WIDTH, BACKGROUND_HEIGHT = WIDTH, HEIGHT

BACKGROUND_IMAGE = pygame.image.load(os.path.join('Assets', 'grass3.jpg'))
BACKGROUND = pygame.transform.scale(BACKGROUND_IMAGE, (BACKGROUND_WIDTH, BACKGROUND_HEIGHT))


def draw_window(turtle, strawberry):
    WIN.fill(GREEN)
    WIN.blit(BACKGROUND, (0, 0))

    WIN.blit(TURTLE, (turtle.x, turtle.y))
    for s in strawberry:
        WIN.blit(STRAWBERRY, (s.x, s.y))

    pygame.display.update()


def turtle_handle_movement(loc, turtle):
    turtle.x = loc[0] - TURTLE_WIDTH/2
    turtle.y = loc[1] - TURTLE_HEIGHT/2


def strawberry_handle(strawberry, turtle):
    for s in strawberry:
        s.y += STRAWBERRY_VEL
        if turtle.colliderect(s):
            strawberry.remove(s)
        elif s.y > HEIGHT:
            strawberry.remove(s)


def main():
    turtle = pygame.Rect(200, 200, TURTLE_WIDTH, TURTLE_HEIGHT)
    spawn_strawberry = 1
    wait_spawn_strawberry = 100
    i = 0
    strawberry = []
    # strawberry = pygame.Rect(100, 100, STRAWBERRY_WIDTH, STRAWBERRY_HEIGHT)

    mx, my = pygame.mouse.get_pos()
    loc = [mx, my]

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)

        # mouse
        mx, my = pygame.mouse.get_pos()
        loc = [mx, my]
        i += 1
        if spawn_strawberry == 1:
            s = pygame.Rect(random.randint(STRAWBERRY_WIDTH, WIDTH - (2 * STRAWBERRY_WIDTH)), 50, STRAWBERRY_WIDTH,
                            STRAWBERRY_HEIGHT)
            strawberry.append(s)
            spawn_strawberry = 0

        if i > wait_spawn_strawberry:
            spawn_strawberry = 1
            i = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        #keys_pressed = pygame.key.get_pressed()
        turtle_handle_movement(loc, turtle)
        strawberry_handle(strawberry, turtle)

        draw_window(turtle, strawberry)

    pygame.quit()


if __name__ == "__main__":
    main()
