from enum import auto
from faulthandler import disable
from tkinter import *
from tkinter import filedialog
from tkinter import font
from turtle import bgcolor
from PIL import Image
from PIL import ImageTk
from click import command
import cv2
import imutils
import tkinter as tk
from tkinter import ttk
import numpy as np
from matplotlib.pyplot import gray
from itertools import count


faceClassif = cv2.CascadeClassifier("haarcascade_russian_plate_number.xml")

cap = None
root = tk.Tk()
my_tabs = ttk.Notebook(root)  # declaring
root.title("SNC IIoT-B14 Steaming Paining Counter")
root.geometry("700x500")


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
minArea = 500
start_Model_2 = False
start_Model_3 = False
start_Model_4 = False
start_Model_5 = False
start_Model_6 = False
Reset_Counters = False
run = False
plateCascade = cv2.CascadeClassifier(
    "haarcascade_russian_plate_number.xml")
#** ---lower color detection ---#
h_lower = 94
s_lower = 36
v_lower = 134
#** ---upper color detection---#
h_upper = 179
s_upper = 255
v_upper = 255
#** ------------------------ **#


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
        btnEnd1.configure(state="active")
        rad1.configure(state="disabled")
        rad2.configure(state="disabled")
        rad3.configure(state="disabled")
        rad4.configure(state="disabled")
        rad5.configure(state="disabled")
        rad6.configure(state="disabled")
        my_tabs.hide(tab2)
        lblInfoVideoPath.configure(text="")
        cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        H36TL1B_visualizar()
    if selected.get() == 2:
        btnEnd.configure(state="active")
        btnEnd1.configure(state="active")
        rad1.configure(state="disabled")
        rad2.configure(state="disabled")
        rad3.configure(state="disabled")
        rad4.configure(state="disabled")
        rad5.configure(state="disabled")
        rad6.configure(state="disabled")
        my_tabs.hide(tab2)
        lblInfoVideoPath.configure(text="")
        cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        H36TL2B_visualizar()
    if selected.get() == 3:
        btnEnd.configure(state="active")
        btnEnd1.configure(state="active")
        rad1.configure(state="disabled")
        rad2.configure(state="disabled")
        rad3.configure(state="disabled")
        rad4.configure(state="disabled")
        rad5.configure(state="disabled")
        rad6.configure(state="disabled")
        my_tabs.hide(tab2)
        lblInfoVideoPath.configure(text="")
        cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        H36TL1R_visualizar()
    if selected.get() == 4:
        btnEnd.configure(state="active")
        btnEnd1.configure(state="active")
        rad1.configure(state="disabled")
        rad2.configure(state="disabled")
        rad3.configure(state="disabled")
        rad4.configure(state="disabled")
        rad5.configure(state="disabled")
        rad6.configure(state="disabled")
        my_tabs.hide(tab2)
        lblInfoVideoPath.configure(text="")
        cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        H36TL2R_visualizar()
    if selected.get() == 5:
        btnEnd.configure(state="active")
        btnEnd1.configure(state="active")
        rad1.configure(state="disabled")
        rad2.configure(state="disabled")
        rad3.configure(state="disabled")
        rad4.configure(state="disabled")
        rad5.configure(state="disabled")
        rad6.configure(state="disabled")
        my_tabs.hide(tab2)
        lblInfoVideoPath.configure(text="")
        cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        H46TL1B_visualizar()
    if selected.get() == 6:
        btnEnd.configure(state="active")
        btnEnd1.configure(state="active")
        rad1.configure(state="disabled")
        rad2.configure(state="disabled")
        rad3.configure(state="disabled")
        rad4.configure(state="disabled")
        rad5.configure(state="disabled")
        rad6.configure(state="disabled")
        my_tabs.hide(tab2)
        lblInfoVideoPath.configure(text="")
        cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        H46TL2B_visualizar()
    if run == True:
        print("auto_run")
        btnEnd.configure(state="active")
        btnEnd1.configure(state="active")
        lblInfoVideoPath.configure(text="")
        #cap = cv2.VideoCapture(0)
        Auto_visualizar()
        # my_tabs.hide(tab1)

