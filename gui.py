#  -------------------------------------------------------------
#   (IIOT-B14) SNC Former Public Company Limited All rights reserved.
#   This file is part of the IIOT-B14 project. Counter part of line "Painting B14"
#   Created by : IIOT-B14 on 2022/06/06
#  -------------------------------------------------------------

from cProfile import run
from pyexpat import model
from tkinter import *
from tkinter import filedialog
from tokenize import Name
from turtle import bgcolor
from PIL import Image
from PIL import ImageTk
import cv2
import imutils
import tkinter as tk
from tkinter import ttk
import numpy as np
from matplotlib.pyplot import gray
from itertools import count

plateCascade = cv2.CascadeClassifier(
    "haarcascade_russian_plate_number.xml")
#faceClassif = cv2.CascadeClassifier("haarcascade_russian_plate_number.xml")

cap = None
root = tk.Tk()
my_tabs = ttk.Notebook(root)  # declaring
root.title("SNC IIoT-B14 Steaming Paining Counter")
root.geometry("800x480")

object_color = (0, 0, 255)
detect_line = []
each_line = 40
each_line = 40
counter = 0
state = 0
counter_line = 40
each_line = 40
text_color = (0, 255, 0)
object_color = (0, 0, 255)
counter_line = 50
each_line = 30
text_color = (0, 255, 0)
object_color = (0, 0, 255)
blurr = 10
bord = 10
error = 100
detect_line = []
counter = 0
state = 0
count = 0
run_model1 = 0
minArea = 500
data2 = 0
running = 0
#** -----------------------------------status start functions main-----------------------------------------**#
start_Model_1 = False
start_Model_2 = False
start_Model_3 = False
start_Model_4 = False
start_Model_5 = False
start_Model_6 = False
Reset_Counters = False
#** -------------------------------- startus for  Reset Founction Counter -------------------------------- **#


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


def start_state():
    global state
    state = 0
    return state


start_state()


def video():
    global cap
    if selected.get() == 1:
        btnEnd.configure(state="active")
        rad1.configure(state="disabled")
        rad2.configure(state="disabled")
        rad3.configure(state="disabled")
        rad4.configure(state="disabled")
        rad5.configure(state="disabled")
        rad6.configure(state="disabled")
        lblInfoVideoPath.configure(text="")
        cap = cv2.VideoCapture(0)
        my_tabs.hide(tab2)
        # NOTE: color detected for Model H36TL1B

        def model_1():  # color detected for Model H36TL1B
            global model1lower, model1upper, Name_Model
            model1lower = [94, 36, 134]
            model1upper = [179, 255, 255]
            Name_Model = "Model: H36TL1B"
            return model1lower, model1upper
        model_1()
        Manual()
    if selected.get() == 2:
        btnEnd.configure(state="active")
        rad1.configure(state="disabled")
        rad2.configure(state="disabled")
        rad3.configure(state="disabled")
        rad4.configure(state="disabled")
        rad5.configure(state="disabled")
        rad6.configure(state="disabled")
        lblInfoVideoPath.configure(text="")
        cap = cv2.VideoCapture(0)
        my_tabs.hide(tab2)
        # NOTE: color detected for Model H36TL2B

        def model_2():  # color detected for Model H36TL2B
            global model1lower, model1upper, Name_Model
            model1lower = [94, 36, 134]
            model1upper = [179, 255, 255]
            Name_Model = "Model: H36TL2B"
            return model1lower, model1upper, Name_Model
        model_2()
        Manual()
    if selected.get() == 3:
        btnEnd.configure(state="active")
        rad1.configure(state="disabled")
        rad2.configure(state="disabled")
        rad3.configure(state="disabled")
        rad4.configure(state="disabled")
        rad5.configure(state="disabled")
        rad6.configure(state="disabled")
        lblInfoVideoPath.configure(text="")
        cap = cv2.VideoCapture(0)
        my_tabs.hide(tab2)
        # NOTE: color detected for Model H36TL1R

        def model_3():  # color detected for Model H36TL1R
            global model1lower, model1upper, Name_Model
            model1lower = [94, 36, 134]
            model1upper = [179, 255, 255]
            Name_Model = "Model: H36TL1R"
            return model1lower, model1upper, Name_Model
        model_3()
        Manual()
    if selected.get() == 4:
        btnEnd.configure(state="active")
        rad1.configure(state="disabled")
        rad2.configure(state="disabled")
        rad3.configure(state="disabled")
        rad4.configure(state="disabled")
        rad5.configure(state="disabled")
        rad6.configure(state="disabled")
        lblInfoVideoPath.configure(text="")
        cap = cv2.VideoCapture(0)
        my_tabs.hide(tab2)
        # NOTE: color detected for Model H36TL2R

        def model_4():  # color detected for Model H36TL2R
            global model1lower, model1upper, Name_Model
            model1lower = [94, 36, 134]
            model1upper = [179, 255, 255]
            Name_Model = "Model: H36TL2R"
            return model1lower, model1upper, Name_Model
        model_4()
        Manual()
    if selected.get() == 5:
        btnEnd.configure(state="active")
        rad1.configure(state="disabled")
        rad2.configure(state="disabled")
        rad3.configure(state="disabled")
        rad4.configure(state="disabled")
        rad5.configure(state="disabled")
        rad6.configure(state="disabled")
        lblInfoVideoPath.configure(text="")
        cap = cv2.VideoCapture(0)
        my_tabs.hide(tab2)
        # NOTE: color detected for Model H46TL1R

        def model_5():  # color detected for Model H46TL1R
            global model1lower, model1upper, Name_Model
            model1lower = [94, 36, 134]
            model1upper = [179, 255, 255]
            Name_Model = "Model: H46TL1R"
            return model1lower, model1upper, Name_Model
        model_5()
        Manual()
    if selected.get() == 6:
        btnEnd.configure(state="active")
        rad1.configure(state="disabled")
        rad2.configure(state="disabled")
        rad3.configure(state="disabled")
        rad4.configure(state="disabled")
        rad5.configure(state="disabled")
        rad6.configure(state="disabled")
        lblInfoVideoPath.configure(text="")
        cap = cv2.VideoCapture(0)
        # NOTE: color detected for Model H46TL2R
        my_tabs.hide(tab2)

        def model_6():  # color detected for Model H46TL2R
            global model1lower, model1upper, Name_Model
            model1lower = [94, 36, 134]
            model1upper = [179, 255, 255]
            Name_Model = "Model: H46TL2R"
            return model1lower, model1upper, Name_Model
        model_6()
        Manual()
    if selected.get() == 7:
        btnEnd.configure(state="active")
        rad1.configure(state="disabled")
        rad2.configure(state="disabled")
        rad3.configure(state="disabled")
        rad4.configure(state="disabled")
        rad5.configure(state="disabled")
        rad6.configure(state="disabled")
        rad7.configure(state="disabled")
        lblInfoVideoPath.configure(text="")
        cap = cv2.VideoCapture(0)
        # NOTE: color detected for Model H46TL2R
        my_tabs.hide(tab2)

        def model_7():  # color detected for Model H46TL2R
            global model1lower, model1upper, Name_Model
            model1lower = [94, 36, 134]
            model1upper = [179, 255, 255]
            Name_Model = "Seaching..."
            return model1lower, model1upper, Name_Model
        model_7()
        auto()


