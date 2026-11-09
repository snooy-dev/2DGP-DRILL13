from pico2d import (draw_rectangle, get_canvas_height, get_canvas_width,
                    load_font, load_image)
from sdl2 import SDL_KEYDOWN, SDLK_0, SDLK_1, SDLK_2, SDLK_i
from sdl2.sdlttf import TTF_CloseFont

is_open = False
image = None
font = None


def init():
    global is_open, image, font
    is_open = False
    image = load_image('item_select.png')
    font = load_font('C:/Windows/Fonts/arial.ttf', 16)


def finish():
    global is_open, image, font
    if font is not None:
        # pico2d.Font에는 SDL 글꼴 자원을 해제하는 소멸자가 없다.
        TTF_CloseFont(font.font)
    is_open = False
    image = None
    font = None


def handle_event(event, boy):
    global is_open
    if event.type == SDL_KEYDOWN and event.key == SDLK_i:
        if not getattr(event, 'repeat', False):
            is_open = not is_open
        return True
    if (is_open and event.type == SDL_KEYDOWN and
            event.key in (SDLK_0, SDLK_1, SDLK_2)):
        boy.select_ball(event.key - SDLK_0)
        return True
    return False


def draw(boy):
    if not is_open:
        return
    left = get_canvas_width() - image.w - 20
    top = get_canvas_height() - 20
    image.draw(left + image.w / 2, top - image.h / 2)
    row_y = top - (42, 107, 175)[boy.ball_type]
    draw_rectangle(left + 6, row_y - 28, left + image.w - 6, row_y + 28,
                   40, 130, 40)
    bottom = top - image.h
    draw_rectangle(left, bottom - 50, left + image.w, bottom,
                   220, 220, 220, filled=True)
    label = ('None', 'Small', 'Large')[boy.ball_type]
    font.draw(left + 12, bottom - 16,
              f'Selected: {boy.ball_type} ({label})')
    font.draw(left + 12, bottom - 36, 'I: Close')