#------ Manual Mode ------#


def H36TL1B_visualizar():
    global cap
    ret, img = cap.read()
    if ret == True:
        img = imutils.resize(img, width=400)
        img = H36TL1B(img)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        im = Image.fromarray(img)
        frame = ImageTk.PhotoImage(image=im)
        lblVideo.configure(image=frame)
        lblVideo.image = frame
        lblVideo.after(10, H36TL1B_visualizar)
    else:
        lblVideo.image = ""
        lblInfoVideoPath.configure(text="")
        rad1.configure(state="active")
        rad2.configure(state="active")
        selected.set(0)
        btnEnd.configure(state="disabled")
        cap.release()


def H36TL1B(img):
    from itertools import count
    count = 0

    def countfunc(count):
        global counter
        counter = counter + 1
        return counter
    while(1):  # For Model H36TL2 Blue
        lblInfo2 = Label(
            tab1, text=(counter), font="bold", bg='white', width=20, height=2)
        lblInfo2.place(relx=0.8, rely=0.24,
                       anchor="center")
        lblInfo3 = Label(
            tab1, text="Model: H36TL1B", font="bold", bg='white', width=20, height=2)
        lblInfo3.place(relx=0.8, rely=0.4,
                       anchor="center")
        blur = cv2.blur(img, (25, 25))
        hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)

        lower = np.array([94, 36, 134], np.uint8)
        upper = np.array([179, 255, 255], np.uint8)

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
        return img


def H36TL2B_visualizar():
    global cap
    ret, img = cap.read()
    if ret == True:
        img = imutils.resize(img, width=400)
        img = H36TL2B(img)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        im = Image.fromarray(img)
        frame = ImageTk.PhotoImage(image=im)
        lblVideo.configure(image=frame)
        lblVideo.image = frame
        lblVideo.after(10, H36TL2B_visualizar)
    else:
        lblVideo.image = ""
        lblInfoVideoPath.configure(text="")
        rad1.configure(state="active")
        rad2.configure(state="active")
        selected.set(0)
        btnEnd.configure(state="disabled")
        cap.release()


def H36TL2B(img):
    from itertools import count
    count = 0

    def countfunc(count):
        global counter
        counter = counter + 1
        return counter
    while(1):  # For Model H36TL2 Blue
        lblInfo2 = Label(
            tab1, text=(counter), font="bold", bg='white', width=20, height=2)
        lblInfo2.place(relx=0.8, rely=0.24,
                       anchor="center")
        lblInfo3 = Label(
            tab1, text="Model: H36TL2B", font="bold", bg='white', width=20, height=2)
        lblInfo3.place(relx=0.8, rely=0.4,
                       anchor="center")
        blur = cv2.blur(img, (25, 25))
        hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)

        lower = np.array([94, 36, 134], np.uint8)
        upper = np.array([179, 255, 255], np.uint8)

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
        return img


def H36TL1R_visualizar():  # edit
    global cap
    ret, img = cap.read()
    if ret == True:
        img = imutils.resize(img, width=400)
        img = H36TL1R(img)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        im = Image.fromarray(img)
        frame = ImageTk.PhotoImage(image=im)
        lblVideo.configure(image=frame)
        lblVideo.image = frame
        lblVideo.after(10, H36TL1R_visualizar)  # edit
    else:
        lblVideo.image = ""
        lblInfoVideoPath.configure(text="")
        rad1.configure(state="active")
        rad2.configure(state="active")
        selected.set(0)
        btnEnd.configure(state="disabled")
        cap.release()


def H36TL1R(img):  # edit
    from itertools import count
    count = 0

    def countfunc(count):
        global counter
        counter = counter + 1
        return counter
    while(1):  # For Model H36TL2 Blue
        lblInfo2 = Label(
            tab1, text=(counter), font="bold", bg='white', width=20, height=2)
        lblInfo2.place(relx=0.8, rely=0.24,
                       anchor="center")
        lblInfo3 = Label(
            tab1, text="Model: H36TL1R", font="bold", bg='white', width=20, height=2)
        lblInfo3.place(relx=0.8, rely=0.4,
                       anchor="center")
        blur = cv2.blur(img, (25, 25))
        hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)

        lower = np.array([94, 36, 134], np.uint8)
        upper = np.array([179, 255, 255], np.uint8)

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
        return img


