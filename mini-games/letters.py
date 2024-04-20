import pygame
import sys
import random

def run_letter_game():
    pygame.init()

    WIDTH, HEIGHT = 800, 600
    SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("LETTER")

    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    FONT = pygame.font.Font(None, 100)
    SMALL_FONT = pygame.font.Font(None, 36)

    score = 0
    time_limit = 5000
    current_time = pygame.time.get_ticks()
    end_time = current_time + time_limit

    running = True

    current_letter = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.unicode.upper() == current_letter:
                    score += 1
                    current_letter = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
                    current_time = pygame.time.get_ticks()
                    end_time = current_time + time_limit
                else:
                    score -= 1

                time_limit -= 500

                if time_limit < 1000:
                    time_limit = 1000

        current_time = pygame.time.get_ticks()

        if current_time >= end_time:
            running = False

        SCREEN.fill(BLACK)

        text_surface = FONT.render(current_letter, True, WHITE)
        text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        SCREEN.blit(text_surface, text_rect)

        time_left = max(0, (end_time - current_time) // 1000)
        time_text = FONT.render("Time left: " + str(time_left), True, WHITE)
        SCREEN.blit(time_text, (10, 10))

        pygame.display.flip()

        pygame.time.delay(10)

    pygame.quit()
    sys.exit()
