import cv2

def canny(img):

    if img is None:
        cap.release()
        cv2.destroyAllWindows()
        exit()

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    kernel = 5
    blur = cv2.GaussianBlur(gray, (kernel, kernel), 0)
    canny = cv2.Canny(blur, 50, 150)
    return canny


cap = cv2.VideoCapture("./videos/test4.mp4")

while(cap.isOpened()):
    ret, frame = cap.read()
    frame = cv2.resize(frame, (640,400))
    canny_image = canny(frame)
    cv2.imshow("Canny Image", canny_image)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()