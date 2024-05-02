import pygame
import time
import random

pygame.init()

white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

dis_width = 600
dis_height = 400

dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game')

clock = pygame.time.Clock()

snake_block = 10
initial_snake_speed = 15

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

food_probabilities = {
    "normal_food": 0.6,
    "bonus_food": 0.3,
    "super_food": 0.1
}

class Food:
    def __init__(self, food_type, x, y, timer):
        self.food_type = food_type
        self.x = x
        self.y = y
        self.timer = timer

def generate_food():
    food_type = random.choices(
        list(food_probabilities.keys()),
        weights=list(food_probabilities.values())
    )[0]
    food_x = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    food_y = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
    return food_type, food_x, food_y

active_foods = []

def update_food_timers():
    for food in active_foods:
        food.timer -= 1
        if food.timer <= 0:
            active_foods.remove(food)

def Your_score(score, level):
    value = score_font.render("Score: " + str(score) + " Level: " + str(level), True, yellow)
    dis.blit(value, [0, 0])

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])

def food_on_snake(foodx, foody, snake_list):
    if [foodx, foody] in snake_list:
        return True
    return False

def gameLoop():
    game_over = False
    game_close = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    snake_speed = initial_snake_speed
    level = 1

    food_type, foodx, foody = generate_food()
    active_foods.append(Food(food_type, foodx, foody, 100))

    while not game_over:

        while game_close:
            dis.fill(blue)
            message("You Lost! Press C-Play Again or Q-Quit", red)
            Your_score(Length_of_snake - 1, level)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x1_change == 0:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT and x1_change == 0:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP and y1_change == 0:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN and y1_change == 0:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(blue)

        update_food_timers()
        for food in active_foods:
            pygame.draw.rect(dis, green, [food.x, food.y, snake_block, snake_block])

        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1, level)

        pygame.display.update()

        for food in active_foods:
            if x1 == food.x and y1 == food.y:
                active_foods.remove(food)
                food_type, foodx, foody = generate_food()
                active_foods.append(Food(food_type, foodx, foody, 100))
                Length_of_snake += 1

                if Length_of_snake % 3 == 0:
                    level += 1
                    snake_speed += 5

        clock.tick(snake_speed)

    pygame.quit()
    quit()

gameLoop()