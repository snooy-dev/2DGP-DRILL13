from pico2d import get_canvas_height, get_canvas_width, load_image
from sdl2 import SDL_KEYDOWN, SDLK_i

is_open = False
image = None


def init():
    global is_open, image
    is_open = False
    image = load_image('item_select.png')


def finish():
    global is_open, image
    is_open = False
    image = None


def handle_event(event, boy):
    global is_open
    if event.type == SDL_KEYDOWN and event.key == SDLK_i:
        if not getattr(event, 'repeat', False):
            is_open = not is_open
        return True
    return False


def draw(boy):
    if is_open:
        image.draw(get_canvas_width() - image.w / 2 - 20,
                   get_canvas_height() - image.h / 2 - 20)