def H36TL2R_visualizar():  # edit
    global cap
    ret, img = cap.read()
    if ret == True:
        img = imutils.resize(img, width=400)
        img = H36TL2R(img)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        im = Image.fromarray(img)
        frame = ImageTk.PhotoImage(image=im)
        lblVideo.configure(image=frame)
        lblVideo.image = frame
        lblVideo.after(10, H36TL2R_visualizar)  # edit
    else:
        lblVideo.image = ""
        lblInfoVideoPath.configure(text="")
        rad1.configure(state="active")
        rad2.configure(state="active")
        selected.set(0)
        btnEnd.configure(state="disabled")
        cap.release()


def H36TL2R(img):  # edit
    from itertools import count
    count = 0

    def countfunc(count):
        global counter
        counter = counter + 1
        return counter
    while(1):  # For Model H36TL2 Blue
        lblInfo2 = Label(
            tab1, text=(counter), font="bold", bg='white', width=20, height=2)
        lblInfo2.place(relx=0.8, rely=0.24,
                       anchor="center")
        lblInfo3 = Label(
            tab1, text="Model: H36TL2R", font="bold", bg='white', width=20, height=2)
        lblInfo3.place(relx=0.8, rely=0.4,
                       anchor="center")
        blur = cv2.blur(img, (25, 25))
        hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)

        lower = np.array([94, 36, 134], np.uint8)
        upper = np.array([179, 255, 255], np.uint8)

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
        return img


def H46TL1B_visualizar():  # edit
    global cap
    ret, img = cap.read()
    if ret == True:
        img = imutils.resize(img, width=400)
        img = H46TL1B(img)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        im = Image.fromarray(img)
        frame = ImageTk.PhotoImage(image=im)
        lblVideo.configure(image=frame)
        lblVideo.image = frame
        lblVideo.after(10, H46TL1B_visualizar)  # edit
    else:
        lblVideo.image = ""
        lblInfoVideoPath.configure(text="")
        rad1.configure(state="active")
        rad2.configure(state="active")
        selected.set(0)
        btnEnd.configure(state="disabled")
        cap.release()


def H46TL1B(img):  # edit
    from itertools import count
    count = 0

    def countfunc(count):
        global counter
        counter = counter + 1
        return counter
    while(1):  # For Model H36TL2 Blue
        lblInfo2 = Label(
            tab1, text=(counter), font="bold", bg='white', width=20, height=2)
        lblInfo2.place(relx=0.8, rely=0.24,
                       anchor="center")
        lblInfo3 = Label(
            tab1, text="Model: H46TL1B", font="bold", bg='white', width=20, height=2)
        lblInfo3.place(relx=0.8, rely=0.4,
                       anchor="center")
        blur = cv2.blur(img, (25, 25))
        hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)

        lower = np.array([94, 36, 134], np.uint8)
        upper = np.array([179, 255, 255], np.uint8)

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
        return img


def H46TL2B_visualizar():  # edit
    global cap
    ret, img = cap.read()
    if ret == True:
        img = imutils.resize(img, width=400)
        img = H46TL2B(img)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        im = Image.fromarray(img)
        frame = ImageTk.PhotoImage(image=im)
        lblVideo.configure(image=frame)
        lblVideo.image = frame
        lblVideo.after(10, H46TL2B_visualizar)  # edit
    else:
        lblVideo.image = ""
        lblInfoVideoPath.configure(text="")
        rad1.configure(state="active")
        rad2.configure(state="active")
        selected.set(0)
        btnEnd.configure(state="disabled")
        cap.release()


