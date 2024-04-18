import pygame, datetime
import draw_button
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
end_page = False
hack_notify = False


#images
heart_img = pygame.transform.scale(pygame.image.load("images/icons/heart.png"), (45, 45))
brain_img = pygame.transform.scale(pygame.image.load("images/icons/brain.png"), (45, 45))
smile_img = pygame.transform.scale(pygame.image.load("images/icons/smile.png"), (45, 45))
kbtu_icon = pygame.transform.scale(pygame.image.load("images/map/kbtu.png"), (300, 200))
club_icon = pygame.transform.scale(pygame.image.load("images/map/club.png"), (100, 300))
theatre_icon = pygame.transform.scale(pygame.image.load("images/map/theatre.png"), (300, 180))
dorm_icon = pygame.transform.scale(pygame.image.load("images/map/dorm.png"), (270, 150))
pause_icon = pygame.transform.scale(pygame.image.load("images/buttons/pause.png"), (60, 60))
tasklist_icon = pygame.transform.scale(pygame.image.load("images/buttons/taskslist.png"), (60, 60))
map_icon = pygame.transform.scale(pygame.image.load("images/icons/map_icon.png"), (60, 60))
gym_icon = pygame.transform.scale(pygame.image.load("images/icons/gym_icon.png"), (270, 150))

#Backgrounds
uni_img1 = pygame.transform.scale(pygame.image.load("images/backgrounds/uni1.png"), (1700, 1465))
uni_img2 = pygame.transform.scale(pygame.image.load("images/backgrounds/uni2.png"), (1700, 1465))
uni_img3 = pygame.transform.scale(pygame.image.load("images/backgrounds/uni3.png"), (1700, 1465))
map_background = pygame.transform.scale(pygame.image.load("images/backgrounds/map.png"), (1700, 1000))
dorm_background = pygame.transform.scale(pygame.image.load("images/backgrounds/main.png"), (1700, 1465))
menu_background = pygame.transform.scale(pygame.image.load("images/backgrounds/main_blur.png"), (1700, 1465))
gym_background = pygame.transform.scale(pygame.image.load("images/backgrounds/gym.png"), (1700, 1465))
gym_for_games = pygame.transform.scale(pygame.image.load("images/backgrounds/gym_for_games.png"), (1700, 1465))
#Buttons
kbtu_button = kbtu_icon.get_rect(center = (1500, 320))
club_button = club_icon.get_rect(center = (750, 200))
theatre_button = theatre_icon.get_rect(center = (1050, 840))
dorm_button = dorm_icon.get_rect(center = (150, 240))
gym_button = gym_icon.get_rect(center = (300, 800))
pause_button = pause_icon.get_rect(center = (1650, 40))
map_button = map_icon.get_rect(center = (1650, 120))
tasklist_button = tasklist_icon.get_rect(center = (1650, 200))


#Font
font = pygame.font.SysFont('Arial', 30)
font_notifications = pygame.font.SysFont('Arial', 20)

#Boolean variables for buttons
start_button_pressed = False

#Length of parameters
health_length = 100
smile_length = 50
brain_length = 10
timeline = 0


