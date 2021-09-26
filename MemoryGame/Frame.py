import pygame
from pygame.constants import MOUSEBUTTONUP, QUIT
from Buttons import StartButton


WIDTH = 1280
HEIGHT = 720
BLACK = (0, 0, 0)   # 검정색
WHIRT = (255, 255, 255)   # 하얀색

is_game_start = False


TITLE = "Memory Game"
start_button = StartButton(120, 120, (120, HEIGHT-120))


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)


# 메인루프
running = True
while running:
    click_pos = None
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break
        elif event.type == pygame.MOUSEBUTTONUP:
            click_pos = pygame.mouse.get_pos()
            print(click_pos)

    screen.fill(BLACK)
    if is_game_start:
        pass
    else:
        # 시작화면표시
        start_button.displayScreen(screen, WHIRT)

    pygame.display.update()

pygame.quit()
