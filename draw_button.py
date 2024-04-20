import pygame

def draw_button(screen, font, x, y, width, height, text, text_color, back_color, boarder_color):
    pygame.draw.rect(screen, back_color, (x, y, width, height))
    pygame.draw.rect(screen, boarder_color, (x, y, width, height), 2)  
    text_surface = font.render(text, True, text_color)
    text_rect = text_surface.get_rect(center=(x + width / 2, y + height / 2))
    screen.blit(text_surface, text_rect)