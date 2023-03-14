import cv2
#from cvzone.HandTrackingModule import HandDetector
import cvzone
from time import sleep
from cvzone.HandTrackingModule import HandDetector
import numpy as np
import cvzone
from pynput.keyboard import Controller

cap = cv2.VideoCapture(1)
cap.set(3, 1280)
cap.set(4, 720)

detector = HandDetector(detectionCon=0.8)

keys = [["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"],
        ["A", "S", "D", "F", "G", "H", "J", "K", "L", ";"],
        ["Z", "X", "C", "V", "B", "N", "M", ",", ".", "/"],
        [" "]]
finaText = ""

keyboard = Controller()

def drawAll(img, buttonList):

    for button in buttonList:
        x, y = button.pos
        w, h = button.size
        cvzone.cornerRect(img,(button.pos[0], button.pos[1], button.size[0], button.size[1]), 20, rt=0) #bordes verdes de los rectangulos
        cv2.rectangle(img, button.pos, (x + w, y + h), (155, 155, 155), cv2.FILLED)
        cv2.putText(img, button.text, (x + 20, y + 65),
                    cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 4)
    return img

class Button():
    def __init__(self, pos, text, size=[85,85]):
        self.pos = pos
        self.size = size
        self.text = text

#    def draw(self, img):

        # return img

buttonList = []
for i in range(len(keys)):
    for j, key in enumerate(keys[i]):
        buttonList.append(Button([100 * j + 50, 100 * i + 50], key))

# myButton = Button([100, 100],"Q")
# myButton = Button([100, 100],"Q")

while True:
    success, img = cap.read()
    hands, img = detector.findHands(img)
    #lmList, bbox = detector.findPosition(img)

    if hands and len(hands) == 2:
        hand1 = hands[0]
        lmList = hand1["lmList"]
        img = drawAll(img, buttonList)

        if lmList:
            for button in buttonList:
                x,y = button.pos
                w,h = button.size

                if x < lmList[8][0] < x+w and y<lmList[8][1]< y + h:
                    cv2.rectangle(img, button.pos, (x + w, y + h), (175, 0, 0), cv2.FILLED)
                    cv2.putText(img, button.text, (x + 20, y + 65),
                                cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 4)
                    #l, _, _ = detector.findDistance(8, 12, img)#when you want to ignore something in python you can write an underscore
                    length, info, img = detector.findDistance(lmList[8][0:2],lmList[12][0:2], img)
                    length2, info, img = detector.findDistance(lmList[4][0:2], lmList[12][0:2], img)

                    if length2<30:
                        keyboard.press(button.text)
                        cv2.rectangle(img, button.pos, (x + w, y + h), (0, 255, 0), cv2.FILLED)
                        cv2.putText(img, button.text, (x + 20, y + 65),
                                    cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 4)
                        finaText += button.text
                        sleep(0.05)

    cv2.rectangle(img, (50, 350), (700, 450), (155, 155, 155), cv2.FILLED)
    cv2.putText(img, finaText, (60, 430),
                cv2.FONT_HERSHEY_PLAIN, 5, (255, 255, 255), 5)


    cv2.imshow("Image", img)
    k = cv2.waitKey(1)
    if k == 27:
        break

