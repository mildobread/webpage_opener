import tkinter as tk

def button_clicked():
    print("Button Clicked")

root = tk.Tk()

button = tk.Button(root, text="Click Me")
button.pack()

button.bind("<Button-1>", lambda event: button_clicked())

root.mainloop()