import pygame
pygame.init()
# WITHOUT MINIMAX :PLAYER vs PLAYER
#ALWAYS X GOES FIRST

screen=pygame.display.set_mode([300,300])
pygame.display.set_caption("TICTACTOE")
running =True
screen.fill(pygame.Color("Blue"))
clicked=False
mark=[]
player=1
pos=[]
winner=0
gameover=False
font=pygame.font.SysFont(None,40)



#DRAW THE BOARD
def drawbackground():
 for i in range(1,3):
    pygame.draw.line(screen,(180,250,255),(0,i*100),(300,i*100),4)
    pygame.draw.line(screen, (180, 250, 255), (i*100,0),(i*100,300),4)
#####################################
#CREATE MARKERS
def marker():
     for x in range(3):
         row=[0]*3
         mark.append(row)
####################################
#DRAW MARKERS
def drawmark():
    xpos=0
    for x in mark:
        ypos=0
        for y in x:
            if y==1:
                pygame.draw.line(screen,(255,0,0),(xpos*100+15,ypos*100+15),(xpos*100+85,ypos*100+85),10)
                pygame.draw.line(screen, (255, 0, 0), (xpos * 100 + 85, ypos * 100 + 15),(xpos * 100 + 15, ypos * 100 + 85), 10)
            if y==-1:
                pygame.draw.circle(screen,(0,255,0),(xpos*100+50,ypos*100+50),38,5)
            ypos+=1
        xpos+=1
############################################
def check():

    global winner
    global gameover
    ypos=0
    for x in mark:

        if sum(x)==3:



            winner=1
            gameover=True

        if sum(x) == -3:
                winner = 2
                gameover = True
        if mark[0][ypos]+mark[1][ypos]+mark[2][ypos]==3:
            winner=1
            gameover=True
        if mark[0][ypos]+mark[1][ypos]+mark[2][ypos]==-3:
            winner=2
            gameover=True
        ypos+=1
    if mark[0][0]+mark[1][1]+mark[2][2]==3 or mark[0][2]+mark[1][1]+mark[2][0]==3:
        winner=1
        gameover=True
    if mark[0][0]+mark[1][1]+mark[2][2]==-3 or mark[0][2]+mark[1][1]+mark[2][0]==-3:
        winner=2
        gameover=True
##############################################
def checkwinner(winner):
    if winner==1:
      win_text="Player "+"X"+" wins!"
    elif winner==2:
      win_text="Player "+"O"+" wins!"

    win_img=font.render(win_text,True,(0,255,0))
    pygame.draw.rect(screen,(120,130,0),(80,120,200,40))
    screen.blit(win_img,(80,130))

marker()
while running:
    drawbackground()
    drawmark()

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running =False

        if gameover==False:
         if event.type==pygame.MOUSEBUTTONDOWN and clicked==False:
            clicked=True
         if event .type==pygame.MOUSEBUTTONDOWN and clicked ==True:
            clicked=False
            pos=pygame.mouse.get_pos()
            cellx=pos[0]
            celly=pos[1]
            if mark[cellx//100][celly//100]==0:
                mark[cellx // 100][celly // 100]=player
                player=player*-1
                check()
    if gameover==True:
        checkwinner(winner)
    pygame.display.update()





