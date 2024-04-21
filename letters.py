import pygame
from sprite_player import *
import random
damir = Student()
bg = pygame.transform.scale(pygame.image.load("images/backgrounds/gym_for_games.png"), (1700, 1465))
def run_letter_game():
    pygame.init()

    WIDTH, HEIGHT = 1700, 1000
    SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("LETTER")

    WHITE = (255, 255, 255)
    fr_index = 0

    FONT = pygame.font.Font(None, 100)

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
            return score

        SCREEN.blit(bg, (0,0))

        text_surface = FONT.render(current_letter, True, WHITE)
        text_rect = text_surface.get_rect(center=(WIDTH // 2 + 400, HEIGHT // 2))
        SCREEN.blit(text_surface, text_rect)

        time_left = max(0, (end_time - current_time) // 1000)
        time_text = FONT.render("Time left: " + str(time_left), True, WHITE)
        score_text = FONT.render("Score: " + str(score), True, WHITE)
        SCREEN.blit(time_text, (10, 10))
        SCREEN.blit(score_text, (10, 80))
        damir.boxing(SCREEN, fr_index)
        fr_index = (fr_index + 1) % len(boxings)

        pygame.display.flip()

        pygame.time.delay(10)
        pygame.time.Clock().tick(10)
