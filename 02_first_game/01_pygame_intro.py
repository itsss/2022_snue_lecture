import pygame as pg
# pygame 라이브러리를 추가합니다. as라는 예약어로 이름을 바꿔서도 사용할 수 있습니다.

# pygame 초기화하는 코드 작성
pg.init()

screen = pg.display.set_mode((600, 600))

# 게임 제목을 "나만의 첫 게임"으로 변경
pg.display.set_caption("나만의 첫 게임")

# pygame이 실행될 수 있도록 running 변수에 적절한 값을 넣기
# 이곳에 들어가야 하는 값은 True / False 중 하나입니다.
# True / False는 부울(Bool) 이라는 이름으로도 불립니다!
running = True

while running:
    pg.display.update()