def H46TL2B(img):  # edit
    from itertools import count
    count = 0

    def countfunc(count):
        global counter
        counter = counter + 1
        return counter
    while(1):  # For Model H36TL2 Blue
        lblInfo2 = Label(
            tab1, text=(counter), font="bold", bg='white', width=20, height=2)
        lblInfo2.place(relx=0.8, rely=0.24,
                       anchor="center")
        lblInfo3 = Label(
            tab1, text="Model: H46TL2B", font="bold", bg='white', width=20, height=2)
        lblInfo3.place(relx=0.8, rely=0.4,
                       anchor="center")
        blur = cv2.blur(img, (25, 25))
        hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)

        lower = np.array([94, 36, 134], np.uint8)
        upper = np.array([179, 255, 255], np.uint8)

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
        return img
# ------ End of Manual Mode -------#


def Auto_visualizar():
    cap = cv2.VideoCapture(0)
    #global cap
    ret, img = cap.read()
    if ret == True:
        img = imutils.resize(img, width=400)
        img = steam(img)
        imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        im = Image.fromarray(imgGray)
        frame = ImageTk.PhotoImage(image=im)
        lblVideo.configure(image=frame)
        lblVideo.image = frame
        lblVideo.after(10, Auto_visualizar)
    else:
        lblVideo.image = ""
        lblInfoVideoPath.configure(text="")
        rad1.configure(state="active")
        rad2.configure(state="active")
        selected.set(0)
        btnEnd.configure(state="disabled")
        cap.release()


def steam(img):
    import cv2
    count = 0
    #** ---lower color detection ---#
    h_lower = 94
    s_lower = 36
    v_lower = 134
    #** ---upper color detection---#
    h_upper = 179
    s_upper = 255
    v_upper = 255
    #** ------------------------ **#
    count_1 = 0  # NOTE : Counter For Model 234500
    count_2 = 0  # NOTE : Counter For Model 123500
    count_3 = 0  # NOTE : Counter For Model H36TL2B
    count_4 = 0  # NOTE : Counter For Model H36TL1B
    count_5 = 0  # NOTE : Counter For Model H36TL2R
    count_6 = 0  # NOTE : Counter For Model H36TL2R

    #!! --- Define center point of detected --- !!#
    def center_point(x, y, w, h):
        ww = int(w/2)
        hh = int(h/2)
        cx = int(x+ww)
        cy = int(y+hh)
        return cx, cy
    #!!-------------------------------------------------------------------------------------#
    #** ---function for counter line--- **#

    def countfunc(count):  # For Model 1
        global counter
        counter = counter + 1
        return counter

    def countfunc_2(count):  # For Model 2
        global counter_2
        counter_2 = counter_2 + 1
        return counter_2

    #!! -- Define counter line--- !!#
    def x_line(img, percent):
        posit = int((img.shape[1]*percent)/100)
        left_line = posit - each_line
        right_line = posit + each_line
        return posit, left_line, right_line
