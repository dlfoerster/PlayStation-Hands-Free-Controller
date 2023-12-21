import cv2
import time
import mediapipe as mp
import enum
import os
import math
import HandTrackingModule as htm
import sys
import pyautogui as pg

###########################
    # Hand detector vars
detector = htm.HandDetector(detectionConfidence=0.5)
landmarks = htm.HandLandmark
wCam, hCam = 2000, 1250
###########################

def in_button(lmList: list, p1: tuple, p2: tuple) -> bool:
    if (lmList[landmarks.THUMB_JOINT_LOWER][1] > lmList[landmarks.PINKY_FINGER_JOINT_LOWER][1]):
        return lmList[landmarks.INDEX_FINGER_TIP][1] > p1[0] and lmList[landmarks.INDEX_FINGER_TIP][1] < p2[0]\
            and lmList[landmarks.INDEX_FINGER_JOINT_UPPER][1] > p1[0] and lmList[landmarks.INDEX_FINGER_JOINT_UPPER][1] < p2[0]\
            and lmList[landmarks.MIDDLE_FINGER_TIP][1] > p1[0] and lmList[landmarks.MIDDLE_FINGER_TIP][1] < p2[0]\
            and lmList[landmarks.MIDDLE_FINGER_JOINT_UPPER][1] > p1[0] and lmList[landmarks.MIDDLE_FINGER_JOINT_UPPER][1] < p2[0]\
            and lmList[landmarks.INDEX_FINGER_TIP][2] > p1[1] and lmList[landmarks.INDEX_FINGER_TIP][2] < p2[1]\
            and lmList[landmarks.INDEX_FINGER_JOINT_UPPER][2] > p1[1] and lmList[landmarks.INDEX_FINGER_JOINT_UPPER][2] < p2[1]\
            and lmList[landmarks.MIDDLE_FINGER_TIP][2] > p1[1] and lmList[landmarks.MIDDLE_FINGER_TIP][2] < p2[1]\
            and lmList[landmarks.MIDDLE_FINGER_JOINT_UPPER][2] > p1[1] and lmList[landmarks.MIDDLE_FINGER_JOINT_UPPER][2] < p2[1]\
            and lmList[landmarks.THUMB_TIP][1] < lmList[landmarks.THUMB_JOINT_UPPER][1]
    else:
            return lmList[landmarks.INDEX_FINGER_TIP][1] > p1[0] and lmList[landmarks.INDEX_FINGER_TIP][1] < p2[0]\
            and lmList[landmarks.INDEX_FINGER_JOINT_UPPER][1] > p1[0] and lmList[landmarks.INDEX_FINGER_JOINT_UPPER][1] < p2[0]\
            and lmList[landmarks.MIDDLE_FINGER_TIP][1] > p1[0] and lmList[landmarks.MIDDLE_FINGER_TIP][1] < p2[0]\
            and lmList[landmarks.MIDDLE_FINGER_JOINT_UPPER][1] > p1[0] and lmList[landmarks.MIDDLE_FINGER_JOINT_UPPER][1] < p2[0]\
            and lmList[landmarks.INDEX_FINGER_TIP][2] > p1[1] and lmList[landmarks.INDEX_FINGER_TIP][2] < p2[1]\
            and lmList[landmarks.INDEX_FINGER_JOINT_UPPER][2] > p1[1] and lmList[landmarks.INDEX_FINGER_JOINT_UPPER][2] < p2[1]\
            and lmList[landmarks.MIDDLE_FINGER_TIP][2] > p1[1] and lmList[landmarks.MIDDLE_FINGER_TIP][2] < p2[1]\
            and lmList[landmarks.MIDDLE_FINGER_JOINT_UPPER][2] > p1[1] and lmList[landmarks.MIDDLE_FINGER_JOINT_UPPER][2] < p2[1]\
            and lmList[landmarks.THUMB_TIP][1] > lmList[landmarks.THUMB_JOINT_UPPER][1]
    
