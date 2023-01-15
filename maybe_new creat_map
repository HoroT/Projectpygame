import os
import sys

import pygame

FPS = 50
pygame.init()
pygame.key.set_repeat(200, 70)

size = WIDTH, HEIGHT = 1000, 1000
STEP = 50

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()


def load_level(filename):
    filename = "data/" + filename
    # читаем уровень, убирая символы перевода строки
    with open(filename, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]

    # и подсчитываем максимальную длину
    max_width = max(map(len, level_map))

    # дополняем каждую строку пустыми клетками ('.')
    return list(map(lambda x: x.ljust(max_width, '.'), level_map))


def load_image(name, color_key=None):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname).convert()
    except pygame.error as message:
        print('Cannot load image:', name)
        raise SystemExit(message)

    if color_key is not None:
        if color_key == -1:
            color_key = image.get_at((0, 0))
        image.set_colorkey(color_key)
    else:
        image = image.convert_alpha()
    return image


tile_images = {
    'hor_wall': pygame.image.load('data/hor_wall.png'),
    'empty': pygame.image.load('data/grass.png'),
    'ver_wall': pygame.image.load('data/ver_wall.png'),
    'r1_wall': pygame.image.load('data/right_wall.png'),
    'l1_wall': pygame.image.load('data/left_wall.png'),
    'r2_wall': pygame.image.load('data/right_wall2.png'),
    'l2_wall': pygame.image.load('data/left_wall2.png'),
    't1_u': pygame.image.load('data/t1_u.png'),
    't2_u': pygame.image.load('data/t2_u.png'),
    't3_u': pygame.image.load('data/t3_u.png'),
    't1_d': pygame.image.load('data/t1_d.png'),
    't2_d': pygame.image.load('data/t2_d.png'),
    't3_d': pygame.image.load('data/t3_d.png'),
    'rd': pygame.image.load('data/road.png'),
    'wt': pygame.image.load('data/water.png'),
    'farm': pygame.image.load('data/farm.png')
}
player_image = load_image('mar.png')

tile_width = tile_height = 50
player = None
all_sprites = pygame.sprite.Group()
tiles_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()


class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(tiles_group, all_sprites)
        self.image = tile_images[tile_type]
        self.rect = self.image.get_rect().move(
            tile_width * pos_x, tile_height * pos_y)


class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(player_group, all_sprites)
        self.image = player_image
        self.rect = self.image.get_rect().move(
            tile_width * pos_x + 15, tile_height * pos_y + 5)


def generate_level(level):
    new_player, x, y = None, None, None
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == '.':
                Tile('empty', x, y)
            elif level[y][x] == '#':
                Tile('hor_wall', x, y)
            elif level[y][x] == '1':
                Tile('ver_wall', x, y)
            elif level[y][x] == '@':
                Tile('empty', x, y)
                new_player = Player(x, y)
            elif level[y][x] == '2':
                Tile('r1_wall', x, y)
            elif level[y][x] == '3':
                Tile('l1_wall', x, y)
            elif level[y][x] == '4':
                Tile('l2_wall', x, y)
            elif level[y][x] == '5':
                Tile('r2_wall', x, y)
            elif level[y][x] == 't':
                Tile('t1_u', x, y)
            elif level[y][x] == '6':
                Tile('t2_u', x, y)
            elif level[y][x] == '7':
                Tile('t3_u', x, y)
            elif level[y][x] == '8':
                Tile('t1_d', x, y)
            elif level[y][x] == '9':
                Tile('t2_d', x, y)
            elif level[y][x] == '0':
                Tile('t3_d', x, y)
            elif level[y][x] == 'r':
                Tile('rd', x, y)
            elif level[y][x] == 'w':
                Tile('wt', x, y)
            elif level[y][x] == 'f':
                Tile('farm', x, y)
    # вернем игрока, а также размер поля в клетках
    return new_player, x, y


def terminate():
    pygame.quit()
    sys.exit()


def start_screen():
    intro_text = ["ЗАСТАВКА", "",
                  "Правила игры",
                  "Если в правилах несколько строк,",
                  "приходится выводить их построчно"]

    fon = pygame.transform.scale(load_image('fon.jpg'), (WIDTH, HEIGHT))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 50
    for line in intro_text:
        string_rendered = font.render(line, True, pygame.Color('white'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                return  # начинаем игру

        clock.tick(FPS)


class Camera:
    # зададим начальный сдвиг камеры
    def __init__(self):
        self.dx = 0
        self.dy = 0

    # сдвинуть объект obj на смещение камеры
    def apply(self, obj):
        obj.rect.x += self.dx
        obj.rect.y += self.dy

    # позиционировать камеру на объекте target
    def update(self, target):
        self.dx = -(target.rect.x + target.rect.w // 2 - WIDTH // 2)
        self.dy = -(target.rect.y + target.rect.h // 2 - HEIGHT // 2)


#start_screen()
player, level_x, level_y = generate_level(load_level('map.txt'))
running = True
camera = Camera()
camera.update(player)
for sprite in all_sprites:
    camera.apply(sprite)
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.rect.x -= STEP
            if event.key == pygame.K_RIGHT:
                player.rect.x += STEP
            if event.key == pygame.K_UP:
                player.rect.y -= STEP
            if event.key == pygame.K_DOWN:
                player.rect.y += STEP
            # изменяем ракурс камеры
            camera.update(player)
            # обновляем положение всех спрайтов
            for sprite in all_sprites:
                camera.apply(sprite)

    screen.fill(pygame.Color(0, 0, 0))
    tiles_group.draw(screen)
    player_group.draw(screen)

    pygame.display.flip()

    clock.tick(FPS)
terminate()
