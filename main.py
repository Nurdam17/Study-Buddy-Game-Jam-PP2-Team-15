import pygame
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
end_page = False
hack_notify = False
paused = False

#------------------------------------------------------------------------------------------------------------------
#images
heart_img = pygame.transform.scale(pygame.image.load("images/icons/heart.png"), (45, 45))
brain_img = pygame.transform.scale(pygame.image.load("images/icons/brain.png"), (45, 45))
smile_img = pygame.transform.scale(pygame.image.load("images/icons/smile.png"), (45, 45))
kbtu_icon = pygame.transform.scale(pygame.image.load("images/map/kbtu.png"), (300, 200))
club_icon = pygame.transform.scale(pygame.image.load("images/map/club.png"), (100, 300))
theatre_icon = pygame.transform.scale(pygame.image.load("images/map/theatre.png"), (300, 180))
dorm_icon = pygame.transform.scale(pygame.image.load("images/map/dorm.png"), (270, 150))
pause_icon = pygame.transform.scale(pygame.image.load("images/buttons/pause.png"), (60, 60))
map_icon = pygame.transform.scale(pygame.image.load("images/icons/map_icon.png"), (60, 60))
gym_icon = pygame.transform.scale(pygame.image.load("images/map/gym_icon.png"), (270, 150))

#Backgrounds
uni_img1 = pygame.transform.scale(pygame.image.load("images/backgrounds/uni1.png"), (1700, 1465))
uni_img2 = pygame.transform.scale(pygame.image.load("images/backgrounds/uni2.png"), (1700, 1465))
uni_img3 = pygame.transform.scale(pygame.image.load("images/backgrounds/uni3.png"), (1700, 1465))
map_background = pygame.transform.scale(pygame.image.load("images/backgrounds/map.png"), (1700, 1000))
dorm_background = pygame.transform.scale(pygame.image.load("images/backgrounds/main.png"), (1700, 1465))
menu_background = pygame.transform.scale(pygame.image.load("images/backgrounds/main_blur.png"), (1700, 1465))
gym_background = pygame.transform.scale(pygame.image.load("images/backgrounds/gym.png"), (1700, 1465))
gym_for_games = pygame.transform.scale(pygame.image.load("images/backgrounds/gym_for_games.png"), (1700, 1465))
club_bg = pygame.transform.scale(pygame.image.load("images/backgrounds/club_back.png"), (1700, 1465))
theatre_bg = pygame.transform.scale(pygame.image.load("images/backgrounds/theatre.png"), (1700, 1000))

#For Gym
dumbell_5kg = pygame.transform.scale(pygame.image.load("images/icons/5kg.png"), (45, 45))
dumbell_10kg = pygame.transform.scale(pygame.image.load("images/icons/10kg.png"), (70, 70))
dumbell_15kg = pygame.transform.scale(pygame.image.load("images/icons/15kg.png"), (94, 94))
gant_bot = pygame.transform.scale(pygame.image.load("images/icons/gant_bot.png"), (400, 450))
box_img = pygame.transform.scale(pygame.image.load("images/icons/box.png"), (120, 550))
tournique_img = pygame.transform.scale(pygame.image.load("images/icons/tourniquet.png"), (400, 200))


#Images of buttons for menu page
start_img = pygame.transform.scale(pygame.image.load("images/buttons/start.png"), (300, 100))
exit_img = pygame.transform.scale(pygame.image.load("images/buttons/exit.png"), (300, 100))
resume_img = pygame.transform.scale(pygame.image.load("images/buttons/resume.png"), (300, 100))
settings_img = pygame.transform.scale(pygame.image.load("images/buttons/settings.png"), (300, 100))

#Images of notifications
accept_img = pygame.transform.scale(pygame.image.load("images/buttons/accept.png"), (100, 100))
decline_img = pygame.transform.scale(pygame.image.load("images/buttons/decline.png"), (100, 100))

#Images for uni
physics_img = pygame.transform.scale(pygame.image.load("images/buttons/physics.png"), (220, 70))
pp2_img = pygame.transform.scale(pygame.image.load("images/buttons/pp2.png"), (200, 70))
history_img = pygame.transform.scale(pygame.image.load("images/buttons/history.png"), (200, 70))

