import pygame as pg

pg.init()
screen = pg.display.set_mode((600, 600))

background_img = pg.image.load("../background.JPG")
background_img = pg.transform.scale(background_img, (600, 600))
character = pg.image.load("character.png")
character = pg.transform.scale(character, (100, 100))

running = True

# character_pos 변수에 캐릭터의 위치 값(x,y) 좌표를 저장할 수 있도록 코드를 작성하기
character_pos = character.get_rect()

while running:

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        # 만약 감지한 이벤트가 키보드가 눌린 이벤트인지 확인하기
        elif event.type == pg.KEYDOWN:
            # 이벤트가 키보드 왼쪽 방향키(<) 인지 판단하는 코드를 작성하기
            if event.key == pg.K_LEFT:
                # 캐릭터의 x 좌표를 -10 만큼 변경하기
                character_pos.x -= 10
                # "왼쪽으로 10만큼 이동" 을 출력하기
                print("왼쪽으로 10만큼 이동")
            # 이벤트가 키보드 오른쪽 방향키(>)인지 판단하는 코드를 작성하기
            if event.key == pg.K_RIGHT:
                # 캐릭터의 x 좌표를 +10 만큼 변경하기
                character_pos.x += 10
                # "오른쪽으로 10만큼 이동" 을 출력하기
                print("오른쪽으로 10만큼 이동")

    screen.blit(background_img, background_img.get_rect())
    screen.blit(character, character_pos)

    pg.display.update()

pg.quit()