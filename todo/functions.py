import cv2
from todo.opencv1 import resimincele
from django.shortcuts import render,HttpResponse,redirect
from django.http import HttpResponseRedirect
def resimincele(adres):
 faceCascade=cv2.CascadeClassifier("todo/haarcascade_frontalface_default.xml")
 img=cv2.imread(adres)
 imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
 faces=faceCascade.detectMultiScale(imgGray,1.1,4)
 if not len(faces)==0:
  x=faces[0,0]
  y=faces[0,1]
  h=faces[0,2]
  w=faces[0,3]
  print(faces[0,0])
  img_son=cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
  cv2.imwrite(adres, img_son)
def handle_uploaded_file(f):  
    with open('media/'+f.name, 'wb+') as destination:  
        for chunk in f.chunks():  
            destination.write(chunk)
    resimincele('media/'+f.name)  
    return HttpResponse("<center><img src=media/"+f.name+"/></center>") 
    
