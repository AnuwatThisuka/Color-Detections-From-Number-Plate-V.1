import tkinter as tk
root = tk.Tk()

root.overrideredirect(True)
root.overrideredirect(False)
root.attributes('-fullscreen', True)
root.title("FullScreen")
label = tk.Label(
    root, text="Hello! Press 🪟 logo on the keypad > select the python logo > Close window to close")
labela = tk.Label(root, text="🎉🎉🎉")
label.pack()
labela.pack()

root.mainloop()
