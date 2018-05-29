from tkinter import *


frame_on = False

def com():
    global frame_on
    if not frame_on:
        frame_on = True
    else:
        frame_on = False

    if frame_on:
        window.geometry("800x600")
        frame2 = Frame(window, bg='blue', width=400, height=600)
        frame2.pack(side='right')
    else:
        window.geometry("400x600")


window = Tk()
window.title("name")
window.geometry("400x600")


frame1 = Frame(window,bg='red',width=400,height=600)
frame1.pack(side='left')
frame1.propagate(0)

button = Button(frame1, text='click',command=com)
button.pack()



window.mainloop()