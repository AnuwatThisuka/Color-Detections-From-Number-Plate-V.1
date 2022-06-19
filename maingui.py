from faulthandler import disable
from tkinter import *
from tkinter import filedialog
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
        my_tabs.hide(tab2)
        lblInfoVideoPath.configure(text="")
        cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        H36TL1B_visualizar()
    if selected.get() == 2:
        btnEnd.configure(state="active")
        rad1.configure(state="disabled")
        rad2.configure(state="disabled")
        rad3.configure(state="disabled")
        rad4.configure(state="disabled")
        rad5.configure(state="disabled")
        rad6.configure(state="disabled")
        lblInfoVideoPath.configure(text="")
        cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        H36TL2B_visualizar()
    if selected.get() == 3:
        btnEnd.configure(state="active")
        rad1.configure(state="disabled")
        rad2.configure(state="disabled")
        rad3.configure(state="disabled")
        rad4.configure(state="disabled")
        rad5.configure(state="disabled")
        rad6.configure(state="disabled")
        lblInfoVideoPath.configure(text="")
        cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        H36TL1R_visualizar()
    if selected.get() == 4:
        btnEnd.configure(state="active")
        rad1.configure(state="disabled")
        rad2.configure(state="disabled")
        rad3.configure(state="disabled")
        rad4.configure(state="disabled")
        rad5.configure(state="disabled")
        rad6.configure(state="disabled")
        lblInfoVideoPath.configure(text="")
        cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        H36TL2R_visualizar()
    if selected.get() == 5:
        btnEnd.configure(state="active")
        rad1.configure(state="disabled")
        rad2.configure(state="disabled")
        rad3.configure(state="disabled")
        rad4.configure(state="disabled")
        rad5.configure(state="disabled")
        rad6.configure(state="disabled")
        lblInfoVideoPath.configure(text="")
        cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        H46TL1B_visualizar()
    if selected.get() == 6:
        btnEnd.configure(state="active")
        rad1.configure(state="disabled")
        rad2.configure(state="disabled")
        rad3.configure(state="disabled")
        rad4.configure(state="disabled")
        rad5.configure(state="disabled")
        rad6.configure(state="disabled")
        lblInfoVideoPath.configure(text="")
        cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        H46TL2B_visualizar()


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

lblInfo1 = Label(
    tab1, text="SNC IIoT-B14 Steaming Paining Counter", font="bold")
lblInfo1.place(relx=0.5, rely=0.03, anchor="center")


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


b2 = tk.Button(tab2, text='Run Auto', width=20, command=video)
b2.grid(row=2, column=2)

lblInfoVideoPath = Label(tab1, text="", width=20)
lblInfoVideoPath.place(relx=0.2, rely=0.5, anchor="center")
lblVideo = Label(tab1)
lblVideo.place(relx=0.32, rely=0.5, anchor="center")
btnEnd = Button(tab1, text="Exit Programs",
                state="disabled", command=Exit_Programs)
btnEnd.place(relx=0.5, rely=0.9, anchor="center")
root.mainloop()
