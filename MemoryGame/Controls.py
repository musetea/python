from random import randrange
from pygame import Rect, draw
import pygame


class StartButton:
    def __init__(self, width, height, position, font):
        self.button = Rect(0, 0, width, height)
        self.button.center = position
        self.font = font

    def displayScreen(self, screen, color, level):
        draw.circle(screen, color, self.button.center, 60, 5)

        msg = self.font.render("{level}", True, (0, 0, 0))
        msg_rect = msg.get_rect(center=self.button.center)

        screen.fill((255, 255, 255))
        screen.blit(msg, msg_rect)

    # 클릭위치체크
    def check(self, pos):
        if self.button.collidepoint(pos):
            return True
        else:
            return False

# 게임그리드맵


FONT_SIZE = 120


class GameGrid:

    number_buttons = []

    def __init__(self, rows, columns, font):
        # self.screen = screen
        self.rows = rows
        self.columns = columns
        self.grid = []
        self.font = font

    def setup(self, count):

        self.shuffle_gird(count)

    def shuffle_gird(self, count):
        rows = self.rows
        columns = self.columns
        # self.number_buttons.clear()

        self.grid = [[0 for col in range(columns)] for row in range(rows)]
        #
        number = 1
        while number <= count:
            row_idx = randrange(0, rows)
            col_idx = randrange(0, columns)
            if self.grid[row_idx][col_idx] != 0:
                self.grid[row_idx][col_idx] = number
                number += 1

                center_x = MARGIN_LEFT + \
                    (col_idx * CELL_SIZE) + (CELL_SIZE / 2)
                center_y = MARGIN_TOP + (row_idx * CELL_SIZE) + (CELL_SIZE / 2)
                print(BUTTON_SIZE, center_x, center_y)

                button = ButtonRect(center_x, center_y)
                self.number_buttons.append(button)

    def draw_grid(self, screen, color):
        print(self.number_buttons)

        for idx, button in enumerate(self.number_buttons, start=1):
            # pass
            button.drawRect(screen, color)

            # 숫자넣기
            # cell_text = self.font.render(str(idx), True, (0, 0, 0))
            # print(idx, button)
            # cell_rect = cell_text.get_rect(center=rect_btn.button.center)
            # screen.blit(cell_text, cell_rect)
            # print(cell_text)

            # print(self.buttons)

    def check_buttons(self, pos):
        for button in self.number_buttons:
            if button.collidepoint(pos):
                if button == self.number_buttons[0]:
                    print("Correct")
                    del self.number_buttons[0]
                    return True
                else:
                    print("wrong")
                    return False

    def remain_numbers(self):
        return len(self.number_buttons)


class ButtonRect(Rect):

    def __init__(self, center_x, center_y):
        self.button = Rect(0, 0, BUTTON_SIZE, BUTTON_SIZE)
        self.button.center = (center_x, center_y)
        print(self.button)

    def drawRect(self, screen, color):
        draw.rect(screen, color, self.button.center)
