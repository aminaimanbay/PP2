#Imports
import pygame, sys
from pygame.locals import *
import random, time

#Initialzing 
pygame.init()

#Setting up FPS 
FPS = 60
FramePerSec = pygame.time.Clock()

#Creating colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

#Other Variables for use in the program
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = random.randint(1, 5)
SCORE = 0
MAX_HEALTH = 200
SUM = 0

#Setting up Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

background = pygame.image.load("AnimatedStreet.png")

#Create a white screen 
DISPLAYSURF = pygame.display.set_mode((400,600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")

#Music of background
pygame.mixer.music.load('jumpingexplorer.mp3')
pygame.mixer.music.play(-1)  



class Enemy(pygame.sprite.Sprite):
      def __init__(self,x, y, speed):
        w = random.randint(28, 55)
        h=random.randint(59, 85) 
        super().__init__() 
        self.image = pygame.image.load("Enemy.png")
        self.surf = pygame.Surface((w,h)) 
        self.rect = self.surf.get_rect(center = (random.randint(40,SCREEN_WIDTH-40)
                                                 , 0))
        self.speed = speed

      def move(self):
        global SCORE
        self.rect.move_ip(0,SPEED)
        w = random.randint(28, 75)
        h=random.randint(59, 100) 

        if self.rect.top > 600:
            SCORE += 1
            xx = [60, 210, 360]
            x = xx[random.randint(0, 2)]
            y = random.randint(-200, -100)
            self.speed = random.randint(3, 7)
            self.rect.center = (x, y)
        else:
            self.rect.move_ip(0, self.speed)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Player.png")
        self.surf = pygame.Surface((40, 75))
        self.rect = self.surf.get_rect(center = (160, 520))
        self.health = 200
       
    def move(self):
        pressed_keys = pygame.key.get_pressed()
    
        pygame.mixer.Sound('Clickbutton.mp3').play()
        
        if self.rect.left > 0:
                if pressed_keys[K_LEFT]:
                    self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:        
                if pressed_keys[K_RIGHT]:
                    self.rect.move_ip(5, 0)

    def draw_health(self):
        r = min(255, 255 - (255 * ((self.health - (MAX_HEALTH - self.health)) / MAX_HEALTH)))
        b = min(255, 255 * (self.health / (MAX_HEALTH / 2)))
        color = (r, 0, b)
        width = int(self.rect.width * self.health / MAX_HEALTH)
        self.health_bar = pygame.Rect(0, 0, width, 9)
        pygame.draw.rect(self.image, color, self.health_bar)

                  
class Coin (pygame.sprite.Sprite):
        def __init__(self):
            super().__init__() 
            self.image = pygame.image.load("coin.png")
            self.surf = pygame.Surface((3, 3))
            self.rect = self.surf.get_rect(center = (10, 10))

        def move(self):
            self.rect.move_ip(0,7)
            if (self.rect.bottom > 600):
                self.rect.top = 0
                self.rect.center = (random.randint(10, SCREEN_WIDTH - 10), 0)

#Setting up Sprites        
P1 = Player()

E1 = Enemy(60, -50, 5)

C1 = Coin()
C2 = Coin()
C3 = Coin()

#Creating Sprites Groups
enemies = pygame.sprite.Group()
enemies.add(E1)

coins = pygame.sprite.Group()
coins.add (C1)
coins.add (C2)
coins.add (C3)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)

all_sprites.add(C1)
all_sprites.add(C2)
all_sprites.add(C3)

#Adding a new User event 
ADDENEMY = pygame.USEREVENT + 2
pygame.time.set_timer(ADDENEMY, 9000)


#Game Loop
while True:
      
    #Cycles through all events occuring  
    for event in pygame.event.get():  
        
        if event.type == ADDENEMY:
            # Create the new enemy and add it to sprite groups
            new_enemy = Enemy(60,-50,5)
            enemies.add(new_enemy)
            all_sprites.add(new_enemy) 
            
        elif event.type == QUIT:
            pygame.quit()
            sys.exit()

    

    DISPLAYSURF.blit(background, (0,0))
    scores = font_small.render("Score " + str(SCORE), True, BLACK)
    DISPLAYSURF.blit(scores, (10,10))
    sums = font_small.render("Coins " + str(SUM), True, BLACK)
    DISPLAYSURF.blit(sums, (290,10))


    #Moves and Re-draws all Sprites
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()

    
    P1.draw_health()

    #To be run if collision occurs between Player and Coin
    if pygame.sprite.spritecollideany(P1, coins):
        SUM+=1
        
    #To be run if collision occurs between Player and Enemy
    if pygame.sprite.spritecollideany(P1, enemies):
        P1.health -=1
        if P1.health ==0 :
            pygame.mixer.Sound('crash.wav').play()
            time.sleep(1)
                   
            DISPLAYSURF.fill(RED)
            DISPLAYSURF.blit(game_over, (30,250))
          
            pygame.display.update()
            for entity in all_sprites:
                entity.kill() 
            time.sleep(2)
            pygame.quit()
            sys.exit()    

            
        
    pygame.display.update()
    enemies.update()
    FramePerSec.tick(FPS)
    

