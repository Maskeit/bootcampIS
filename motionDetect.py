import cv2
from cvzone.PoseModule import PoseDetector
import mediapipe as mp

detector = PoseDetector()
cap = cv2.VideoCapture(1)

# bestImg = cv2.ColorTrans(cap/255)^255
while True:
    success, img = cap.read()

    img = detector.findPose(img)
    imlist, bbox = detector.findPosition(img)
    flip1= cv2.flip(img,1)
    cv2.imshow("Myresult", flip1)

    k = cv2.waitKey(1)
    if k == 27:
        break
"""
import cv2
from cvzone.PoseModule import PoseDetector
import mediapipe as mp

detector = PoseDetector()
cap = cv2.VideoCapture(2)

#bestImg = cv2.ColorTrans(cap/255)^255
while True:
    success, img = cap.read()
    
    img = detector.findPose(img)
    imlist,bbox = detector.findPosition(img)
    cv2.imshow("Myresult", img)
    k = cv2.waitKey(1)
    if k == 27:
        break
"""
