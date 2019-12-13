import cv2


cam = cv2.VideoCapture(0)


while True:
    result, frame = cam.read()

    cv2.imshow("Image", frame)
    key = cv2.waitKey(1)
    if key == 27:
        break

