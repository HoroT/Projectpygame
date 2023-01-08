import pygame
#from game_screen import Cursor

pygame.display.init()
img = pygame.image.load('картинки/fon_menu.jpg')
screen = pygame.display.set_mode(img.get_size(), pygame.FULLSCREEN)
w, h = screen.get_size()

all_sprites = pygame.sprite.Group()
sprite = pygame.sprite.Sprite()



class new(pygame.sprite.Sprite):
    image = pygame.image.load("картинки/cursor.png")

    def __init__(self, *group):
        super().__init__(*group)
        self.image = new.image
        self.image = pygame.transform.scale(self.image, (400, 50))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = w // 2 - 200, h // 3 - 150


class reg(pygame.sprite.Sprite):
    image = pygame.image.load("картинки/interface.jpg")

    def __init__(self, *group):
        super().__init__(*group)
        self.image = reg.image
        self.image = pygame.transform.scale(self.image, (400, 50))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = w // 2 - 200, h // 3


class setting(pygame.sprite.Sprite):
    image = pygame.image.load("картинки/interface.jpg")

    def __init__(self, *group):
        super().__init__(*group)
        self.image = reg.image
        self.image = pygame.transform.scale(self.image, (400, 50))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = w // 2 - 200, h // 3 + 150


class ex(pygame.sprite.Sprite):
    image = pygame.image.load("картинки/interface.jpg")

    def __init__(self, *group):
        super().__init__(*group)
        self.image = reg.image
        self.image = pygame.transform.scale(self.image, (400, 50))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = w // 3 * 2, h // 3 * 2


running = True
new(all_sprites)
reg(all_sprites)
setting(all_sprites)
ex(all_sprites)
while running:
    screen.fill((0, 0, 0))
    screen.blit(img, (0, 0))
    all_sprites.draw(screen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # program closure
            running = False
        '''if event.type == pygame.MOUSEMOTION:  # getting mouse position
            pos = event.pos
        if event.type == pygame.MOUSEBUTTONUP:  # creating a menu button
            if (w // 27) < pos[0] < (w // 27) + (w // 5):
                if (h // 171) < pos[1] < (h // 171) + (h // 26):
                    running = False'''

    '''if pygame.mouse.get_focused():
        Cursor.render(pos)'''

    pygame.display.flip()
pygame.quit()
