import pygame
import pygame_menu
from pygame.locals import *
import random
import sys
import time

pygame.init()
screen = pygame.display.set_mode((800, 600))


def set_random_position():
    return 10* round((random.randint(18, 782))/10),  10*round ((random.randint(18, 582))/10)

food_x, food_y = set_random_position()


class Snake:
    def __init__(self, x, y):
        self.size = 1
        self.elements = [[x, y]]
        self.radius = 10
        self.dx = 5 
        self.dy = 0
        self.is_add = False
        self.speed = 10


    def draw1(self):
        for element in self.elements:
            pygame.draw.circle(screen, (255, 0, 0), element, self.radius)
    
    def draw2(self):
        for element in self.elements:
            pygame.draw.circle(screen, (0, 0, 255), element, self.radius)

    def add_to_snake(self):
        self.size += 1
        self.elements.append([0, 0])
        self.is_add = False
        if self.size % 5 == 0:
            self.speed += 5

    def move(self):
        if self.is_add:
            self.add_to_snake()

        for i in range(self.size - 1, 0, -1):
            self.elements[i][0] = self.elements[i - 1][0]
            self.elements[i][1] = self.elements[i - 1][1]

        self.elements[0][0] += self.dx
        self.elements[0][1] += self.dy
        
    def eat(self, foodx, foody):
        x = self.elements[0][0]
        y = self.elements[0][1]
        
        if foodx <= x <= foodx + 10 and foody <= y <= foody + 10:
            return True
        return False

    def check_for_boundaries(self, game_over):
        if any((
            self.elements[0][0] > 782
            or self.elements[0][0] < 18,
            self.elements[0][1] > 582
            or self.elements[0][1] < 18
                )):
            game_over()

    def check_for_walls(self, game_over):
        if (self.elements[0][0] > 190 and self.elements[0][0] < 220 and self.elements[0][1] > 290 and  self.elements[0][1] < 460):
            game_over()
        if (self.elements[0][0] > 490 and self.elements[0][0] < 710 and self.elements[0][1] > 90 and self.elements[0][1] < 120):
            game_over()
        if (self.elements[0][0] > 640 and self.elements[0][0] < 670 and self.elements[0][1] > 440 and  self.elements[0][1] < 510):
            game_over()

snake1 = Snake(100, 100)
snake2 = Snake(150, 100)


d = 5
FPS = 30
clock = pygame.time.Clock()
def rectangle():
    pygame.draw.rect(screen, (0,255,0), [0, 0, 800, 600], 18)

def game_over():
    my_font = pygame.font.SysFont('times new roman', 100)
    text_final = my_font.render('YOU LOST', True, (255,0,0))
    screen.fill((0,0,0))
    screen.blit(text_final, (200,300))
    pygame.display.flip()
    clock.tick(30)
    pygame.quit()
    sys.exit()


def cache (filename):
    global c,code
    try:
        c = open(filename + ".txt", "rt")
        code = eval(c.read())
        c.close()
    except:
        c = open(filename + ".txt", "wt")
        c.write("{'': ''}")
        c.close()

        c = open(filename + ".txt", "rt")
        code = eval(c.read())
        c.close()

def find(filename,variable):
    global c,code
    c = open(filename + ".txt", "rt")
    code = eval(c.read())
    c.close()
    variable2 = code.get(variable)
    return variable2

def store(filename,variable,info):
    global c,code
    code[variable] = info
    c = open(filename + ".txt", "wt")
    c.write(str(code))
    c.close()


file = "snakefile"


cache (file)


def the_game():
    running= True
    global food_x, food_y,  d
    while running:
        clock.tick(snake1.speed)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                if event.key == pygame.K_SPACE:
                    food_x, food_y = set_random_position()
                    ########################################################
                if event.key == pygame.K_c :
                    clearcache(file) 
                if event.key == pygame.K_s :
                    store(file,"food_x",food_x)
                    store(file,"food_y",food_y)
                    store(file,"snake1.elements[0][0]",snake1.elements[0][0])                   
                    store(file,"snake1.elements[0][1]",snake1.elements[0][1])
                    store(file,"snake2.elements[0][0]",snake2.elements[0][0])                    
                    store(file,"snake2.elements[0][1]",snake2.elements[0][1])





                if event.key == pygame.K_q :
                    game_over()

                if event.key == pygame.K_RIGHT and snake1.dx != -d:
                    snake1.dx, snake1.dy = d, 0

                if event.key == pygame.K_LEFT and snake1.dx != d:
                    snake1.dx, snake1.dy = -d, 0

                if event.key == pygame.K_UP and snake1.dy != d:
                    snake1.dx, snake1.dy = 0, -d
              
                if event.key == pygame.K_DOWN and snake1.dy != -d:
                    snake1.dx, snake1.dy = 0, d
                

                if event.key == pygame.K_d and snake2.dx != -d:
                    snake2.dx, snake2.dy = d, 0
                
                if event.key == pygame.K_a and snake2.dx != d:
                    snake2.dx, snake2.dy = -d, 0
               
                if event.key == pygame.K_w and snake2.dy != d:
                    snake2.dx, snake2.dy = 0, -d
                
                if event.key == pygame.K_s and snake2.dy != -d:
                    snake2.dx, snake2.dy = 0, d
              
        if snake1.eat(food_x, food_y):
            snake1.is_add = True
            food_x, food_y = set_random_position()

        if snake2.eat(food_x, food_y):
            snake2.is_add = True
            food_x, food_y = set_random_position()

        snake1.move()
        snake2.move()
        screen.fill((0, 0, 0))
        snake1.draw1()
        snake2.draw2()
        rectangle()
        pygame.draw.rect(screen, (0, 255, 255), (food_x, food_y, 10, 10))
        snake1.check_for_boundaries(game_over)
        snake2.check_for_boundaries(game_over)
        pygame.display.flip()

