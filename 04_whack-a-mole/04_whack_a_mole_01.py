import pygame as pg

pg.init()
screen = pg.display.set_mode((800, 600))

background_img = pg.image.load("whack_a_mole.png")
font = pg.font.SysFont("nanumbarungothic", 30)

# 게임 점수 저장
score = 0

running = True

while running:

    # 시간 및 점수를 문자열 객체로 변환해 변수에 넣기.
    time_text = font.render(str(pg.time.get_ticks() // 1000), True, (0, 0, 0), None)
    score_text = font.render(str(score), True, (0, 0, 0), None)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        # 화면 내에 마우스가 클릭되면 점수를 1씩 증가하는 코드를 작성하기.
        if event.type == pg.MOUSEBUTTONDOWN:
            score += 1

    screen.blit(background_img, background_img.get_rect())
    # 시간과 점수를 화면에 표시하는 코드를 작성하기.
    screen.blit(time_text, (680, 55))
    screen.blit(score_text, (55, 55))

    pg.display.update()

pg.quit()