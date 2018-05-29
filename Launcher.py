from tkinter import *
from tkinter import font
from data import *
import realtime_search
import monthly_search
import badair_search

window = Tk()
window.title("대기 현황 APP")
window.geometry("400x600")
service_key = 'fD%2FcMGFxBktwTG9%2BdUNuSZG%2FCnhfGOUAeEXyQUz6woSWm3JNpQazLAdKEmDuuYd7XZAmOnf6kWcWt49MrbnqcQ%3D%3D'
database = []
Days = ['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31']
frame_on = False

frame1 = Frame(window, width=400, height=600)
frame1.pack(side='left')
frame1.propagate(0)

frame2 = Frame(window, width=600, height=600)
frame2.pack(side='right')
frame2.propagate(0)

canvas = Canvas(frame2, width=540, height=400, bg='white', borderwidth='10', relief='ridge')
canvas.pack()
canvas.place(x=10, y=10)

def show_graph():
    global frame_on
    if not frame_on:
        frame_on = True
    else:
        frame_on = False

    if frame_on:
        window.geometry("1000x600")
    else:
        window.geometry("400x600")

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

    if frame_on:
        NameFont = font.Font(frame2, size=25, weight='bold', family='Consolas')
        namelabel = Label(frame2, font=NameFont, text=data.station+'의 대기 현황 그래프')
        namelabel.pack()
        namelabel.place(x=30, y=500)

        so2coord = 55,400,55,400-data.so2*100
        so2line = canvas.create_line(so2coord, width=15, fill='red')
        so2valuelabel = Label(canvas, font=TempFont, text=data.so2)
        so2valuelabel.pack()
        so2valuelabel.place(x=30, y=400-data.so2*100-30)

        cocoord = 145,400,145,400-data.co*100
        coline = canvas.create_line(cocoord, width=15, fill='red')
        covaluelabel = Label(canvas, font=TempFont, text=data.co)
        covaluelabel.pack()
        covaluelabel.place(x=125, y=400-data.co*100-30)

        o3coord = 235,400,235,400-data.o3*100
        o3line = canvas.create_line(o3coord, width=15, fill='red')
        o3valuelabel = Label(canvas, font=TempFont, text=data.o3)
        o3valuelabel.pack()
        o3valuelabel.place(x=210, y=400-data.o3*100-30)

        no2coord = 325,400,325,400-data.no2*100
        no2line = canvas.create_line(no2coord, width=15, fill='red')
        no2valuelabel = Label(canvas, font=TempFont, text=data.no2)
        no2valuelabel.pack()
        no2valuelabel.place(x=300, y=400-data.no2*100-30)

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

def month_devide(database,month):
    name = ''
    time = ''
    so2 = 0
    co = 0
    o3 = 0
    no2 = 0
    pm10 = 0
    pm25 = 0
    cnt = 0
    for ele in database:
        if ele.month == month:
            time = ele.year+'-'+ele.month+'-'+ele.date+'-'+'평균'
            name = ele.station
            so2 += ele.so2
            co += ele.co
            o3 += ele.o3
            no2 += ele.no2
            pm10 += ele.pm10
            pm25 += ele.pm25
            cnt += 1
    if cnt > 0:
        res = data(name,time,so2/cnt,co/cnt,o3/cnt,no2/cnt,pm10/cnt,pm25/cnt)
        return res

def day_devide(database,month):
    global Days
    name = ''
    time = ''
    so2 = 0
    co = 0
    o3 = 0
    no2 = 0
    pm10 = 0
    pm25 = 0
    cnt = 0
    res = []
    for day in Days:
        for ele in database:
            if ele.date == day and ele.month == month:
                time = ele.year+'-'+ele.month+'-'+ele.date+'-'+'평균'
                name = ele.station
                so2 += ele.so2
                co += ele.co
                o3 += ele.o3
                no2 += ele.no2
                pm10 += ele.pm10
                pm25 += ele.pm25
                cnt += 1

        if cnt > 0:
            res.append(data(name,time,so2/cnt,co/cnt,o3/cnt,no2/cnt,pm10/cnt,pm25/cnt))
            time = ''
            so2 = 0
            co = 0
            o3 = 0
            no2 = 0
            pm10 = 0
            pm25 = 0
            cnt = 0

    return res

def InitTopText():
    TempFont = font.Font(frame1, size=20, weight='bold', family='consolas')
    MainText = Label(frame1, font=TempFont, text='[대기 현황 검색 APP]')
    MainText.pack()
    MainText.place(x=60)

