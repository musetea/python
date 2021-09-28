from pygame import display, image
from pygame.constants import K_LEFT, K_RIGHT, K_UP, K_DOWN

WINDOW_WIDTH = 480
WINDOW_HEIGHT = 640
SPEED = 0.5


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
        # elif self.y_pos > (WINDOW_HEIGHT-self.height):
        #     self.y_pos = WINDOW_HEIGHT-self.height

        screen.blit(self.character, (self.x_pos, self.y_pos))

    def keyDown(self, key):
        # print(self.to_x, self.to_y)
        if key == K_LEFT:
            self.to_x -= SPEED
        elif key == K_RIGHT:
            self.to_x += SPEED
        # elif key == K_UP:
        #     self.to_y -= SPEED
        # elif key == K_DOWN:
        #     self.to_y += SPEED

    def keyUp(self, key):
        if key == K_LEFT or key == K_RIGHT:
            self.to_x = 0
        # elif key == K_UP or key == K_DOWN:
        #     self.to_y = 0

    def getRect(self):
        rect = self.character.get_rect()
        rect.left = self.x_pos
        rect.top = self.y_pos
        return rect
