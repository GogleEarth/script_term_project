from tkinter import *
from tkinter import ttk
from tkinter import font
from data import *
from divide import *
import realtime_search
import monthly_search
import badair_search
import sendmail

window = Tk()
window.title("대기 현황 APP")
window.geometry("1000x600")
window.resizable(False, False)

service_key = 'fD%2FcMGFxBktwTG9%2BdUNuSZG%2FCnhfGOUAeEXyQUz6woSWm3JNpQazLAdKEmDuuYd7XZAmOnf6kWcWt49MrbnqcQ%3D%3D'

database = []
maildatalist = []
mailflag = 0
monthlyflag = 2

frame2 = Frame(window, width=580, height=600)
frame2.pack(side='right')
frame2.propagate(0)

canvas = Canvas(frame2, width=540, height=400, bg='white', borderwidth='10', relief='ridge')
canvas.pack()
canvas.place(x=0, y=10)

def drawgraph(canvas,data):
    global frame_on,frame2
    TempFont = font.Font(frame2, size=12, weight='bold', family='Consolas')

    frame2.destroy()
    frame2 = Frame(window, width=600, height=600)
    frame2.pack(side='right')
    frame2.propagate(0)

    canvas = Canvas(frame2, width=540, height=400, bg='white', borderwidth='10', relief='ridge')
    canvas.pack()
    canvas.place(x=10, y=10)

    NameFont = font.Font(frame2, size=25, weight='bold', family='Consolas')
    namelabel = Label(frame2, font=NameFont, text=data.station+'의 대기 현황 그래프')
    namelabel.pack()
    namelabel.place(x=30, y=500)

    so2coord = 55,400,55,400-data.so2*3000
    so2line = canvas.create_line(so2coord, width=15, fill='yellow')
    so2valuelabel = Label(canvas, font=TempFont, text='{0:.3f}'.format(data.so2))
    so2valuelabel.pack()
    so2valuelabel.place(x=30, y=400-data.so2*3000-30)

    cocoord = 145,400,145,400-data.co*300
    coline = canvas.create_line(cocoord, width=15, fill='yellow')
    covaluelabel = Label(canvas, font=TempFont, text='{0:.3f}'.format(data.co))
    covaluelabel.pack()
    covaluelabel.place(x=125, y=400-data.co*300-30)

    o3coord = 235,400,235,400-data.o3*3000
    o3line = canvas.create_line(o3coord, width=15, fill='yellow')
    o3valuelabel = Label(canvas, font=TempFont, text='{0:.3f}'.format(data.o3))
    o3valuelabel.pack()
    o3valuelabel.place(x=210, y=400-data.o3*3000-30)

    no2coord = 325,400,325,400-data.no2*3000
    no2line = canvas.create_line(no2coord, width=15, fill='yellow')
    no2valuelabel = Label(canvas, font=TempFont, text='{0:.3f}'.format(data.no2))
    no2valuelabel.pack()
    no2valuelabel.place(x=300, y=400-data.no2*3000-30)

    pm10coord = 415,400,415,400-data.pm10
    pm10line = canvas.create_line(pm10coord, width=15, fill='red')
    pm10valuelabel = Label(canvas, font=TempFont, text=data.pm10)
    pm10valuelabel.pack()
    pm10valuelabel.place(x=405, y=400-data.pm10-30)

    pm25coord = 505,400,505,400-data.pm25
    pm25line = canvas.create_line(pm25coord, width=15, fill='red')
    pm25valuelabel = Label(canvas, font=TempFont, text=data.pm25)
    pm25valuelabel.pack()
    pm25valuelabel.place(x=495, y=400-data.pm25-30)

    so2label = Label(canvas, font=TempFont, text='아황산')
    so2label.pack()
    so2label.place(x=30, y=400)

    colabel = Label(canvas, font=TempFont, text='일산화탄소')
    colabel.pack()
    colabel.place(x=105, y=400)

    o3label = Label(canvas, font=TempFont, text='오존')
    o3label.pack()
    o3label.place(x=215, y=400)

    no2label = Label(canvas, font=TempFont, text='이산화질소')
    no2label.pack()
    no2label.place(x=285, y=400)

    pm10label = Label(canvas, font=TempFont, text='미세먼지')
    pm10label.pack()
    pm10label.place(x=385, y=400)

    pm25label = Label(canvas, font=TempFont, text='초미세먼지')
    pm25label.pack()
    pm25label.place(x=465, y=400)

def InitTopText():
    TempFont = font.Font(window, size=20, weight='bold', family='consolas')
    MainText = Label(window, font=TempFont, text='[대기 현황 검색 APP]')
    MainText.pack()
    MainText.place(x=60)

