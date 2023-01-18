import pygame



class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, player_group, all_sprites, tile_width, tile_height):
        super().__init__(player_group, all_sprites)
        self.speed = 50
        self.forward = AnimatedSprite(pygame.image.load("iamges/walk_forward.jpg"), 1, 5).frames
        self.back = AnimatedSprite(pygame.image.load("iamges/walk_back.jpg"), 1, 5).frames
        self.right = AnimatedSprite(pygame.image.load("iamges/walk_right.jpg"), 1, 5).frames
        self.left = AnimatedSprite(pygame.image.load("iamges/walk_left.jpg"), 1, 5).frames
        self.le = 0
        self.ri = 0
        self.fo = 0
        self.ba = 0
        self.score = 0
        self.image = self.start_picture(self.score)
        self.rect = self.image.get_rect().move(
            tile_width * pos_x + 15, tile_height * pos_y + 5)

    def start_picture(self, sc):
        if sc == 0:
            return self.forward[0]
        elif sc == 1:
            return self.back[0]
        elif sc == 2:
            return self.left[0]
        elif sc == 3:
            return self.right[0]

    def update(self):
        self.image = self.start_picture(self.score)
        if pygame.key.get_pressed()[pygame.K_a]:  # left moving
            self.score = 2
            self.rect.x -= self.speed
            self.le += 1
            if self.le != 5:
                self.image = self.left[self.le]
            else:
                self.le = 0
                self.image = self.left[self.le]
        elif pygame.key.get_pressed()[pygame.K_d]:  # right moving
            self.score = 3
            self.rect.x += self.speed
            self.ri += 1
            if self.ri != 5:
                self.image = self.right[self.ri]
            else:
                self.ri = 0
                self.image = self.right[self.ri]
        elif pygame.key.get_pressed()[pygame.K_w]:  # forward moving
            self.score = 0
            self.rect.y -= self.speed
            self.fo += 1
            if self.fo != 5:
                self.image = self.forward[self.fo]
            else:
                self.fo = 0
                self.image = self.forward[self.fo]
        elif pygame.key.get_pressed()[pygame.K_s]:  # back moving
            self.score = 1
            self.rect.y += self.speed
            self.ba += 1
            if self.ba != 5:
                self.image = self.back[self.ba]
            else:
                self.ba = 0
                self.image = self.back[self.ba]
        return self.image


class AnimatedSprite(pygame.sprite.Sprite):     # cutting sprites
    def __init__(self, sheet, columns, rows):
        self.frames = []
        self.cut_sheet(sheet, columns, rows)
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]

    def cut_sheet(self, sheet, columns, rows):
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns,
                                sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pygame.Rect(
                    frame_location, self.rect.size)))   #
