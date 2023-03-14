from cvzone.SerialModule import SerialObject
import time

mySerial = SerialObject("COM5", 9600, 1) #conectando arduino
while True:
    mySerial.sendData([1, 1, 1, 1, 1])
    time.sleep(2)
    mySerial.sendData([0, 0, 0, 0, 0])
    time.sleep(2)