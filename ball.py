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
        self.g = [0, 9.8];
        # 합성 가속도
        self.a = [self.g[0], self.g[1]];

        # 질량
        self.mass = mass;

        # 반지름
        self.radius = radius * self.mass;

        # t:  현재까지 누적된 시뮬레이션 시간
        self.t = 0;

        # v0: v(0), 즉 시간 0초일 때 초기 속도
        self.v0 = v0;

        # v: v(T=t), 즉 시간이 T=t초 일때 (현재 속도)
        self.v = [self.v0[0], self.v0[1]];

        # s0: s(T=0), 즉 시간 0초일 때 T=0초 일 때 초기 위치

        # s: s(T=t), 즉 시간이 T=t초 일때 (현재 위치)