def auto():
    import cv2
    from itertools import count
    from PIL import Image
    from PIL import ImageTk
    count = 0

    #print("Auto is Running...")

    def countfunc(count):
        global counter
        counter = counter + 1
        return counter
    labelcounter = Label(
        tab1, text=(counter), font="bold", bg='white', width=20, height=2)
    labelcounter.place(relx=0.8, rely=0.24,
                       anchor="center")
    lblInfo4 = Label(
        tab1, text=(Name_Model), font="bold", bg='white', width=20, height=2)
    lblInfo4.place(relx=0.8, rely=0.4,
                   anchor="center")
    while run_model1 == 0:  # For Model H36TL2 Blue
        ret, img = cap.read()
        #img = cv2.flip(img1, 0)
        imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        numberPlates = plateCascade.detectMultiScale(
            imgray, scaleFactor=1.05, minNeighbors=7)
        for (x, y, w, h) in numberPlates:
            area1 = w * h
            if area1 > minArea and data2 == 0:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
                imgRoi = img[y:y+h, x:x+w]
                number = numberPlates[0]
                if area1 > 60000 and data2 == 0:
                    state = 0
                    cv2.imwrite(
                        "C:\\Users\\Acer\\Desktop\\IIOT-B14-Project\\Auto_Paining\\IMAGE\\Model"".jpg", imgRoi)

                    def start_functions():
                        global data2
                        data2 = 1
                        return data2
                    start_functions()
                    print("Model Detected")
                    break
                break
            break
        if data2 == 1 and start_Model_1 == False and start_Model_2 == False and start_Model_3 == False and start_Model_4 == False and start_Model_5 == False and start_Model_6 == False:
            import cv2
            import numpy as np
            import pytesseract
            import os
            from PIL import Image
            pytesseract.pytesseract.tesseract_cmd = r"C://Program Files//Tesseract-OCR//tesseract.exe"
            img = cv2.imread(
                "C:\\Users\\Acer\\Desktop\\IIOT-B14-Project\\Auto_Paining\\IMAGE\\Model.jpg")
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
                #print("Model 234500 is detected")
                break
            elif ("123432" in Model_number) == True:
                def start_Model1():
                    global start_Model_2
                    start_Model_2 = True
                    return start_Model_2
                start_Model1()
                print("Model 1234008 is detected")
                break
            elif ("1234009" in Model_number) == True:
                def start_Model2():
                    global start_Model_3
                    start_Model_3 = True
                    return start_Model_3
                start_Model2()
                print("Model 1234009 is detected")
                break
            elif ("0000000" in Model_number) == True:
                def Reset():  # For Model H36TL2 Product Blue
                    global data2
                    data2 = 0
                    return data2
                Reset()
                break
            elif ("360028" in Model_number) == True:
                def start_Model3():  # For Model H36TL2 Product Blue
                    global start_Model_3
                    start_Model_3 = True
                    return start_Model_3
                start_Model3()
                print("Model H36TL2 Product Blue")
                break
            elif ("360018" in Model_number) == True:
                def start_Model4():  # For Model H36TL1 Product Blue
                    global start_Model_4
                    start_Model_4 = True
                    return start_Model_4
                start_Model4()
                break
            elif ("36002R" in Model_number) == True:
                def start_Model5():  # For Model H36TL2 Product Red
                    global start_Model_5
                    start_Model_5 = True
                    return start_Model_5
                start_Model5()
                break
            elif ("36001R" in Model_number) == True:
                def start_Model6():  # For Model H36TL2 Product Green
                    global start_Model_6
                    start_Model_6 = True
                    return start_Model_6
                start_Model6()
                break
            elif ("H36TL2B" in Model_number) == True:
                print("Detected")

                def Reset():
                    global data2
                    data2 = 0
                    return data2
                Reset()
                break
            else:
                print("Model Not Found")

                def Reset():
                    global data2
                    data2 = 0
                    return data2
                Reset()
                break
        while start_Model_1 == True:
            print("Model 1 Started is Detected")

            def auto_model_1():  # color detected for Model H46TL2R
                global model1lower, model1upper, Name_Model, running
                model1lower = [94, 36, 134]
                model1upper = [179, 255, 255]
                Name_Model = "Model: 234500"
                running = 1
                return model1lower, model1upper, Name_Model, running
            auto_model_1()
            labelcounter = Label(
                tab1, text=(counter), font="bold", bg='white', width=20, height=2)
            labelcounter.place(relx=0.8, rely=0.24,
                               anchor="center")
            lblInfo4 = Label(
                tab1, text=(Name_Model), font="bold", bg='white', width=20, height=2)
            lblInfo4.place(relx=0.8, rely=0.4,
                           anchor="center")
            break
        while start_Model_2 == True:
            print("Model 2 Started is Detected")

            def auto_model_2():  # color detected for Model H46TL2R
                global model1lower, model1upper, Name_Model, running
                model1lower = [100, 36, 134]
                model1upper = [179, 255, 255]
                Name_Model = "Model: 123432"
                running = 1
                return model1lower, model1upper, Name_Model, running
            auto_model_2()
            labelcounter = Label(
                tab1, text=(counter), font="bold", bg='white', width=20, height=2)
            labelcounter.place(relx=0.8, rely=0.24,
                               anchor="center")
            lblInfo4 = Label(
                tab1, text=(Name_Model), font="bold", bg='white', width=20, height=2)
            lblInfo4.place(relx=0.8, rely=0.4,
                           anchor="center")
            break

        while running == 1:
            print(model1lower, model1upper)
            break

        #cv2.imshow("img", img)
        img = imutils.resize(img, width=400)
        frame = Image.fromarray(img)
        imgtk = ImageTk.PhotoImage(image=frame)
        lblVideo.imgtk = imgtk
        lblVideo.configure(image=imgtk)
        lblVideo.after(10, auto)
        return img
    img = imutils.resize(img, width=400)
    frame = Image.fromarray(img)
    imgtk = ImageTk.PhotoImage(image=frame)
    lblVideo.imgtk = imgtk
    lblVideo.configure(image=imgtk)
    lblVideo.after(10, auto)
    return img


