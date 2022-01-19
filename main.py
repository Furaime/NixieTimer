import pygame
import sys
import time
from tubes import tubes
from pygame.constants import (
    QUIT, KEYDOWN, K_F9, K_F10
)

# 76 x 112
screen = pygame.display.set_mode((608, 112))

pygame.display.set_caption("Nixie Tube Timer")

screen.blit(tubes[0], (0, 0))
screen.blit(tubes[0], (76, 0))
screen.blit(tubes[10], (152, 0))
screen.blit(tubes[0], (228, 0))
screen.blit(tubes[0], (304, 0))
screen.blit(tubes[10], (380, 0))
screen.blit(tubes[0], (456, 0))
screen.blit(tubes[0], (532, 0))

running = 1
pause = 0
state = pause
start = 0
shuffle = 2


def timer():
    new = time.time_ns()
    now = (new - start) // 1000000000
    now = now % (24 * 3600)
    hour = now // 3600
    hour_d = hour // 10
    hour_u = hour % 10
    now %= 3600
    minutes = now // 60
    minus_d = minutes // 10
    minus_u = minutes % 10
    now %= 60
    sec_d = now // 10
    sec_u = now % 10

    screen.blit(tubes[hour_d], (0, 0))
    screen.blit(tubes[hour_u], (76, 0))
    screen.blit(tubes[10], (152, 0))
    screen.blit(tubes[minus_d], (228, 0))
    screen.blit(tubes[minus_u], (304, 0))
    screen.blit(tubes[10], (380, 0))
    screen.blit(tubes[sec_d], (456, 0))
    screen.blit(tubes[sec_u], (532, 0))


while 1:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_F9:
                state = pause
            if event.key == K_F10:
                state = running
    else:
        screen.blit(tubes[0], (0, 0))
        screen.blit(tubes[0], (76, 0))
        screen.blit(tubes[10], (152, 0))
        screen.blit(tubes[0], (228, 0))
        screen.blit(tubes[0], (304, 0))
        screen.blit(tubes[10], (380, 0))
        screen.blit(tubes[0], (456, 0))
        screen.blit(tubes[0], (532, 0))
        if start == 0:
            pygame.display.flip()

        if state == running:
            if start == 0:
                start = time.time_ns()
            timer()
            pygame.display.flip()
