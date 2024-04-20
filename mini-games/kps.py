import pygame
import sys

pygame.init()
WIDTH, HEIGHT = 1000, 800
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Kps")
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FONT = pygame.font.Font(None, 36)
space_counter = 0
space_pressed = False
start_time = None

def display_result():
    result = FONT.render(f"KPS: {space_counter / 10} ", True, WHITE)
    SCREEN.blit(result, (200, 200  ))
    pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            if not space_pressed:
                space_pressed = True
                start_time = pygame.time.get_ticks() / 1000
            space_counter += 1

    SCREEN.fill(BLACK)

    show_counter = FONT.render(f"Hits: {space_counter}", True, WHITE)
    SCREEN.blit(show_counter, (10, 10))

    if space_pressed:
        current_time = pygame.time.get_ticks() / 1000
        show_time = FONT.render(f"Time: {round((10 - (current_time - start_time)), 2)}", True, WHITE)
        SCREEN.blit(show_time, (200, 10))
        if current_time - start_time >= 10:
            display_result()
            pygame.time.wait(5000)
            running = False

    pygame.display.flip()

pygame.quit()
sys.exit()
