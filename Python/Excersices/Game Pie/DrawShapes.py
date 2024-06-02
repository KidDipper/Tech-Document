import math
import pygame,sys
from pygame.locals import *
pygame.init()

screen = pygame.display.set_mode((600,500))
pygame.display.set_caption("Drawing shapes")

pos_x = 300
pos_y = 200
vel_x = 2
vel_y = 1

myFont= pygame.font.Font(None,60)
textImage = myFont.render("Hello Pygame",True,(255,255,255))

while True:
    for event in pygame.event.get():
        if event.type in (QUIT,MOUSEBUTTONDOWN):
            sys.exit()
    screen.fill((0,0,200))

    #Show the font
    screen.blit(textImage,(100,100))

    #draw a circle
    colorCircle = 255,255,0
    positionCircle = 300,250
    radius = 100
    widthCircle = 10
    pygame.draw.circle(screen,colorCircle,positionCircle,radius,widthCircle)
    
    #move the rectangle
    pos_x += vel_x
    pos_y += vel_y

    #keep the rectangle in the screen
    if pos_x > 500 or pos_x <0:
        vel_x = -vel_x
    if pos_y > 400 or pos_y <0:
        vel_y = -vel_y
    
    #draw the rectangle
    color = 255,255,0
    width = 0
    pos = pos_x,pos_y,100,100
    pygame.draw.rect(screen,color,pos,width)


    #draw the line
    colorLine = 100,255,200
    widthLine = 8
    pygame.draw.line(screen,colorLine,(100,100),(500,400),widthLine)
    
    #draw the arc
    colorArc = 255,0,255
    positionArc = 200,150,200,200
    start_angle = math.radians(0)
    end_angle = math.radians(180)
    widthArc = 5
    pygame.draw.arc(screen,colorArc,positionArc,start_angle,end_angle,widthArc)

    pygame.display.update()





