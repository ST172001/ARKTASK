import cv2
import numpy as np
markelon=cv2.imread('zucky_elon.png')

mark=cv2.imread('mark.png')
print(mark[0,0])
i=0
j=0
while(i<1440):
    while(j<977):
        b=markelon[j,i]
        if b[0]==44 and b[1]==88 and b[2]==95:
             print(j,i)
        j+=1
    j=0
    i+=1


if cv2.waitKey(0)==ord('q'):
    cv2.destroyWindows()