#!!---------------------------------------#
    #success, img = cap.read()
    left_line = x_line(img, counter_line)[1] - each_line
    while(1):
        while(1):
            #success, img = cap.read()
            #imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            numberPlates = plateCascade .detectMultiScale(
                imgGray, scaleFactor=1.05, minNeighbors=7)
            for (x, y, w, h) in numberPlates:
                area1 = w * h
                #** --- Functions Detected Number Plate ---**#
                if area1 > minArea and data2 == 0:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
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
                #** --- End of Function Number plate ---**#
            #
            #
            #
            #** ---Functions ORC Number Plate---**#
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

                #** ---Main Confirm Function Start For First Run System--- **#
                if ("234500" in Model_number) == True:
                    def start_Model():
                        global start_Model_1
                        start_Model_1 = True
                        return start_Model_1
                    start_Model()
                    print("Model 234500 is detected")
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
                    def Reset():
                        global data2
                        data2 = 0
                        return data2
                    Reset()
                    break
                #
                #
                #
                #
                # NOTE : Production is detected
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
                    def start_Model6():  # For Model H36TL1 Product Red
                        global start_Model_6
                        start_Model_6 = True
                        return start_Model_6
                    start_Model6()
                    break
                elif ("H36TL2B" in Model_number) == True:
                    def Reset():
                        global data2
                        data2 = 0
                        return data2
                    Reset()
                    break
                # End of Product Detected

                #!! --- Not Found Model ---- !!#
                else:
                    print("Model Not Found")

                    def Reset():
                        global data2
                        data2 = 0
                        return data2
                    Reset()
                    break
            # **---End of Confirm Function Start---** #
            #
            #
            #
            # **---Start Model 1---** #
            while start_Model_1 == True:  # Model 234500
                blur = cv2.blur(img, (25, 25))
                hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)

                lower = np.array(
                    [h_lower, s_lower, v_lower], np.uint8)  # Define lower range of COLOR_BGR2GRAY
                upper = np.array(
                    [h_upper, s_upper, v_upper], np.uint8)  # Define upper range of COLOR_BGR2GRAY

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
                                    # countfunc(count)
                                    count_1 += 1
                                    cv2.line(img, (x_line(img, counter_line)[0], bord), (x_line(
                                        img, counter_line)[0], img.shape[0]-bord), (0, 250, 0), 5)
                            detect_line.remove((x, y))
                #** ---Functions main Reset --- **#
                imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                numberPlates = plateCascade .detectMultiScale(
                    imgGray, scaleFactor=1.05, minNeighbors=7)
                for (x, y, w, h) in numberPlates:
                    area1 = w * h
                    if area1 > minArea and Reset_Counters == False:
                        cv2.rectangle(img, (x, y), (x+w, y+h),
                                      (255, 255, 0), 2)
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
                            global count_1, count_2, count_3, count_4, count_5, count_6, Reset_Counters, start_Model_1, start_Model_2, start_Model_3, start_Model_4, start_Model_5, start_Model_6, data2, count, counter_2
                            Reset_Counters = False
                            start_Model_1 = True  # Model is True
                            start_Model_2 = False
                            start_Model_3 = False
                            start_Model_4 = False
                            start_Model_5 = False
                            start_Model_6 = False
                            data2 = 0
                            count = 0
                            count_1 = 0
                            count_2 = 0
                            count_3 = 0
                            count_4 = 0
                            count_5 = 0
                            count_6 = 0
                            counter_2 = 0
                            return count_1, count_2, count_3, count_4, count_5, count_6, Reset_Counters, start_Model_1, start_Model_2, start_Model_3, start_Model_4, start_Model_5, start_Model_6, data2, count, counter_2
                        Reset_1()
                        break
                    elif ("123432" in Model_Reset):
                        def H36TL2():
                            global count_1, count_2, count_3, count_4, count_5, count_6, Reset_Counters, start_Model_1, start_Model_2, start_Model_3, start_Model_4, start_Model_5, start_Model_6, data2, count, counter_2
                            Reset_Counters = False
                            start_Model_1 = False
                            start_Model_2 = True  # Model is True
                            start_Model_3 = False
                            start_Model_4 = False
                            start_Model_5 = False
                            start_Model_6 = False
                            data2 = 0
                            count = 0
                            count_1 = 0
                            count_2 = 0
                            count_3 = 0
                            count_4 = 0
                            count_5 = 0
                            count_6 = 0
                            counter_2 = 0
                            return count_1, count_2, count_3, count_4, count_5, count_6.Reset_Counters, start_Model_1, start_Model_2, start_Model_3, start_Model_4, start_Model_5, start_Model_6, data2, count, counter_2
                        H36TL2()
                        break
                    elif("360028" in Model_Reset):
                        def H36TL2B():
                            global count_1, count_2, count_3, count_4, count_5, count_6, Reset_Counters, start_Model_1, start_Model_2, start_Model_3, start_Model_4, start_Model_5, start_Model_6, data2, count, counter_2
                            Reset_Counters = False
                            start_Model_1 = False
                            start_Model_2 = False
                            start_Model_3 = True  # Model is True
                            start_Model_4 = False
                            start_Model_5 = False
                            start_Model_6 = False
                            data2 = 0
                            count = 0
                            count_1 = 0
                            count_2 = 0
                            count_3 = 0
                            count_4 = 0
                            count_5 = 0
                            count_6 = 0
                            counter_2 = 0
                            return count_1, count_2, count_3, count_4, count_5, count_6, Reset_Counters, start_Model_1, start_Model_2, start_Model_3, start_Model_4, start_Model_5, start_Model_6, data2, count, counter_2
                        H36TL2B()
                        break
                    elif("36001B" in Model_Reset):
                        def H36TL1B():
                            global count_1, count_2, count_3, count_4, count_5, count_6, Reset_Counters, start_Model_1, start_Model_2, start_Model_3, start_Model_4, start_Model_5, start_Model_6, data2, count, counter_2
                            Reset_Counters = False
                            start_Model_1 = False
                            start_Model_2 = False
                            start_Model_3 = False
                            start_Model_4 = True  # Model is True
                            start_Model_5 = False
                            start_Model_6 = False
                            data2 = 0
                            count = 0
                            count_1 = 0
                            count_2 = 0
                            count_3 = 0
                            count_4 = 0
                            count_5 = 0
                            count_6 = 0
                            counter_2 = 0
                            return count_1, count_2, count_3, count_4, count_5, count_6, Reset_Counters, start_Model_1, start_Model_2, start_Model_3, start_Model_4, start_Model_5, start_Model_6, data2, count, counter_2
                        H36TL1B()
                        break
                    elif("36002R" in Model_Reset):
                        def H36TL2R():
                            global count_1, count_2, count_3, count_4, count_5, count_6, Reset_Counters, start_Model_1, start_Model_2, start_Model_3, start_Model_4, start_Model_5, start_Model_6, data2, count, counter_2
                            Reset_Counters = False
                            start_Model_1 = False
                            start_Model_2 = False
                            start_Model_3 = False
                            start_Model_4 = False
                            start_Model_5 = True  # Model is True
                            start_Model_6 = False
                            data2 = 0
                            count = 0
                            count_1 = 0
                            count_2 = 0
                            count_3 = 0
                            count_4 = 0
                            count_5 = 0
                            count_6 = 0
                            counter_2 = 0
                            return count_1, count_2, count_3, count_4, count_5, count_6, Reset_Counters, start_Model_1, start_Model_2, start_Model_3, start_Model_4, start_Model_5, start_Model_6, data2, count, counter_2
                        H36TL2R()
                        break
                    elif("36001R" in Model_Reset):
                        def H36TL1R():
                            global count_1, count_2, count_3, count_4, count_5, count_6, Reset_Counters, start_Model_1, start_Model_2, start_Model_3, start_Model_4, start_Model_5, start_Model_6, data2, count, counter_2
                            Reset_Counters = False
                            start_Model_1 = False
                            start_Model_2 = False
                            start_Model_3 = False
                            start_Model_4 = False
                            start_Model_5 = False
                            start_Model_6 = True  # Model is True
                            data2 = 0
                            count = 0
                            count_1 = 0
                            count_2 = 0
                            count_3 = 0
                            count_4 = 0
                            count_5 = 0
                            count_6 = 0
                            counter_2 = 0
                            return count_1, count_2, count_3, count_4, count_5, count_6, Reset_Counters, start_Model_1, start_Model_2, start_Model_3, start_Model_4, start_Model_5, start_Model_6, data2, count, counter_2
                        H36TL1R()
                        break
                    else:
                        def Reset():
                            global data2
                            data2 = 0
                            return data2
                        Reset()

                        def Reset_1():
                            global count_1, count_2, count_3, count_4, count_5, count_6, Reset_Counters, start_Model_1, start_Model_2, start_Model_3, start_Model_4, start_Model_5, start_Model_6, data2, count, counter_2
                            Reset_Counters = False
                            start_Model_1 = False
                            start_Model_2 = False
                            start_Model_3 = False
                            start_Model_4 = False
                            start_Model_5 = False
                            start_Model_6 = False
                            data2 = 0
                            count = 0
                            count_1 = 0
                            count_2 = 0
                            count_3 = 0
                            count_4 = 0
                            count_5 = 0
                            count_6 = 0
                            counter_2 = 0
                            return count_1, count_2, count_3, count_4, count_5, count_6, Reset_Counters, start_Model_1, start_Model_2, start_Model_3, start_Model_4, start_Model_5, start_Model_6, data2, count, counter_2
                        Reset_1()
                        print("Model not found")
                        break
                cv2.putText(img, str(count_1), (550, 400),
                            cv2.FONT_HERSHEY_SIMPLEX, 2, text_color, 3, cv2.LINE_AA)
                cv2.putText(img, str("Model: 234500"), (20, 50),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2, cv2.LINE_AA)
                break
            #** -----------------------------------------Steam Show Counter System---------------------------------------------#
            cv2.imshow("IIOT-B14", img)
            if cv2.waitKey(1) & 0xFF == ord('s'):
                cv2.imwrite(
                    "\\IMAGE\\Model-"+str(count)+".jpg", img)
                cv2.rectangle(img, (0, 200), (640, 300),
                              (0, 255, 0), cv2.FILLED)
                cv2.putText(img, "Scan Number", (15, 265),
                            cv2.FONT_HERSHEY_COMPLEX, 2, (0, 0, 255), 2)
                cv2.waitKey(500)
                count += 1
                cap.release()
                cap.destroyAllWindows()
            if not success:
                break
            else:
                success, buffer = cv2.imencode('.jpg', img)
                img = buffer.tobytes()
                yield (b'--frame\r\n'
                       b'Content-Type: image/jpeg\r\n\r\n' + img + b'\r\n')


