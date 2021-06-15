import cv2
import pygame
from pygame.locals import *
pygame.init()
screen=pygame.display.set_mode((1080,720))
fpsClock=pygame.time.Clock()
run=True
face_cascade=cv2.CascadeClassifier('fasecascade.xml')
cap = cv2.VideoCapture(0)
fps=60
font=pygame.font.SysFont('z003',30)
player_score=0
live_ball=False
winner=0

def draw_board():
    screen.fill((50,25,90))
    pygame.draw.line(screen,(255,255,255),(0,50),(1080,50))
    pygame.draw.line(screen,(255,255,255),(100,50),(100,720))
    pygame.draw.line(screen, (255, 255, 255), (980, 50), (980, 720))
def draw_text(text,font,text_color,x,y):
    img=font.render(text,True,text_color)
    screen.blit(img,(x,y))
class Board():
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.rect=Rect(self.x,self.y,100,20)

    def update(self,x,y):
        self.x = x
        self.y = y
        self.rect = Rect(self.x, self.y, 100, 20)


    def draw(self,color=(255,255,255)):
        pygame.draw.rect(screen,color,self.rect)
class ball():
    def __init__(self,x,y):
        self.reset(x,y)
    def move(self):
        if self.rect.top<50:
            self.speed_y*=-1
        if self.rect.bottom>720:
            self.winner=1
            self.speed_y*=-1
        if self.rect.colliderect(player_paddle):
            self.speed_y*=-1
        if self.rect.left<100:
            self.speed_x *= -1
        if self.rect.right >980:
            self.speed_x *= -1
        self.rect.x+=self.speed_x
        self.rect.y+=self.speed_y
        return self.winner
    def draw(self):
        pygame.draw.circle(screen,(220,80,20),(self.rect.x+self.ball_rad,self.rect.y+self.ball_rad),self.ball_rad)
    def reset(self,x,y):
        self.x=x
        self.y=y
        self.ball_rad=10
        self.rect=Rect(self.x,self.y,self.ball_rad*2,self.ball_rad*2)
        self.speed_x=-10
        self.speed_y=10
        self.winner=0
#CREATE OBJECTS
player_paddle=Board(20,30)
football=ball(300,100)


while run:
    fpsClock.tick(fps)


    # OPENCV PART
    _, frame = cap.read()
    frame = cv2.resize(frame, (1080, 720))
    
    frame = cv2.flip(frame, 1)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    for (x, y, w, h) in faces:
        cv2.rectangle(gray, (x, y), (x + w, y + h), (255, 0, 0), 3)

    draw_board()
    draw_text("PLAYER SCORE:" + str(player_score), font,(255,255,255), 640 - 200, 25)
    player_paddle.update(x,680)
    player_paddle.draw()

    if live_ball==True:
        winner=football.move()
        if winner==0:
            player_paddle.update(x,y)
            football.draw()
        else:
            live_ball=False
            if winner==1:
                player_score+=-1
    #promopt player instructiona
    if live_ball==False:
        if winner==0:
            draw_text("CLICK ANYWHERE TO START",font,(220,80,20),390,340)
        if winner==1:
            draw_text("YOU LOST", font, (220, 80, 20), 390, 340)

    #event handler
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
        if event.type==pygame.MOUSEBUTTONDOWN and live_ball==False:
            live_ball=True
            football.reset(300,100)


    pygame.display.update()
    if cv2.waitKey(1)==ord('q'):
        break