#Buttons
kbtu_button = kbtu_icon.get_rect(center = (1500, 320))
club_button = club_icon.get_rect(center = (750, 200))
theatre_button = theatre_icon.get_rect(center = (1050, 840))
dorm_button = dorm_icon.get_rect(center = (150, 240))
gym_button = gym_icon.get_rect(center = (300, 800))
pause_button = pause_icon.get_rect(center = (1650, 40))
map_button = map_icon.get_rect(center = (1650, 120))
dumbell1_button = dumbell_5kg.get_rect(center = (1095, 400))
dumbell2_button = dumbell_10kg.get_rect(center = (1116, 485))
dumbell3_button = dumbell_15kg.get_rect(center = (1136, 585))
dumbelr1_button = dumbell_5kg.get_rect(center = (905, 400))
dumbelr2_button = dumbell_10kg.get_rect(center = (883, 485))
dumbelr3_button = dumbell_15kg.get_rect(center = (859, 585))
gant_button = gant_bot.get_rect(center = (1000, 510))
box_button = box_img.get_rect(center = (220, 380))
tournique_button = tournique_img.get_rect(center = (600, 300))
start_button = start_img.get_rect(center = (WIDTH//2, HEIGHT//2 - 200))
settings_button = settings_img.get_rect(center = (WIDTH//2, HEIGHT//2 - 50))
resume_button = resume_img.get_rect(center = (WIDTH//2, HEIGHT//2 + 100))
exit_button = exit_img.get_rect(center = (WIDTH//2, HEIGHT//2 + 250))
physics_button = physics_img.get_rect(center = (70, 250))
history_button = history_img.get_rect(center = (70, 350))
pp2_button = pp2_img.get_rect(center = (70, 450))

#-------------------------------------------------------------------------------------------------------------------------

#Font
font = pygame.font.SysFont('Arial', 30)
font_notifications = pygame.font.SysFont('Arial', 20)

#Boolean variables for buttons
start_button_pressed = False

#Length of parameters
health_length = 50
smile_length = 50
brain_length = 10
timeline = 0

#Function that restart game
def restart_game():
    global health, brain, smile, timeline, hack_notify, gym_page, uni_page, menu_page, map_page, club_page, theatre_page, paused
    health = 50
    brain = 10
    smile = 50
    timeline = 0
    hack_notify = False
    gym_page = False
    map_page = False
    menu_page = False
    uni_page = False
    club_page = False
    theatre_page = False
    paused = False

while True:
    screen.fill((0, 0, 0))
    while menu_page:
        screen.blit(menu_background, (0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if start_button.collidepoint(mouse_pos):
                    main_page = True
                    menu_page = False
                
                if settings_button.collidepoint(mouse_pos):
                    settings_page = True
                    menu_page = False

                if resume_button.collidepoint(mouse_pos):
                    main_page = True
                    menu_page = False
                
                if exit_button.collidepoint(mouse_pos):
                    exit()

        screen.blit(start_img, start_button.topleft)
        screen.blit(settings_img, settings_button.topleft)
        screen.blit(resume_img, resume_button.topleft)
        screen.blit(exit_img, exit_button.topleft)
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
        draw_button.draw_button(screen, font, 72, 122, brain_length, 20, "", (0, 0, 0), (0, 123, 203), (0,0,0))
        #Drawing timeline
        draw_button.draw_button(screen, font, 1100, 20, 360, 24, "", (0, 0, 0), (255, 255, 255),(0, 0, 0))
        draw_button.draw_button(screen, font, 1102, 22, timeline/60, 20, "", (0, 0, 0), (0, 255, 0),(0, 0, 0))
        #drawing buttons for main page
        screen.blit(map_icon, map_button.topleft)
        screen.blit(pause_icon, pause_button.topleft)

        timeline+=1

        if timeline == 7200:
            hack_notify = True

        elif timeline == 7800:
            hack_notify = False
        
        elif timeline == 14400:
            hack_notify = True
        
        elif timeline == 15000:
            hack_notify = False
        
        elif timeline == 20000:
            hack_notify = True

        elif timeline == 20600:
            hack_notify = False

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
            screen.blit(kbtu_icon, kbtu_button.topleft)
            screen.blit(club_icon, club_button.topleft)
            screen.blit(theatre_icon, theatre_button.topleft)
            screen.blit(dorm_icon, dorm_button.topleft)
            screen.blit(gym_icon, gym_button.topleft)
            screen.blit(pause_icon, pause_button.topleft)
            pygame.display.update()


            while uni_page:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        exit()

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        pos = pygame.mouse.get_pos()
                        if pause_button.collidepoint(pos):
                            paused = True
                        if map_button.collidepoint(pos):
                            uni_page = False

                screen.blit(uni_img1, (0,0))
                
                screen.blit(heart_img, (15, 10))
                screen.blit(smile_img, (15, 60))
                screen.blit(brain_img, (15, 110))
                draw_button.draw_button(screen, font, 70, 20, 104, 24, "", (0, 0, 0), (255, 255, 255),(0, 0, 0))
                draw_button.draw_button(screen, font, 72, 22, health_length, 20, "", (0, 0, 0), (255, 0, 0),(0, 0, 0))
                draw_button.draw_button(screen, font, 70, 70, 104, 24, "", (0, 0, 0), (255, 255, 255),(0, 0, 0))
                draw_button.draw_button(screen, font, 72, 72, smile_length, 20, "", (0, 0, 0), (255, 255, 0), (0,0,0))
                draw_button.draw_button(screen, font, 70, 120, 104, 24, "", (0, 0, 0), (255, 255, 255),(0, 0, 0))
                draw_button.draw_button(screen, font, 72, 122, brain_length, 20, "", (0, 0, 0), (0, 123, 203), (0,0,0))

                surface_of_rect = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
                surface_of_rect.set_alpha(128)

                # Draw a transparent rectangle onto the surface
                rect = pygame.Rect(80, 200, 350, 600)
                pygame.draw.rect(surface_of_rect, (0, 0, 0), rect)
                
                #Drawing buttons
                screen.blit(pause_icon, pause_button.topleft)
                screen.blit(map_icon, map_button.topleft)
                screen.blit(surface_of_rect, (0, 0))
                screen.blit(history_img, history_button.topright)
                screen.blit(pp2_img, pp2_button.topright)
                screen.blit(physics_img, physics_button.topright)

                pygame.display.update()

                while paused:
                    screen.blit(menu_background, (0,0))
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            exit()

                        if event.type == pygame.MOUSEBUTTONDOWN:
                            mouse_pos = pygame.mouse.get_pos()
                            if start_button.collidepoint(mouse_pos):
                                restart_game()
                                main_page = True

                            
                            # if settings_rect.collidepoint(mouse_pos):
                            #     settings_page = True
                            #     menu_page = False

                            if resume_button.collidepoint(mouse_pos):
                                paused = False
                            
                            if exit_button.collidepoint(mouse_pos):
                                exit()

                    screen.blit(start_img, start_button.topleft)
                    screen.blit(settings_img, settings_button.topleft)
                    screen.blit(resume_img, resume_button.topleft)
                    screen.blit(exit_img, exit_button.topleft)
                    pygame.display.update()
                    

            while gym_page:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        exit()

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        pos = pygame.mouse.get_pos()
                        if pause_button.collidepoint(pos):
                            paused = True
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
                draw_button.draw_button(screen, font, 72, 122, brain_length, 20, "", (0, 0, 0), (0, 123, 203), (0,0,0))

                #Drawing buttons
                screen.blit(pause_icon, pause_button.topleft)
                screen.blit(map_icon, map_button.topleft)
                screen.blit(dumbell_5kg, dumbell1_button.topleft)
                screen.blit(dumbell_10kg, dumbell2_button.topleft)
                screen.blit(dumbell_15kg, dumbell3_button.topleft)
                screen.blit(dumbell_5kg, dumbelr1_button.topleft)
                screen.blit(dumbell_10kg, dumbelr2_button.topleft)
                screen.blit(dumbell_15kg, dumbelr3_button.topleft)
                screen.blit(gant_bot, gant_button.topleft)
                screen.blit(box_img, box_button.topleft)
                screen.blit(tournique_img, tournique_button.topleft)
                pygame.display.update()

                while paused:
                    screen.blit(menu_background, (0,0))
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            exit()

                        if event.type == pygame.MOUSEBUTTONDOWN:
                            mouse_pos = pygame.mouse.get_pos()
                            if start_button.collidepoint(mouse_pos):
                                restart_game()
                                main_page = True

                            
                            # if settings_rect.collidepoint(mouse_pos):
                            #     settings_page = True
                            #     menu_page = False

                            if resume_button.collidepoint(mouse_pos):
                                paused = False
                            
                            if exit_button.collidepoint(mouse_pos):
                                exit()

                    screen.blit(start_img, start_button.topleft)
                    screen.blit(settings_img, settings_button.topleft)
                    screen.blit(resume_img, resume_button.topleft)
                    screen.blit(exit_img, exit_button.topleft)
                    pygame.display.update()

            while theatre_page:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        exit()

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        pos = pygame.mouse.get_pos()
                        if pause_button.collidepoint(pos):
                            paused = True
                        if map_button.collidepoint(pos):
                            theatre_page = False


                screen.blit(theatre_bg, (0,0))
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
                draw_button.draw_button(screen, font, 72, 122, brain_length, 20, "", (0, 0, 0), (0, 123, 203), (0,0,0))

                #Drawing buttons
                screen.blit(pause_icon, pause_button.topleft)
                screen.blit(map_icon, map_button.topleft)

                pygame.display.update()

                while paused:
                    screen.blit(menu_background, (0,0))
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            exit()

                        if event.type == pygame.MOUSEBUTTONDOWN:
                            mouse_pos = pygame.mouse.get_pos()
                            if start_button.collidepoint(mouse_pos):
                                restart_game()
                                main_page = True

                            
                            # if settings_rect.collidepoint(mouse_pos):
                            #     settings_page = True
                            #     menu_page = False

                            if resume_button.collidepoint(mouse_pos):
                                paused = False
                            
                            if exit_button.collidepoint(mouse_pos):
                                exit()

                    screen.blit(start_img, start_button.topleft)
                    screen.blit(settings_img, settings_button.topleft)
                    screen.blit(resume_img, resume_button.topleft)
                    screen.blit(exit_img, exit_button.topleft)
                    pygame.display.update()


            while club_page:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        exit()

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        pos = pygame.mouse.get_pos()
                        if pause_button.collidepoint(pos):
                            paused = True

                        if map_button.collidepoint(pos):
                            club_page = False


                screen.blit(club_bg, (0,0))
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
                draw_button.draw_button(screen, font, 72, 122, brain_length, 20, "", (0, 0, 0), (0, 123, 203), (0,0,0))

                #Drawing buttons
                screen.blit(pause_icon, pause_button.topleft)
                screen.blit(map_icon, map_button.topleft)
                
                pygame.display.update()

                while paused:
                    screen.blit(menu_background, (0,0))
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            exit()

                        if event.type == pygame.MOUSEBUTTONDOWN:
                            mouse_pos = pygame.mouse.get_pos()
                            if start_button.collidepoint(mouse_pos):
                                restart_game()
                                main_page = True

                            
                            # if settings_rect.collidepoint(mouse_pos):
                            #     settings_page = True
                            #     menu_page = False

                            if resume_button.collidepoint(mouse_pos):
                                paused = False
                            
                            if exit_button.collidepoint(mouse_pos):
                                exit()

                    screen.blit(start_img, start_button.topleft)
                    screen.blit(settings_img, settings_button.topleft)
                    screen.blit(resume_img, resume_button.topleft)
                    screen.blit(exit_img, exit_button.topleft)
                    pygame.display.update() 

    while end_page:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        screen.blit(menu_background, (0,0))

        pygame.display.update()

    pygame.display.update()