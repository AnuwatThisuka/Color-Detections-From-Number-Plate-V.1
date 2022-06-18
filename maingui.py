import cv2
import tkinter as tk
from tkinter import *
from tkinter import ttk
my_w = tk.Tk()
my_w.geometry("700x500")

my_tabs = ttk.Notebook(my_w)  # declaring

tab1 = ttk.Frame(my_tabs)
tab2 = ttk.Frame(my_tabs)
tab3 = ttk.Frame(my_tabs)

my_tabs.add(tab1, text='Manual')  # adding tab
my_tabs.add(tab2, text='Auto')  # adding tab
my_tabs.add(tab3, text='Data History')  # adding tab
my_tabs.pack(expand=1, fill="both")


def run_auto():
    print("Auto")
    b1.configure(state="disabled")
    # import the opencv library
    # define a video capture object
    cap = cv2.VideoCapture(0)
    while(True):
        ret, frame = cap.read()
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()


l1 = tk.Label(tab1, text="SNC IIOT-B14 Steaming Paining Counter", font="bold")
l1.grid(column=0, row=0, columnspan=2, padx=150)
b1 = tk.Button(tab1, text='Run Auto', command=run_auto)
#b1 = tk.Button(tab1, text='STOP').grid(column=0, row=1)
b1.place(relx=0.85, rely=0.1, anchor=tk.NW)

l2 = tk.Label(tab2, text='I am tab-1', bg='yellow', width=10)
l2.grid(row=1, column=1)  # using grid
b2 = tk.Button(tab2, text='I am tab-1')
b2.grid(row=2, column=2)

l3 = tk.Label(tab3, text='I am tab-1', bg='yellow', width=10)
l3.grid(row=1, column=1)  # using grid
b3 = tk.Button(tab3, text='I am tab-1')
b3.grid(row=2, column=2)

my_w.mainloop()  # Keep the window open
