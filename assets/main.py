import pygame
import draw_button
from sprite_player import *
import random
import kps
import levelrect
import letters
import notification
import hackaton
import quizpp, quizphis, quizhistoryy
import jackpot
import text
import sounds
pygame.init()

#SIZE
WIDTH = 1700
HEIGHT = 1000
FPS = 15
clock = pygame.time.Clock()

#COLORS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Study-Buddy")

menu_page = True
main_page = False
map_page = False
uni_page = False
gym_page = False
club_page = False
theatre_page = False
paused = False
pullup = False
end_page = False
hack_notify = False
paused = False
animation = False
boxing = False
pullup = False
ganteli = False
casino_page = False
showing_result = False
pp2_quiz = False
physics_quiz = False
history_quiz = False
jackpot_page = False
ill = False
win_hack = False
illness = random.randint(0, 5400)

#################################################### - ANIMATIONS - ########################################################
dream_index = 0
blink_index = 0
rotate_index = 0
box_index = 0
pullup_index = 0
ganteli_index = 0
student = Student()
actions = [rotate_head, blinking, dreaming]
#################################################### -------------- ########################################################

limits = { "history" : 0, "pp2" : 0, "physics" : 0, "boxing" : 0, "pull" : 0, "hammer" : 0, 
    "historical" : 0, "comedy" : 0, "drama" : 0, "drink" : 0, "dance" : 0}

#------------------------------------------------------------------------------------------------------------------
#images
heart_img = pygame.transform.scale(pygame.image.load("images/icons/heart.png"), (45, 45))
brain_img = pygame.transform.scale(pygame.image.load("images/icons/brain.png"), (45, 45))
smile_img = pygame.transform.scale(pygame.image.load("images/icons/smile.png"), (45, 45))
kbtu_icon = pygame.transform.scale(pygame.image.load("images/map/kbtu_icon.png"), (300, 200))
club_icon = pygame.transform.scale(pygame.image.load("images/map/club_icon.png"), (100, 300))
theatre_icon = pygame.transform.scale(pygame.image.load("images/map/theatre_icon.png"), (300, 180))
dorm_icon = pygame.transform.scale(pygame.image.load("images/map/dorm.png"), (270, 150))
pause_icon = pygame.transform.scale(pygame.image.load("images/buttons/pause.png"), (60, 60))
map_icon = pygame.transform.scale(pygame.image.load("images/icons/map_icon.png"), (60, 60))
gym_icon = pygame.transform.scale(pygame.image.load("images/map/gym_icon.png"), (270, 150))

#Backgrounds
uni_img1 = pygame.transform.scale(pygame.image.load("images/backgrounds/uniroom1.png"), (1700, 1465))
uni_img2 = pygame.transform.scale(pygame.image.load("images/backgrounds/uniroom2.png"), (1700, 1465))
uni_img3 = pygame.transform.scale(pygame.image.load("images/backgrounds/uniroom3.png"), (1700, 1465))
map_background = pygame.transform.scale(pygame.image.load("images/backgrounds/map.png"), (1700, 1000))
dorm_background = pygame.transform.scale(pygame.image.load("images/backgrounds/main_bg.png"), (1700, 1465))
menu_background = pygame.transform.scale(pygame.image.load("images/backgrounds/menu_bg.png"), (1700, 1465))
gym_background = pygame.transform.scale(pygame.image.load("images/backgrounds/gym_bg.png"), (1700, 1465))
gym_for_games = pygame.transform.scale(pygame.image.load("images/backgrounds/gym_for_games.png"), (1700, 1465))
club_bg = pygame.transform.scale(pygame.image.load("images/backgrounds/club_bg.png"), (1700, 1465))
theatre_bg = pygame.transform.scale(pygame.image.load("images/backgrounds/theatre_bg.png"), (1700, 1000))
casino_bg = pygame.transform.scale(pygame.image.load("images/backgrounds/casino_bg.png"), (1700, 1065))
notify = pygame.transform.scale(pygame.image.load("images/backgrounds/notification.png"), (400, 200))

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

#Images of notifications
accept_img = pygame.transform.scale(pygame.image.load("images/buttons/accept.png"), (200, 50))
decline_img = pygame.transform.scale(pygame.image.load("images/buttons/decline.png"), (200, 50))

