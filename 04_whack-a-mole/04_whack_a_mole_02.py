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

while running:

    screen.blit(background_img, background_img.get_rect())

    time_text = font.render(str(pg.time.get_ticks() // 1000), True, (0, 0, 0), None)
    score_text = font.render(str(score), True, (0, 0, 0), None)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.MOUSEBUTTONDOWN:  # 만약 마우스 버튼을 클릭 이벤트가 감지되었다면?
            # 랜덤한 위치에 두더지가 생성되도록 코드를 작성하기.
            screen.blit(mole_img, random.choice(mole_pos))

            # 두더지가 일정한 시간동안(2초 동안) 보일 수 있도록 게임을 잠깐 멈춰 주기.
            pg.display.update()
            pg.time.wait(2000)

    screen.blit(time_text, (680, 55))
    screen.blit(score_text, (55, 55))

    pg.display.update()

pg.quit()