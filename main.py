import random
import sys
import pygame
from pygame import mixer

speed_game = 1
score_game = 0


def create_car():
    random_x = random.choice(pos_x)
    new_car = car_surface.get_rect(midtop=(random_x, 10))
    return new_car


def move_car(cars, score):
    new_cars = []
    for car in cars:
        car.centery += speed_game
        if car.centery < 600:
            new_cars.append(car)
        else:
            score += 10
    return new_cars, score


def draw_cars(cars):
    for car in cars:
        screen.blit(car_surface, car)


def check_collision(cars):
    for car in cars:
        if car_main.colliderect(car):
            return False
    return True


def display_start_game():
    start_surface = game_font.render(str("Press space to play"), True, (255, 0, 0))
    start_rect = start_surface.get_rect(center=(216, 200))
    screen.blit(start_surface, start_rect)


def display_score():
    score_surface = game_font.render("Score: " + str(int(score_game)), True, (255, 255, 0))
    score_rect = score_surface.get_rect(center=(216, 100))
    screen.blit(score_surface, score_rect)


pygame.mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=512)

# Intialize the pygame
pygame.init()

game_font = pygame.font.SysFont('timesnewroman', 35)
score_font = pygame.font.SysFont('Bauhaus93', 35)

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

driving_sound = pygame.mixer.Sound('sound/car_driving2.wav')
hit_sound = pygame.mixer.Sound('sound/sfx_hit.wav')
count_down_sound = pygame.mixer.Sound('sound/count_down.mp3')
# timer cars

car_time = pygame.USEREVENT
timer_car = 2000
pygame.time.set_timer(car_time, timer_car)

game_active = False
start_game = True
# driving_sound.play(-1)
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
            if event.key == pygame.K_SPACE and not game_active:
                start_game = False
                game_active = True
                count_down_sound.play()
                pygame.time.wait(3000)
                driving_sound.play(-1)

    if index_car < 0:
        index_car = 0
    if index_car > 3:
        index_car = 3

    speed_game = (score_game // 100) + 1

    screen.blit(background, (0, 0))

    if game_active:
        # driving_sound.play()
        if not check_collision(car_list):
            hit_sound.play()
            game_active = False
            start_game = True
        car_main.centerx = pos_x[index_car]
        screen.blit(car_main_surface, car_main)
        car_list, score_game = move_car(car_list, score_game)
        draw_cars(car_list)
        display_score()
        print(speed_game)
    else:
        car_list.clear()
        driving_sound.stop()

    if start_game:
        display_start_game()

    pygame.display.update()
    clock.tick(120)
