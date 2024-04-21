import pygame
from jackpot_obj import *
import random
jack = Jackpot()
bg = pygame.transform.scale(pygame.image.load("images/backgrounds/casino_bg.png"), (1700, 1065))

def run_game():
    pygame.init()
    WIDTH = 1700
    HEIGHT = 1000
    SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
    FPS = 60
    clock = pygame.time.Clock()
    i = 0
    score = 0
    v = False
    font = pygame.font.Font("font/minecraft.ttf", 45)


    SYMBOLS = ['1', '2', '3', '4', '5', '6', '7']
    PROBABILITIES = [0.166, 0.166, 0.166, 0.166, 0.166, 0.166, 0.029]
    def draw_text(text, font, color, surface, x, y):
            text_obj = font.render(text, True, color)
            text_rect = text_obj.get_rect()
            text_rect.center = (x, y)
            surface.blit(text_obj, text_rect)

    def spin_reels():
        result = []
        for _ in range(3):
            symbol = random.choices(SYMBOLS, weights=PROBABILITIES)[0]
            result.append(symbol)
        return result
    done = True
    while done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    v = True
                if event.key == pygame.K_b:
                    return score

        if v:
            SCREEN.blit(bg, (0,0))
            jack.animation(SCREEN, i)
            res = spin_reels()
            jack.locate_first(SCREEN, int(res[0]) - 1)
            jack.locate_second(SCREEN, int(res[1]) - 1)
            jack.locate_third(SCREEN, int(res[2]) - 1)
            i = (i+1)%len(jack_animation)
            if i == 29:
                v = False
                if res[0] == 7 and res[1] == 7 and res[2]==7:
                    score += 90
                elif res[0] == res[1] == res[2]:
                    score += 30
                elif res[0] == 7 or res[1] == 7 or res[2] == 0:
                    score += 5
                else:
                    score -= 3

            draw_text("Score: " + str(score), font, (255, 255, 255),
                    SCREEN, WIDTH // 2, HEIGHT // 2 - 400)
            
        if score < -33:
            done = False
            return score
            

        pygame.display.flip()
        pygame.display.update()
        clock.tick(FPS//2)