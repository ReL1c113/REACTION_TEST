import pygame
import random
import time

pygame.init()
screen = pygame.display.set_mode((1500, 800))
screen.fill((0, 0, 255))
time1 = [300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900]
y = random.choice(time1)
x = 0
gameover = False
score_list = []

start_font = pygame.font.Font('freesansbold.ttf', 32)
final_score_font = pygame.font.Font('freesansbold.ttf', 32)


def starting():
    start_note = start_font.render("WAIT FOR RED IF COLOR BLUE STOP AT GREEN", True, (0, 0, 0))
    screen.blit(start_note, (450, 100))


def final_score_ren():
    score_ms = final_score_font.render(str(score_list) + "ms", True, (0, 0, 0))
    screen.blit(score_ms, (550, 500))


run = True

while (run):

    starting()
    y = y + 0.5
    if y == 1500:
        screen.fill((255, 0, 0))
        time_start = int(round(time.time() * 1000))

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            screen.fill((0, 255, 0))
            time_end = int(round(time.time() * 1000))
            final_time = int(time_end) - int(time_start)
            score_list.append(int(final_time))
            gameover = True
            x = x + 1
    if gameover and x <= 4:
        screen.fill((0, 0, 255))
        y = random.choice(time1)
        starting()
        y = y + 0.5
        if y == 1500:
            screen.fill((255, 0, 0))
            time_start = int(round(time.time() * 1000))
        gameover = False
    final_score_ren()

    pygame.display.update()
