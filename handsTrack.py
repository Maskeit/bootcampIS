import cv2
import time
from cvzone.HandTrackingModule import HandDetector

cap = cv2.VideoCapture(1)
detector = HandDetector(detectionCon= 0.8, maxHands=2)
while True:
    success, img = cap.read()

    hands, img = detector.findHands(img)# with draw ,flipType=False
    #hands = detector.findHands(img, draw=False) # No Draw

    if hands:
        hand1 = hands[0]
        lmList1 = hand1["lmList"] # list of 21 landmarks points
        bbox1 = hand1["bbox"] #bounding box info x, y, w, h
        centerPoint1 = hand1["center"]# center of the hand cx, cy
        handType1 = hand1["type"]#hand type left or right
        # finger1_8 = hand1[8]

        #print(len(lmList1), lmList1)
        #print(bbox1)
        #print(centerPoint1)
        #print(handType1)
        fingers1 = detector.fingersUp(hand1)
        #length, info, img = detector.findDistance(lmList1[4][:2], lmList1[20][:2], img) #with draw del punto 4 al 20 de los dedos del landmark

        if len(hands) == 2: # usually left
            hand2 = hands[1]
            lmList2 = hand2["lmList"]  # list of 21 landmarks points
            bbox2 = hand2["bbox"]  # bounding box info x, y, w, h
            centerPoint2 = hand2["center"]  # center of the hand cx, cy
            handType2 = hand2["type"]  # hand type left or right
            # finger2_8 = hand2[8]

            fingers2 = detector.fingersUp(hand2)
            #print(fingers1, fingers2) # imprime como array los valores para 1 up 2 down

            # length, info, img = detector.findDistance(lmList1[8][0:2], lmList2[8][0:2], img)  # with draw
            # length, info, img = detector.findDistance(lmList1[4][0:2], lmList2[4][0:2], img)  # with draw
            # length, info, img = detector.findDistance(lmList1[8][0:2], lmList1[4][0:2], img)  # with draw
            # length, info, img = detector.findDistance(lmList2[8][0:2], lmList2[4][0:2], img)  # with draw
            length, info, img = detector.findDistance(centerPoint1, centerPoint2, img)  # with draw
    cv2.imshow("image", img)
    k = cv2.waitKey(1)
    if k == 27:
        break