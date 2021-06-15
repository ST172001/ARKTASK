import cv2
import numpy as np
img=cv2.imread('Level1.png',0)
i=0
j=0
while(i<177):
    while(j<177):
        print(chr(img[i,j]))
        j+=1
    j=0
    i+=1


