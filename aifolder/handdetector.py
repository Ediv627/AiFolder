import cv2

import cvzone
from cvzone.HandTrackingModule import HandDetector

detector = HandDetector(maxHands=1)

video = cv2.VideoCapture(0)

while True:
    vid , frame = video.read()
    hands, frame = detector.findHands(frame)
    if hands:
        hand = hands[0]
        fingers = detector.fingersUp(hand)
        if all(finger == 1 for finger in fingers):
            print(fingers)
        else:
           print(fingers)
        


    #flipped = cv2.flip(frame,1)
    cv2.imshow("ai",frame)
    if cv2.waitKey(1) == ord("q") :
        break