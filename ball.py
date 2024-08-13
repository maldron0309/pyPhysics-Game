import pygame

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WITHE = (255, 255, 255)
BLACK = (0, 0, 0)
GARY = (100, 100, 100)
YELLOW = (255, 255, 0)

class Ball:
    def __init__(self, mass = 1, s0 = [0, 0], v0 = [0, 0], a = [0, 0], radius = 10, color = RED):
        # g: 중력가속도 9.8m/s^2