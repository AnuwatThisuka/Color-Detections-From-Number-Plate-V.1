from tkinter import *
from tkinter import filedialog
from PIL import Image
from PIL import ImageTk
import cv2
import imutils
import tkinter as tk
from tkinter import ttk

faceClassif = cv2.CascadeClassifier("haarcascade_russian_plate_number.xml")

cap = None
root = tk.Tk()
my_tabs = ttk.Notebook(root)  # declaring
root.title("SNC IIoT-B14 Steaming Paining Counter")
root.geometry("700x500")


def video():
    global cap
    if selected.get() == 1:
        print("Seleccionado: test")
    if selected.get() == 2:
        btnEnd.configure(state="active")
        rad1.configure(state="disabled")
        rad2.configure(state="disabled")
        lblInfoVideoPath.configure(text="")
        cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        visualizar()


def visualizar():
    global cap
    ret, frame = cap.read()
    if ret == True:
        frame = imutils.resize(frame, width=400)
        frame = deteccion_facilal(frame)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        im = Image.fromarray(frame)
        img = ImageTk.PhotoImage(image=im)
        lblVideo.configure(image=img)
        lblVideo.image = img
        lblVideo.after(10, visualizar)
    else:
        lblVideo.image = ""
        lblInfoVideoPath.configure(text="")
        rad1.configure(state="active")
        rad2.configure(state="active")
        selected.set(0)
        btnEnd.configure(state="disabled")
        cap.release()


def deteccion_facilal(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceClassif.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    return frame


def finalizar_limpiar():
    lblVideo.image = ""
    lblInfoVideoPath.configure(text="")
    rad1.configure(state="active")
    rad2.configure(state="active")
    selected.set(0)
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
lblInfo1.place(x=180, y=10)
lblInfo2 = Label(
    tab1, text="Counter", font="bold")
lblInfo2.grid(column=0, row=3, padx=2, pady=10)
selected = IntVar()
rad1 = Radiobutton(tab1, text="Manual", width=20, value=1,
                   variable=selected, command=video)
rad2 = Radiobutton(tab1, text="Auto", width=20, value=2,
                   variable=selected, command=video)
rad1.place(x=180, y=50)
rad2.place(x=200, y=50)
lblInfoVideoPath = Label(tab1, text="", width=20)
lblInfoVideoPath.grid(column=0, row=2)
lblVideo = Label(tab1)
lblVideo.grid(column=0, row=3, columnspan=2)
btnEnd = Button(tab1, text="Exit Programs",
                state="disabled", command=finalizar_limpiar)
btnEnd.grid(column=0, row=4, columnspan=2, pady=10)
root.mainloop()