def Run_auto():
    global run
    run = True
    print(run)
    video()
    return run


def Exit_Programs():
    lblVideo.image = ""
    lblInfoVideoPath.configure(text="Test")
    rad1.configure(state="active")
    rad2.configure(state="active")
    rad3.configure(state="active")
    rad4.configure(state="active")
    rad5.configure(state="active")
    rad6.configure(state="active")
    my_tabs.add(tab2)
    selected.set(0)

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

# Header company
lblInfo1 = Label(
    tab1, text="SNC IIoT-B14 Steaming Paining Counter", font="bold")
lblInfo1.place(relx=0.5, rely=0.03, anchor="center")

header = Label(tab2, text="SNC IIoT-B14 Steaming Paining Counter", font="bold")
header.place(relx=0.5, rely=0.03, anchor="center")


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

rad1.place(relx=0.1, rely=0.1, anchor="center")
rad2.place(relx=0.25, rely=0.1, anchor="center")
rad3.place(relx=0.4, rely=0.1, anchor="center")
rad4.place(relx=0.55, rely=0.1, anchor="center")
rad5.place(relx=0.1, rely=0.15, anchor="center")
rad6.place(relx=0.25, rely=0.15, anchor="center")


ModelShow = Label(
    tab2, text=(counter), font="bold", bg='white', width=20, height=2)
ModelShow.place(relx=0.8, rely=0.24,
                anchor="center")
Showcounter = Label(
    tab2, text="Model: H46TL2B", font="bold", bg='white', width=20, height=2)
Showcounter.place(relx=0.8, rely=0.4,
                  anchor="center")

b2 = tk.Button(tab2, text="Run Auto", width=20,
               height=3, command=Run_auto, font="bold", bg='green')
b2.place(relx=0.8, rely=0.6,
         anchor="center")

lblInfoVideoPath = Label(tab1, text="", width=20)
lblInfoVideoPath.place(relx=0.2, rely=0.5, anchor="center")
lblVideo = Label(tab1)
lblVideo.place(relx=0.32, rely=0.5, anchor="center")
btnEnd = Button(tab1, text="Exit Programs",
                state="disabled", command=Exit_Programs)
btnEnd.place(relx=0.5, rely=0.9, anchor="center")
btnEnd1 = Button(tab2, text="Exit Programs",
                 state="disabled", command=Exit_Programs)
btnEnd1.place(relx=0.5, rely=0.9, anchor="center")
root.mainloop()
