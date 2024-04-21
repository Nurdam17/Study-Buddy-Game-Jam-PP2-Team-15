import pygame,sys
pygame.init()

w = 800
h = 600
screen = pygame.display.set_mode((w, h))
font = pygame.font.SysFont('Arial', 30)

clock = pygame.time.Clock()
FPS = 1
start = 60
running = True

while running:
    screen.fill((0,0,0))
    text = font.render("Timer: {:.2f}".format(start), True, (255, 255, 255))
    text_rect = text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))
    screen.blit(text, text_rect)
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    start -= 1
    if start <= 0:
        running = False
    pygame.display.flip()

pygame.quit()
sys.exit()