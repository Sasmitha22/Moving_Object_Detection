import cv2
import imutils

vs = cv2.VideoCapture(0)
frame1 = None
area = 500
text = ""

while True:
    _, img = vs.read()
    img = imutils.resize(img, width=500)
    grayimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gaussianimg = cv2.GaussianBlur(grayimg, (21, 21), 0)

    if frame1 is None:
        frame1 = gaussianimg
        continue

    imgdiff = cv2.absdiff(frame1, gaussianimg)
    threshimg = cv2.threshold(imgdiff, 25, 255, cv2.THRESH_BINARY)[1]
    threshimg = cv2.dilate(threshimg, None, iterations=2)

    contours, _ = cv2.findContours(threshimg.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for i in contours:
        if cv2.contourArea(i) < area:
            continue
        x, y, w, h = cv2.boundingRect(i)
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        text = "Moving Object detected"

    cv2.putText(img, text, (10, 20),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

    cv2.imshow("cameraFeed", img)
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

vs.release()
cv2.destroyAllWindows()
