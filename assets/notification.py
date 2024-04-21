import pygame


pygame.init()

font_path = "font/minecraft.ttf"
custom_font = pygame.font.Font(font_path, 30)
custom_font1 = pygame.font.Font(font_path, 20)


notification_text = "Mr. Kelgenbayev"
notification_mess = ("Hello, do you wanna participate ")
notification_mess1 = ("on Hackathon?")

win_text = "My congratulations!"
win_mess = ("You won this hackathon")
win_mess1 = ("+8")

lose_text = "Unfortunately"
lose_mess = ("You lose")
lose_mess1 = ("-4")

ill_text = "Unfortunately"
ill_mess = "You illed"
ill_mess1 = "-10 Health"

def draw_text(surface, text, font, color, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.topleft = (x, y)
    surface.blit(text_surface, text_rect)