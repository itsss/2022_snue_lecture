import pygame as pg

pg.init()
screen = pg.display.set_mode((600, 600))

background_img = pg.image.load("../background.JPG")
background_img = pg.transform.scale(background_img, (600, 600))
character = pg.image.load("character.png")
character = pg.transform.scale(character, (100, 100))

running = True

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            # 종료 버튼을 누르면 무한 반복문을 빠져나오는 코드 작성하기

            running = False

    screen.blit(background_img, background_img.get_rect())
    screen.blit(character, character.get_rect())

    pg.display.update()

# (2) 무한 반복문을 빠져나오면 파이게임을 종료하는 코드를 작성하세요.
pg.quit()

# (3) 정상적으로 종료되었다는 것을 알 수 있게 "정상 종료됨" 이라는 문자열을 출력하세요.
print("정상 종료됨")