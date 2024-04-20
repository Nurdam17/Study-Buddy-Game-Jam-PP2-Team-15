import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 600, 400
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("asfdsgsdg")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)

RECT_WIDTH, RECT_HEIGHT = 50, 350

TOP_RED_HEIGHT = RECT_HEIGHT * 0.25
BOTTOM_RED_HEIGHT = RECT_HEIGHT * 0.25
YELLOW_HEIGHT_TOP = RECT_HEIGHT * 0.20
YELLOW_HEIGHT_BOTTOM = RECT_HEIGHT * 0.20
GREEN_HEIGHT_BOTTOM = RECT_HEIGHT * 0.10

top_red_y = HEIGHT // 2 - RECT_HEIGHT // 2
bottom_red_y = HEIGHT // 2 + RECT_HEIGHT // 2 - BOTTOM_RED_HEIGHT

RECT_COLOR = WHITE

LINE_COLOR = WHITE
LINE_WIDTH = 2
LINE_Y = HEIGHT // 2
LINE_SPEED = 2
LINE_SPEED_GIVEN = False
move_line = True

# Счет и скорость
score = 0
score_given = False

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            move_line = not move_line

    # move line
    if move_line:
        if LINE_Y <= HEIGHT // 2 - RECT_HEIGHT // 2 or LINE_Y >= HEIGHT // 2 + RECT_HEIGHT // 2:
            LINE_SPEED = -LINE_SPEED
            score_given = False
        LINE_Y += LINE_SPEED

    if (HEIGHT - RECT_HEIGHT)/2 + (RECT_HEIGHT/4) + (RECT_HEIGHT/5) <= LINE_Y <= (HEIGHT - RECT_HEIGHT)/2 + (RECT_HEIGHT/4) + (RECT_HEIGHT/5) + (RECT_HEIGHT/10) and not move_line and not score_given:
        score += 1
        score_given = True
        if LINE_SPEED < 0:
            LINE_SPEED -= 1
            LINE_SPEED_GIVEN = True
        else:
            LINE_SPEED += 1
            LINE_SPEED_GIVEN = True

    if (LINE_Y <= top_red_y + TOP_RED_HEIGHT or LINE_Y >= bottom_red_y) and not move_line:
        pygame.quit()
        sys.exit()

    SCREEN.fill(BLACK)

    # levels
    pygame.draw.rect(SCREEN, RED, (WIDTH // 2 - RECT_WIDTH // 2, top_red_y, RECT_WIDTH, TOP_RED_HEIGHT))
    pygame.draw.rect(SCREEN, YELLOW, (WIDTH // 2 - RECT_WIDTH // 2, top_red_y + TOP_RED_HEIGHT, RECT_WIDTH, YELLOW_HEIGHT_TOP))
    pygame.draw.rect(SCREEN, RED, (WIDTH // 2 - RECT_WIDTH // 2, bottom_red_y, RECT_WIDTH, BOTTOM_RED_HEIGHT))
    pygame.draw.rect(SCREEN, YELLOW, (WIDTH // 2 - RECT_WIDTH // 2, bottom_red_y - YELLOW_HEIGHT_BOTTOM, RECT_WIDTH, YELLOW_HEIGHT_BOTTOM))
    pygame.draw.rect(SCREEN, GREEN, (WIDTH // 2 - RECT_WIDTH // 2, bottom_red_y - YELLOW_HEIGHT_BOTTOM - GREEN_HEIGHT_BOTTOM, RECT_WIDTH, GREEN_HEIGHT_BOTTOM))
    pygame.draw.rect(SCREEN, RECT_COLOR, (WIDTH // 2 - RECT_WIDTH // 2, top_red_y + TOP_RED_HEIGHT + YELLOW_HEIGHT_TOP, RECT_WIDTH, RECT_HEIGHT - TOP_RED_HEIGHT - BOTTOM_RED_HEIGHT - YELLOW_HEIGHT_TOP - YELLOW_HEIGHT_BOTTOM - GREEN_HEIGHT_BOTTOM))

    pygame.draw.line(SCREEN, LINE_COLOR, (WIDTH // 2 - RECT_WIDTH // 2, LINE_Y), (WIDTH // 2 + RECT_WIDTH // 2, LINE_Y), LINE_WIDTH)

    font = pygame.font.Font(None, 36)
    text = font.render("Score: " + str(score), True, WHITE)
    SCREEN.blit(text, (10, 10))

    speed_text = font.render("Speed: " + str(abs(LINE_SPEED)), True, WHITE)
    SCREEN.blit(speed_text, (10, 40))


    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()
sys.exit()
