import pygame

def display_text(text, font_size, color, x, y, surface):
    font = pygame.font.SysFont("font/minecraft.ttf", font_size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.topleft = (x, y)
    surface.blit(text_surface, text_rect)