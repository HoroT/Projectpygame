import pygame as pg

pg.init()
size = w, h = 800, 800
screen = pg.display.set_mode(size)


def main():
    font = pg.font.Font(None, 32)
    input_box = pg.Rect(w // 3 * 2, h // 8, 140, 32)
    input_box1 = pg.Rect(w // 3 * 2, h // 8 * 2, 140, 32)
    input_box2 = pg.Rect(w // 3 * 2, h // 8 * 3, 140, 32)
    input_box3 = pg.Rect(w // 3 * 2, h // 8 * 4, 140, 32)
    input_box4 = pg.Rect(w // 3 * 2, h // 8 * 5, 140, 32)
    input_box5 = pg.Rect(w // 3 * 2, h // 8 * 6, 140, 32)
    input_box6 = pg.Rect(w // 3 * 2, h // 8 * 7, 140, 32)

    color_inactive = pg.Color('lightskyblue3')
    color_active = pg.Color('dodgerblue2')
    color = color_inactive
    active = False
    text = ''
    done = False

    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
            if event.type == pg.MOUSEBUTTONDOWN:
                # If the user clicked on the input_box rect.
                if input_box.collidepoint(event.pos):
                    # Toggle the active variable.
                    active = not active
                else:
                    active = False
                # Change the current color of the input box.
                color = color_active if active else color_inactive
            if event.type == pg.KEYDOWN:
                if active:
                    if event.key == pg.K_RETURN:
                        print(text)
                        text = ''
                    elif event.key == pg.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

        screen.fill((30, 30, 30))
        # Render the current text.
        txt_surface = font.render(text, True, color)
        # Resize the box if the text is too long.
        width = max(200, txt_surface.get_width() + 10)
        input_box.w = width
        input_box1.w = width
        input_box2.w = width
        input_box3.w = width
        input_box4.w = width
        input_box5.w = width
        input_box6.w = width

        screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
        pg.draw.rect(screen, color, input_box, 2)

        screen.blit(txt_surface, (input_box1.x + 5, input_box1.y + 5))
        pg.draw.rect(screen, color, input_box1, 2)

        screen.blit(txt_surface, (input_box2.x + 5, input_box2.y + 5))
        pg.draw.rect(screen, color, input_box2, 2)

        screen.blit(txt_surface, (input_box3.x + 5, input_box3.y + 5))
        pg.draw.rect(screen, color, input_box3, 2)

        screen.blit(txt_surface, (input_box4.x + 5, input_box4.y + 5))
        pg.draw.rect(screen, color, input_box4, 2)

        screen.blit(txt_surface, (input_box5.x + 5, input_box5.y + 5))
        pg.draw.rect(screen, color, input_box5, 2)

        screen.blit(txt_surface, (input_box6.x + 5, input_box6.y + 5))
        pg.draw.rect(screen, color, input_box6, 2)

        pg.display.flip()
        clock.tick(30)


if __name__ == '__main__':
    clock = pg.time.Clock()
    main()
    pg.quit()