def Manual():
    from itertools import count
    count = 0

    print("Manual is Running...")

    def countfunc(count):
        global counter
        counter = counter + 1
        return counter
    labelcounter = Label(
        tab1, text=(counter), font="bold", bg='white', width=20, height=2)
    labelcounter.place(relx=0.8, rely=0.24,
                       anchor="center")
    lblInfo4 = Label(
        tab1, text=(Name_Model), font="bold", bg='white', width=20, height=2)
    lblInfo4.place(relx=0.8, rely=0.4,
                   anchor="center")
    while run_model1 == 0:  # For Model H36TL2 Blue
        ret, img1 = cap.read()
        img = cv2.flip(img1, 1)
        blur = cv2.blur(img, (25, 25))
        hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)

        lower = np.array(model1lower, np.uint8)
        upper = np.array(model1upper, np.uint8)

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
                        def set_state_1():
                            global state
                            state = 1
                            return state
                        set_state_1()
                    if (x < x_line(img, counter_line)[2] and x > x_line(img, counter_line)[1]-20):
                        cv2.line(img, (x_line(img, counter_line)[1], bord), (x_line(
                            img, counter_line)[1], img.shape[0]-bord), (0, 255, 0), 2)
                        cv2.line(img, (x_line(img, counter_line)[2], bord), (x_line(
                            img, counter_line)[2], img.shape[0]-bord), (0, 255, 0), 2)
                        test = x_line(img, counter_line)[1]
                        print(state)
                        if (x < x_line(img, counter_line)[1]) and state == 1:
                            def set_state():
                                global state
                                state = 0
                                return state
                            set_state()
                            countfunc(count)
                            print(counter)
                            cv2.line(img, (x_line(img, counter_line)[0], bord), (x_line(
                                img, counter_line)[0], img.shape[0]-bord), (0, 250, 0), 5)
                    detect_line.remove((x, y))
        #cv2.imshow("img", img)
        img2 = imutils.resize(img, width=400)
        frame = Image.fromarray(img2)
        imgtk = ImageTk.PhotoImage(image=frame)
        lblVideo.imgtk = imgtk
        lblVideo.configure(image=imgtk)
        lblVideo.after(10, Manual)
        return img


