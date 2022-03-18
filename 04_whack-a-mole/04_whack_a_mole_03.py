import pygame as pg
import random

pg.init()
screen = pg.display.set_mode((800, 600))

background_img = pg.image.load("whack_a_mole.png")
mole_img = pg.image.load("mole.png")
mole_img = pg.transform.scale(mole_img, (150, 100))

font = pg.font.SysFont("nanumbarungothic", 30)

running = True
score = 0
# 구멍 좌표 리스트
mole_pos = [(50,120), (300,120), (550,120), (50,255), (300,255), (550,255), (50,390), (300,390), (550,390)]

# check_time 변수에 어떤 값이 들어가야 일정한 시간을 측정할 수 있을지 코드를 작성하기. (boolean 타입)
check_time = True

while running:

    screen.blit(background_img, background_img.get_rect())

    time_text = font.render(str(pg.time.get_ticks() // 1000), True, (0, 0, 0), None)
    score_text = font.render(str(score), True, (0, 0, 0), None)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    # 2초 간격을 체크하기.
    if (pg.time.get_ticks() // 1000) % 2 == 0:
        # check_time 변수를 활용해 2초마다 두더지가 등장하도록 코드를 작성하기.
        if check_time == True:
            check_time = False
            screen.blit(mole_img, random.choice(mole_pos))
            pg.display.update()
            pg.time.wait(500)
    # check_time 변수를 초기화하는 코드를 작성하기.
    else:
        check_time = True

    screen.blit(time_text, (680, 55))
    screen.blit(score_text, (55, 55))

    pg.display.update()

pg.quit()
