import pygame
import random
#initializing pygame instance
pygame.init()
#for decreasing the snake spped
clock = pygame.time.Clock()
#setting up the game window
window_width=500 #(0,790)
window_height=500

#module #function #function
window=pygame.display.set_mode((window_width,window_height))

#caption for the window
pygame.display.set_caption("Snake Game")

white=(255,255,255)
black=(0,0,0)
red=(255,0,0)

game_over=False
score=0
x=5
x1=window_width//2
y1=window_height//2

x1_change=0
y1_change=0

length_of_snake=1
snake_body=[]

rand_x=round(random.randrange(0,window_width-10) / 10)*10.0 #food will only be on 0,10,20... so 137 div by 10 ,13 make it to 130  
# rand_x = random.randrange(0, window_width, 10)
rand_y=round(random.randrange(0,window_height-10) / 10)*10.0
while not game_over:
    #event in game (click)
    for event in pygame.event.get():
        if(event.type==pygame.QUIT):
            game_over=True
        #check for arrow key pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                #400-10(width of box)
                x1_change=-10
                y1_change=0
            elif event.key==pygame.K_RIGHT:
                x1_change=10
                y1_change=0
            elif event.key==pygame.K_UP:
                x1_change=0
                y1_change=-10
            elif event.key==pygame.K_DOWN:
                x1_change=0
                y1_change=10
    x1=x1+x1_change
    y1=y1+y1_change

    #boundary conditions
    if x1>=window_width or x1<0 or y1>=window_height or y1<0:
        game_over=True
    window.fill(black)

    snake_head=[]
    snake_head.append(x1)
    snake_head.append(y1)

    snake_body.append(snake_head)

    #making snake to grow only when it eats
    if(len(snake_body)>length_of_snake):
        del snake_body[0]

    #snake hitting itself
    for segment in snake_body[:-1]:
        if segment == snake_head:
            game_over=True

    #displaying score
    font_style=pygame.font.SysFont(None,50)# #size of font
    score_text=font_style.render("score: "+str(score),True,white)#text #antialias #background
    window.blit(score_text,(10,10))#coordinates

    if(x1==rand_x and y1==rand_y):
        rand_x=round(random.randrange(0,window_width-10) / 10)*10.0
        rand_y=round(random.randrange(0,window_height-10) / 10)*10.0
        length_of_snake+=1
        score+=1

    #drawing food
    pygame.draw.rect(
        window,
        red,
        [rand_x,rand_y,10,10]
        )
    
    #drawing a snake
    #initially snake is a small rectangular box
    #pygame.draw.rect(window,white,[x1,y1,10,10]) #left #top #width #height #surface #color #position and dimentions

    for segment in snake_body:
        pygame.draw.rect(window,white,[segment[0],segment[1],10,10])
    #update display window
    pygame.display.update()
    if score % 5 == 0 and score != 0:
        x =score
    clock.tick(x) #10 frames per second(5-30)
    print(x)

