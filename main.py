import pygame, datetime
from date import *
import draw_button
import pullup_game
pygame.init()

#SIZE
WIDTH = 1700
HEIGHT = 1000
FPS = 60
clock = pygame.time.Clock()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Student Life")

menu_page = True
main_page = False
map_page = False
settings_page = False
uni_page = False
gym_page = False
club_page = False
theatre_page = False
paused = False
pullup = False
moving_down_pullup = False

#images
heart_img = pygame.image.load("images/heart.png")
heart_img = pygame.transform.scale(heart_img, (30, 30))
brain_img = pygame.image.load("images/brain.png")
brain_img = pygame.transform.scale(brain_img, (30, 30))
smile_img = pygame.image.load("images/smile.png")
smile_img = pygame.transform.scale(smile_img, (30, 30))

#Buttons
font = pygame.font.SysFont('Arial', 30)
# plus_img = pygame.image.load("/Users/damirnurmagambetov/Desktop/PP2_Labs/Lab_9/2_task/icons/plus.png")
# plus_img = pygame.transform.scale(plus_img, (40, 40))
# but1_rect = plus_img.get_rect(center = (700, 400))
# start_surface = font.render("Start Game", True, (0, 0, 0))
# start_rect = start_surface.get_rect(center=(WIDTH//2, HEIGHT//2 - 200))
# settings_surface = font.render("Settings", True, (0, 0, 0))
# settings_rect = start_surface.get_rect(center=(WIDTH//2, HEIGHT//2 - 100))
# exit_surface = font.render("Exit Game", True, (0, 0, 0))
# exit_rect = start_surface.get_rect(center=(WIDTH//2, HEIGHT//2))

#For brain
def draw_brain(x, y, width, height, text, text_color):
    pygame.draw.rect(screen, (0, 0, 255), (x, y, width, height))
    text_surface = font.render(text, True, text_color)
    text_rect = text_surface.get_rect(center=(x + width / 2, y + height / 2))
    screen.blit(text_surface, text_rect)

#Boolean variables for buttons
start_button_pressed = False

#Length of parameters
health_length = 100
smile_length = 50
brain_length = 10

uni_img = pygame.image.load("images/pixil-frame-0 (2).png")
uni_img = pygame.transform.scale(uni_img, (1700, 1465))
kbtu_img = pygame.image.load("images/kbtu.png")
kbtu_img = pygame.transform.scale(kbtu_img, (1000, 700))

speed_of_pullup = 50000


