import pygame as pg

pg.init()
screen = pg.display.set_mode((600, 600))

background_img = pg.image.load("../background.JPG")
background_img = pg.transform.scale(background_img, (600, 600))
character = pg.image.load("character.png")
character = pg.transform.scale(character, (100, 100))

running = True

while running:
    # event 변수명을 활용해서 이벤트를 받을 수 있는 코드 작성하기
    for event in pg.event.get():
        if event.type == pg.QUIT:
            # 파이게임의 오른쪽 상단에 있는 종료 버튼을 누르면 "EXIT!" 라는 문자열 출력하기
            print("EXIT!")

    screen.blit(background_img, background_img.get_rect())
    screen.blit(character, character.get_rect())

    pg.display.update()