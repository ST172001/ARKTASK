import cv2
img=cv2.imread('tree.mp3.png')
i=0
j=0
array=[]
while(j< 390):
    while(i<390):
       b=img[j][i][0]

       array.append(b)
       i+=1
    i=0
    j+=1
file=open("song.bin","wb")
file.write(bytearray(array))







