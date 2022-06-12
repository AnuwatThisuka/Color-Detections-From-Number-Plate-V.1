from matplotlib.pyplot import gray
import re
from itertools import count
from re import A
import cv2
import numpy as np

frameWidth = 640  # Frame Width
franeHeight = 480   # Frame Height

#-------------------------------------------------------------------------------------#


def center_point(x, y, w, h):
    ww = int(w/2)
    hh = int(h/2)
    cx = int(x+ww)
    cy = int(y+hh)
    return cx, cy


def x_line(img, percent):
    posit = int((img.shape[1]*percent)/100)
    left_line = posit - each_line
    right_line = posit + each_line
    return posit, left_line, right_line


counter_line = 50
each_line = 50
text_color = (0, 255, 0)
object_color = (0, 0, 255)
blurr = 10
bord = 10
error = 100
detect_line = []
counter = 0
state = 0
# lower color detection
h_lower = 94
s_lower = 36
v_lower = 134
# upper color detection
h_upper = 179
s_upper = 255
v_upper = 255


url = 'rtsp://10.1.76.236:554/live/0/SUB'
plateCascade = cv2.CascadeClassifier(
    "C:\\Users\\Acer\\Desktop\\IIOT-B14-Project\\Auto_Paining\\haarcascade_russian_plate_number.xml")
minArea = 500

cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, franeHeight)
cap.set(10, 150)
count = 0
state = 0
data2 = 0
loop = True
success, img = cap.read()
left_line = x_line(img, counter_line)[1] - each_line


def countfunc(count):
    global counter
    counter = counter + 1
    return counter