def InitInputLabel():
    global Name1Label,Name2Label,MonthLabel, AddrLabel1, AddrLabel2, AddrLabel3\
        , realtap, monthtap, badtap

    TempFont = font.Font(realtap, size=15, weight='bold', family = 'Consolas')
    Text = Label(realtap, font=TempFont, text='측정소\n입력')
    Text.pack()
    Text.place(x=15,y=10)
    Name1Label = Entry(realtap, font=TempFont, width=15, borderwidth=12, relief='ridge')
    Name1Label.pack()
    Name1Label.place(x=100, y=10)

    Text = Label(realtap, font=TempFont, text='메일 주소')
    Text.pack()
    Text.place(x=10,y=90)
    AddrLabel1 = Entry(realtap, width=20, borderwidth=10, relief='ridge')
    AddrLabel1.pack()
    AddrLabel1.place(x=110, y=84)

    Text = Label(monthtap, font=TempFont, text='측정소\n입력')
    Text.pack()
    Text.place(x=15,y=10)
    Name2Label = Entry(monthtap, font=TempFont, width=15, borderwidth=12, relief='ridge')
    Name2Label.pack()
    Name2Label.place(x=100, y=10)

    Text = Label(monthtap, font=TempFont, text='월 입력(01~12)')
    Text.pack()
    Text.place(x=15,y=75)
    MonthLabel = Entry(monthtap, font=TempFont, width=10, borderwidth=12, relief='ridge')
    MonthLabel.pack()
    MonthLabel.place(x=180, y=64)

    Text = Label(monthtap, font=TempFont, text='메일 주소')
    Text.pack()
    Text.place(x=10,y=125)
    AddrLabel2 = Entry(monthtap, width=20, borderwidth=10, relief='ridge')
    AddrLabel2.pack()
    AddrLabel2.place(x=110, y=119)

    Text = Label(badtap, font=TempFont, text='메일 주소')
    Text.pack()
    Text.place(x=10,y=90)
    AddrLabel3 = Entry(badtap, width=20, borderwidth=10, relief='ridge')
    AddrLabel3.pack()
    AddrLabel3.place(x=110, y=84)

def InitListBox():
    global monthtap, badtap, list1, list2
    list1 = Listbox(monthtap,width=15,height=17, borderwidth=12, relief='ridge')
    list1.pack()
    list1.place(y=200)

    SearchButton1 = Button(monthtap, text="조회",command = ListClick1)
    SearchButton1.pack()
    SearchButton1.place(x=110, y=200)

    list2 = Listbox(badtap,width=15,height=17, borderwidth=12, relief='ridge')
    list2.pack()
    list2.place(y=200)

    SearchButton2 = Button(badtap, text="조회",command = ListClick2)
    SearchButton2.pack()
    SearchButton2.place(x=110, y=200)

def InitSearchButton():
    global realtap, monthtap, badtap

    TempFont = font.Font(realtap, size=12, weight='bold', family = 'Consolas')
    SearchButton = Button(realtap, font = TempFont, text="검색",command = SearchButtonAction1)
    SearchButton.pack()
    SearchButton.place(x=310, y=16)

    TempFont = font.Font(monthtap, size=12, weight='bold', family = 'Consolas')
    SearchButton = Button(monthtap, font = TempFont, text="검색",command = SearchButtonAction2)
    SearchButton.pack()
    SearchButton.place(x=310, y=16)

    TempFont = font.Font(badtap, size=12, weight='bold', family = 'Consolas')
    SearchButton = Button(badtap, font = TempFont, text="검색",command = SearchButtonAction3)
    SearchButton.pack()
    SearchButton.place(x=170, y=10)

def InitMailButton():
    global realtap, monthtap, badtap

    TempFont = font.Font(realtap, size=12, weight='bold', family = 'Consolas')
    SearchButton = Button(realtap, font = TempFont, text="메일보내기",command = MailButtonAction)
    SearchButton.pack()
    SearchButton.place(x=280, y=85)

    TempFont = font.Font(monthtap, size=12, weight='bold', family = 'Consolas')
    SearchButton = Button(monthtap, font = TempFont, text="메일보내기",command = MailButtonAction)
    SearchButton.pack()
    SearchButton.place(x=280, y=119)

    TempFont = font.Font(badtap, size=12, weight='bold', family = 'Consolas')
    SearchButton = Button(badtap, font = TempFont, text="메일보내기",command = MailButtonAction)
    SearchButton.pack()
    SearchButton.place(x=280, y=85)

def InitNoteBook():
    global note, realtap, monthtap, badtap

    note = ttk.Notebook(window, width=380, height=500)

    realtap = Frame(note)
    note.add(realtap, text='실시간 검색')

    monthtap = Frame(note)
    note.add(monthtap, text='월별 검색')

    badtap = Frame(note)
    note.add(badtap, text='대기상태나쁨조회')

    note.pack(expand=1, fill='both')
    note.place(x=10, y=50)

def RenderReady_realtime(data):
    global RenderText1

    data.print_data(RenderText1)

