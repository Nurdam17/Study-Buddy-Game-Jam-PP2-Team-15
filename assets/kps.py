import pygame
from sprite_player import *
damir = Student()
gym_background = pygame.transform.scale(pygame.image.load("images/backgrounds/gym_bg.png"), (1700, 1465))

def kps_game():
    pygame.init()
    WIDTH, HEIGHT = 1700, 1000
    
    SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    FONT = pygame.font.Font(None, 36)
    space_counter = 0
    space_pressed = False 
    start_time = None  

    fr_index = 0

    def display_result():
        result = FONT.render(f"KPS: {space_counter / 10} ", True, WHITE)
        SCREEN.blit(result, (200, 200))
        pygame.display.flip()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                if not space_pressed:
                    space_pressed = True
                    start_time = pygame.time.get_ticks() / 1000
                space_counter += 1

        SCREEN.blit(gym_background, (0,0))

        show_counter = FONT.render(f"Score: {space_counter}", True, WHITE)
        SCREEN.blit(show_counter, (10, 10))
        damir.ganteling(SCREEN, fr_index)
        fr_index = (fr_index + 1) % len(gantelis)

        if space_pressed:
            current_time = pygame.time.get_ticks() / 1000
            show_time = FONT.render(f"Time: {round((10 - (current_time - start_time)), 2)}", True, WHITE)
            SCREEN.blit(show_time, (200, 10))

            if current_time - start_time >= 10:
                display_result()
                pygame.time.wait(2000)
                running = False
                return space_counter

        pygame.display.flip()
        pygame.time.Clock().tick(15)