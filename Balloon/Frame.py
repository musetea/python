from os import path
import pygame
from pygame import display, image, font, time
from pygame.constants import K_LEFT, K_RIGHT, K_SPACE

WIDTH = 640
HEIGHT = 480
CHARACTER_SPEED = 5
WEAPON_SPEED = 10
BALLOONS_SPEED_Y = [-18, -15, -12, -9]

TITLE = "나도 팡"
FPS = 30
weapons = []    # 무기리스트
# 볼4개
balloons = []
bolls = []
weapon_remove_idx = -1
bool_remove_idx = -1
time_totals = 5
time_start_tick = time.get_ticks()
game_result = "Game Over"

pygame.init()
font.init()
screen = display.set_mode((WIDTH, HEIGHT))
display.set_caption(TITLE)
clock = pygame.time.Clock()  # FPS
gameFont = font.Font(None, 40)

# 유틸
# 현재폴더반환


def get_current_path(imgPath):
    curr_path = path.dirname(__file__)
    image_path = path.join(curr_path, imgPath)
    return image_path


def game_over():
    msg = gameFont.render(game_result, True, (255, 255, 0))
    msg_rect = msg.get_rect(center=(int(WIDTH/2), int(HEIGHT/2)))
    screen.blit(msg, msg_rect)
    display.update()
    time.delay(3000)

# 클래스
# 스테이지


class Stage(object):
    def __init__(self, imgPath):
        self.stage = image.load(imgPath)
        self.size = self.stage.get_rect().size
        self.width = self.size[0]
        self.height = self.size[1]

# 캐릭터


class Character(object):
    position_x = 0
    position_y = 0
    move_x = 0
    move_y = 0

    def __init__(self, imgPath):
        self.character = image.load(imgPath)
        self.size = self.character.get_rect().size
        self.width = self.size[0]
        self.height = self.size[1]

    def keyDown(self, key):
        if key == K_LEFT:
            self.move_x -= CHARACTER_SPEED
            self.position_x += self.move_x
        elif key == K_RIGHT:
            self.move_x += CHARACTER_SPEED
            self.position_x += self.move_x

        # 경제설정
        if self.position_x < 0:
            self.position_x = 0
        elif self.position_x > (WIDTH - self.width):
            self.position_x = WIDTH - self.width

    def keyUp(self, key):
        if key == K_LEFT or key == K_RIGHT:
            self.move_x = 0

    def position(self, x, y):
        self.position_x = x
        self.position_y = y

    def getRect(self):
        rect = self.character.get_rect()
        rect.top = self.position_y
        rect.left = self.position_y
        return rect

    def draw(self, screen, delta):
        x = self.position_x
        y = self.position_y
        screen.blit(self.character, (x, y))

# 무기


class Weapon(object):
    def __init__(self, imgPath):
        self.weapon = image.load(imgPath)
        self.size = self.weapon.get_rect().size
        self.width = self.size[0]

    def getRect(self, pos_x, pos_y):
        rect = self.weapon.get_rect()
        rect.left = pos_x
        rect.top = pos_y
        return rect

# 풍성


class Balloon(object):

    def __init__(self, img):
        self.bool = image.load(img)
        self.size = self.bool.get_rect().size
        self.width = self.size[0]
        self.height = self.size[1]

    def postion(self, x, y):
        self.position_x = x
        self.position_y = y

    def getRect(self):
        return self.bool.get_rect()


class Boll(object):
    position_x = 50
    position_y = 50
    image_idx = 0
    move_x = 3
    move_y = -6
    speed_y = BALLOONS_SPEED_Y[0]

    def __init__(self, pos_x, pos_y, img_idx, to_x, to_y, speed_y):
        self.position_x = pos_x
        self.position_y = pos_y
        self.image_idx = img_idx
        self.move_x = to_x
        self.move_y = to_y
        self.speed_y = speed_y

    def draw(self, screen, balloon):
        self.position_x += self.move_x
        self.position_y += self.move_y
        screen.blit(balloon.bool, (self.position_x,  self.position_y))


image_dir = get_current_path("images")
print(image_dir)
background = image.load(path.join(image_dir, "background.png"))
stage = Stage(path.join(image_dir, "stage.png"))
character = Character(path.join(image_dir, "character.png"))
character.position((WIDTH/2) - (character.width/2),
                   HEIGHT - stage.height - character.height)
weapon = Weapon(path.join(image_dir, "weapon.png"))
balloons.append(Balloon(path.join(image_dir, "balloon1.png")))
balloons.append(Balloon(path.join(image_dir, "balloon2.png")))
balloons.append(Balloon(path.join(image_dir, "balloon3.png")))
balloons.append(Balloon(path.join(image_dir, "balloon4.png")))