def InitRenderText():
    global RenderText1, RenderText2, RenderText3, realtap, monthtap, badtap

    RenderText1 = Text(realtap, width=49, height=20, borderwidth=12, relief='ridge')
    RenderText1.pack()
    RenderText1.place(x=5, y=200)

    RenderText2 = Text(monthtap, width=30, height=21, borderwidth=12, relief='ridge')
    RenderText2.pack()
    RenderText2.place(x=130, y=200)

    RenderText3 = Text(badtap, width=30, height=21, borderwidth=12, relief='ridge')
    RenderText3.pack()
    RenderText3.place(x=130, y=200)

def SearchButtonAction1():
    global canvas,maildatalist,mailflag,Name1Label,RenderText1,database,realtap

    RenderText1.configure(state='normal')
    RenderText1.delete(0.0, END)
    mailflag = 0
    maildatalist.clear()
    data = realtime_search.realtime_search(service_key,Name1Label.get())
    RenderReady_realtime(data)
    maildatalist.append(data)
    drawgraph(canvas,data)

    database.clear()

def SearchButtonAction2():
    global canvas,maildatalist,mailflag,Name2Label,RenderText2,monthlyflag,list1,MonthLabel,database

    list1.delete(0,'end')
    RenderText2.delete(1.0,END)
    newlist = []
    database.clear()
    maildatalist.clear()
    monthly_search.monthly_search(service_key,Name2Label.get(),database)
    if monthlyflag == 1:
        mailflag = 1
        for data in database:
            if data.month == MonthLabel.get():
                maildatalist.append(data)
                list1.insert('end', data.date+'일'+data.hour+'시')
    elif monthlyflag == 2:
        mailflag = 2
        newlist = day_devide(database,MonthLabel.get())
        for data in newlist:
            maildatalist.append(data)
            list1.insert('end', data.date+'일 평균')
    elif monthlyflag == 3:
        mailflag = 3
        data = month_devide(database,MonthLabel.get())
        maildatalist.append(data)
        list1.insert('end', data.month+'월 평균')

def SearchButtonAction3():
    global canvas,maildatalist,mailflag,list2

    list2.delete(0,'end')
    database.clear()
    maildatalist.clear()
    mailflag = 4
    badair_search.badair_search(service_key,database)

    for data in database:
        list2.insert('end',data)

def MailButtonAction():
    global maildatalist,mailflag,AddrLabel1, AddrLabel2, AddrLabel3

    senderAddr = "dkekfps1@gmail.com"
    password = "ss073508!!"
    recAddr = ''

    if mailflag == 0:
        recAddr = AddrLabel1.get()
    elif mailflag == 4:
        recAddr = AddrLabel3.get()
    else:
        recAddr = AddrLabel2.get()

    print(maildatalist)

    if len(maildatalist) > 0:
        sendmail.send_mail(senderAddr, password, recAddr, maildatalist, mailflag)

def InitRadioButton():
    global monthtap
    TempFont = font.Font(monthtap, size=13, family='Consolas')

    rad1 = Radiobutton(monthtap, text='시간대', value=1, font=TempFont, command=SelectRadio1)
    rad1.pack()
    rad1.place(x=30,y=170)

    rad2 = Radiobutton(monthtap, text='일 평균', value=2, font=TempFont, command=SelectRadio2)
    rad2.pack()
    rad2.place(x=135,y=170)

    rad3 = Radiobutton(monthtap, text='월 평균', value=3, font=TempFont, command=SelectRadio3)
    rad3.pack()
    rad3.place(x=240,y=170)

def SelectRadio1():
    global monthlyflag

    monthlyflag = 1

def SelectRadio2():
    global monthlyflag

    monthlyflag = 2

def SelectRadio3():
    global monthlyflag

    monthlyflag = 3

def ListClick1():
    global list1, RenderText2, maildatalist, monthlyflag

    RenderText2.delete(1.0,END)
    data = list1.curselection()[0]
    if monthlyflag == 1:
        maildatalist[data].print_data(RenderText2)
    elif monthlyflag == 2:
        maildatalist[data].print_data_dayaver(RenderText2)
    elif monthlyflag == 3:
        maildatalist[data].print_data_monthaver(RenderText2)

    drawgraph(canvas, maildatalist[data])

def ListClick2():
    global list2, RenderText3, maildatalist, canvas, database

    RenderText3.delete(1.0,END)
    data = list2.curselection()[0]
    print(data)

    info = realtime_search.realtime_search(service_key,database[data])
    info.print_data(RenderText3)

    flag = True
    for data in maildatalist:
        if info.station == data.station:
            flag = False

    if flag:
        maildatalist.append(info)

    drawgraph(canvas,info)


InitNoteBook()
InitInputLabel()
InitTopText()
InitMailButton()
InitRenderText()
InitSearchButton()
InitRadioButton()
InitListBox()

window.mainloop()