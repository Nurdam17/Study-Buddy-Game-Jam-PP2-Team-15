import pygame
import draw_button
pygame.init()

#SIZE
WIDTH = 1700
HEIGHT = 1000
FPS = 10
clock = pygame.time.Clock()

#COLORS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Student Life")
bg = pygame.image.load("images/backgrounds/main_bg.png")
bg = pygame.transform.scale(bg, (1700, 1465))
run = True

frame_index = 0
animation_speed = 19  # Number of frames per second
clock = pygame.time.Clock()

w, h = 500, 650

dream1 = pygame.transform.scale(pygame.image.load("images/animations/dreaming/dream1.png"), (w, h))
dream2 = pygame.transform.scale(pygame.image.load("images/animations/dreaming/dream2.png"), (w, h))
dream3 = pygame.transform.scale(pygame.image.load("images/animations/dreaming/dream3.png"), (w, h))
dream4 = pygame.transform.scale(pygame.image.load("images/animations/dreaming/dream4.png"), (w, h))
dream5 = pygame.transform.scale(pygame.image.load("images/animations/dreaming/dream5.png"), (w, h))
dream6 = pygame.transform.scale(pygame.image.load("images/animations/dreaming/dream6.png"), (w, h))
dream7 = pygame.transform.scale(pygame.image.load("images/animations/dreaming/dream7.png"), (w, h))
dream8 = pygame.transform.scale(pygame.image.load("images/animations/dreaming/dream8.png"), (w, h))
dream9 = pygame.transform.scale(pygame.image.load("images/animations/dreaming/dream9.png"), (w, h))
dream10 = pygame.transform.scale(pygame.image.load("images/animations/dreaming/dream10.png"), (w, h))
dream11 = pygame.transform.scale(pygame.image.load("images/animations/dreaming/dream11.png"), (w, h))
dream12 = pygame.transform.scale(pygame.image.load("images/animations/dreaming/dream12.png"), (w, h))
dream13 = pygame.transform.scale(pygame.image.load("images/animations/dreaming/dream13.png"), (w, h))
dream14 = pygame.transform.scale(pygame.image.load("images/animations/dreaming/dream14.png"), (w, h))
dream15 = pygame.transform.scale(pygame.image.load("images/animations/dreaming/dream15.png"), (w, h))
dream16 = pygame.transform.scale(pygame.image.load("images/animations/dreaming/dream16.png"), (w, h))
dream17 = pygame.transform.scale(pygame.image.load("images/animations/dreaming/dream17.png"), (w, h))
dream18 = pygame.transform.scale(pygame.image.load("images/animations/dreaming/dream18.png"), (w, h))
dream19 = pygame.transform.scale(pygame.image.load("images/animations/dreaming/dream19.png"), (w, h))
dreaming = [dream1, dream2, dream3, dream4, dream5, dream6, dream7,
            dream8, dream9, dream10, dream11, dream12, dream13, dream14,
            dream15, dream16, dream17, dream18, dream19]

while run:
    screen.blit(bg, (0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    screen.blit(dreaming[frame_index], (280, 350))

    # Update the display
    pygame.display.flip()

    # Increment the frame index for the next frame
    frame_index = (frame_index + 1) % len(dreaming)

    # Delay to control the speed of the animation
    clock.tick(animation_speed)