#
bolls.append(Boll(
    pos_x=50,
    pos_y=50,
    img_idx=0,
    to_x=3,
    to_y=-6,
    speed_y=-18
))


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

            if event.key == K_SPACE:
                weapon_x_pos = character.position_x + \
                    (character.width/2) - weapon.width/2
                weapon_y_pos = character.position_y
                print(weapon_x_pos, weapon_y_pos)
                weapons.append([weapon_x_pos, weapon_y_pos])

        if event.type == pygame.KEYUP:
            character.keyUp(event.key)

    weapons = [[w[0], w[1] - WEAPON_SPEED] for w in weapons]
    weapons = [[w[0], w[1]] for w in weapons if w[1] > 0]

    # 볼
    # 볼화면출력 (인덱스정보가 필요시)
    for boll_idx, bool in enumerate(bolls):
        balloon = balloons[bool.image_idx]

        if bool.position_x <= 0 or bool.position_x > (WIDTH - balloon.width):
            bool.move_x *= -1

        # 위아래
        if bool.position_y > HEIGHT - stage.height:
            bool.move_y = bool.speed_y
        else:
            bool.move_y += 0.5

        bool.position_x += bool.move_x
        bool.position_y += bool.move_y

    # 충돌처리
    character_rect = character.getRect()
    for bool_idx, bool in enumerate(bolls):
        balloon = balloons[bool.image_idx]
        bool_rect = balloon.getRect()
        bool_rect.left = bool.position_x
        bool_rect.top = bool.position_y
        #  캐릭처 충돌체크
        if character_rect.colliderect(bool_rect):
            print("충돌!!!")
            running = False
            break
        # 무기충돌체크
        for weapon_idx, val in enumerate(weapons):
            x_pos, y_pos = val
            weapon_rect = weapon.getRect(x_pos, y_pos)
            if weapon_rect.colliderect(bool_rect):
                print("무기충돌!!!")
                weapon_remove_idx = weapon_idx
                bool_remove_idx = bool_idx

                #
                if bool.image_idx < 3:
                    b_width = bool_rect.size[0]
                    b_height = bool_rect.size[1]
                    newBalloon = balloons[bool.image_idx + 1]
                    new_ball_rect = newBalloon.getRect()
                    new_ball_widht = new_ball_rect.size[0]
                    new_ball_height = new_ball_rect.size[1]

                    leftBool = Boll(pos_x=bool.position_x + (b_width/2) - (new_ball_widht/2),
                                    pos_y=bool.position_y +
                                    (b_height/2) - (new_ball_height/2),
                                    img_idx=bool.image_idx + 1, to_x=-3, to_y=-6, speed_y=BALLOONS_SPEED_Y[bool.image_idx + 1])
                    bolls.append(leftBool)
                    rightBool = Boll(pos_x=bool.position_x + (b_width/2) - (new_ball_widht/2),
                                     pos_y=bool.position_y +
                                     (b_height/2) - (new_ball_height/2),
                                     img_idx=bool.image_idx + 1, to_x=3, to_y=-6, speed_y=BALLOONS_SPEED_Y[bool.image_idx + 1])
                    bolls.append(rightBool)
                break
        else:
            continue
        break

    # 삭제처리
    if bool_remove_idx > -1:
        del bolls[bool_remove_idx]
        bool_remove_idx = -1    # 초기화

    if weapon_remove_idx > -1:
        del weapons[weapon_remove_idx]
        weapon_remove_idx = -1  # 초기화

    if len(bolls) <= 0:
        game_result = "Mission Completed"
        running = False

    # 배경이미지
    screen.blit(background, (0, 0))
    # 무기그리기
    for x_pos, y_pos in weapons:
        screen.blit(weapon.weapon, (x_pos, y_pos))

    for bool_idx, bool in enumerate(bolls):
        bool.draw(screen, balloons[bool.image_idx])

    screen.blit(stage.stage, (0, HEIGHT - stage.height))
    character.draw(screen, delta)

    # 타임체크
    curr_time = (time.get_ticks() - time_start_tick)/1000
    elapsed_time = int(time_totals - curr_time)
    disp_timer = "Time : {}".format(elapsed_time)
    timer = gameFont.render(disp_timer, True, (255, 255, 255))
    screen.blit(timer, (WIDTH-timer.get_width()-10, 10))
    if elapsed_time < 0:
        game_result = "Time Over"
        running = False

    display.update()

game_over()
pygame.quit()
