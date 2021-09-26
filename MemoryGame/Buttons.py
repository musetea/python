import pygame


class StartButton:
    def __init__(self, width, height, position):
        self.button = pygame.Rect(0, 0, width, height)
        self.button.center = position

    def displayScreen(self, screen, color):
        pygame.draw.circle(screen, color, self.button.center, 60, 5)