def start_the_easy_game():
    the_game()

def start_the_hard_game():
    running= True
    global food_x, food_y,  d
    while running:
        clock.tick(snake1.speed)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                if event.key == pygame.K_SPACE:
                    food_x, food_y = set_random_position()
                if event.key == pygame.K_q :
                    game_over()

                if event.key == pygame.K_RIGHT and snake1.dx != -d:
                    snake1.dx, snake1.dy = d, 0

                if event.key == pygame.K_LEFT and snake1.dx != d:
                    snake1.dx, snake1.dy = -d, 0

                if event.key == pygame.K_UP and snake1.dy != d:
                    snake1.dx, snake1.dy = 0, -d
              
                if event.key == pygame.K_DOWN and snake1.dy != -d:
                    snake1.dx, snake1.dy = 0, d
                

                if event.key == pygame.K_d and snake2.dx != -d:
                    snake2.dx, snake2.dy = d, 0
                
                if event.key == pygame.K_a and snake2.dx != d:
                    snake2.dx, snake2.dy = -d, 0
               
                if event.key == pygame.K_w and snake2.dy != d:
                    snake2.dx, snake2.dy = 0, -d
                
                if event.key == pygame.K_s and snake2.dy != -d:
                    snake2.dx, snake2.dy = 0, d
              

        if snake1.eat(food_x, food_y):
            snake1.is_add = True
            food_x, food_y = set_random_position()

        if snake2.eat(food_x, food_y):
            snake2.is_add = True
            food_x, food_y = set_random_position()

        snake1.move()
        snake2.move()
        screen.fill((0, 0, 0))
        snake1.draw1()
        snake2.draw2()
        rectangle()
        pygame.draw.rect(screen, (0, 255, 255), (food_x, food_y, 10, 10))

        pygame.draw.rect(screen, (0,255,0), [200, 300, 10, 150])
        pygame.draw.rect(screen, (0,255,0), [500, 100, 200, 10])
        pygame.draw.rect(screen, (0,255,0), [650, 450, 10, 50])

        snake1.check_for_boundaries(game_over)
        snake2.check_for_boundaries(game_over)
        snake1.check_for_walls(game_over)
        snake2.check_for_walls(game_over)

        pygame.display.flip()
    
def continuegame():
    running= True
    global food_x, food_y,  d
    food_x = find(file,"food_x")
    food_y = find(file,"food_y")
    snake1.elements[0][0]=find(file,"snake1.elements[0][0]")
    snake1.elements[0][1]=find(file,"snake1.elements[0][1]")
    snake2.elements[0][0]=find(file,"snake2.elements[0][0]")
    snake2.elements[0][1]=find(file,"snake2.elements[0][1]")
    
    while running:
        clock.tick(snake1.speed)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                if event.key == pygame.K_SPACE:
                    food_x, food_y = set_random_position()
                    ########################################################
                if event.key == pygame.K_c :
                    clearcache(file) 
                if event.key == pygame.K_s :
                    store(file,"food_x",food_x)
                    store(file,"food_y",food_y)
                    store(file,"snake1.elements[0][0]",snake1.elements[0][0])                   
                    store(file,"snake1.elements[0][1]",snake1.elements[0][1])
                    store(file,"snake2.elements[0][0]",snake2.elements[0][0])                    
                    store(file,"snake2.elements[0][1]",snake2.elements[0][1])





                if event.key == pygame.K_q :
                    game_over()

                if event.key == pygame.K_RIGHT and snake1.dx != -d:
                    snake1.dx, snake1.dy = d, 0

                if event.key == pygame.K_LEFT and snake1.dx != d:
                    snake1.dx, snake1.dy = -d, 0

                if event.key == pygame.K_UP and snake1.dy != d:
                    snake1.dx, snake1.dy = 0, -d
              
                if event.key == pygame.K_DOWN and snake1.dy != -d:
                    snake1.dx, snake1.dy = 0, d
                

                if event.key == pygame.K_d and snake2.dx != -d:
                    snake2.dx, snake2.dy = d, 0
                
                if event.key == pygame.K_a and snake2.dx != d:
                    snake2.dx, snake2.dy = -d, 0
               
                if event.key == pygame.K_w and snake2.dy != d:
                    snake2.dx, snake2.dy = 0, -d
                
                if event.key == pygame.K_s and snake2.dy != -d:
                    snake2.dx, snake2.dy = 0, d
              
        if snake1.eat(food_x, food_y):
            snake1.is_add = True
            food_x, food_y = set_random_position()

        if snake2.eat(food_x, food_y):
            snake2.is_add = True
            food_x, food_y = set_random_position()

        snake1.move()
        snake2.move()
        screen.fill((0, 0, 0))
        snake1.draw1()
        snake2.draw2()
        rectangle()
        pygame.draw.rect(screen, (0, 255, 255), (food_x, food_y, 10, 10))
        snake1.check_for_boundaries(game_over)
        snake2.check_for_boundaries(game_over)
        pygame.display.flip()

    


menu = pygame_menu.Menu('Snake',300, 400,  theme=pygame_menu.themes.THEME_BLUE)
menu.add
menu.add.button('Easy', start_the_easy_game)
menu.add.button('Hard', start_the_hard_game)
menu.add.label("q=Quit, space=food shift")
menu.add.button('Continue',continuegame)
menu.add.button('Quit', pygame_menu.events.EXIT)

menu.mainloop(screen)

pygame.quit()