def Exit_Programs():
    lblVideo.image = ""
    lblInfoVideoPath.configure(text="Test")
    rad1.configure(state="active")
    rad2.configure(state="active")
    rad3.configure(state="active")
    rad4.configure(state="active")
    rad5.configure(state="active")
    rad6.configure(state="active")
    selected.set(0)
    my_tabs.add(tab2)

    def set_count():
        global counter
        counter = 0
        return counter
    set_count()
    cap.release()


tab1 = ttk.Frame(my_tabs)
tab2 = ttk.Frame(my_tabs)
tab3 = ttk.Frame(my_tabs)

my_tabs.add(tab1, text='Manual')  # adding tab
my_tabs.add(tab2, text='Auto')  # adding tab
my_tabs.add(tab3, text='Data History')  # adding tab
my_tabs.pack(expand=1, fill="both")

lblInfo1 = Label(
    tab1, text="SNC IIoT-B14 Steaming Paining Counter", font="bold")
lblInfo1.place(relx=0.5, rely=0.03, anchor="center")

logotab2 = Label(
    tab2, text="SNC IIoT-B14 Steaming Paining Counter", font="bold")
logotab2.place(relx=0.5, rely=0.03, anchor="center")


selected = IntVar()
rad1 = Radiobutton(tab1, text="H36TL1B", width=13, value=1,
                   variable=selected, command=video)
rad2 = Radiobutton(tab1, text="H36TL2B", width=13, value=2,
                   variable=selected, command=video)
rad3 = Radiobutton(tab1, text="H36TL1R", width=13, value=3,
                   variable=selected, command=video)
rad4 = Radiobutton(tab1, text="H36TL2R", width=13, value=4,
                   variable=selected, command=video)
rad5 = Radiobutton(tab1, text="H46TL2B", width=13, value=5,
                   variable=selected, command=video)
rad6 = Radiobutton(tab1, text="H52TL1B", width=13, value=6,
                   variable=selected, command=video)
rad7 = Radiobutton(tab1, text="Run Auto", width=13, value=7,
                   variable=selected, command=video, bg='green')

rad1.place(relx=0.1, rely=0.1, anchor="center")
rad2.place(relx=0.25, rely=0.1, anchor="center")
rad3.place(relx=0.4, rely=0.1, anchor="center")
rad4.place(relx=0.55, rely=0.1, anchor="center")
rad5.place(relx=0.1, rely=0.15, anchor="center")
rad6.place(relx=0.25, rely=0.15, anchor="center")
rad7.place(relx=0.4, rely=0.15, anchor="center")


b2 = tk.Button(tab2, text='Run Auto', width=20, command=auto)
b2.grid(row=2, column=2)


lblInfoVideoPath = Label(tab2, text="", width=20)
lblInfoVideoPath.place(relx=0.2, rely=0.5, anchor="center")

lblInfoVideoPath1 = Label(tab2, text="", width=20)
lblInfoVideoPath1.place(relx=0.2, rely=0.5, anchor="center")

lblVideo = Label(tab1)
lblVideo.place(relx=0.32, rely=0.5, anchor="center")

btnEnd = Button(tab1, text="Exit Programs",
                state="disabled", command=Exit_Programs)
btnEnd.place(relx=0.5, rely=0.9, anchor="center")
root.mainloop()
