import cv2
import numpy as np
import face_recognition
imgUma=face_recognition.load_image_file('ImageBasics/UmaS.JPG')
imgUma=cv2.cvtColor(imgUma, cv2.COLOR_BGR2RGB)

imgTest=face_recognition.load_image_file('ImageBasics/UmaTest.JPG')
imgTest=cv2.cvtColor(imgTest, cv2.COLOR_BGR2RGB)

faceLoc=face_recognition.face_locations(imgUma)[0]
encodeUma=face_recognition.face_encodings(imgUma)[0]
cv2.rectangle(imgUma,(faceLoc[3],faceLoc[0]),(faceLoc[1],faceLoc[2]),(255,0,255),2)

faceLocTest=face_recognition.face_locations(imgTest)[0]
encodeTest=face_recognition.face_encodings(imgTest)[0]
cv2.rectangle(imgTest,(faceLocTest[3],faceLocTest[0]),(faceLocTest[1],faceLocTest[2]),(255,0,255),2)

results=face_recognition.compare_faces([encodeUma],encodeTest)
faceDis=face_recognition.face_distance([encodeUma],encodeTest)
print(results,faceDis)

cv2.putText(imgTest,f'{results} {faceDis}',(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)

print(faceLoc)





cv2.imshow('Uma Shree',imgUma)
cv2.imshow('Uma Shree Test',imgTest)

cv2.waitKey(0)
