from pico2d import *

open_canvas(1280, 1024)
ground = load_image('TUK_GROUND.png')
character = load_image('earthgirl.png')

def handle_events():
    global running

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False

running = True
x = 1280 // 2
y = 1024 // 2
frame = 0

while running:
    clear_canvas()
    ground.draw(1280 // 2, 1024 // 2)
    update_canvas()
    handle_events()

close_canvas()
