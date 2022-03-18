import pygame as pg

pg.init()
screen = pg.display.set_mode((600, 600))

# 배경화면 이미지를 가져오기
background_img = pg.image.load("../background.JPG")
background_img = pg.transform.scale(background_img, (600, 600))

running = True

while running:
    # 배경화면 이미지를 추가하기
    screen.blit(background_img, background_img.get_rect())

    pg.display.update()