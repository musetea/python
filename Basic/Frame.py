import os
import pygame
from pygame import display, image, font, time
from pygame.constants import K_UP

# 초기화작업
WINDOW_WIDTH = 480
WINDOW_HEIGHT = 640
SPEED = 0.5
FPS = 30
FONT_SIZE = 40
TITLE = "Basic Game"
WHITE = (255, 255, 255)   # 하얀색


pygame.init()
font.init()
screen = display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
display.set_caption(TITLE)
clock = pygame.time.Clock()  # FPS

#
move_x = 0
move_y = 0
gameFont = font.Font(None, FONT_SIZE)
time_total_sec = 10  # 10초동안게임
time_tick = time.get_ticks()    # 현재시간정보취득


class Charecter:
    # 좌표
    to_x = 0
    to_y = 0
    speed = 10

    def __init__(self, imgPath):
        self.character = image.load(imgPath)
        self.size = self.character.get_rect().size
        self.width = self.size[0]
        self.height = self.size[1]
        self.x_pos = (WINDOW_WIDTH // 2) - (self.width // 2)
        self.y_pos = WINDOW_HEIGHT - self.height

    def position(self, x, y):
        self.x_pos = x - (self.width // 2)
        self.y_pos = y - self.height

    def drawCharacter(self, screen, delta):

        self.x_pos += (self.to_x * delta)
        self.y_pos += (self.to_y * delta)
        # 가로경계설정
        if self.x_pos < 0:
            self.x_pos = 0
        elif self.x_pos > (WINDOW_WIDTH - self.width):
            self.x_pos = WINDOW_WIDTH - self.width
        # 세로경계설정
        if self.y_pos < 0:
            self.y_pos = 0
        elif self.y_pos > (WINDOW_HEIGHT-self.height):
            self.y_pos = WINDOW_HEIGHT-self.height

        screen.blit(self.character, (self.x_pos, self.y_pos))

    def keyDown(self, key):
        # print(self.to_x, self.to_y)
        if key == pygame.K_LEFT:
            self.to_x -= SPEED
        elif key == pygame.K_RIGHT:
            self.to_x += SPEED
        elif key == pygame.K_UP:
            self.to_y -= SPEED
        elif key == pygame.K_DOWN:
            self.to_y += SPEED

    def keyUp(self, key):
        if key == pygame.K_LEFT or key == pygame.K_RIGHT:
            self.to_x = 0
        elif key == pygame.K_UP or key == pygame.K_DOWN:
            self.to_y = 0

    def getRect(self):
        rect = self.character.get_rect()
        rect.left = self.x_pos
        rect.top = self.y_pos
        return rect


# gui
current_dir = os.path.dirname(os.path.realpath(__file__))
# print(current_dir)
background = image.load(os.path.join(current_dir, "images/background.png"))
character = Charecter(os.path.join(current_dir, "images/character.png"))
enemy = Charecter(os.path.join(current_dir, "images/enemy.png"))
enemy.position(WINDOW_WIDTH/2, (WINDOW_HEIGHT/2))

# character = image.load(os.path.join(current_dir, "images/character.png"))
# character_size = character.get_rect().size
# character_x_pos = (WINDOW_WIDTH//2) - (character_size[0]//2)
# character_y_pos = WINDOW_HEIGHT-character_size[1]


running = True
while running:
    delta = clock.tick(FPS)
    # 이벤트 루프(체크)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break
        if event.type == pygame.KEYDOWN:
            character.keyDown(event.key)
            # if event.key == pygame.K_LEFT:
            #     move_x -= MOVE
            # elif event.key == pygame.K_RIGHT:
            #     move_x += MOVE
            # elif event.key == pygame.K_UP:
            #     move_y -= MOVE
            # elif event.key == pygame.K_DOWN:
            #     move_y += MOVE

        if event.type == pygame.KEYUP:
            character.keyUp(event.key)

    # 화면업데이트
    screen.blit(background, (0, 0))
    # character_x_pos += move_x
    # character_y_pos += move_y
    # if character_x_pos < 0:
    #     character_x_pos = 0
    # elif character_x_pos > WINDOW_WIDTH - character_size[0]:
    #     character_x_pos = WINDOW_WIDTH - character_size[0]

    # screen.blit(character, (character_x_pos, character_y_pos))

    character_rect = character.getRect()
    enemy_rect = enemy.getRect()

    if character_rect.colliderect(enemy_rect):
        print("충돌!!!")
        running = False
        time.delay(2000)

    character.drawCharacter(screen, delta)
    enemy.drawCharacter(screen, delta)

    # 시간정보
    elapsed_time = (time.get_ticks() - time_tick) / 1000
    timer = gameFont.render(
        str(int((time_total_sec - elapsed_time))), True, WHITE)
    screen.blit(timer, (10, 10))

    if time_total_sec - elapsed_time <= 0:
        print("타임아웃")
        time.delay(2000)
        running = False

    # 화면업데이트
    display.update()

# 프로그램 종료
pygame.quit()
