import pygame
w_jack = 600
h_jack = 600

jack_initial_img = pygame.transform.scale(pygame.image.load("images/animations/jackpot_playing/jack1.png"), (w_jack, h_jack))

jack1 = pygame.transform.scale(pygame.image.load("images/animations/jackpot_playing/jack1.png"), (w_jack, h_jack))
jack2 = pygame.transform.scale(pygame.image.load("images/animations/jackpot_playing/jack2.png"), (w_jack, h_jack))
jack3 = pygame.transform.scale(pygame.image.load("images/animations/jackpot_playing/jack3.png"), (w_jack, h_jack))
jack4 = pygame.transform.scale(pygame.image.load("images/animations/jackpot_playing/jack4.png"), (w_jack, h_jack))
jack5 = pygame.transform.scale(pygame.image.load("images/animations/jackpot_playing/jack5.png"), (w_jack, h_jack))
jack6 = pygame.transform.scale(pygame.image.load("images/animations/jackpot_playing/jack6.png"), (w_jack, h_jack))
jack7 = pygame.transform.scale(pygame.image.load("images/animations/jackpot_playing/jack7.png"), (w_jack, h_jack))
jack8 = pygame.transform.scale(pygame.image.load("images/animations/jackpot_playing/jack8.png"), (w_jack, h_jack))
jack9 = pygame.transform.scale(pygame.image.load("images/animations/jackpot_playing/jack9.png"), (w_jack, h_jack))
jack10 = pygame.transform.scale(pygame.image.load("images/animations/jackpot_playing/jack10.png"), (w_jack, h_jack))
jack11 = pygame.transform.scale(pygame.image.load("images/animations/jackpot_playing/jack11.png"), (w_jack, h_jack))
jack12 = pygame.transform.scale(pygame.image.load("images/animations/jackpot_playing/jack12.png"), (w_jack, h_jack))
jack13 = pygame.transform.scale(pygame.image.load("images/animations/jackpot_playing/jack13.png"), (w_jack, h_jack))
jack14 = pygame.transform.scale(pygame.image.load("images/animations/jackpot_playing/jack14.png"), (w_jack, h_jack))
jack15 = pygame.transform.scale(pygame.image.load("images/animations/jackpot_playing/jack15.png"), (w_jack, h_jack))
jack16 = pygame.transform.scale(pygame.image.load("images/animations/jackpot_playing/jack16.png"), (w_jack, h_jack))
jack17 = pygame.transform.scale(pygame.image.load("images/animations/jackpot_playing/jack17.png"), (w_jack, h_jack))
jack18 = pygame.transform.scale(pygame.image.load("images/animations/jackpot_playing/jack18.png"), (w_jack, h_jack))
jack19 = pygame.transform.scale(pygame.image.load("images/animations/jackpot_playing/jack19.png"), (w_jack, h_jack))
jack20 = pygame.transform.scale(pygame.image.load("images/animations/jackpot_playing/jack20.png"), (w_jack, h_jack))
jack21 = pygame.transform.scale(pygame.image.load("images/animations/jackpot_playing/jack21.png"), (w_jack, h_jack))
jack22 = pygame.transform.scale(pygame.image.load("images/animations/jackpot_playing/jack22.png"), (w_jack, h_jack))
jack23 = pygame.transform.scale(pygame.image.load("images/animations/jackpot_playing/jack23.png"), (w_jack, h_jack))
jack24 = pygame.transform.scale(pygame.image.load("images/animations/jackpot_playing/jack24.png"), (w_jack, h_jack))
jack25 = pygame.transform.scale(pygame.image.load("images/animations/jackpot_playing/jack25.png"), (w_jack, h_jack))
jack26 = pygame.transform.scale(pygame.image.load("images/animations/jackpot_playing/jack26.png"), (w_jack, h_jack))
jack27 = pygame.transform.scale(pygame.image.load("images/animations/jackpot_playing/jack27.png"), (w_jack, h_jack))
jack28 = pygame.transform.scale(pygame.image.load("images/animations/jackpot_playing/jack28.png"), (w_jack, h_jack))
jack29 = pygame.transform.scale(pygame.image.load("images/animations/jackpot_playing/jack29.png"), (w_jack, h_jack))
jack30 = pygame.transform.scale(pygame.image.load("images/animations/jackpot_playing/jack30.png"), (w_jack, h_jack))

jack_animation = [jack1, jack2, jack3, jack4, jack5, jack6, jack7, jack8, jack9, jack10,
                  jack11, jack12, jack13, jack14, jack15, jack16, jack17, jack18, jack19, jack20,
                  jack21, jack22, jack23, jack24, jack25, jack26, jack27, jack28, jack29, jack30]

w_num = 81
h_num = 81
num1 = pygame.transform.scale(pygame.image.load("images/icons/jackpot_numbers/num1.png"), (w_num, h_num))
num2 = pygame.transform.scale(pygame.image.load("images/icons/jackpot_numbers/num2.png"), (w_num, h_num))
num3 = pygame.transform.scale(pygame.image.load("images/icons/jackpot_numbers/num3.png"), (w_num, h_num))
num4 = pygame.transform.scale(pygame.image.load("images/icons/jackpot_numbers/num4.png"), (w_num, h_num))
num5 = pygame.transform.scale(pygame.image.load("images/icons/jackpot_numbers/num5.png"), (w_num, h_num))
num6 = pygame.transform.scale(pygame.image.load("images/icons/jackpot_numbers/num6.png"), (w_num, h_num))
num7 = pygame.transform.scale(pygame.image.load("images/icons/jackpot_numbers/num7.png"), (w_num, h_num))
nums = [num1, num2, num3, num4, num5, num6, num7]

class Jackpot(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = jack_initial_img
        self.rect = self.image.get_rect()
        self.rect.x = 570
        self.rect.y = 200
        self.rect.center = (self.rect.x, self.rect.y) 

    def animation(self,screen, frame_index):
        screen.blit(jack_animation[frame_index], self.rect.center)

    def locate_first(self, screen, index):
        screen.blit(nums[index], (self.rect.x + 430, self.rect.y + 629))

    def locate_second(self, screen, index):
        screen.blit(nums[index], (self.rect.x + 560, self.rect.y + 629))

    def locate_third(self, screen, index):
        screen.blit(nums[index], (self.rect.x + 690, self.rect.y + 629))