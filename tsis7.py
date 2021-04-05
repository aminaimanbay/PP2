import pygame 
import math
pygame.init()

white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)
black = (0, 0, 0)

surface = pygame.display.set_mode((900, 675))

def rectangle():
    pygame.draw.rect(surface, black, [50, 15, 780, 540], 2)

def verticallines():
  
    for i in range(80, 850, 120): 
        if i == 440:
            pygame.draw.line(surface, black, [i, 15], [i, 555], 2)
        elif i == 560:
            pygame.draw.line(surface, black, [i, 15], [i, 45], 1)
            pygame.draw.line(surface, black, [i, 105], [i, 555], 1)
        else:
            pygame.draw.line(surface, black, [i, 15], [i, 555], 1)

def horizontallines():
    for i in range(45, 580, 60): 
        if i == 285:
            pygame.draw.line(surface, black, [50, i], [830, i], 2)
        else:
            pygame.draw.line(surface, black, [50, i], [830, i], 1)

def dividerofx():
    
    for i in range(95, 800, 30):
        pygame.draw.line(surface, black, [i, 15], [i, 23], 1)
        pygame.draw.line(surface, black, [i, 547], [i, 555], 1)
    for i in range(110, 800, 60):
        pygame.draw.line(surface, black, [i, 15], [i, 30], 1)
        pygame.draw.line(surface, black, [i, 540], [i, 555], 1)
    for i in range(140, 830, 120):
        pygame.draw.line(surface, black, [i, 15], [i, 35], 1)
        pygame.draw.line(surface, black, [i, 535], [i, 555], 1)

def dividerofy():

    for i in range(60, 520, 30):
        pygame.draw.line(surface, black, [50, i], [55, i], 1)
        pygame.draw.line(surface, black, [825, i], [830, i], 1)
    for i in range(75, 500, 60):
        pygame.draw.line(surface, black, [50, i], [65, i], 1)
        pygame.draw.line(surface, black, [815, i], [830, i], 1)

def singraph():
    for i in range(80, 800):
        sin1 = 240 * math.sin((i-80) / 120 * math.pi)
        sin2 = 240 * math.sin((i-79) / 120 * math.pi)
        pygame.draw.aaline(surface, red, (i, 285 + sin1), ((i+1), 285+sin2))

def cosgraph():    
    for i in range(80, 800, 2):
        cos1 = 240 * math.cos((i-80) / 120 * math.pi)
        cos2 = 240 * math.cos((i-81) / 120 * math.pi)
        pygame.draw.aaline(surface, blue, (i, 285 + cos1), ((i-1), 285 + cos2))
    
def numsvertical():
    nums = [ '1.00' , '0.75' , '0.50' , '0.25' , '0.00']
    myiter = iter(nums)

    font = pygame.font.SysFont('times new roman', 18, False, True)
    for i in range(32, 273, 60):
        text = font.render(next(myiter), True, black)
        surface.blit(text, (7, i))

    nums.remove('0.00')
    myiter = iter(list(map(lambda x: '-' + x, nums)))

    myiter = iter(nums[::-1])
    for i in range(330, 520, 60):
        text = font.render('-'+next(myiter), True, black)
        surface.blit(text, (7, i))

def numshorizontal():
    p = chr(960)
    d = chr(95)
    mpi = ['3'+p, '2'+p, p]
    half_mpi = ['5'+p, '3'+p, ' '+ p]
    myiter = iter(half_mpi)
    my_iter = iter(mpi)

    font = pygame.font.SysFont('times new roman', 20, False, True)

    for i in range(140, 400, 120): #left side
        text = font.render(next(myiter), True, black)
        text2 = font.render(d+" "+d+d+d, True, black)
        text3 = font.render('2', True, black)
        surface.blit(text, (i-8, 560))
        surface.blit(text2, (i-25, 560))
        surface.blit(text3, (i-6, 580))

    for i in range(70, 350, 120):
        text = font.render('-'+ next(my_iter), True, black)
        surface.blit(text, (i, 560))

    text = font.render('0', True, black)
    text_x = font.render('X', True, black)
    surface.blit(text, (435, 560))
    surface.blit(text_x, (435, 590))

    myiter = iter(half_mpi[::-1])
    my_iter = iter(mpi[::-1])

    for i in range(500, 741, 120):
        text = font.render(next(myiter), True, black)
        text2 = font.render(d+d+d, True, black)
        text3 = font.render('2', True, black)
        surface.blit(text, (i-8, 560))
        surface.blit(text2, (i-10, 560))
        surface.blit(text3, (i-6, 580))

    for i in range(550, 801, 120):
        text = font.render(next(my_iter), True, black)
        surface.blit(text, (i, 560))
     
def sinandcostext():
    font = pygame.font.SysFont('times new roman', 25, False, False)
    sin_text = font.render('sin x', True, black)
    cos_text = font.render('cos x', True, black)
    surface.blit(sin_text, (540, 45))
    surface.blit(cos_text, (535, 75))
    pygame.draw.line(surface, red, (597, 60), (640, 60), 1)
    for x in range(597, 642, 6):
        pygame.draw.line(surface, blue, (x, 93), (x+2, 93), 1)

done = True
while done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False
    surface.fill(white)

    rectangle()
    verticallines()
    horizontallines()
    dividerofx()
    dividerofy()
    singraph()
    cosgraph()
    numsvertical()
    numshorizontal()
    sinandcostext()

    pygame.display.update()
pygame.quit()
