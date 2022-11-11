#sign language
import cv2
import numpy as np
import HandTrackingModule as ht

cap = cv2.VideoCapture(0 , cv2.CAP_DSHOW)
cap.set(3 , 800)
cap.set(4 , 700)

detector  = ht.HandDetector()

def getNumber(fingers):
    s = ""
    for i in fingers:
        s += str(i)
    
    if(s == "00011"):
        return "OKAY"
    elif(s == "01000"):
        return "OUT"
    elif(s == "01100"):
        return "VICTORY"
    elif(s== "10000"):
        return "FINE"
    elif(s== "11111"):
        return "STOP"
    elif(s== "01001"):
        return "ROCK"    
    
while(True):
    _ , img = cap.read()
    
    img = cv2.flip(img , 1)
    # Bilateral shift
    
    img = detector.findHands(img)

    idList = detector.findPosition(img , False)
    tipId = [4 , 8 , 12 , 16 , 20]

    if(len(idList)!=0):
        fingers = []
        if(idList[tipId[0]][1] < idList[tipId[0]-2][1]):
            fingers.append(1)
        else:
            fingers.append(0)
        
        for id in range(1 , len(tipId)):
            if(idList[tipId[id]][2] < idList[tipId[id]-2][2]):
                fingers.append(1)
            else:
                fingers.append(0) 

        cv2.putText(img , str(getNumber(fingers)) , (45 , 375) , cv2.FONT_HERSHEY_PLAIN , 10 , (255 , 0 , 255) , 20)
    
    cv2.imshow("Result" , img)
    cv2.waitKey(1)
