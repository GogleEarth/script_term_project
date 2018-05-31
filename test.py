from tkinter import *

window = Tk()
window.title("name")
window.geometry("400x600")

frame = Frame(window, width=600, height=600)
frame.pack()

canvas = Canvas(frame, width=355, height=555, bg='white', borderwidth='10', relief='ridge')
canvas.pack()
canvas.place(x=10, y=10)

grape_coord1 = 55,570,55,570-150
grape1 = canvas.create_line(grape_coord1, width=15, fill='red')

grape_coord2 = 110,570,110,570-200
grape2 = canvas.create_line(grape_coord2, width=15, fill='blue')

grape_coord3 = 165,570,165,570-100
grape3 = canvas.create_line(grape_coord3, width=15, fill='yellow')

grape_coord4 = 220,570,220,570-50
grape4 = canvas.create_line(grape_coord4, width=15, fill='green')

grape_coord5 = 275,570,275,570-500
grape5 = canvas.create_line(grape_coord5, width=15, fill='pink')

grape_coord6 = 330,570,330,570-350
grape6 = canvas.create_line(grape_coord6, width=15, fill='black')

window.mainloop()