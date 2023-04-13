from tkinter import *

window=Tk()

window.title("First Window Tkinter")
window.minsize(width=500,height=400)
label_1=Label(text="I am a label", font=("Arial",16, "bold"))
label_1.pack()
label_1.config(text="New TEXT")


def button_clicked():
    label_1.config(text="I got click")

button_1=Button(text="Click Me", command=button_clicked)
button_1.pack()

window.mainloop()