while True:
    screen.fill((0, 0, 0))
    while menu_page:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if start_rect.collidepoint(mouse_pos):
                    main_page = True
                    menu_page = False
                
                if settings_rect.collidepoint(mouse_pos):
                    settings_page = True
                    menu_page = False

                if resume_rect.collidepoint(mouse_pos):
                    main_page = True
                    menu_page = False
                
                if quit_rect.collidepoint(mouse_pos):
                    exit()

        screen.fill((128, 128, 128))
        draw_button.draw_button(screen, font, WIDTH//2, HEIGHT//2 - 200, 200, 50, "Start Game", (0, 0, 0), (255, 255, 255),(0, 0, 0))
        start_rect = pygame.Rect(WIDTH//2, HEIGHT//2 - 200, 200, 50)
        draw_button.draw_button(screen, font, WIDTH//2, HEIGHT//2 - 100, 200, 50, "Settings", (0, 0, 0), (255, 255, 255),(0, 0, 0))
        settings_rect = pygame.Rect(WIDTH//2, HEIGHT//2 - 100, 200, 50)
        draw_button.draw_button(screen, font, WIDTH//2, HEIGHT//2, 200, 50, "Resume", (0, 0, 0), (255, 255, 255),(0, 0, 0))
        resume_rect = pygame.Rect(WIDTH//2, HEIGHT//2, 200, 50)
        draw_button.draw_button(screen, font, WIDTH//2, HEIGHT//2 + 100, 200, 50, "Quit Game", (0, 0, 0), (255, 255, 255),(0, 0, 0))
        quit_rect = pygame.Rect(WIDTH//2, HEIGHT//2 + 100, 200, 50)
        pygame.display.update()

        while settings_page:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        menu_page = True
                        settings_page = False
            screen.fill((100, 100, 100))
            pygame.display.update()

    while main_page:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    menu_page = True
                    main_page = False

                    
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if map_rect.collidepoint(pos):
                    map_page = True
                    main_page = False

        screen.fill((200, 200, 200))
        screen.blit(heart_img, (10, 10))
        screen.blit(smile_img, (10, 45))
        screen.blit(brain_img, (10, 80))
        draw_button.draw_button(screen, font, 50, 10, 104, 24, "", (0, 0, 0), (255, 255, 255),(0, 0, 0))
        draw_button.draw_button(screen, font, 52, 12, health_length, 20, "", (0, 0, 0), (255, 0, 0),(0, 0, 0))
        draw_button.draw_button(screen, font, 50, 45, 104, 24, "", (0, 0, 0), (255, 255, 255),(0, 0, 0))
        draw_button.draw_button(screen, font, 52, 47, smile_length, 20, "", (0, 0, 0), (255, 255, 0), (0,0,0))
        draw_button.draw_button(screen, font, 50, 80, 104, 24, "", (0, 0, 0), (255, 255, 255),(0, 0, 0))
        draw_button.draw_button(screen, font, 52, 82, brain_length, 20, "", (0, 0, 0), (0, 0, 255), (0,0,0))
        draw_button.draw_button(screen, font, WIDTH-40, 10, 30, 30, "", (0, 0, 0), (255, 255, 255),(0, 0, 0))
        map_rect = pygame.Rect(WIDTH-40, 10, 30, 30)

        while map_page:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        main_page = True
                        map_page = False

                    if event.key == pygame.K_q:
                        uni_page = True

                    if event.key == pygame.K_g:
                        gym_page = True

                    if event.key == pygame.K_t:
                        theatre_page = True
                    
                    if event.key == pygame.K_c:
                        club_page = True

            screen.fill((100, 100, 100))
            screen.blit(kbtu_img, (0,0))
            pygame.display.update()


            while uni_page:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        exit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            uni_page = False

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        pos = pygame.mouse.get_pos()
                        pass

                screen.fill((0, 0, 0))
                screen.blit(uni_img, (0,0))
                draw_button.draw_button(screen, font, 300, 50, 300, 50, "Calculus", (255, 128, 128), (255, 255, 255),(0, 0, 0))
                draw_button.draw_button(screen, font, 850, 50, 300, 50, "History", (255, 128, 128), (255, 255, 255),(0, 0, 0))
                draw_button.draw_button(screen, font, 1300, 50, 300, 50, "Physics", (255, 128, 128), (255, 255, 255),(0, 0, 0))
                
                screen.blit(heart_img, (10, 10))
                screen.blit(smile_img, (10, 45))
                screen.blit(brain_img, (10, 80))
                draw_button.draw_button(screen, font, 50, 10, 104, 24, "", (0, 0, 0), (255, 255, 255),(0, 0, 0))
                draw_button.draw_button(screen, font, 52, 12, health_length, 20, "", (0, 0, 0), (255, 0, 0),(0, 0, 0))
                draw_button.draw_button(screen, font, 50, 45, 104, 24, "", (0, 0, 0), (255, 255, 255),(0, 0, 0))
                draw_button.draw_button(screen, font, 52, 47, smile_length, 20, "", (0, 0, 0), (255, 255, 0), (0,0,0))
                draw_button.draw_button(screen, font, 50, 80, 104, 24, "", (0, 0, 0), (255, 255, 255),(0, 0, 0))
                draw_button.draw_button(screen, font, 52, 82, brain_length, 20, "", (0, 0, 0), (0, 0, 255), (0,0,0))
                draw_button.draw_button(screen, font, WIDTH-40, 10, 30, 30, "", (0, 0, 0), (255, 255, 255),(0, 0, 0))
                
                pygame.display.update()

            while gym_page:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        exit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_g:
                            gym_page = False
                        if event.key == pygame.K_z:
                            pullup = True

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        pos = pygame.mouse.get_pos()
                        pass
                    
                screen.fill((0, 0, 0))
                draw_button.draw_button(screen, font, WIDTH//2 + 150, HEIGHT//2 - 25, 300, 50, "Get Stronger", (255, 128, 128), (255, 255, 255),(0, 0, 0))

                screen.blit(heart_img, (10, 10))
                screen.blit(smile_img, (10, 45))
                screen.blit(brain_img, (10, 80))
                draw_button.draw_button(screen, font, 50, 10, 104, 24, "", (0, 0, 0), (255, 255, 255),(0, 0, 0))
                draw_button.draw_button(screen, font, 52, 12, health_length, 20, "", (0, 0, 0), (255, 0, 0),(0, 0, 0))
                draw_button.draw_button(screen, font, 50, 45, 104, 24, "", (0, 0, 0), (255, 255, 255),(0, 0, 0))
                draw_button.draw_button(screen, font, 52, 47, smile_length, 20, "", (0, 0, 0), (255, 255, 0), (0,0,0))
                draw_button.draw_button(screen, font, 50, 80, 104, 24, "", (0, 0, 0), (255, 255, 255),(0, 0, 0))
                draw_button.draw_button(screen, font, 52, 82, brain_length, 20, "", (0, 0, 0), (0, 0, 255), (0,0,0))
                draw_button.draw_button(screen, font, WIDTH-40, 10, 30, 30, "", (0, 0, 0), (255, 255, 255),(0, 0, 0))

                while pullup:
                    screen.fill((128, 255, 255))
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            exit()
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_z:
                                pullup = False
                            if event.key == pygame.K_s:
                                moving_down_pullup = True

                    draw_button.draw_button(screen, font, 200, 200, 100, 600, "", (0, 0, 0), (255, 0, 0),(0, 0, 0))
                    draw_button.draw_button(screen, font, 200, 370, 100, 260, "", (0, 0, 0), (255, 255, 0), (0, 0, 0))
                    draw_button.draw_button(screen, font, 200, 470, 100, 60, "", (0, 0, 0), (0, 255, 0), (0, 0, 0))
                    draw_button.draw_button(screen, font, 100, 500, 300, 10, "", (0,0,0), (0, 0, 0), (0,0,0))

                pygame.display.update()

            while theatre_page:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        exit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_t:
                            theatre_page = False

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        pos = pygame.mouse.get_pos()
                        pass

                screen.fill((0, 0, 0))
                draw_button.draw_button(screen, font, 300, 50, 300, 50, "Romance", (255, 128, 128), (255, 255, 255),(0, 0, 0))
                draw_button.draw_button(screen, font, 850, 50, 300, 50, "Drama", (255, 128, 128), (255, 255, 255),(0, 0, 0))
                draw_button.draw_button(screen, font, 1300, 50, 300, 50, "Historical", (255, 128, 128), (255, 255, 255),(0, 0, 0))

                screen.blit(heart_img, (10, 10))
                screen.blit(smile_img, (10, 45))
                screen.blit(brain_img, (10, 80))
                draw_button.draw_button(screen, font, 50, 10, 104, 24, "", (0, 0, 0), (255, 255, 255),(0, 0, 0))
                draw_button.draw_button(screen, font, 52, 12, health_length, 20, "", (0, 0, 0), (255, 0, 0),(0, 0, 0))
                draw_button.draw_button(screen, font, 50, 45, 104, 24, "", (0, 0, 0), (255, 255, 255),(0, 0, 0))
                draw_button.draw_button(screen, font, 52, 47, smile_length, 20, "", (0, 0, 0), (255, 255, 0), (0,0,0))
                draw_button.draw_button(screen, font, 50, 80, 104, 24, "", (0, 0, 0), (255, 255, 255),(0, 0, 0))
                draw_button.draw_button(screen, font, 52, 82, brain_length, 20, "", (0, 0, 0), (0, 0, 255), (0,0,0))
                draw_button.draw_button(screen, font, WIDTH-40, 10, 30, 30, "", (0, 0, 0), (255, 255, 255),(0, 0, 0))

                pygame.display.update()


            while club_page:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        exit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_c:
                            club_page = False

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        pos = pygame.mouse.get_pos()
                        pass

                screen.fill((0, 0, 0))
                draw_button.draw_button(screen, font, 300, 50, 300, 50, "Just Dance", (255, 128, 128), (255, 255, 255),(0, 0, 0))
                draw_button.draw_button(screen, font, 850, 50, 300, 50, "Iwu jane Qyzben tanysu", (255, 128, 128), (255, 255, 255),(0, 0, 0))
                draw_button.draw_button(screen, font, 1300, 50, 300, 50, "Jestko iwu", (255, 128, 128), (255, 255, 255),(0, 0, 0))

                screen.blit(heart_img, (10, 10))
                screen.blit(smile_img, (10, 45))
                screen.blit(brain_img, (10, 80))
                draw_button.draw_button(screen, font, 50, 10, 104, 24, "", (0, 0, 0), (255, 255, 255),(0, 0, 0))
                draw_button.draw_button(screen, font, 52, 12, health_length, 20, "", (0, 0, 0), (255, 0, 0),(0, 0, 0))
                draw_button.draw_button(screen, font, 50, 45, 104, 24, "", (0, 0, 0), (255, 255, 255),(0, 0, 0))
                draw_button.draw_button(screen, font, 52, 47, smile_length, 20, "", (0, 0, 0), (255, 255, 0), (0,0,0))
                draw_button.draw_button(screen, font, 50, 80, 104, 24, "", (0, 0, 0), (255, 255, 255),(0, 0, 0))
                draw_button.draw_button(screen, font, 52, 82, brain_length, 20, "", (0, 0, 0), (0, 0, 255), (0,0,0))
                draw_button.draw_button(screen, font, WIDTH-40, 10, 30, 30, "", (0, 0, 0), (255, 255, 255),(0, 0, 0))
                
                pygame.display.update()

        pygame.display.update()