while True:
    screen.fill((0, 0, 0))
    while menu_page:
        screen.blit(menu_background, (0,0))
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
                    
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if map_button.collidepoint(pos):
                    map_page = True
                if pause_button.collidepoint(pos):
                    menu_page = True
                    main_page = False

        screen.fill((200, 200, 200))
        screen.blit(dorm_background, (0,0))
        screen.blit(heart_img, (15, 10))
        screen.blit(smile_img, (15, 60))
        screen.blit(brain_img, (15, 110))
        draw_button.draw_button(screen, font, 70, 20, 104, 24, "", (0, 0, 0), (255, 255, 255),(0, 0, 0))
        draw_button.draw_button(screen, font, 72, 22, health_length, 20, "", (0, 0, 0), (255, 0, 0),(0, 0, 0))
        draw_button.draw_button(screen, font, 70, 70, 104, 24, "", (0, 0, 0), (255, 255, 255),(0, 0, 0))
        draw_button.draw_button(screen, font, 72, 72, smile_length, 20, "", (0, 0, 0), (255, 255, 0), (0,0,0))
        draw_button.draw_button(screen, font, 70, 120, 104, 24, "", (0, 0, 0), (255, 255, 255),(0, 0, 0))
        draw_button.draw_button(screen, font, 72, 122, brain_length, 20, "", (0, 0, 0), (0, 0, 255), (0,0,0))
        #Drawing timeline
        draw_button.draw_button(screen, font, 1100, 20, 360, 24, "", (0, 0, 0), (255, 255, 255),(0, 0, 0))
        draw_button.draw_button(screen, font, 1102, 22, timeline/60, 20, "", (0, 0, 0), (0, 255, 0),(0, 0, 0))
        #drawing buttons for main page
        pygame.draw.rect(screen, (255, 253, 214), map_button)
        screen.blit(map_icon, map_button.topleft)
        pygame.draw.rect(screen, (255, 253, 214), tasklist_button)
        screen.blit(tasklist_icon, tasklist_button.topleft)
        pygame.draw.rect(screen, (255, 253, 214), pause_button)
        screen.blit(pause_icon, pause_button.topleft)

        timeline+=1

        if timeline == 360:
            hack_notify = True

        elif timeline == 720:
            hack_notify = False
        
        elif timeline == 14400:
            hack_notify = True
        
        elif timeline == 20000:
            hack_notify = True

        elif timeline == 21600:
            end_page = True
            main_page = False

        if hack_notify:
            draw_button.draw_button(screen, font_notifications, 500, 300, 500, 300, "MR Kelgenbayev: Hello everyone! If you want to participate in Game Jam, then accept it", (0, 0,0), (255, 255, 255), (0,0,0))
        clock.tick(FPS)
        pygame.display.update()


        

        while map_page:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if dorm_button.collidepoint(pos):
                        map_page = False

                    if kbtu_button.collidepoint(pos):
                        uni_page = True

                    if gym_button.collidepoint(pos):
                        gym_page = True

                    if theatre_button.collidepoint(pos):
                        theatre_page = True
                    
                    if club_button.collidepoint(pos):
                        club_page = True

                    if pause_button.collidepoint(pos):
                        menu_page = True
                        map_page = False

            screen.fill((100, 100, 100))
            screen.blit(map_background, (0,0))
            #Drawing buttons for locations
            pygame.draw.rect(screen, (255, 253, 214), kbtu_button)
            screen.blit(kbtu_icon, kbtu_button.topleft)
            pygame.draw.rect(screen, (255, 253, 214), club_button)
            screen.blit(club_icon, club_button.topleft)
            pygame.draw.rect(screen, (255, 253, 214), theatre_button)
            screen.blit(theatre_icon, theatre_button.topleft)
            pygame.draw.rect(screen, (255, 253, 214), dorm_button)
            screen.blit(dorm_icon, dorm_button.topleft)
            pygame.draw.rect(screen, (255, 253, 214), gym_button)
            screen.blit(gym_icon, gym_button.topleft)
            pygame.draw.rect(screen, (255, 253, 214), pause_button)
            screen.blit(pause_icon, pause_button.topleft)
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
                        if pause_button.collidepoint(pos):
                            menu_page = True
                            uni_page = False
                            map_page = False
                        if map_button.collidepoint(pos):
                            uni_page = False

                screen.fill((0, 0, 0))
                screen.blit(uni_img1, (0,0))
                draw_button.draw_button(screen, font, 300, 50, 300, 50, "Calculus", (255, 128, 128), (255, 255, 255),(0, 0, 0))
                draw_button.draw_button(screen, font, 850, 50, 300, 50, "History", (255, 128, 128), (255, 255, 255),(0, 0, 0))
                draw_button.draw_button(screen, font, 1300, 50, 300, 50, "Physics", (255, 128, 128), (255, 255, 255),(0, 0, 0))
                
                screen.blit(heart_img, (15, 10))
                screen.blit(smile_img, (15, 60))
                screen.blit(brain_img, (15, 110))
                draw_button.draw_button(screen, font, 70, 20, 104, 24, "", (0, 0, 0), (255, 255, 255),(0, 0, 0))
                draw_button.draw_button(screen, font, 72, 22, health_length, 20, "", (0, 0, 0), (255, 0, 0),(0, 0, 0))
                draw_button.draw_button(screen, font, 70, 70, 104, 24, "", (0, 0, 0), (255, 255, 255),(0, 0, 0))
                draw_button.draw_button(screen, font, 72, 72, smile_length, 20, "", (0, 0, 0), (255, 255, 0), (0,0,0))
                draw_button.draw_button(screen, font, 70, 120, 104, 24, "", (0, 0, 0), (255, 255, 255),(0, 0, 0))
                draw_button.draw_button(screen, font, 72, 122, brain_length, 20, "", (0, 0, 0), (0, 0, 255), (0,0,0))
                
                #Drawing buttons
                pygame.draw.rect(screen, (255, 253, 214), pause_button)
                screen.blit(pause_icon, pause_button.topleft)
                pygame.draw.rect(screen, (255, 253, 214), map_button)
                screen.blit(map_icon, map_button.topleft)

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
                        if pause_button.collidepoint(pos):
                            menu_page = True
                            gym_page = False
                            map_page = False
                        if map_button.collidepoint(pos):
                            gym_page = False

                    
                screen.blit(gym_background, (0,0))

                screen.blit(heart_img, (15, 10))
                screen.blit(smile_img, (15, 60))
                screen.blit(brain_img, (15, 110))
                draw_button.draw_button(screen, font, 70, 20, 104, 24, "", (0, 0, 0), (255, 255, 255),(0, 0, 0))
                draw_button.draw_button(screen, font, 72, 22, health_length, 20, "", (0, 0, 0), (255, 0, 0),(0, 0, 0))
                draw_button.draw_button(screen, font, 70, 70, 104, 24, "", (0, 0, 0), (255, 255, 255),(0, 0, 0))
                draw_button.draw_button(screen, font, 72, 72, smile_length, 20, "", (0, 0, 0), (255, 255, 0), (0,0,0))
                draw_button.draw_button(screen, font, 70, 120, 104, 24, "", (0, 0, 0), (255, 255, 255),(0, 0, 0))
                draw_button.draw_button(screen, font, 72, 122, brain_length, 20, "", (0, 0, 0), (0, 0, 255), (0,0,0))

                #Drawing buttons
                pygame.draw.rect(screen, (255, 253, 214), pause_button)
                screen.blit(pause_icon, pause_button.topleft)
                pygame.draw.rect(screen, (255, 253, 214), map_button)
                screen.blit(map_icon, map_button.topleft)
                pygame.display.update()

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

            while theatre_page:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        exit()

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        pos = pygame.mouse.get_pos()
                        if pause_button.collidepoint(pos):
                            menu_page = True
                            theatre_page = False
                            map_page = False
                        if map_button.collidepoint(pos):
                            theatre_page = False


                screen.fill((0, 0, 0))
                draw_button.draw_button(screen, font, 300, 50, 300, 50, "Romance", (255, 128, 128), (255, 255, 255),(0, 0, 0))
                draw_button.draw_button(screen, font, 850, 50, 300, 50, "Drama", (255, 128, 128), (255, 255, 255),(0, 0, 0))
                draw_button.draw_button(screen, font, 1300, 50, 300, 50, "Historical", (255, 128, 128), (255, 255, 255),(0, 0, 0))

                screen.blit(heart_img, (15, 10))
                screen.blit(smile_img, (15, 60))
                screen.blit(brain_img, (15, 110))
                draw_button.draw_button(screen, font, 70, 20, 104, 24, "", (0, 0, 0), (255, 255, 255),(0, 0, 0))
                draw_button.draw_button(screen, font, 72, 22, health_length, 20, "", (0, 0, 0), (255, 0, 0),(0, 0, 0))
                draw_button.draw_button(screen, font, 70, 70, 104, 24, "", (0, 0, 0), (255, 255, 255),(0, 0, 0))
                draw_button.draw_button(screen, font, 72, 72, smile_length, 20, "", (0, 0, 0), (255, 255, 0), (0,0,0))
                draw_button.draw_button(screen, font, 70, 120, 104, 24, "", (0, 0, 0), (255, 255, 255),(0, 0, 0))
                draw_button.draw_button(screen, font, 72, 122, brain_length, 20, "", (0, 0, 0), (0, 0, 255), (0,0,0))

                #Drawing buttons
                pygame.draw.rect(screen, (255, 253, 214), pause_button)
                screen.blit(pause_icon, pause_button.topleft)
                pygame.draw.rect(screen, (255, 253, 214), map_button)
                screen.blit(map_icon, map_button.topleft)

                pygame.display.update()


            while club_page:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        exit()

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        pos = pygame.mouse.get_pos()
                        if pause_button.collidepoint(pos):
                            menu_page = True
                            club_page = False
                            map_page = False

                        if map_button.collidepoint(pos):
                            club_page = False


                screen.fill((0, 0, 0))
                draw_button.draw_button(screen, font, 300, 50, 300, 50, "Just Dance", (255, 128, 128), (255, 255, 255),(0, 0, 0))
                draw_button.draw_button(screen, font, 850, 50, 300, 50, "Iwu jane Qyzben tanysu", (255, 128, 128), (255, 255, 255),(0, 0, 0))
                draw_button.draw_button(screen, font, 1300, 50, 300, 50, "Casino", (255, 128, 128), (255, 255, 255),(0, 0, 0))

                screen.blit(heart_img, (15, 10))
                screen.blit(smile_img, (15, 60))
                screen.blit(brain_img, (15, 110))
                draw_button.draw_button(screen, font, 70, 20, 104, 24, "", (0, 0, 0), (255, 255, 255),(0, 0, 0))
                draw_button.draw_button(screen, font, 72, 22, health_length, 20, "", (0, 0, 0), (255, 0, 0),(0, 0, 0))
                draw_button.draw_button(screen, font, 70, 70, 104, 24, "", (0, 0, 0), (255, 255, 255),(0, 0, 0))
                draw_button.draw_button(screen, font, 72, 72, smile_length, 20, "", (0, 0, 0), (255, 255, 0), (0,0,0))
                draw_button.draw_button(screen, font, 70, 120, 104, 24, "", (0, 0, 0), (255, 255, 255),(0, 0, 0))
                draw_button.draw_button(screen, font, 72, 122, brain_length, 20, "", (0, 0, 0), (0, 0, 255), (0,0,0))

                #Drawing buttons
                pygame.draw.rect(screen, (255, 253, 214), pause_button)
                screen.blit(pause_icon, pause_button.topleft)
                pygame.draw.rect(screen, (255, 253, 214), map_button)
                screen.blit(map_icon, map_button.topleft)
                
                pygame.display.update()

    while end_page:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        screen.blit(menu_background, (0,0))

        pygame.display.update()

    pygame.display.update()