#  -------------------------------------------------------------
#   (IIOT-B14) All rights reserved.
#   This file is part of the IIOT-B14 project. Counter part of line "Painting B14"
#   Created by : IIOT-B14 on 2022/06/06
#  -------------------------------------------------------------

from matplotlib.pyplot import gray
import re
from itertools import count
from re import A
import cv2
import numpy as np

#** --- Set frame --- **#
frameWidth = 640  # Frame Width
franeHeight = 480   # Frame Height
#** -------------------------------------------------------------------------------------#

#!! --- Define center point of detected --- !!#


def center_point(x, y, w, h):
    ww = int(w/2)
    hh = int(h/2)
    cx = int(x+ww)
    cy = int(y+hh)
    return cx, cy
#!!-------------------------------------------------------------------------------------#


#!! -- Define counter line--- !!#
# def x_line(img, percent):
#    posit = int((img.shape[1]*percent)/100)
#    left_line = posit - each_line
#    right_line = posit + each_line
#    return posit, left_line, right_line
#!!-------------------------------------------------------------------------------------#


#** -------------------------- Config Other Variable -----------------------------------#
counter_line = 50
each_line = 50
text_color = (0, 255, 0)
object_color = (0, 0, 255)
blurr = 10
bord = 10
error = 100
detect_line = []
counter = 0
counter_2 = 0
state = 0
#** -------------------------------- lower color detection --------------------------------#
h_lower = 94
s_lower = 36
v_lower = 134
#** -------------------------------- upper color detection --------------------------------#
h_upper = 179
s_upper = 255
v_upper = 255
#** -------------------------------------------------------------------------------------- **#


#! ---Set up video capture for ip camera
url = 'rtsp://10.1.76.236:554/live/0/SUB'
#! -------------------------------- #

#** ---Loading Model for detection Number plate--- **#
plateCascade = cv2.CascadeClassifier(
    "haarcascade_russian_plate_number.xml")

#!! -----------------------------Setting Rang Detected of Number plate -------------------------------- #
minArea = 500
#!! ------------------------------------------------------------- #


#!! ---------------------------- Config State For Counter System -------------------------------- !!#
cap = cv2.VideoCapture(0)
count = 0
state = 0
data2 = 0
loop = True


#** ---function for counter line--- **#
def countfunc(count):  # For Model 1
    global counter
    counter = counter + 1
    return counter


def countfunc_2(count):  # For Model 2
    global counter_2
    counter_2 = counter_2 + 1
    return counter_2


#** -----------------------------------status start functions main-----------------------------------------**#
start_Model_1 = False
start_Model_2 = False
start_Model_3 = False
Reset_Counters = False
#** -------------------------------- startus for  Reset Founction Counter -------------------------------- **#


