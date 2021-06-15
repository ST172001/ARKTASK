import cv2
maze=cv2.imread('maze.png')

i=0
j=0

while i<457:
    while j<180:
        b=maze[j,i]
        if b[0]==230:
            maze[j,i]=(0,0,0)
        else:
            maze[j,i]=(255,255,255)
        j+=1
    j=0
    i+=1

cv2.imshow("mazw",maze)
cv2.imwrite("mazelevel.png",maze)
cv2.waitKey(0)