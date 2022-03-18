import pygame as pg

pg.init()
screen = pg.display.set_mode((600, 600))

background_img = pg.image.load("../background.JPG")
background_img = pg.transform.scale(background_img, (600, 600))

# 캐릭터의 이미지 추가하기.
character = pg.image.load("character.png")

# 가져온 캐릭터의 이미지의 사이즈 축소하기. 구체적으로 가로 100, 세로 100으로 변경하기.
character = pg.transform.scale(character, (100, 100))

running = True

while running:
    screen.blit(background_img, background_img.get_rect())
    # 캐릭터의 이미지를 추가하기
    screen.blit(character, character.get_rect())

    pg.display.update()