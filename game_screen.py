import pygame

if __name__ == '__main__':
    pygame.display.init()
    img = pygame.image.load('картинки/interface.jpg')
    screen = pygame.display.set_mode(img.get_size(), pygame.FULLSCREEN)
    w, h = screen.get_size()
    img = pygame.transform.scale(img, (w, h))


class Curs:
    def __init__(self):
        self.Cursor = pygame.image.load('картинки/cursor.png')
        pygame.mouse.set_visible(False)
        self.Cursor = pygame.transform.scale(self.Cursor, (33, 42))

    def render(self, pos):
        screen.blit(self.Cursor, (pos[0], pos[1]))


if __name__ == '__main__':
    Cursor, pos = Curs(), None
    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(img, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # program closure
                running = False
            if event.type == pygame.MOUSEMOTION:  # getting mouse position
                pos = event.pos
            if event.type == pygame.MOUSEBUTTONUP:  # creating a menu button
                if (w // 27) < pos[0] < (w // 27) + (w // 5):
                    if (h // 171) < pos[1] < (h // 171) + (h // 26):
                        running = False

        if pygame.mouse.get_focused():
            Cursor.render(pos)

        pygame.display.flip()
    pygame.quit()
