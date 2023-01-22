from Man import Player

import sys

import pygame


def load_level(filename):
    filename = filename
    # читаем уровень, убирая символы перевода строки
    with open(filename, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]

    # и подсчитываем максимальную длину
    max_width = max(map(len, level_map))

    # дополняем каждую строку пустыми клетками ('w')
    return list(map(lambda x: x.ljust(max_width, 'w'), level_map))


class Tile(pygame.sprite.Sprite):  # determination of cells
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(tiles_group, all_sprites)
        self.image = tile_images[tile_type]
        self.rect = self.image.get_rect().move(
            tile_width * pos_x, tile_height * pos_y)


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
                new_player = Player(x, y, player_group, all_sprites, tile_width, tile_height)
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


if __name__ == '__main__':
    FPS = 60
    clock = pygame.time.Clock()

    pygame.display.init()

    pygame.key.set_repeat(200, 70)  # function for pressing the key

    size = WIDTH, HEIGHT = 500, 500
    screen = pygame.display.set_mode(size)

    tile_images = {
        'hor_wall': pygame.image.load('pictures_and_txt/walls/hor_wall.png'),
        'empty': pygame.image.load('pictures_and_txt/another_textures/ice_land.png'),
        'ver_wall': pygame.image.load('pictures_and_txt/walls/ver_wall.png'),
        'r1_wall': pygame.image.load('pictures_and_txt/walls/right_wall.png'),
        'l1_wall': pygame.image.load('pictures_and_txt/walls/left_wall.png'),
        'r2_wall': pygame.image.load('pictures_and_txt/walls/right_wall2.png'),
        'l2_wall': pygame.image.load('pictures_and_txt/walls/left_wall2.png'),
        't1_u': pygame.image.load('pictures_and_txt/forest/t1_u.png'),
        't2_u': pygame.image.load('pictures_and_txt/forest/t2_u.png'),
        't3_u': pygame.image.load('pictures_and_txt/forest/t3_u.png'),
        't1_d': pygame.image.load('pictures_and_txt/forest/t1_d.png'),
        't2_d': pygame.image.load('pictures_and_txt/forest/t2_d.png'),
        't3_d': pygame.image.load('pictures_and_txt/forest/t3_d.png'),
        'rd': pygame.image.load('pictures_and_txt/another_textures/road.png'),
        'wt': pygame.image.load('pictures_and_txt/another_textures/water.png'),
        'farm': pygame.image.load('pictures_and_txt/another_textures/farm.png')
    }

    tile_width = tile_height = 50

    all_sprites = pygame.sprite.Group()
    tiles_group = pygame.sprite.Group()
    player_group = pygame.sprite.Group()
    wall_group = pygame.sprite.Group()

    player, level_x, level_y = generate_level(load_level('map_cart1.txt'))

    camera = Camera()
    for sprite in all_sprites:
        camera.apply(sprite)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                player.update()

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
