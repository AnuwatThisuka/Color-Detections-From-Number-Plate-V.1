import tkinter as tk
from tkinter import ttk


root = tk.Tk()
root.title("Tab Widget")
tabControl = ttk.Notebook(root)

tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)
tab3 = ttk.Frame(tabControl)

tabControl.add(tab1, text='Auto')
tabControl.add(tab2, text='Manual')
tabControl.add(tab3, text='Data History')
tabControl.pack(expand=1, fill="both")

tap_auto = ttk.Label(tab1, text="Tab 1").grid(
    column=0, row=0, padx=100, pady=60)
tap_manual = ttk.Label(tab2, text="Tab 2").grid(
    column=0, row=0, padx=100, pady=60)
tap_data_history = ttk.Label(tab3, text="Tab 3").grid(
    column=0, row=0, padx=100, pady=60)


root.mainloop()
