
filename = './video12.mp4'

import cv2
import imutils
from DetectPlate import detection
import text_recognition

cap = cv2.VideoCapture(filename)
count = 0
while cap.isOpened():
    ret,frame = cap.read()
    if ret == True:
        cv2.imwrite("./output/frame%d.jpg" % count, frame)
        count = count + 1
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()
plate_detect = False
i = 1
while not plate_detect and i < count:
    car_image = imread("./output/frame%d.jpg"%(count-i), as_gray=True)
    plate_detect=detection(car_image)
    i += 1

if plate_detect == False:
    print("Detection Not Successful")
else:
    text_recognition.text_data()
