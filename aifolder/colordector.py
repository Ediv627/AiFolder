import cv2
import numpy as np

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1200)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

while True:
    vid, frame = cap.read()
    
    hsv_frames = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    height, width, _ = frame.shape
    cx = int(width / 2)
    cy = int(height / 2)
    pixel_centre = hsv_frames[cy, cx]
   
    hue_value = pixel_centre[0]
    color = "Undefined"
    if hue_value < 5:
        color = "RED"
    elif hue_value < 22:
        color = "Orange"
    elif hue_value < 33:
        color = "Yellow"
    elif hue_value < 70:
        color = "Green"
    elif hue_value < 131:
        color = "Blue"
    elif hue_value < 167:
        color = "Violet"
    else:
        color = "Other Color"

    # اقلب الإطار أولاً
    flips = cv2.flip(frame, 1)

    # ضع النص على الإطار المقلوب بعد عملية القلب
    cv2.putText(flips, color, (10, 50), 0, 2, (0, 255, 0), 3)
    
    print(pixel_centre)
    cv2.circle(flips, (cx, cy), 5, (255, 0, 0), 3)

    # عرض الإطار المقلوب
    cv2.imshow("Color Detection", flips)
    
    end = cv2.waitKey(1)
    if end == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()