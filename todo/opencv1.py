import cv2 # default cascade
def resimincele(adres):
 faceCascade=cv2.CascadeClassifier("todo/haarcascade_frontalface_default.xml")
 img=cv2.imread(adres)
 imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
 faces=faceCascade.detectMultiScale(imgGray,1.1,4)
 x=faces[0,0]
 y=faces[0,1]
 h=faces[0,2]
 w=faces[0,3]
 print(faces[0,0])
 img_son=cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
 cv2.imwrite(adres, img_son)



