import pygame
import draw_button
pygame.init()

#SIZE
WIDTH = 1700
HEIGHT = 1000
FPS = 60
clock = pygame.time.Clock()

#COLORS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Student Life")
bg = pygame.image.load("images/backgrounds/main.png")
bg = pygame.transform.scale(bg, (1700, 1465))
run = True

frame_index = 0
animation_speed = 15  # Number of frames per second
clock = pygame.time.Clock()

w, h = 500, 500

blink1 = pygame.transform.scale(pygame.image.load("images/animations/blink/blink1.png"), (w, h))
blink2 = pygame.transform.scale(pygame.image.load("images/animations/blink/blink2.png"), (w, h))
blink3 = pygame.transform.scale(pygame.image.load("images/animations/blink/blink3.png"), (w, h))
blink4 = pygame.transform.scale(pygame.image.load("images/animations/blink/blink4.png"), (w, h))
blink5 = pygame.transform.scale(pygame.image.load("images/animations/blink/blink5.png"), (w, h))
blinking = [blink1, blink2, blink3, blink4, blink5]

while run:
    screen.blit(bg, (0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    screen.blit(blinking[frame_index], (280, 490))

    # Update the display
    pygame.display.flip()

    # Increment the frame index for the next frame
    frame_index = (frame_index + 1) % len(blinking)

    # Delay to control the speed of the animation
    clock.tick(animation_speed)
