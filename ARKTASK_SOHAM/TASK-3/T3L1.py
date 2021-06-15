import cv2
import numpy as np
img=cv2.imread('Level1.png')
newimage1=np.zeros((200,150,3),dtype='uint8')
newimage2=np.zeros((200,150,3),dtype='uint8')
newimage3=np.zeros((200,150,3),dtype='uint8')
i=6
j=94
k=0
m=0
n=0
bluearray=[]
greenarray=[]
redarray=[]
while i<177:
    if k>=30000:
        break
    while j<177:
      if k == 30000:
            break
      b =img[i, j]

      bluearray.append(b[0])
      greenarray.append(b[1])
      redarray.append(b[2])
      j+=1
      k+=1
    i+=1
    j=0
print(len(bluearray))
m=0
n=0
c=0
while m<200:
    while n<150:
        newimage1[m,n]=(bluearray[c],0,0)
        c=c+1
        n=n+1
    n=0
    m=m+1

a=0
b=0
d=0
while a<200:
    while b<150:
        newimage2[a,b]=(0,greenarray[d],0)
        d=d+1
        b=b+1
    a=a+1
    b=0
m = 0
n = 0
c = 0
while m < 200:
    while n < 150:
        newimage3[m,n] = (0, 0, redarray[c])
        c = c + 1
        n = n + 1
    n = 0
    m = m + 1
finalimage=newimage1+newimage2+newimage3
cv2.imshow("nummpy",finalimage)
cv2.imwrite("mark.png",finalimage)
print(finalimage[0,0])
if cv2.waitKey(0)==ord('q'):
    cv2.destroyWindow()