def main():
    # Webcam perameters
    cap = cv2.VideoCapture(0)
    cap.set(3, wCam)
    cap.set(4, hCam)

    # Hand detector vars
    detector = htm.HandDetector(detectionConfidence=0.5)
    landmarks = htm.HandLandmark

    while True:
    # Read camera image and add number overlay
        success, img = cap.read()
    # Find hands and position of landmakrs
        img = detector.find_hands(img, True)
        lmList = detector.find_position(img)
        
        # LEFT
        if lmList:
            if (lmList[landmarks.PINKY_FINGER_TIP][1] < 150 or lmList[landmarks.THUMB_TIP][1])\
                and lmList[landmarks.RING_FINGER_TIP][1] < 150 \
                and lmList[landmarks.MIDDLE_FINGER_TIP][1] < 150 and lmList[landmarks.INDEX_FINGER_TIP][1] < 150\
                    and lmList[landmarks.MIDDLE_FINGER_TIP][2] > 150 and lmList[landmarks.MIDDLE_FINGER_TIP][2] < 600:
                cv2.rectangle(img,(0,600),(150, 150), (124,52,127), cv2.FILLED)
                pg.press('LEFT')
            else:
                cv2.rectangle(img,(0,600),(150, 150), (248, 105, 255), cv2.FILLED)    
        else:    
            cv2.rectangle(img,(0,600),(150, 150), (248, 105, 255), cv2.FILLED)

        # RIGHT
        if lmList:
            if (lmList[landmarks.THUMB_TIP][1] > 1150 or lmList[landmarks.PINKY_FINGER_TIP][1] > 1150) and lmList[landmarks.RING_FINGER_TIP][1] > 1150 \
                and lmList[landmarks.MIDDLE_FINGER_TIP][1] > 1150 and lmList[landmarks.INDEX_FINGER_TIP][1] > 1150\
                    and lmList[landmarks.MIDDLE_FINGER_TIP][2] > 150 and lmList[landmarks.MIDDLE_FINGER_TIP][2] < 600:
                cv2.rectangle(img,(1100,600),(1440, 150), (51,51,127), cv2.FILLED)
                pg.press('RIGHT')
            else:
                cv2.rectangle(img,(1100,600),(1440, 150), (102, 102, 255), cv2.FILLED)
        else:
            cv2.rectangle(img,(1100,600),(1440, 150), (102, 102, 255), cv2.FILLED)

        # UP
        if lmList:
            if lmList[landmarks.INDEX_FINGER_TIP][2] < 150 and lmList[landmarks.MIDDLE_FINGER_TIP][2] < 150\
                and lmList[landmarks.PINKY_FINGER_TIP][2] < 150 and lmList[landmarks.RING_FINGER_TIP][2] < 150\
                    and lmList[landmarks.INDEX_FINGER_TIP][1] > 150 and lmList[landmarks.PINKY_FINGER_TIP][1] < 1100:
                cv2.rectangle(img,(150,0),(1100, 150), (80, 113, 32), cv2.FILLED)
                pg.press('UP')
            else:
                cv2.rectangle(img,(150,0),(1100, 150), (160, 226, 64), cv2.FILLED)
        else:
            cv2.rectangle(img,(150,0),(1100, 150), (160, 226, 64), cv2.FILLED)

        # DOWN
        if lmList:
            if lmList[landmarks.INDEX_FINGER_TIP][2] > 600 and lmList[landmarks.MIDDLE_FINGER_TIP][2] > 600\
                and lmList[landmarks.PINKY_FINGER_TIP][2] > 600 and lmList[landmarks.RING_FINGER_TIP][2] > 600\
                    and lmList[landmarks.THUMB_TIP][1] > 150 and lmList[landmarks.PINKY_FINGER_TIP][1] < 1100:
                cv2.rectangle(img,(150,600),(1100, 750), (116, 89, 62), cv2.FILLED)
                pg.press('DOWN')
            else:
                cv2.rectangle(img,(150,600),(1100, 750), (232, 178, 124), cv2.FILLED)
        else:
            cv2.rectangle(img,(150,600),(1100, 750), (232, 178, 124), cv2.FILLED)

        # CROSS
        if lmList:
            if in_button(lmList, (150,150),(250,250)):
                cv2.rectangle(img,(150,150),(250,250),(63,63,63),cv2.FILLED)
                pg.press('ENTER')
            else:
                cv2.rectangle(img,(150,150),(250,250),(0,0,0),cv2.FILLED)
        else:
            cv2.rectangle(img,(150,150),(250,250),(0,0,0),cv2.FILLED)
        cv2.line(img,(175,175),(225,225),(232,178,124),2)
        cv2.line(img,(175,225),(225,175),(232,178,124),2)

        # CIRCLE
        if lmList:
            if in_button(lmList,(1000,150),(1100,250)):
                cv2.rectangle(img,(1000,150),(1100,250),(63,63,63),cv2.FILLED)
                pg.press('ESCAPE')
            else:
                cv2.rectangle(img,(1000,150),(1100,250),(0,0,0),cv2.FILLED)    
        else:
            cv2.rectangle(img,(1000,150),(1100,250),(0,0,0),cv2.FILLED)
        cv2.circle(img,(1050,200), 25, (102, 102, 255),2)

        # Buttons
        cv2.putText(img, "LEFT", (25, 375), cv2.FONT_ITALIC, 1, (0,0,0), 2)
        cv2.putText(img, "RIGHT", (1150, 375), cv2.FONT_ITALIC, 1, (0,0,0), 2)
        cv2.putText(img, "UP", (600, 95), cv2.FONT_ITALIC, 1, (0,0,0), 2)
        cv2.putText(img, "DOWN", (580, 675), cv2.FONT_ITALIC, 1, (0,0,0), 2)

    # Display image
        cv2.imshow("Image", img)
        cv2.waitKey(1)

if __name__ == "__main__":
    main()