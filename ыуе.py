import pygame

pygame.init()
pygame.display.init()
size = w, h = pygame.display.Info().current_w, pygame.display.Info().current_h
screen = pygame.display.set_mode()


def draw(screen):
    screen.fill((22, 22, 22))
    font = pygame.font.Font(None, 50)
    text = font.render("Движение вверх:", True, (100, 255, 100))
    text_x = w // 3 - text.get_width() // 2
    text_y = h // 8 - text.get_height() // 2
    text_w = text.get_width()
    text_h = text.get_height()
    screen.blit(text, (text_x, text_y))
    pygame.draw.rect(screen, (0, 255, 0), (text_x - 10, text_y - 10,
                                           text_w + 20, text_h + 20), 1)

    text1 = font.render("Движение вниз:", True, (100, 255, 100))
    text_x1 = w // 3 - text.get_width() // 2
    text_y1 = h // 8 * 2 - text.get_height() // 2
    text_w1 = text.get_width()
    text_h1 = text.get_height()
    screen.blit(text1, (text_x1, text_y1))
    pygame.draw.rect(screen, (0, 255, 0), (text_x1 - 10, text_y1 - 10,
                                           text_w1 + 20, text_h1 + 20), 1)

    text2 = font.render("Движение вправо:", True, (100, 255, 100))
    text_x2 = w // 3 - text.get_width() // 2
    text_y2 = h // 8 * 3 - text.get_height() // 2
    text_w2 = text.get_width()
    text_h2 = text.get_height()
    screen.blit(text2, (text_x2, text_y2))
    pygame.draw.rect(screen, (0, 255, 0), (text_x2 - 10, text_y2 - 10,
                                           text_w2 + 40, text_h2 + 20), 1)

    text3 = font.render("Движение влево:", True, (100, 255, 100))
    text_x3 = w // 3 - text.get_width() // 2
    text_y3 = h // 8 * 4 - text.get_height() // 2
    text_w3 = text.get_width()
    text_h3 = text.get_height()
    screen.blit(text3, (text_x3, text_y3))
    pygame.draw.rect(screen, (0, 255, 0), (text_x3 - 10, text_y3 - 10,
                                           text_w3 + 20, text_h3 + 20), 1)

    text4 = font.render("Сохранение:", True, (100, 255, 100))
    text_x4 = w // 3 - text.get_width() // 2
    text_y4 = h // 8 * 5 - text.get_height() // 2
    text_w4 = text.get_width()
    text_h4 = text.get_height()
    screen.blit(text4, (text_x4, text_y4))
    pygame.draw.rect(screen, (0, 255, 0), (text_x4 - 10, text_y4 - 10,
                                           text_w4 + 20, text_h4 + 20), 1)

    text5 = font.render("Сбор рессурсов:", True, (100, 255, 100))
    text_x5 = w // 3 - text.get_width() // 2
    text_y5 = h // 8 * 6 - text.get_height() // 2
    text_w5 = text.get_width()
    text_h5 = text.get_height()
    screen.blit(text5, (text_x5, text_y5))
    pygame.draw.rect(screen, (0, 255, 0), (text_x5 - 10, text_y5 - 10,
                                           text_w5 + 20, text_h5 + 20), 1)

    text6 = font.render("Выход в меню:", True, (100, 255, 100))
    text_x6 = w // 3 - text.get_width() // 2
    text_y6 = h // 8 * 7 - text.get_height() // 2
    text_w6 = text.get_width()
    text_h6 = text.get_height()
    screen.blit(text6, (text_x6, text_y6))
    pygame.draw.rect(screen, (0, 255, 0), (text_x6 - 10, text_y6 - 10,
                                           text_w6 + 20, text_h6 + 20), 1)


