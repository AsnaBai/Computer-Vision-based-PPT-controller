import cv2
import os
from cvzone.HandTrackingModule import HandDetector
import numpy as np

#webcam hs and ws
width, height = 1280, 720

# attaching presentation
folderPath = "Presentation"

#camera setup
cap = cv2.VideoCapture(0)
cap.set(3, width)
cap.set(4, height)

pathImages = sorted(os.listdir(folderPath), key=len)
print(pathImages)

#varibles
imgNumber = 0
hs, ws = int(120 * 1), int(213 * 1)
gestureThreshold = 600
buttonPressed = False
buttonCounter = 0
buttonDelay = 30
annotations = [[]]
annotationNumber = 0
annotationStart = False

# Hand detector
detector = HandDetector(detectionCon=0.3, maxHands=2)

while True:
    #import images
    success, img = cap.read()
    img = cv2.flip(img, 1)

    pathFullImage = os.path.join(folderPath, pathImages[imgNumber])
    imgCurrent = cv2.imread(pathFullImage)

    # Resize the presentation image to fit the screen
    h, w, _ = imgCurrent.shape
    imgCurrent = cv2.resize(imgCurrent, (width, height))

    hands, img = detector.findHands(img)
    cv2.line(img, (0, gestureThreshold), (width, gestureThreshold,), (0, 255, 0), 5)
    print(annotationNumber)

    if hands and buttonPressed is False:
        hand = hands[0]
        fingers = detector.fingersUp(hand)
        cx, cy = hand['center']
        lmList = hand['lmList']

        # constrain values for easier drawing
        xVal = int(np.interp(lmList[8][0], [0, 1280], [0, 1280]))  #  the slide width is 1280
        yVal = int(np.interp(lmList[8][1], [25, 720], [25, 720]))  #  the slide height is 720
        indexFinger = xVal, yVal



        if cy <= gestureThreshold:  #if hand is at the height of the face
            annotationStart = False
            #gesture 1 - Left
            if fingers == [1, 0, 0, 0, 0]:
                annotationStart = False
                print("Left")
                if imgNumber > 0:
                    buttonPressed = True
                    annotations = [[]]
                    annotationNumber = 0
                    imgNumber -= 1

            # gesture 2 - right
            if fingers == [0, 0, 0, 0, 1]:
                annotationStart = False
                print("Right")
                if imgNumber < len(pathImages) - 1:
                    buttonPressed = True
                    annotations = [[]]
                    annotationNumber = 0
                    imgNumber += 1

            #gesture 3- show pointer
            if fingers == [0, 1, 1, 0, 0]:
                cv2.circle(imgCurrent, indexFinger, 12, (0, 0, 255), cv2.FILLED)
                annotationStart = False

            # gesture 4- Draw  pointer
            if fingers == [0, 1, 0, 0, 0]:
                if annotationStart is False:
                    annotationStart = True
                    annotationNumber += 1
                    annotations.append([])
                cv2.circle(imgCurrent, indexFinger, 12, (0, 0, 255), cv2.FILLED)
                annotations[annotationNumber].append(indexFinger)



            else:
                annotationStart = False

            # gesture 5- erasing
            if fingers == [0, 1, 1, 1, 0]:
                if annotations:
                    if annotationNumber >= 0:
                        annotations.pop()
                    annotationNumber -= 1
                    bottonPressed = True
        else:
            annotationStart = False

    #button pressed iterations
    if buttonPressed:
        buttonCounter += 1
        if buttonCounter > buttonDelay:
            buttonCounter = 0
            buttonPressed = False

    for i, points in enumerate(annotations):
        for j in range(len(points)):
            cv2.circle(imgCurrent, points[j], 8, (0,255,255), cv2.FILLED)
            if j > 0:
                cv2.line(imgCurrent, points[j-1], points[j], (0,255,255), 3)

    #for i in range(len(annotations)):
        #for j in range(len(annotations[i])):
            #if j != 0:
                #cv2.line(imgCurrent, annotations[i][j - 1], annotations[i][j], (0, 0, 255), 12)

    # Adding webcam image on the slides
    imgSmall = cv2.resize(img, (ws, hs))
    h, w, _ = imgCurrent.shape
    x = w - ws - 10  # Adjust the x-coordinate based on the size of the presentation image
    y = 10
    imgCurrent[y:y + hs, x:x + ws] = imgSmall

    cv2.imshow("Image", img)
    cv2.imshow("Slides", imgCurrent)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
