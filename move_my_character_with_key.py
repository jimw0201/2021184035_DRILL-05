from pico2d import *

open_canvas(1280, 1024)
ground = load_image('TUK_GROUND.png')
character = load_image('earthgirl.png')

def handle_events():
    global running, x, y, dir_x, dir_y

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir_x += 1
            elif event.key == SDLK_LEFT:
                dir_x -= 1
            elif event.key == SDLK_UP:
                dir_y += 1
            elif event.key == SDLK_DOWN:
                dir_y -= 1
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir_x -= 1
            elif event.key == SDLK_LEFT:
                dir_x += 1
            elif event.key == SDLK_UP:
                dir_y -= 1
            elif event.key == SDLK_DOWN:
                dir_y += 1

running = True
x = 1280 // 2
y = 1024 // 2
frame = 0           # 걷는 모션 프레임
dir_frame = 200     # 걷는 방향 프레임
flip = False        # 좌우 반전
dir_x = 0
dir_y = 0

# 캐릭터의 크기
character_width = 200
character_height = 200

while running:
    clear_canvas()
    ground.draw(640, 512)

    if dir_y > 0:  # 윗쪽 이동 (셋째줄 이미지)
        dir_frame = 0
        flip = False
    elif dir_y < 0:  # 아랫쪽 이동 (첫째줄 이미지)
        dir_frame = 400
        flip = False
    elif dir_x > 0:  # 오른쪽 이동 (둘째줄 이미지)
        dir_frame = 200
        flip = True  # 좌우 반전 True
    elif dir_x < 0:  # 왼쪽 이동 (둘째줄 이미지)
        dir_frame = 200
        flip = False

    # 좌우 반전 여부에 따라 이미지 그리기
    if flip:
        character.clip_composite_draw(frame * 200, dir_frame, 200, 200, 0, 'h', x, y, character_width, character_height)
    else:
        character.clip_draw(frame * 200, dir_frame, character_width, character_height, x, y)

    update_canvas()
    handle_events()

    # 화면 경계 체크
    if x + dir_x * 5 > 1280 - (character_width // 2) + 100:  # 오른쪽 끝에 도달했을 때
        x = 1280 - (character_width // 2) + 100
    elif x + dir_x * 5 < (character_width // 2) - 100:  # 왼쪽 끝에 도달했을 때
        x = (character_width // 2) - 100
    else:
        x += dir_x * 5

    if y + dir_y * 5 > 1024 - (character_height // 2) + 100:  # 윗쪽 끝에 도달했을 때
        y = 1024 - (character_height // 2) + 100
    elif y + dir_y * 5 < (character_height // 2) - 100:  # 아랫쪽 끝에 도달했을 때
        y = (character_height // 2) - 100
    else:
        y += dir_y * 5

    frame = (frame + 1) % 8
    delay(0.05)

close_canvas()
