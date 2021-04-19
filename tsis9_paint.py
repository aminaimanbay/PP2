import pygame
pygame.init()

screen=pygame.display.set_mode([1200,600])
screen.fill((255,255,255))
keep_going=True

WHITE=(255,255,255)
RED=(255,0,0)
YELLOW=(255,255,0)
GREEN=(0,255,0)
BLUE=(0,0,255)
BLACK=(0,0,0)
PINK=(255,0,255)


pygame.draw.rect(screen,RED,(0,50,20,20))
pygame.draw.rect(screen,YELLOW,(0,70,20,20))
pygame.draw.rect(screen,GREEN,(20,50,20,20))
pygame.draw.rect(screen,BLUE,(20,70,20,20))
pygame.draw.rect(screen,BLACK,(0,90,20,20))
pygame.draw.rect(screen,PINK,(20,90,20,20))
eraser = pygame.transform.scale(pygame.image.load("eraser.png"), (40, 40))
circle = pygame.transform.scale(pygame.image.load("circle.png"), (40, 40))
rect=pygame.transform.scale(pygame.image.load("rect.png"),(40,40))
brush=pygame.transform.scale(pygame.image.load("brush.png"),(40,40))
screen.blit(eraser, [0,110])
screen.blit(circle, [0,150])
screen.blit(rect, [0,190])
screen.blit(brush, [0,230])

mousedn=False
color=BLACK
radius=6
case= 0

pstn=(0,0)
cur = (0,0)


while keep_going:

    for event in pygame.event.get():
        if event.type== pygame.KEYDOWN:
            if event.key == pygame.K_s :
                pygame.image.save(screen,'image.png')
            elif event.key == pygame.K_l:
                screen=pygame.image.load('image.png')
        if event.type==pygame.QUIT:
            keep_going=False
        if event.type==pygame.MOUSEBUTTONDOWN:
            mousedn=True
            pstn = pygame.mouse.get_pos()
            if pstn[0] < 20 and pstn[1] < 70 and pstn[1] > 50:
                color= RED
            elif pstn[0] < 40 and pstn[0] > 20 and pstn[1] < 70 and pstn[1] > 50:
                color= GREEN
            elif pstn[0] < 20 and pstn[1] < 90 and pstn[1] > 70:
                color= YELLOW
            elif pstn[0] < 40 and pstn[0] > 20 and pstn[1] < 90 and pstn[1] > 70:
                color= BLUE
            elif pstn[0] < 20 and pstn[1] < 110 and pstn[1] > 90:
                color= BLACK
            elif pstn[0] < 40 and pstn[0] > 20 and pstn[1] < 110 and pstn[1] > 90:
                color= PINK
            elif pstn[0] < 40 and pstn[1] < 150 and pstn[1] > 110:
                color = WHITE
            elif pstn[0] < 40 and pstn[1] < 190 and pstn[1] > 150:
                case= 1
                radius= 43
            elif pstn[0] < 40 and pstn[1] < 230 and pstn[1] > 190:
                case= 2
            elif pstn[0] < 40 and pstn[1] < 270 and pstn[1] > 230:
                case=0
                radius=6

        if event.type == pygame.MOUSEMOTION and mousedn == True:
            #pstn=cur
            cur = pygame.mouse.get_pos()

        if event.type==pygame.MOUSEBUTTONUP:
            #pstn = None
            mousedn=False

        if mousedn:
            pstn = pygame.mouse.get_pos()
            x=abs(cur[0]-pstn[0])
            y=abs(cur[1]-pstn[1])
            if pstn[0]>60:
                if case==1 :
                    pygame.draw.circle(screen,color,pstn,radius)
                elif case==2 :
                    pygame.draw.rect(screen, color, [pstn[0], pstn[1], x, y ]  )
                elif case==0 :
                    pygame.draw.circle(screen,color,pstn,6)
        pygame.display.update()


pygame.display.flip()
        

pygame.quit()