class Video(object):
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    def __del__(self):
        self.cap.release()

    def get_frame(self):
        success, img = cap.read()

        def x_line(img, percent):
            posit = int((img.shape[1]*percent)/100)
            left_line = posit - each_line
            right_line = posit + each_line
            return posit, left_line, right_line
        left_line = x_line(img, counter_line)[1] - each_line
        success, img = cap.read()
        imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        numberPlates = plateCascade .detectMultiScale(
            imgGray, scaleFactor=1.05, minNeighbors=7)
        for (x, y, w, h) in numberPlates:
            area1 = w * h
            #** -------------------------------- Functions Detected Number Plate-----------------------------------------**#
            if area1 > minArea and data2 == 0:
                cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
                imgRoi = img[y:y+h, x:x+w]
                number = numberPlates[0]
                if area1 > 60000 and data2 == 0:
                    state = 0
                    print("Model Detected")
                    cv2.imwrite(
                        "C:\\Users\\Acer\\Desktop\\IIOT-B14-Project\\Auto_Paining\\Model\\Model"".jpg", imgRoi)

                    def start_functions():
                        global data2
                        data2 = 1
                        return data2
                    start_functions()
                break
            break
            #** ------------------------------- End of Function Number plate -------------------------------**#
        #
        #
        #
        #** -----------------------------------Functions ORC Number Plate-----------------------------------------**#
        if data2 == 1 and start_Model_1 == False and start_Model_2 == False and start_Model_3 == False:
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
                adaptive_threshold, lang='eng', config='--psm 10')
            # print(Model)
            Model_number = (Model)

            #** ----------------------------- Main Confirm Function Start For First Run System ----------------------------------- **#
            if ("234500" in Model_number) == True:
                def start_Model():
                    global start_Model_1
                    start_Model_1 = True
                    return start_Model_1
                start_Model()
                print("Model 234500 is detected")
            elif ("123432" in Model_number) == True:
                def start_Model1():
                    global start_Model_2
                    start_Model_2 = True
                    return start_Model_2
                start_Model1()
                print("Model 1234008 is detected")
            elif ("1234009" in Model_number) == True:
                def start_Model2():
                    global start_Model_3
                    start_Model_3 = True
                    return start_Model_3
                start_Model2()
                print("Model 1234009 is detected")
            elif ("0000000" in Model_number) == True:
                def Reset():
                    global data2
                    data2 = 0
                    return data2
                Reset()
            #!! --- Not Found Model ---- !!#
            else:
                print("Model Not Found")

                def Reset():
                    global data2
                    data2 = 0
                    return data2
                Reset()
        # **------------------------------End of Confirm Function Start-------------------------------------------** #
        #
        #
        #
        # **--------------------------------------Start Model 1---------------------------------------------------** #
        while start_Model_1 == True:  # Model 234500
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
                img, counter_line)[0], img.shape[0]-bord), (255, 255, 0), 2)
            cv2.line(img, (x_line(img, counter_line)[1], bord), (x_line(
                img, counter_line)[1], img.shape[0]-bord), (255, 255, 0), 2)
            cv2.line(img, (x_line(img, counter_line)[2], bord), (x_line(
                img, counter_line)[2], img.shape[0]-bord), (255, 255, 0), 2)
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
                                cv2.line(img, (x_line(img, counter_line)[0], bord), (x_line(
                                    img, counter_line)[0], img.shape[0]-bord), (0, 250, 0), 5)
                        detect_line.remove((x, y))
            #** ----------------------------------------- Functions main Reset --------------------------------------- **#
            imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            numberPlates = plateCascade .detectMultiScale(
                imgGray, scaleFactor=1.05, minNeighbors=7)
            for (x, y, w, h) in numberPlates:
                area1 = w * h
                if area1 > minArea and Reset_Counters == False:
                    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 255, 0), 2)
                    number = numberPlates[0]
                    imgmodel = img[y:y+h, x:x+w]
                    if area1 > 60000 and Reset_Counters == False:
                        cv2.imwrite(
                            "C:\\Users\\Acer\\Desktop\\IIOT-B14-Project\\Auto_Paining\\RESET\\Reset"".jpg", imgmodel)

                        def function_Reset():
                            global Reset_Counters
                            Reset_Counters = True
                            return Reset_Counters
                        function_Reset()
                        break
                    break
                break
            if Reset_Counters == True:
                import cv2
                import numpy as np
                import pytesseract
                import os
                from PIL import Image
                pytesseract.pytesseract.tesseract_cmd = r"C://Program Files//Tesseract-OCR//tesseract.exe"
                img = cv2.imread(
                    "C:\\Users\\Acer\\Desktop\\IIOT-B14-Project\\Auto_Paining\\RESET\\Reset.jpg")
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                adaptive_threshold = cv2.adaptiveThreshold(
                    gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 85, 11)
                Model_Reset = pytesseract.image_to_string(
                    adaptive_threshold, lang='eng', config='--psm 10')
                print(Model_Reset)
                #** --------------------------------- Reset All State From Counter System started ----------------------------------- **#
                if ("234500" in Model_Reset):
                    def Reset_1():
                        global Reset_Counters, start_Model_1, start_Model_2, start_Model_3, data2, count, counter_2
                        Reset_Counters = False
                        start_Model_1 = True
                        start_Model_2 = False
                        start_Model_3 = False
                        data2 = 0
                        count = 0
                        counter_2 = 0
                        return Reset_Counters, start_Model_1, start_Model_2, start_Model_3, data2, count, counter_2
                    Reset_1()
                    break
                elif ("123432" in Model_Reset):
                    def H36TL2():
                        global Reset_Counters, start_Model_1, start_Model_2, start_Model_3, data2, count, counter_2
                        Reset_Counters = False
                        start_Model_1 = False
                        start_Model_2 = True
                        start_Model_3 = False
                        data2 = 0
                        count = 0
                        counter_2
                        return Reset_Counters, start_Model_1, start_Model_2, start_Model_3, data2, count, counter_2
                    H36TL2()
                    break
                else:
                    def Reset():
                        global data2
                        data2 = 0
                        return data2
                    Reset()

                    def Reset_1():
                        global Reset_Counters, start_Model_1, start_Model_2, start_Model_3, data2, count, counter_2
                        Reset_Counters = False
                        start_Model_1 = False
                        start_Model_2 = False
                        start_Model_3 = False
                        data2 = 0
                        count = 0
                        counter_2 = 0
                        return Reset_Counters, start_Model_1, start_Model_2, start_Model_3, data2, count, counter_2
                    Reset_1()
                    print("Model not found")
                    break
            cv2.putText(img, str(counter), (550, 400),
                        cv2.FONT_HERSHEY_SIMPLEX, 2, text_color, 3, cv2.LINE_AA)
            cv2.putText(img, str("Model: 234500"), (20, 50),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2, cv2.LINE_AA)
            break
         #** ----------------------------------------- End of Functions OCR Reset -------------------------------- **#
        #*---------------------------------------End of Start Model 1-------------------------------------------#
        #
        #
        #
        #*--- Start Model 2 ---**#
        while start_Model_2 == True:  # Model 1234008
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
                                countfunc_2(count)
                                # print("Counter: ", counfunc(count))
                                cv2.line(img, (x_line(img, counter_line)[0], bord), (x_line(
                                    img, counter_line)[0], img.shape[0]-bord), (0, 250, 0), 5)
                        detect_line.remove((x, y))
            #** ----------------------------------------- Functions main Reset --------------------------------------- **#
            imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            numberPlates = plateCascade .detectMultiScale(
                imgGray, scaleFactor=1.05, minNeighbors=7)
            for (x, y, w, h) in numberPlates:
                area1 = w * h
                if area1 > minArea and Reset_Counters == False:
                    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 255, 0), 2)
                    number = numberPlates[0]
                    imRoi2 = img[y:y+h, x:x+w]
                    if area1 > 60000 and Reset_Counters == False:
                        cv2.imwrite(
                            "C:\\Users\\Acer\\Desktop\\IIOT-B14-Project\\Auto_Paining\\RESET\\Reset"".jpg", imRoi2)

                        def function_Reset():
                            global Reset_Counters
                            Reset_Counters = True
                            return Reset_Counters
                        function_Reset()
                        break
                    break
            if Reset_Counters == True:
                import cv2
                import numpy as np
                import pytesseract
                import os
                from PIL import Image
                pytesseract.pytesseract.tesseract_cmd = r"C://Program Files//Tesseract-OCR//tesseract.exe"
                img = cv2.imread(
                    "C:\\Users\\Acer\\Desktop\\IIOT-B14-Project\\Auto_Paining\\RESET\\RESET.jpg")
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                adaptive_threshold = cv2.adaptiveThreshold(
                    gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 85, 11)
                Model_Reset = pytesseract.image_to_string(
                    adaptive_threshold, lang='eng', config='--psm 10')

                #** --------------------------------- Reset All State From Counter System started ----------------------------------- **#
                if ("234500" in Model_Reset):
                    def Reset_1():
                        global Reset_Counters, start_Model_1, start_Model_2, start_Model_3, data2, count, counter
                        Reset_Counters = False
                        start_Model_1 = True
                        start_Model_2 = False
                        start_Model_3 = False
                        data2 = 0
                        count = 0
                        counter = 0
                        return Reset_Counters, start_Model_1, start_Model_2, start_Model_3, data2, count, counter
                    Reset_1()
                    break
                elif ("123432" in Model_Reset):
                    def Reset_1():
                        global Reset_Counters, start_Model_1, start_Model_2, start_Model_3, data2, count, counter
                        Reset_Counters = False
                        start_Model_1 = False
                        start_Model_2 = True
                        start_Model_3 = False
                        data2 = 0
                        count = 0
                        counter = 0
                        return Reset_Counters, start_Model_1, start_Model_2, start_Model_3, data2, count, counter
                    Reset_1()
                    break
                else:
                    def Reset():
                        global data2
                        data2 = 0
                        return data2
                    Reset()

                    def Reset_1():
                        global Reset_Counters, start_Model_1, start_Model_2, start_Model_3, data2, count, counter
                        Reset_Counters = False
                        start_Model_1 = False
                        start_Model_2 = False
                        start_Model_3 = False
                        data2 = 0
                        count = 0
                        counter = 0
                        return Reset_Counters, start_Model_1, start_Model_2, start_Model_3, data2, count, counter
                    Reset_1()
                    break
            cv2.putText(img, str(counter_2), (550, 450),
                        cv2.FONT_HERSHEY_SIMPLEX, 2, text_color, 3, cv2.LINE_AA)
            cv2.putText(img, str("H36TL2"), (20, 50),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2, cv2.LINE_AA)
            break
         #** ----------------------------------------- End of Functions OCR Reset -------------------------------- **#
        #* -------------------------------------End of Start Model 2---------------------------------------------#

        #** -----------------------------------------Steam Show Counter System---------------------------------------------#
        cv2.imshow("IIOT-B14", img)
        if cv2.waitKey(1) & 0xFF == ord('s'):
            cv2.imwrite(
                "\\IMAGE\\Model-"+str(count)+".jpg", img)
            cv2.rectangle(img, (0, 200), (640, 300), (0, 255, 0), cv2.FILLED)
            cv2.putText(img, "Scan Number", (15, 265),
                        cv2.FONT_HERSHEY_COMPLEX, 2, (0, 0, 255), 2)
            cv2.waitKey(500)
            count += 1

        success, jpg = cv2.imencode('.jpg', img)
        return jpg.tobytes()
