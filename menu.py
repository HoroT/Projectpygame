import pygame

# from game_screen import Cursor

pygame.display.init()
img = pygame.image.load('картинки/fon_menu.jpg')
screen = pygame.display.set_mode(img.get_size(), pygame.FULLSCREEN)
w, h = screen.get_size()

all_sprites = pygame.sprite.Group()
sprite = pygame.sprite.Sprite()


class new(pygame.sprite.Sprite):
    image = pygame.image.load("картинки/game.png")

    def __init__(self, *group):
        super().__init__(*group)
        self.image = new.image
        self.image = pygame.transform.scale(self.image, (400, 50))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = w // 2 - 200, h // 3 - 150


class reg(pygame.sprite.Sprite):
    image = pygame.image.load("картинки/img.png")

    def __init__(self, *group):
        super().__init__(*group)
        self.image = reg.image
        self.image = pygame.transform.scale(self.image, (400, 50))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = w // 2 - 200, h // 3


'''class sett(pygame.sprite.Sprite):
    image = pygame.image.load("картинки/game.png")

    def __init__(self, *group):
        super().__init__(*group)
        self.image = sett.image
        self.image = pygame.transform.scale(self.image, (400, 50))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = w // 2 - 200, h // 3 + 150'''


class ex(pygame.sprite.Sprite):
    image = pygame.image.load("картинки/ext.png")

    def __init__(self, *group):
        super().__init__(*group)
        self.image = ex.image
        self.image = pygame.transform.scale(self.image, (400, 50))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = w // 2 - 200, h // 3 + 150


running = True
new(all_sprites)
reg(all_sprites)
# sett(all_sprites)
ex(all_sprites)
pos = None
while running:
    screen.fill((0, 0, 0))
    screen.blit(img, (0, 0))
    all_sprites.draw(screen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # program closure
            running = False
        if event.type == pygame.MOUSEMOTION:  # getting mouse position
            pos = event.pos
        if event.type == pygame.MOUSEBUTTONDOWN:  # creating a menu button
            if w // 2 - 200 < pos[0] < w // 2 - 200 + 400:
                if h // 3 + 150 < pos[1] < h // 3 + 150 + 50:
                    running = False

    pygame.display.flip()
pygame.quit()
