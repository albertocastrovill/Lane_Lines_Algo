import cv2

cap = cv2.VideoCapture("./videos/test2.mp4")

while(cap.isOpened()):
    ret, frame = cap.read()
    frame = cv2.resize(frame, (640,400))
    cv2.imshow("Video", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()