def draw1(screen):
    font = pygame.font.Font(None, 50)
    text = font.render("Meню", True, (100, 255, 100))
    text_x = 30
    text_y = 30
    text_w = text.get_width()
    text_h = text.get_height()
    screen.blit(text, (text_x, text_y))
    pygame.draw.rect(screen, (0, 255, 0), (text_x - 10, text_y - 10,
                                           text_w + 20, text_h + 20), 1)

    text1 = font.render("Управление:", True, (100, 255, 100))
    text_x1 = w // 9 - text.get_width() // 2
    text_y1 = h // 8 - text.get_height() // 2
    text_w1 = text.get_width()
    text_h1 = text.get_height()
    screen.blit(text1, (text_x1, text_y1))
    pygame.draw.rect(screen, (0, 255, 0), (text_x1 - 10, text_y1 - 10,
                                           text_w1 + 130, text_h1 + 20), 1)


font = pygame.font.Font(None, 32)
clock = pygame.time.Clock()
input_box = pygame.Rect(w // 3 * 1.5, h // 8 - 30, 500, 58)
input_box1 = pygame.Rect(w // 3 * 1.5, h // 8 * 2 - 30, 500, 58)
input_box2 = pygame.Rect(w // 3 * 1.5, h // 8 * 3 - 30, 500, 58)
input_box3 = pygame.Rect(w // 3 * 1.5, h // 8 * 4 - 30, 500, 58)
input_box4 = pygame.Rect(w // 3 * 1.5, h // 8 * 5 - 30, 500, 58)
input_box5 = pygame.Rect(w // 3 * 1.5, h // 8 * 6 - 30, 500, 58)
input_box6 = pygame.Rect(w // 3 * 1.5, h // 8 * 7 - 30, 500, 58)

color_inactive = pygame.Color('lightskyblue3')
color_active = pygame.Color('dodgerblue2')
color = color_inactive
color1, color2, color3, color4, color5, color6 = color_inactive, color_inactive, color_inactive, \
                                                 color_inactive, color_inactive, color_inactive
active, active1, active2, active3, active4, active5, active6 = False, False, False, False, False, False, False
text, text1, text2, text3, text4, text5, text6 = ' ' * 14 + 'w', ' ' * 14 + 's', ' ' * 14 + 'd', \
                                                 ' ' * 14 + 'a', ' ' * 14 + 'q', ' ' * 14 + 'f', ' ' * 14 + 'r'

setp = False
start = True
running = True
pos = None

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # program closure
            running = False
        if event.type == pygame.MOUSEMOTION:  # getting mouse position
            pos = event.pos

        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_box.collidepoint(event.pos):
                active = not active

            elif input_box1.collidepoint(event.pos) and not active1:
                active1 = True
                active, active2, active3, active4, active5, active6 = False, False, False, False, False, False
            elif input_box2.collidepoint(event.pos) and not active2:
                active2 = True
                active1, active, active3, active4, active5, active6 = False, False, False, False, False, False
            elif input_box3.collidepoint(event.pos) and not active3:
                active3 = True
            elif input_box4.collidepoint(event.pos) and not active4:
                active4 = True
            elif input_box4.collidepoint(event.pos) and not active4:
                active4 = True
            elif input_box5.collidepoint(event.pos) and not active5:
                active5 = True
            elif input_box6.collidepoint(event.pos) and not active6:
                active6 = True
            elif input_box1.collidepoint(event.pos) and active1:
                active1 = False
            elif input_box2.collidepoint(event.pos) and active2:
                active2 = False
            elif input_box3.collidepoint(event.pos) and active3:
                active3 = False
            elif input_box4.collidepoint(event.pos) and active4:
                active4 = False
            elif input_box4.collidepoint(event.pos) and active4:
                active4 = False
            elif input_box5.collidepoint(event.pos) and active5:
                active5 = False
            elif input_box6.collidepoint(event.pos) and active6:
                active6 = False
            else:
                active = False
            color = color_active if active else color_inactive
            color1 = color_active if active1 else color_inactive
            color2 = color_active if active2 else color_inactive
            color3 = color_active if active3 else color_inactive
            color4 = color_active if active4 else color_inactive
            color5 = color_active if active5 else color_inactive
            color6 = color_active if active6 else color_inactive

        if event.type == pygame.KEYDOWN:
            if active:
                if event.key == pygame.K_RETURN:
                    print(text)
                    text = ''
                elif event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                else:
                    text += event.unicode
            if active1:
                if event.key == pygame.K_RETURN:
                    print(text1)
                    text1 = ''
                elif event.key == pygame.K_BACKSPACE:
                    text1 = text1[:-1]
                else:
                    text1 += event.unicode
            if active2:
                if event.key == pygame.K_RETURN:
                    print(text1)
                    text2 = ''
                elif event.key == pygame.K_BACKSPACE:
                    text2 = text2[:-1]
                else:
                    text2 += event.unicode
            if active3:
                if event.key == pygame.K_RETURN:
                    print(text3)
                    text3 = ''
                elif event.key == pygame.K_BACKSPACE:
                    text3 = text3[:-1]
                else:
                    text3 += event.unicode
            if active4:
                if event.key == pygame.K_RETURN:
                    print(text4)
                    text4 = ''
                elif event.key == pygame.K_BACKSPACE:
                    text4 = text4[:-1]
                else:
                    text4 += event.unicode
            if active5:
                if event.key == pygame.K_RETURN:
                    print(text5)
                    text5 = ''
                elif event.key == pygame.K_BACKSPACE:
                    text5 = text5[:-1]
                else:
                    text5 += event.unicode
            if active6:
                if event.key == pygame.K_RETURN:
                    print(text6)
                    text6 = ''
                elif event.key == pygame.K_BACKSPACE:
                    text6 = text6[:-1]
                else:
                    text6 += event.unicode

    screen.fill((30, 30, 30))
    draw(screen)
    draw1(screen)
    txt_surface = font.render(text, True, color)
    txt_surface1 = font.render(text1, True, color)
    txt_surface2 = font.render(text2, True, color)
    txt_surface3 = font.render(text3, True, color)
    txt_surface4 = font.render(text4, True, color)
    txt_surface5 = font.render(text5, True, color)
    txt_surface6 = font.render(text6, True, color)
    # Resize the box if the text is too long.
    width = max(200, txt_surface.get_width() + 10)
    width1 = max(200, txt_surface1.get_width() + 10)
    width2 = max(200, txt_surface2.get_width() + 10)
    width3 = max(200, txt_surface3.get_width() + 10)
    width4 = max(200, txt_surface4.get_width() + 10)
    width5 = max(200, txt_surface5.get_width() + 10)
    width6 = max(200, txt_surface6.get_width() + 10)
    input_box.w = width
    input_box1.w = width1
    input_box2.w = width2
    input_box3.w = width3
    input_box4.w = width4
    input_box5.w = width5
    input_box6.w = width6

    screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
    pygame.draw.rect(screen, color, input_box, 2)

    screen.blit(txt_surface1, (input_box1.x + 5, input_box1.y + 5))
    pygame.draw.rect(screen, color1, input_box1, 2)

    screen.blit(txt_surface2, (input_box2.x + 5, input_box2.y + 5))
    pygame.draw.rect(screen, color2, input_box2, 2)

    screen.blit(txt_surface3, (input_box3.x + 5, input_box3.y + 5))
    pygame.draw.rect(screen, color3, input_box3, 2)

    screen.blit(txt_surface4, (input_box4.x + 5, input_box4.y + 5))
    pygame.draw.rect(screen, color4, input_box4, 2)

    screen.blit(txt_surface5, (input_box5.x + 5, input_box5.y + 5))
    pygame.draw.rect(screen, color5, input_box5, 2)

    screen.blit(txt_surface6, (input_box6.x + 5, input_box6.y + 5))
    pygame.draw.rect(screen, color6, input_box6, 2)
    pygame.display.flip()
    clock.tick(30)
pygame.quit()
