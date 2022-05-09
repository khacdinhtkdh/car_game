import random
import sys
import pygame
from pygame import mixer


def create_car():
    random_x = random.choice(pos_x)
    new_car = car_surface.get_rect(midtop=(random_x, 10))
    return new_car


def move_car(cars):
    new_cars = []
    for car in cars:
        car.centery += 1
        if car.centery < 600:
            new_cars.append(car)
    return new_cars


def draw_cars(cars):
    for car in cars:
        screen.blit(car_surface, car)


def check_collision(cars):
    for car in cars:
        if car_main.colliderect(car):
            return False
    return True


# Intialize the pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((400, 600))
clock = pygame.time.Clock()

# Background
background = pygame.image.load('images/background1.png').convert()
background = pygame.transform.scale2x(background)

car_surface = pygame.image.load('images/car.png').convert()
# car_surface = pygame.transform.scale2x(car_surface)
car_list = []
pos_x = [110, 170, 230, 290]
index_car = 2

car_main_surface = pygame.image.load('images/car_main.png').convert()
car_main = car_main_surface.get_rect(midtop=(pos_x[index_car], 500))
# timer cars
car_time = pygame.USEREVENT
pygame.time.set_timer(car_time, 2500)

# # Sound
# mixer.music.load("background.wav")
# mixer.music.play(-1)
#
# # Caption and Icon
# pygame.display.set_caption("Space Invader")
# icon = pygame.image.load('ufo.png')
# pygame.display.set_icon(icon)
# car_list.extend(create_car())
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == car_time:
            car_list.append(create_car())

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                index_car = index_car - 1
            if event.key == pygame.K_RIGHT:
                index_car = index_car + 1

    if index_car < 0:
        index_car = 0
    if index_car > 3:
        index_car = 3

    screen.blit(background, (0, 0))
    if not check_collision(car_list):
        print('aaaaaaa')
    car_main.centerx = pos_x[index_car]
    screen.blit(car_main_surface, car_main)
    car_list = move_car(car_list)
    draw_cars(car_list)

    pygame.display.update()
    clock.tick(120)
