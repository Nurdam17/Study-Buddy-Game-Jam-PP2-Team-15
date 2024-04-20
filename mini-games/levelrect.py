import pygame
import sys

def draw_game(SCREEN, WIDTH, HEIGHT, WHITE, BLACK, RED, YELLOW, GREEN, FONT):
    pygame.init()

    RECT_WIDTH, RECT_HEIGHT = 50, 350

    TOP_RED_HEIGHT = RECT_HEIGHT * 0.25
    BOTTOM_RED_HEIGHT = RECT_HEIGHT * 0.25
    YELLOW_HEIGHT_TOP = RECT_HEIGHT * 0.20
    YELLOW_HEIGHT_BOTTOM = RECT_HEIGHT * 0.20
    GREEN_HEIGHT_BOTTOM = RECT_HEIGHT * 0.10

    top_red_y = 325
    bottom_red_y = HEIGHT // 2 + RECT_HEIGHT // 2 - BOTTOM_RED_HEIGHT

    RECT_COLOR = WHITE

    LINE_COLOR = BLACK
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


        if (HEIGHT - RECT_HEIGHT) / 2 + (RECT_HEIGHT / 4) + (
                RECT_HEIGHT / 5) <= LINE_Y <= (HEIGHT - RECT_HEIGHT) / 2 + (
                RECT_HEIGHT / 4) + (RECT_HEIGHT / 5) + (
                RECT_HEIGHT / 10) and not move_line and not score_given:
            score += 1
            score_given = True
            if LINE_SPEED < 0:
                LINE_SPEED -= 1
                LINE_SPEED_GIVEN = True
            else:
                LINE_SPEED += 1
                LINE_SPEED_GIVEN = True
        if((LINE_Y >= 412 and LINE_Y <= 482) and not move_line and not score_given):
            score_given = True
            if LINE_SPEED < 0:
                LINE_SPEED -= 1
                LINE_SPEED_GIVEN = True
            else:
                LINE_SPEED += 1
                LINE_SPEED_GIVEN = True
        elif(LINE_Y >= 517 and LINE_Y <= 577) and not move_line and not score_given:
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
        pygame.draw.rect(SCREEN, RED, (200, top_red_y, RECT_WIDTH, TOP_RED_HEIGHT))
        pygame.draw.rect(SCREEN, YELLOW, (200, top_red_y + TOP_RED_HEIGHT, RECT_WIDTH, YELLOW_HEIGHT_TOP))
        pygame.draw.rect(SCREEN, RED, (200, bottom_red_y, RECT_WIDTH, BOTTOM_RED_HEIGHT))
        pygame.draw.rect(SCREEN, YELLOW, (200, bottom_red_y - YELLOW_HEIGHT_BOTTOM, RECT_WIDTH, YELLOW_HEIGHT_BOTTOM))
        pygame.draw.rect(SCREEN, GREEN, (200, bottom_red_y - YELLOW_HEIGHT_BOTTOM - GREEN_HEIGHT_BOTTOM, RECT_WIDTH, GREEN_HEIGHT_BOTTOM))
        pygame.draw.rect(SCREEN, RECT_COLOR, (200, top_red_y + TOP_RED_HEIGHT + YELLOW_HEIGHT_TOP, RECT_WIDTH, RECT_HEIGHT - TOP_RED_HEIGHT - BOTTOM_RED_HEIGHT - YELLOW_HEIGHT_TOP - YELLOW_HEIGHT_BOTTOM - GREEN_HEIGHT_BOTTOM))

        pygame.draw.line(SCREEN, LINE_COLOR, (200, LINE_Y), (250, LINE_Y), LINE_WIDTH)

        # Отображение счета на экране
        score_text = FONT.render("Score: " + str(score), True, WHITE)
        SCREEN.blit(score_text, (10, 10))

        pygame.display.flip()
        pygame.time.Clock().tick(60)

# Теперь вы можете вызвать функцию draw_game и передать ей необходимые параметры экрана, цветов и размеров