#Images for uni
physics_img = pygame.transform.scale(pygame.image.load("images/buttons/physics.png"), (220, 70))
pp2_img = pygame.transform.scale(pygame.image.load("images/buttons/pp2.png"), (220, 70))
history_img = pygame.transform.scale(pygame.image.load("images/buttons/history.png"), (220, 70))

#Images for theatre
drama_img = pygame.transform.scale(pygame.image.load("images/buttons/theatre/drama_button.png"), (220, 70))
comedy_img = pygame.transform.scale(pygame.image.load("images/buttons/theatre/comedy_button.png"), (220, 70))
historical_img = pygame.transform.scale(pygame.image.load("images/buttons/theatre/historical_button.png"), (220, 70))

#Images for club
casino_img = pygame.transform.scale(pygame.image.load("images/buttons/club/casino.png"), (220, 70))
dance_img = pygame.transform.scale(pygame.image.load("images/buttons/club/dance_button.png"), (220, 70))
drink_img = pygame.transform.scale(pygame.image.load("images/buttons/club/drink_button.png"), (220, 70))
jackpot_img = pygame.transform.scale(pygame.image.load("images/buttons/club/jackpot.png"), (580, 760))

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
resume_button = resume_img.get_rect(center = (WIDTH//2, HEIGHT//2))
exit_button = exit_img.get_rect(center = (WIDTH//2, HEIGHT//2 + 200))
physics_button = physics_img.get_rect(center = (260, 300))
history_button = history_img.get_rect(center = (260, 400))
pp2_button = pp2_img.get_rect(center = (260, 500))
drama_button = drama_img.get_rect(center = (540, 450))
historical_button = historical_img.get_rect(center = (850, 450))
comedy_button = comedy_img.get_rect(center = (1170, 450))
casino_button = casino_img.get_rect(center = (1500, 900))
dance_button = dance_img.get_rect(center = (900, 900))
drink_button = drink_img.get_rect(center = (1200, 900))
jackpot_button = jackpot_img.get_rect(center = (280, 450))
accept_button = accept_img.get_rect(center = (1380, 925))
decline_button = decline_img.get_rect(center = (1580, 925))
accept_button2 = accept_img.get_rect(center = (1480, 925))
accept_button3 = accept_img.get_rect(center = (1480, 925))

#-------------------------------------------------------------------------------------------------------------------------

#Font
font = pygame.font.SysFont("font/minecraft.ttf", 30)

#Boolean variables for buttons
start_button_pressed = False

#Length of parameters
health_length = 50
smile_length = 50
brain_length = 5
space_counter = 0
win_score = 0
timeline = 0

#Function that restart game
def restart_game():
    global health_length, brain_length, smile_length, timeline, hack_notify, gym_page, uni_page, menu_page, map_page, club_page, theatre_page, paused
    health_length = 50
    brain_length = 5
    smile_length = 50
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
                

                if resume_button.collidepoint(mouse_pos):
                    main_page = True
                    menu_page = False
                
                if exit_button.collidepoint(mouse_pos):
                    exit()

        screen.blit(start_img, start_button.topleft)
        screen.blit(resume_img, resume_button.topleft)
        screen.blit(exit_img, exit_button.topleft)
        pygame.display.update()
   
    while main_page:
        if pygame.time.get_ticks() % 0.5 == 0:
            sounds.dorm1.play()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
                    
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if map_button.collidepoint(pos):
                    map_page = True
                    sounds.dorm1.stop()
                if pause_button.collidepoint(pos):
                    menu_page = True
                    main_page = False
                    sounds.dorm1.stop()

                if accept_button.collidepoint(pos):
                    showing_result = True
                    hack_notify = False

                if decline_button.collidepoint(pos):
                    hack_notify = False

                if accept_button2.collidepoint(pos):
                    showing_result = False
                    if win_hack:
                        brain_length += win_score
                        win_hack = False
                    win_score = 0

                if accept_button3.collidepoint(pos):
                    ill = False

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
        draw_button.draw_button(screen, font, 1102,  22, 2*timeline/FPS, 20, "", (0, 0, 0), (0, 255, 0),(0, 0, 0))
        #drawing buttons for main page
        screen.blit(map_icon, map_button.topleft)
        screen.blit(pause_icon, pause_button.topleft)

        timeline+=1

        if brain_length >=100:
            brain_length = 100
        if smile_length >= 100:
            smile_length = 100
        if health_length >= 100:
            health_length = 100
        
        if health_length <= 0 or brain_length <= 0 or smile_length <= 0:
                end_page = True
                main_page = False

        if timeline == illness:
            ill = True
            health_length -= 10

        if timeline%900 == 0:
            for i in limits:
                limits[i] = 0

        if timeline%150 == 0:
            health_length -= 5
            brain_length += 2
            smile_length -= 5

        if timeline%75 == 0:
            act = random.choice(actions)
            animation = True


        if timeline == 900:
            hack_notify = True

        elif timeline == 1050:
            hack_notify = False
        
        elif timeline == 1800:
            hack_notify = True
        
        elif timeline == 1950:
            hack_notify = False
        
        elif timeline == 2500:
            hack_notify = True

        elif timeline == 2650:
            hack_notify = False

        elif timeline >= 2700:
            end_page = True
            main_page = False

        if hack_notify:
            screen.blit(notify, (WIDTH - 420, HEIGHT - 250))
            notification.draw_text(screen, notification.notification_text, notification.custom_font, BLACK, WIDTH - 400, HEIGHT - 230)
            notification.draw_text(screen, notification.notification_mess, notification.custom_font1, BLACK, WIDTH - 400, HEIGHT - 170)
            notification.draw_text(screen, notification.notification_mess1, notification.custom_font1, BLACK,
                                   WIDTH - 400, HEIGHT - 130)
            screen.blit(accept_img, accept_button.topleft)
            screen.blit(decline_img, decline_button.topleft)

        if animation:
            if act == rotate_head:
                student.rotating(screen, rotate_index)
                rotate_index = (rotate_index+1) % len(rotate_head)
                if (timeline-75)%11==0:
                    animation = False
            elif act == blinking:
                student.blinking(screen, blink_index)
                blink_index = (blink_index+1) % len(blinking)
                if (timeline-75)%20==0:
                    animation = False
            elif act == dreaming:
                student.dreaming(screen, dream_index)
                dream_index = (dream_index+1) % len(dreaming)
                if (timeline-75)%42==0:
                    animation = False

        elif animation == False:
            screen.blit(student.image, (280, 490))

        if showing_result:
            screen.blit(notify, (WIDTH - 420, HEIGHT - 250))
            res = hackaton.res(brain_length)
            if res > 0:
                notification.draw_text(screen, notification.win_text, notification.custom_font, BLACK, WIDTH - 400, HEIGHT - 230)
                notification.draw_text(screen, notification.win_mess, notification.custom_font1, BLACK, WIDTH - 400, HEIGHT - 170)
                win_score = res
                win_hack = True
            else:
                notification.draw_text(screen, notification.lose_text, notification.custom_font, BLACK, WIDTH - 400, HEIGHT - 230)
                notification.draw_text(screen, notification.lose_mess, notification.custom_font1, BLACK, WIDTH - 400, HEIGHT - 170)
            screen.blit(accept_img, accept_button2)

        if ill:
            screen.blit(notify, (WIDTH - 420, HEIGHT - 250))
            notification.draw_text(screen, notification.ill_text, notification.custom_font, BLACK, WIDTH - 400, HEIGHT - 230)
            notification.draw_text(screen, notification.ill_mess, notification.custom_font1, BLACK, WIDTH - 400, HEIGHT - 170)
            notification.draw_text(screen, notification.ill_mess1, notification.custom_font1, BLACK, WIDTH - 400, HEIGHT - 130)
            screen.blit(accept_img, accept_button3.topleft)


        clock.tick(FPS)
        pygame.display.update()


        

        while map_page:
            sounds.map_back.play()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if dorm_button.collidepoint(pos):
                        map_page = False
                        sounds.map_back.stop()

                    if kbtu_button.collidepoint(pos):
                        uni_page = True
                        sounds.map_back.stop()

                    if gym_button.collidepoint(pos):
                        gym_page = True
                        sounds.map_back.stop()

                    if theatre_button.collidepoint(pos):
                        theatre_page = True
                        sounds.map_back.stop()
                    
                    if club_button.collidepoint(pos):
                        club_page = True
                        sounds.map_back.stop()

                    if pause_button.collidepoint(pos):
                        paused = True
                        sounds.map_back.stop()

            screen.blit(map_background, (0,0))
            #Drawing buttons for locations
            screen.blit(kbtu_icon, kbtu_button.topleft)
            screen.blit(club_icon, club_button.topleft)
            screen.blit(theatre_icon, theatre_button.topleft)
            screen.blit(dorm_icon, dorm_button.topleft)
            screen.blit(gym_icon, gym_button.topleft)
            screen.blit(pause_icon, pause_button.topleft)
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

                        if resume_button.collidepoint(mouse_pos):
                            paused = False
                            
                        if exit_button.collidepoint(mouse_pos):
                            exit()

                screen.blit(start_img, start_button.topleft)
                screen.blit(resume_img, resume_button.topleft)
                screen.blit(exit_img, exit_button.topleft)
                pygame.display.update()


            while uni_page:
                sounds.study.play()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        exit()

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        pos = pygame.mouse.get_pos()
                        if pause_button.collidepoint(pos):
                            paused = True
                            sounds.study.stop()
                        if map_button.collidepoint(pos):
                            uni_page = False
                            sounds.study.stop()

                        if pp2_button.collidepoint(pos) and limits["pp2"]==0:
                            pp2_quiz = True
                        
                        if physics_button.collidepoint(pos) and limits["physics"]==0:
                            physics_quiz = True

                        if history_button.collidepoint(pos) and limits["history"]==0:
                            history_quiz = True

                screen.blit(uni_img1, (0,0))
                timeline += 1

                if timeline%900 == 0:
                    for i in limits:
                        limits[i] = 0

                if timeline%150 == 0:
                    health_length -= 5
                    brain_length += 2
                    smile_length -= 5

                if timeline >= 2700:
                    end_page = True
                    main_page = False
                
                screen.blit(heart_img, (15, 10))
                screen.blit(smile_img, (15, 60))
                screen.blit(brain_img, (15, 110))
                #Drawing timeline
                draw_button.draw_button(screen, font, 1100, 20, 360, 24, "", (0, 0, 0), (255, 255, 255),(0, 0, 0))
                draw_button.draw_button(screen, font, 1102, 22, 2*timeline/FPS, 20, "", (0, 0, 0), (0, 255, 0),(0, 0, 0))
                #Drawing buttons
                draw_button.draw_button(screen, font, 70, 20, 104, 24, "", (0, 0, 0), (255, 255, 255),(0, 0, 0))
                draw_button.draw_button(screen, font, 72, 22, health_length, 20, "", (0, 0, 0), (255, 0, 0),(0, 0, 0))
                draw_button.draw_button(screen, font, 70, 70, 104, 24, "", (0, 0, 0), (255, 255, 255),(0, 0, 0))
                draw_button.draw_button(screen, font, 72, 72, smile_length, 20, "", (0, 0, 0), (255, 255, 0), (0,0,0))
                draw_button.draw_button(screen, font, 70, 120, 104, 24, "", (0, 0, 0), (255, 255, 255),(0, 0, 0))
                draw_button.draw_button(screen, font, 72, 122, brain_length, 20, "", (0, 0, 0), (0, 123, 203), (0,0,0))

                surface_of_rect = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
                surface_of_rect.set_alpha(128)

                # Draw a transparent rectangle onto the surface
                rect = pygame.Rect(110, 250, 300, 300)
                pygame.draw.rect(surface_of_rect, (0, 0, 0), rect)
                
                #Drawing buttons
                screen.blit(pause_icon, pause_button.topleft)
                screen.blit(map_icon, map_button.topleft)
                screen.blit(surface_of_rect, (0, 0))
                screen.blit(history_img, history_button.topleft)
                screen.blit(pp2_img, pp2_button.topleft)
                screen.blit(physics_img, physics_button.topleft)

                if brain_length >=100:
                    brain_length = 100
                if smile_length >= 100:
                    smile_length = 100

                if health_length <= 0 or brain_length <= 0 or smile_length <= 0:
                    end_page = True
                    uni_page = False
                    map_page = False
                    main_page = False

                pygame.display.update()
                clock.tick(15)

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

                            

                            if resume_button.collidepoint(mouse_pos):
                                paused = False
                            
                            if exit_button.collidepoint(mouse_pos):
                                exit()

                    screen.blit(start_img, start_button.topleft)
                    screen.blit(resume_img, resume_button.topleft)
                    screen.blit(exit_img, exit_button.topleft)
                    pygame.display.update()

                if pp2_quiz:
                    sc_pp = quizpp.run_quiz_game()
                    if sc_pp > -1:
                        brain_length += 3*sc_pp
                        smile_length += 4*sc_pp
                        smile_length -= (3-sc_pp)
                        limits["pp2"] += 1
                        pp2_quiz = False

                if physics_quiz:
                    sc_phy = quizphis.run_quiz_game()
                    if sc_phy > -1:
                        brain_length += 3*sc_phy
                        smile_length += 4*sc_phy
                        smile_length -= (3-sc_phy)
                        limits["physics"] += 1
                        physics_quiz = False
                        

                if history_quiz:
                    sc_hist = quizhistoryy.run_quiz_game()
                    if sc_hist > -1:
                        brain_length += sc_hist
                        smile_length += 4*sc_hist
                        smile_length -= (3-sc_hist)
                        limits["history"] += 1
                        history_quiz = False
                    

            while gym_page:
                if pygame.time.get_ticks() % 50 == 0:
                    sounds.gym.play()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        exit()

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        pos = pygame.mouse.get_pos()
                        if pause_button.collidepoint(pos):
                            paused = True
                            sounds.gym.stop()
                        if map_button.collidepoint(pos):
                            gym_page = False
                            sounds.gym.stop()

                        if tournique_button.collidepoint(pos) and limits["pull"] == 0:
                            pullup = True
                        
                        if box_button.collidepoint(pos) and limits["boxing"] == 0:
                            boxing = True
                            sounds.gym.stop()

                        if gant_button.collidepoint(pos) and limits["hammer"] == 0:
                            ganteli = True

                    
                screen.blit(gym_background, (0,0))
                timeline += 1
                if timeline >= 2700:
                    end_page = True
                    main_page = False
                screen.blit(heart_img, (15, 10))
                screen.blit(smile_img, (15, 60))
                screen.blit(brain_img, (15, 110))
                draw_button.draw_button(screen, font, 1100, 20, 360, 24, "", (0, 0, 0), (255, 255, 255),(0, 0, 0))
                draw_button.draw_button(screen, font, 1102, 22, 2*timeline/FPS, 20, "", (0, 0, 0), (0, 255, 0),(0, 0, 0))
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
                clock.tick(FPS)

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


                            if resume_button.collidepoint(mouse_pos):
                                paused = False
                            
                            if exit_button.collidepoint(mouse_pos):
                                exit()

                    screen.blit(start_img, start_button.topleft)
                    screen.blit(resume_img, resume_button.topleft)
                    screen.blit(exit_img, exit_button.topleft)
                    pygame.display.update()

                if health_length >= 100:
                    health_length = 100

                if health_length <= 0 or brain_length <= 0 or smile_length <= 0:
                    end_page = True
                    gym_page = False
                    map_page = False
                    main_page = False


                if boxing:
                    punches = letters.run_letter_game()
                    if punches > -1000:
                        health_length += punches//2
                        limits["boxing"] += 1
                        boxing = False
                    smile_length += 4

                if pullup:
                    sc_pullup = levelrect.pullup_doing(screen, WIDTH, HEIGHT, WHITE, BLACK, RED, YELLOW, GREEN, font)
                    if sc_pullup > -1:
                        health_length += sc_pullup
                        limits["pull"] += 1
                        pullup = False

                    smile_length += 4

                if ganteli:
                    sc_gantel = kps.kps_game()
                    if sc_gantel>-1:
                        if sc_gantel < 40:
                            health_length += 5
                        elif sc_gantel >=40 and sc_gantel < 90:
                            health_length += 8
                        elif sc_gantel >= 90 and sc_gantel < 130:
                            health_length += 12
                        elif sc_gantel >=130:
                            health_length += 15
                        limits["hammer"] += 1
                        ganteli = False

                    smile_length += 4



            while theatre_page:
                sounds.theatre.play()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        exit()

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        pos = pygame.mouse.get_pos()
                        if pause_button.collidepoint(pos):
                            paused = True
                            sounds.theatre.stop()
                        if map_button.collidepoint(pos):
                            theatre_page = False
                            sounds.theatre.stop()

                        if drama_button.collidepoint(pos) and limits["drama"] == 0:
                            smile_length += 2
                            brain_length += 2
                            limits["drama"] += 1

                        if comedy_button.collidepoint(pos) and limits["comedy"] == 0:
                            smile_length += 5
                            limits["comedy"] += 1

                        if historical_button.collidepoint(pos) and limits["historical"] == 0:
                            brain_length += 5
                            limits["historical"] += 1


                screen.blit(theatre_bg, (0,0))
                timeline += 1
                if timeline >= 2700:
                    end_page = True
                    main_page = False
                screen.blit(heart_img, (15, 10))
                screen.blit(smile_img, (15, 60))
                screen.blit(brain_img, (15, 110))
                draw_button.draw_button(screen, font, 1100, 20, 360, 24, "", (0, 0, 0), (255, 255, 255),(0, 0, 0))
                draw_button.draw_button(screen, font, 1102, 22, 2*timeline/FPS, 20, "", (0, 0, 0), (0, 255, 0),(0, 0, 0))
                draw_button.draw_button(screen, font, 70, 20, 104, 24, "", (0, 0, 0), (255, 255, 255),(0, 0, 0))
                draw_button.draw_button(screen, font, 72, 22, health_length, 20, "", (0, 0, 0), (255, 0, 0),(0, 0, 0))
                draw_button.draw_button(screen, font, 70, 70, 104, 24, "", (0, 0, 0), (255, 255, 255),(0, 0, 0))
                draw_button.draw_button(screen, font, 72, 72, smile_length, 20, "", (0, 0, 0), (255, 255, 0), (0,0,0))
                draw_button.draw_button(screen, font, 70, 120, 104, 24, "", (0, 0, 0), (255, 255, 255),(0, 0, 0))
                draw_button.draw_button(screen, font, 72, 122, brain_length, 20, "", (0, 0, 0), (0, 123, 203), (0,0,0))

                #Drawing buttons
                screen.blit(pause_icon, pause_button.topleft)
                screen.blit(map_icon, map_button.topleft)
                screen.blit(drama_img, drama_button)
                screen.blit(comedy_img, comedy_button)
                screen.blit(historical_img, historical_button)

                if brain_length >=100:
                    brain_length = 100
                if smile_length >= 100:
                    smile_length = 100

                if health_length <= 0 or brain_length <= 0 or smile_length <= 0:
                    end_page = True
                    theatre_page = False
                    map_page = False
                    main_page = False

                pygame.display.update()
                clock.tick(FPS)
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

                            if resume_button.collidepoint(mouse_pos):
                                paused = False
                            
                            if exit_button.collidepoint(mouse_pos):
                                exit()

                    screen.blit(start_img, start_button.topleft)
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
                        
                        if casino_button.collidepoint(pos):
                            casino_page = True
                        
                        if drink_button.collidepoint(pos) and limits["drink"] == 0:
                            smile_length += 9
                            brain_length -= 5
                            health_length -= 3
                            limits["drink"] += 1
                            
                        if dance_button.collidepoint(pos) and limits["dance"] == 0:
                            health_length += 2
                            smile_length += 5
                            brain_length -= 3
                            limits["dance"] += 1


                screen.blit(club_bg, (0,0))
                timeline += 1
                if timeline >= 2700:
                    end_page = True
                    main_page = False
                screen.blit(heart_img, (15, 10))
                screen.blit(smile_img, (15, 60))
                screen.blit(brain_img, (15, 110))
                draw_button.draw_button(screen, font, 1100, 20, 360, 24, "", (0, 0, 0), (255, 255, 255),(0, 0, 0))
                draw_button.draw_button(screen, font, 1102, 22, 2*timeline/FPS, 20, "", (0, 0, 0), (0, 255, 0),(0, 0, 0))
                draw_button.draw_button(screen, font, 70, 20, 104, 24, "", (0, 0, 0), (255, 255, 255),(0, 0, 0))
                draw_button.draw_button(screen, font, 72, 22, health_length, 20, "", (0, 0, 0), (255, 0, 0),(0, 0, 0))
                draw_button.draw_button(screen, font, 70, 70, 104, 24, "", (0, 0, 0), (255, 255, 255),(0, 0, 0))
                draw_button.draw_button(screen, font, 72, 72, smile_length, 20, "", (0, 0, 0), (255, 255, 0), (0,0,0))
                draw_button.draw_button(screen, font, 70, 120, 104, 24, "", (0, 0, 0), (255, 255, 255),(0, 0, 0))
                draw_button.draw_button(screen, font, 72, 122, brain_length, 20, "", (0, 0, 0), (0, 123, 203), (0,0,0))

                #Drawing buttons
                screen.blit(pause_icon, pause_button.topleft)
                screen.blit(map_icon, map_button.topleft)
                screen.blit(dance_img, dance_button.topleft)
                screen.blit(drink_img, drink_button.topleft)
                screen.blit(casino_img, casino_button.topleft)

                if health_length <= 0 or brain_length <= 0 or smile_length <= 0:
                    end_page = True
                    club_page = False
                    map_page = False
                    main_page = False
                
                pygame.display.update()
                clock.tick(FPS)
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

                            if resume_button.collidepoint(mouse_pos):
                                paused = False
                            
                            if exit_button.collidepoint(mouse_pos):
                                exit()

                    screen.blit(start_img, start_button.topleft)
                    screen.blit(resume_img, resume_button.topleft)
                    screen.blit(exit_img, exit_button.topleft)
                    pygame.display.update() 

                if casino_page:
                    sc = jackpot.run_game(smile_length, health_length, brain_length)
                    if sc[0] > -10000000000000000 and sc[1] > -1000000000 and sc[2] > -10000000:
                        health_length = sc[1]
                        smile_length = sc[0]
                        brain_length = sc[2]
                        casino_page = False


    while end_page:
        BLACK_C = (0,0,0)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        bg = pygame.transform.scale(pygame.image.load("images/backgrounds/notification.png"), (1700, 1000))
        screen.blit(bg, (0,0))
        if health_length >= 90 and brain_length >= 90 and smile_length>=90:
            text.display_text("You have succeeded in your studies and completed", 60, 
                              BLACK, 230, 150, screen)
            text.display_text("subjects at 4 gpa and thus you will receive an increased scholarship", 60, 
                              BLACK, 230, 300, screen)
            text.display_text(f"HP : {health_length}", 70, BLACK, 650, 450, screen)
            text.display_text(f"Happiness : {smile_length}", 70, BLACK, 650, 570, screen)
            text.display_text(f"Knowledge : {brain_length}", 70, BLACK, 650, 690, screen)
            text.display_text("You really study budy!", 80, 
                              BLACK, 550, 800, screen)
        elif health_length >=70 and smile_length >= 70 and brain_length >= 65:
            text.display_text("You finished this year well", 60, 
                              BLACK, 600, 150, screen)
            text.display_text("but unfortunately did not receive an increased scholarship", 60, 
                              BLACK, 250, 300, screen)
            text.display_text(f"HP : {health_length}", 70, BLACK, 650, 450, screen)
            text.display_text(f"Happiness : {smile_length}", 70, BLACK, 650, 570, screen)
            text.display_text(f"Knowledge : {brain_length}", 70, BLACK, 650, 690, screen)
            text.display_text("Mr Kelgenbaev is proud of you", 80, 
                              BLACK, 450, 800, screen)
        elif health_length >= 30 and smile_length >= 30 and brain_length >= 45:
            text.display_text("You couldn't pass the exams so you have F's", 60, 
                              BLACK, 400, 150, screen)
            text.display_text("Good Luck", 70, 
                              BLACK, 700, 300, screen)
            text.display_text(f"HP : {health_length}", 70, BLACK, 650, 450, screen)
            text.display_text(f"Happiness : {smile_length}", 70, BLACK, 650, 570, screen)
            text.display_text(f"Knowledge : {brain_length}", 70, BLACK, 650, 690, screen)
        else:
            text.display_text("Unfortunately, the KBTU administration expelled you from the university", 60, 
                              BLACK, 180, 250, screen)
            text.display_text("You should to look for a new university", 60, 
                              BLACK, 500, 350, screen)
            text.display_text(f"HP : {health_length}", 70, BLACK, 650, 450, screen)
            text.display_text(f"Happiness : {smile_length}", 70, BLACK, 650, 570, screen)
            text.display_text(f"Knowledge : {brain_length}", 70, BLACK, 650, 690, screen)
            text.display_text("Mr Kelgenbaev is not proud of you", 80, 
                              BLACK, 450, 800, screen)
        pygame.display.update()

    pygame.display.update()
