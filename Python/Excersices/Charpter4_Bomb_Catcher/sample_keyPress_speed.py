import sys,random,time,pygame
from pygame.locals import *
def print_text(font,x,y,text,color=(255,255,255)):
    imgText = font.render(text,True,color)
    screen.blit(imgText,(x,y))

#main program begins
pygame.init()
screen = pygame.display.set_mode((600,500))
pygame.display.set_caption("Keyboard Demo")
font1 = pygame.font.Font(None,24)
font2 = pygame.font.Font(None,200)
white = 255,255,255
yellow = 255,255,0

key_flag = False
correct_answer = 97 #"a"
seconds = 11
score = 0
clock_start = 0
game_over = True

#repeating loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        elif event.type == KEYDOWN:
            key_flag = True
        elif event.type == KEYUP:
            key_flag = False
    
    keys = pygame.key.get_pressed()
    if keys[K_ESCAPE]:
        sys.exit()

    if keys[K_RETURN]:
        if game_over:
            game_over = False
            score = 0
            seconds = 11
    
    clock_start = time.clock()
    current = time.clock() - clock_start
    speed = score * 6
    if seconds - current < 0:
        game_over = True
    elif current <= 10:
        if keys[correct_answer]:
            correct_answer = random.randint(97,122)
            score += 1

#clear the screen