# main function start
start_Model_1 = False
start_Model_2 = False
#-----------------------------------------------------------------------------------------------------#
while(1):
    while(1):
        success, img = cap.read()
        imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        numberPlates = plateCascade .detectMultiScale(
            imgGray, scaleFactor=1.05, minNeighbors=7)
        for (x, y, w, h) in numberPlates:
            area1 = w * h
            if area1 > minArea and data2 == 0:
                cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
                imgRoi = img[y:y+h, x:x+w]
                number = numberPlates[0]
                if area1 > 100000 and data2 == 0:
                    state = 0
                    print("Save Image")
                    cv2.imwrite(
                        "C:\\Users\\Acer\\Desktop\\IIOT-B14-Project\\Auto_Paining\\Model\\Model"".jpg", imgRoi)

                    def start_functions():
                        # print("Start Functions")
                        global data2
                        data2 = 1
                        return data2
                    start_functions()
                print(data2)
                break
            break
        if data2 == 1 and start_Model_1 == False and start_Model_2 == False:
            # print("Data 2 = 1")
            import cv2
            import numpy as np
            import pytesseract
            import os
            from PIL import Image
            pytesseract.pytesseract.tesseract_cmd = r"C://Program Files//Tesseract-OCR//tesseract.exe"
            img = cv2.imread(
                "C:\\Users\\Acer\\Desktop\\IIOT-B14-Project\\Auto_Paining\\Model\\Model.jpg")
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            adaptive_threshold = cv2.adaptiveThreshold(
                gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 85, 11)
            Model = pytesseract.image_to_string(
                adaptive_threshold, lang='eng', config='--psm 3')
            print(Model)
            Model_number = (Model)

            #-----------------------------main confirm function start-----------------------------------#
            if ("234500" in Model_number) == True:
                def start_Model():
                    global start_Model_1
                    start_Model_1 = True
                    return start_Model_1
                start_Model()
                break
            elif ("1234008" in Model_number) == True:
                def start_Model1():
                    global start_Model_2
                    start_Model_2 = True
                    return start_Model_2
                start_Model1()
                break
        #------------------------------end of confirm function start-------------------------------------------#
        # Start Model 1
        while start_Model_1 == True:
            print("Start fuctions counter Model 234500")
            blur = cv2.blur(img, (25, 25))
            hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)

            lower = np.array(
                [h_lower, s_lower, v_lower], np.uint8)
            upper = np.array(
                [h_upper, s_upper, v_upper], np.uint8)

            blue = cv2.inRange(hsv, lower, upper)
            kernal = np.ones((5, 5), "uint8")
            blue = cv2.dilate(blue, kernal)
            res_blue = cv2.bitwise_and(img, img, mask=blue)
            cv2.line(img, (x_line(img, counter_line)[0], bord), (x_line(
                img, counter_line)[0], img.shape[0]-bord), (255, 0, 0), 2)
            cv2.line(img, (x_line(img, counter_line)[1], bord), (x_line(
                img, counter_line)[1], img.shape[0]-bord), (255, 0, 0), 2)
            cv2.line(img, (x_line(img, counter_line)[2], bord), (x_line(
                img, counter_line)[2], img.shape[0]-bord), (255, 0, 0), 2)
            contours, hierarchy = cv2.findContours(
                blue, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            for contour in contours:
                area = cv2.contourArea(contour)
                if(area > 10000):
                    x, y, w, h = cv2.boundingRect(contour)
                    center = center_point(x, y, w, h)
                    cv2.circle(img, center, 5, (0, 0, 255), -1)
                    img = cv2.rectangle(
                        img, (x, y), (x + w, y + h), object_color, 2)
                    detect_line.append(center)
                    for x, y in detect_line:
                        if (x < x_line(img, counter_line)[2] and x > x_line(img, counter_line)[0] and state == 0):
                            state = 1
                        if (x < x_line(img, counter_line)[2] and x > x_line(img, counter_line)[1]-20):
                            cv2.line(img, (x_line(img, counter_line)[1], bord), (x_line(
                                img, counter_line)[1], img.shape[0]-bord), (0, 255, 0), 2)
                            cv2.line(img, (x_line(img, counter_line)[2], bord), (x_line(
                                img, counter_line)[2], img.shape[0]-bord), (0, 255, 0), 2)
                            if (x < x_line(img, counter_line)[1]) and state == 1:
                                state = 0
                                countfunc(count)
                                # print("Counter: ", counfunc(count))
                                cv2.line(img, (x_line(img, counter_line)[0], bord), (x_line(
                                    img, counter_line)[0], img.shape[0]-bord), (0, 250, 0), 5)
                        detect_line.remove((x, y))
            cv2.putText(img, str(counter), (550, 450),
                        cv2.FONT_HERSHEY_SIMPLEX, 2, text_color, 3, cv2.LINE_AA)
            break
        #------------------------------end of start model 1-------------------------------------------#
        # Start Model 1
        while start_Model_2 == True:
            print("Start fuctions counter Model 1234008")
            blur = cv2.blur(img, (25, 25))
            hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)

            lower = np.array(
                [h_lower, s_lower, v_lower], np.uint8)
            upper = np.array(
                [h_upper, s_upper, v_upper], np.uint8)

            blue = cv2.inRange(hsv, lower, upper)
            kernal = np.ones((5, 5), "uint8")
            blue = cv2.dilate(blue, kernal)
            res_blue = cv2.bitwise_and(img, img, mask=blue)
            cv2.line(img, (x_line(img, counter_line)[0], bord), (x_line(
                img, counter_line)[0], img.shape[0]-bord), (255, 0, 0), 2)
            cv2.line(img, (x_line(img, counter_line)[1], bord), (x_line(
                img, counter_line)[1], img.shape[0]-bord), (255, 0, 0), 2)
            cv2.line(img, (x_line(img, counter_line)[2], bord), (x_line(
                img, counter_line)[2], img.shape[0]-bord), (255, 0, 0), 2)
            contours, hierarchy = cv2.findContours(
                blue, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            for contour in contours:
                area = cv2.contourArea(contour)
                if(area > 10000):
                    x, y, w, h = cv2.boundingRect(contour)
                    center = center_point(x, y, w, h)
                    cv2.circle(img, center, 5, (0, 0, 255), -1)
                    img = cv2.rectangle(
                        img, (x, y), (x + w, y + h), object_color, 2)
                    detect_line.append(center)
                    for x, y in detect_line:
                        if (x < x_line(img, counter_line)[2] and x > x_line(img, counter_line)[0] and state == 0):
                            state = 1
                        if (x < x_line(img, counter_line)[2] and x > x_line(img, counter_line)[1]-20):
                            cv2.line(img, (x_line(img, counter_line)[1], bord), (x_line(
                                img, counter_line)[1], img.shape[0]-bord), (0, 255, 0), 2)
                            cv2.line(img, (x_line(img, counter_line)[2], bord), (x_line(
                                img, counter_line)[2], img.shape[0]-bord), (0, 255, 0), 2)
                            if (x < x_line(img, counter_line)[1]) and state == 1:
                                state = 0
                                countfunc(count)
                                # print("Counter: ", counfunc(count))
                                cv2.line(img, (x_line(img, counter_line)[0], bord), (x_line(
                                    img, counter_line)[0], img.shape[0]-bord), (0, 250, 0), 5)
                        detect_line.remove((x, y))
            cv2.putText(img, str(counter), (550, 450),
                        cv2.FONT_HERSHEY_SIMPLEX, 2, text_color, 3, cv2.LINE_AA)
            break
        #-------------------------------------end Model 2---------------------------------------------#
        cv2.imshow("IIOT-B14", img)
        if cv2.waitKey(1) & 0xFF == ord('s'):
            cv2.imwrite(
                "C:\\Users\\Acer\\Desktop\\IIOT-B14-Project\\Auto_Paining\\Model\\Model-"+str(count)+".jpg", img)
            cv2.rectangle(img, (0, 200), (640, 300), (0, 255, 0), cv2.FILLED)
            cv2.putText(img, "Scan Number", (15, 265),
                        cv2.FONT_HERSHEY_COMPLEX, 2, (0, 0, 255), 2)
            cv2.waitKey(500)
            count += 1
