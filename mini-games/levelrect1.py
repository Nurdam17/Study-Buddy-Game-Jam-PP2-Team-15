import pygame
import sys
from levelrect import draw_game

# Инициализация Pygame
pygame.init()

# Определение параметров окна и отображения
WIDTH, HEIGHT = 1700, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("asd")
FONT = pygame.font.Font(None, 36)
# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)

draw_game(SCREEN, WIDTH, HEIGHT, WHITE, BLACK, RED, YELLOW, GREEN, FONT)

pygame.quit()
sys.exit()