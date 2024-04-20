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

head1 = pygame.transform.scale(pygame.image.load("images/animations/head1.png"), (w, h))
head2 = pygame.transform.scale(pygame.image.load("images/animations/head2.png"), (w, h))
head3 = pygame.transform.scale(pygame.image.load("images/animations/head3.png"), (w, h))
head4 = pygame.transform.scale(pygame.image.load("images/animations/head4.png"), (w, h))
head5 = pygame.transform.scale(pygame.image.load("images/animations/head5.png"), (w, h))
head6 = pygame.transform.scale(pygame.image.load("images/animations/head6.png"), (w, h))
head7 = pygame.transform.scale(pygame.image.load("images/animations/head7.png"), (w, h))
head8 = pygame.transform.scale(pygame.image.load("images/animations/head8.png"), (w, h))
head9 = pygame.transform.scale(pygame.image.load("images/animations/head9.png"), (w, h))
head10 = pygame.transform.scale(pygame.image.load("images/animations/head10.png"), (w, h))
head11 = pygame.transform.scale(pygame.image.load("images/animations/head11.png"), (w, h))

rotate_head = [head1, head2, head3, head4,
               head4, head5, head6, head7,
               head8, head9, head10, head11]

while run:
    screen.blit(bg, (0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    screen.blit(rotate_head[frame_index], (280, 490))

    # Update the display
    pygame.display.flip()

    # Increment the frame index for the next frame
    frame_index = (frame_index + 1) % len(rotate_head)

    # Delay to control the speed of the animation
    clock.tick(animation_speed)
