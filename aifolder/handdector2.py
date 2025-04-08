import cv2
import cvzone
from cvzone.HandTrackingModule import HandDetector
#import serial

#aurduino = serial.Serial("com4",9600)
cap = cv2.VideoCapture(0)
detector = HandDetector(maxHands = 1)
while True:
    success,img = cap.read()
    hands,img = detector.findHands(img)
    if hands:
        hand = hands[0]
        
        fingers = detector.fingersUp(hand)
       # print(fingers)
        if all(finger == 1 for finger in fingers):
            x = 1
            print(x)
        elif fingers[1] == 1 and all(finger == 0 for i ,finger in enumerate(fingers) if i != 1):
            x = 2
            print(x)
        else:
            x = 0
            print(x)
        #aurduino.write(str(x).encode())
        
    cv2.imshow("ai-eye",img)
    if cv2.waitKey(1) == ord("q"):
        break