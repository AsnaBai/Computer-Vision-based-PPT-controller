import cv2
width,height=1200, 720
cap=cv2.VideoCapture(0)
cap.set(3,width)
cap.set(4,height)
while True:
    success,img=cap.read()
    cv2.imshow("Image",img)
    key=cv2.waitKey(1)
    if key==ord('q'):
        break