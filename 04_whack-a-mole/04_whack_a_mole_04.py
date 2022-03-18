import pygame as pg
import random

pg.init()
screen = pg.display.set_mode((800, 600))

background_img = pg.image.load("whack_a_mole.png")
mole_img = pg.image.load("mole.png")
mole_img = pg.transform.scale(mole_img, (150, 100))

font = pg.font.SysFont("nanumbarungothic", 30)

# 구멍 좌표 리스트
mole_pos = [(50,120), (300,120), (550,120), (50,255), (300,255), (550,255), (50,390), (300,390), (550,390)]

running = True
check_time = True
# 게임 점수
score = 0
# 두더지 리스트
moles = []

while running:

    screen.blit(background_img, background_img.get_rect())

    time_text = font.render(str(pg.time.get_ticks() // 1000), True, (0, 0, 0), None)
    score_text = font.render(str(score), True, (0, 0, 0), None)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

        if event.type == pg.MOUSEBUTTONDOWN:
            # 두더지가 클릭되었을 때 점수를 증가시키고, 잡은 두더지를 리스트에서 삭제하는 코드를 작성하기.
            for mole in moles:
                if mole.collidepoint(event.pos):
                    score += 1
                    moles.remove(mole)
                    break

    if (pg.time.get_ticks() // 1000) % 2 == 0:
        if check_time:
            # 2초마다 랜덤으로 두더지를 생성해 두더지 리스트(moles)에 담아주는 코드를 작성하기.
            add_mole = screen.blit(mole_img, random.choice(mole_pos))
            moles.append(add_mole)

            check_time = False
    else:
        check_time = True

    # 두더지 리스트를 돌면서 각 두더지를 화면에 그려주는 코드를 작성하기.
    for mole in moles:
        screen.blit(mole_img, mole)

    screen.blit(time_text, (680, 55))
    screen.blit(score_text, (55, 55))

    pg.display.update()

pg.quit()