from tkinter import *
from tkinter import font

g_Tk = Tk()
g_Tk.geometry("800x600+750+200")

def InitTopText():
    TempFont = font.Font(g_Tk, size=20, weight='bold', family='consolas')
    MainText = Label(g_Tk, font=TempFont, text='[대기 현황 검색 APP]')
    MainText.pack()
    MainText.place(x=260)



InitTopText()

g_Tk.mainloop()