def InitInputLabel():
    global NameLabel,MonthLabel,TypeLabel

    TempFont = font.Font(frame1, size=15, weight='bold', family = 'Consolas')
    Text = Label(frame1, font=TempFont, text='측정소\n입력')
    Text.pack()
    Text.place(x=15,y=100)
    NameLabel = Entry(frame1, font=TempFont, width=15, borderwidth=12, relief='ridge')
    NameLabel.pack()
    NameLabel.place(x=110, y=100)

    Text = Label(frame1, font=TempFont, text='월 입력\n(최근 3개월)')
    Text.pack()
    Text.place(x=15,y=150)
    MonthLabel = Entry(frame1, font=TempFont, width=8, borderwidth=12, relief='ridge')
    MonthLabel.pack()
    MonthLabel.place(x=150, y=150)

    Text = Label(frame1, font=TempFont, text='출력 방법\n(시,일,월)')
    Text.pack()
    Text.place(x=15,y=200)
    TypeLabel = Entry(frame1, font=TempFont, width=8, borderwidth=12, relief='ridge')
    TypeLabel.pack()
    TypeLabel.place(x=150, y=200)

def InitSearchButton():
    TempFont = font.Font(frame1, size=12, weight='bold', family = 'Consolas')
    SearchButton = Button(frame1, font = TempFont, text="검색",command = SearchButtonAction)
    SearchButton.pack()
    SearchButton.place(x=330, y=106)

def RenderReady_realtime(database):
    if len(database):
        for data in database:
            data.print_data(RenderText)
    else:
        RenderText.insert(INSERT, "데이터가 없습니다.")

def RenderReady_time(database,month):
    if len(database):
        for data in database:
            if data.month == month:
                data.print_data(RenderText)
    else:
        RenderText.insert(INSERT, "데이터가 없습니다.")

def RenderReady_day(database):
    if len(database):
        for data in database:
            data.print_data_dayaver(RenderText)
    else:
        RenderText.insert(INSERT, "데이터가 없습니다.")

def RenderReady_month(data):
    data.print_data_monthaver(RenderText)

def InitRenderText():
    global RenderText

    RenderTextScrollbar = Scrollbar(window)
    RenderTextScrollbar.pack()
    RenderTextScrollbar.place(x=375, y=200)
    TempFont = font.Font(frame1, size=10, family='Consolas')
    RenderText = Text(frame1, width=49, height=20, borderwidth=12, relief='ridge', yscrollcommand=RenderTextScrollbar.set)
    RenderText.pack()
    RenderText.place(x=10, y=300)
    RenderTextScrollbar.config(command=RenderText.yview)
    RenderTextScrollbar.pack(side=RIGHT, fill=BOTH)
    RenderText.configure(state='disabled')

def InitSearchListBox():
    global SearchListBox

    ListBoxScrollbar = Scrollbar(frame1)
    ListBoxScrollbar.pack()
    ListBoxScrollbar.place(x=255, y=50)

    TempFont = font.Font(frame1, size=15, weight='bold', family='Consolas')
    SearchListBox = Listbox(frame1, font=TempFont, activestyle='none', width=20, height=1, borderwidth=12, relief='ridge', yscrollcommand=ListBoxScrollbar.set)

    SearchListBox.insert(END, "실시간 검색")
    SearchListBox.insert(END, "월별 검색")
    SearchListBox.insert(END, "대기상태 나쁨 조회")
    SearchListBox.pack()
    SearchListBox.place(x=10, y=50)
    ListBoxScrollbar.config(command=SearchListBox.yview)

def SearchButtonAction():
    global SearchListBox,canvas

    RenderText.configure(state='normal')
    RenderText.delete(0.0, END)
    Index = SearchListBox.curselection()[0]
    if Index == 0:
        realtime_search.realtime_search(service_key,NameLabel.get(),database)
        RenderReady_realtime(database)
        data = database[0]
        drawgraph(canvas,data)
    elif Index == 1:
        newlist = []
        monthly_search.monthly_search(service_key,NameLabel.get(),database)
        if TypeLabel.get() == '시':
            RenderReady_time(database,MonthLabel.get())
        elif TypeLabel.get() == '일':
            newlist = day_devide(database,MonthLabel.get())
            RenderReady_day(newlist)
        elif TypeLabel.get() == '월':
            RenderReady_month(month_devide(database,MonthLabel.get()))
    elif Index == 2:
        badair_search.badair_search(service_key,database)
        newdb = []
        for name in database:
            realtime_search.realtime_search(service_key,name,newdb)
        RenderReady_realtime(newdb)

    database.clear()
    print(len(database))
    RenderText.configure(state='disabled')

def InitShowGraphButton():
    TempFont = font.Font(frame1, size=12, weight='bold', family = 'Consolas')
    button = Button(frame1, font=TempFont, text='그래프 보기', command=show_graph)
    button.pack()
    button.place(x=290, y=160)

InitTopText()
InitInputLabel()
InitSearchButton()
InitRenderText()
InitSearchListBox()
InitShowGraphButton()

window.mainloop()