import pygame
from pygame import Rect, display, font, time, event, draw
from pygame.constants import MOUSEBUTTONUP, QUIT
# from Controls import StartButton, GameGrid
from random import *

# 전역변수영역
running = True
hidden = False   # 히든처리
display_timer = None
time_tics = None

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
BLACK = (0, 0, 0)   # 검정색
WHITE = (255, 255, 255)   # 하얀색
DARK_GRAY = (192, 192, 192)  # 그레이
GRAY = (128, 128, 128)  # 그레이
FONT_SIZE = 120
CELL_SIZE = 130
BUTTON_SIZE = 110
MARGIN_TOP = 20
MARGIN_LEFT = 55
TIME_SEC = 5

COLUMNS = 9
ROWS = 5
LEVEL_SPLITER = 3
MAX_COUNT = 20


is_start = False    # 게임여부
current_level = 1
grid = []               # 맵영역
number_buttons = []     # 데이터리스트
TITLE = "Memory Game"


# =======================================================
pygame.init()
font.init()
gameFont = font.Font(None, FONT_SIZE)
screen = display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
display.set_caption(TITLE)


# =======================================================
# 클래스 정의
# =======================================================
class ReckButton:
    def __init__(self, width, height, center_x, center_y, number=None):
        self.button = Rect(0, 0, width, height)
        self.button.center = (center_x, center_y)
        self.number = number

    # 횐색으로 동그라미, 반지름(60), 두께(5)
    def draw_circle(self, screen, color, level=None):
        draw.circle(screen, color, self.button.center, 60, 5)

        if level != None:
            msg = gameFont.render(f"{level}", True, WHITE)
            msg_rect = msg.get_rect(center=self.button.center)
            screen.blit(msg, msg_rect)

    def draw_rect(self, screen, color, hidden):

        if hidden:
            draw.rect(screen, color, self.button)
        else:
            cell = gameFont.render(f"{self.number}", True, WHITE)
            cell_rect = cell.get_rect(center=self.button.center)
            screen.blit(cell, cell_rect)

    # 시작버튼 클릭여부 처리

    def check_click(self, pos):
        if self.button.collidepoint(pos):
            return True
        else:
            return False

# =======================================================


# GUI 작업
start_button = ReckButton(BUTTON_SIZE, BUTTON_SIZE,
                          BUTTON_SIZE, WINDOW_HEIGHT - BUTTON_SIZE)


# setup(current_level)
# 시작화면
def display_start_screen():
    start_button.draw_circle(screen, WHITE, current_level)


# 게임화면
def display_game_screen():
    global hidden

    if not hidden:
        elapsed_time = (time.get_ticks() - time_tics) / 1000
        if elapsed_time > display_timer:
            hidden = True

    for button in number_buttons:
        button.draw_rect(screen, WHITE, hidden)


# 마우스 클릭위치 찾기


def check_buttons(pos):
    global is_start, time_tics

    if is_start:
        check_number_buttons(pos)

    elif start_button.check_click(pos):
        is_start = True
        time_tics = time.get_ticks()    # 현재시간저장
    else:
        pass


def check_number_buttons(pos):
    global hidden, current_level, is_start

    for button in number_buttons:
        if button.check_click(pos):
            if button == number_buttons[0]:
                del number_buttons[0]
                if not hidden:
                    hidden = True
            else:
                gameOver(current_level)
            break

    # Next Level
    if len(number_buttons) == 0:
        is_start = False
        hidden = False
        current_level += 1
        setup(current_level)


def gameOver(level):
    print("Gamo Over!!!")
    global running
    running = False

    msg = gameFont.render(f"Your Current Level {level}", True, WHITE)
    center_x = WINDOW_WIDTH/2
    center_y = WINDOW_HEIGHT/2
    msg_rect = msg.get_rect(center=(center_x, center_y))
    screen.fill(BLACK)
    screen.blit(msg, msg_rect)
    print(msg)

# 세업정의


def setup(level):
    global number_buttons, display_timer

    # 숫자정의
    numberCnt = (level // LEVEL_SPLITER) + 5
    numberCnt = min(numberCnt, 20)

    # 시간설정
    display_timer = TIME_SEC - (level // LEVEL_SPLITER)
    display_timer = max(display_timer, 1)

    grid = [[0 for col in range(COLUMNS)] for row in range(ROWS)]

    number = 1
    while number <= numberCnt:
        row_idx = randrange(0, ROWS)
        col_idx = randrange(0, COLUMNS)
        if grid[row_idx][col_idx] == 0:
            grid[row_idx][col_idx] = number

            # 버튼생성
            center_x = MARGIN_LEFT + (col_idx * CELL_SIZE) + (CELL_SIZE / 2)
            center_y = MARGIN_TOP + (row_idx * CELL_SIZE) + (CELL_SIZE / 2)
            button = ReckButton(BUTTON_SIZE, BUTTON_SIZE,
                                center_x, center_y, number)
            number_buttons.append(button)
            number += 1

    # print(number_buttons)


setup(current_level)

# 메인루프
while running:
    click_pos = None
    for event in pygame.event.get():
        if event.type == QUIT:
            print("Quit Clicked")
            running = False
            # break
        elif event.type == MOUSEBUTTONUP:
            click_pos = pygame.mouse.get_pos()
            check_buttons(click_pos)
    #
    screen.fill(BLACK)

    # 게임여부
    if is_start:
        display_game_screen()
    else:
        display_start_screen()

    pygame.display.update()

time.delay(5000)
pygame.quit()
