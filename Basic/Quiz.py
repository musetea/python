import pygame
from os import path
from random import randint
from pygame import display, image, font, time
from pygame.constants import KEYUP, KEYDOWN
from Charecter import Charecter

# 초기화작업
WINDOW_WIDTH = 480
WINDOW_HEIGHT = 640
SPEED = 0.5
FPS = 30
ENEMY_SPEED = 10
FONT_SIZE = 40
TITLE = "Basic Game"
WHITE = (255, 255, 255)   # 하얀색

pygame.init()
font.init()
screen = display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
display.set_caption(TITLE)
clock = time.Clock()  # FPS

current_dir = path.dirname(path.realpath(__file__))
# print(current_dir)
background = image.load(path.join(current_dir, "images/background.png"))
character = Charecter(path.join(current_dir, "images/character.png"))
enemy = Charecter(path.join(current_dir, "images/enemy.png"))
enemy.position(randint(0, WINDOW_WIDTH-enemy.width), 0)

running = True
while running:
    delta = clock.tick(30)
    # 이벤트 루프(체크)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break
        if event.type == KEYDOWN:
            character.keyDown(event.key)
            pass
        if event.type == KEYUP:
            character.keyUp(event.key)
            pass

    # 배경넣기
    screen.blit(background, (0, 0))

    enemy.y_pos += ENEMY_SPEED
    if enemy.y_pos > WINDOW_HEIGHT:
        enemy.y_pos = 0
        enemy.x_pos = randint(0, WINDOW_WIDTH-enemy.width)

    # 충돌확인
    character_rect = character.getRect()
    enemy_rect = enemy.getRect()
    if character_rect.colliderect(enemy_rect):
        print("충돌!!!")
        running = False
        time.delay(2000)

    # 기본 캐릭터 넣기
    character.drawCharacter(screen, delta)
    enemy.drawCharacter(screen, delta)
    #

    # 화면업데이트
    display.update()


pygame.quit()
