from tkinter import *
from tkinter import font
from data import *
import realtime_search
import monthly_search
import badair_search

window = Tk()
window.title("대기 현황 APP")
window.geometry("400x600+750+200")
service_key = 'fD%2FcMGFxBktwTG9%2BdUNuSZG%2FCnhfGOUAeEXyQUz6woSWm3JNpQazLAdKEmDuuYd7XZAmOnf6kWcWt49MrbnqcQ%3D%3D'
database = []
Days = ['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31']


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
    TempFont = font.Font(window, size=20, weight='bold', family='consolas')
    MainText = Label(window, font=TempFont, text='[대기 현황 검색 APP]')
    MainText.pack()
    MainText.place(x=60)

def InitInputLabel():
    global NameLabel,MonthLabel,TypeLabel

    TempFont = font.Font(window, size=15, weight='bold', family = 'Consolas')
    Text = Label(window, font=TempFont, text='측정소\n입력')
    Text.pack()
    Text.place(x=15,y=100)
    NameLabel = Entry(window, font=TempFont, width=15, borderwidth=12, relief='ridge')
    NameLabel.pack()
    NameLabel.place(x=110, y=100)

    Text = Label(window, font=TempFont, text='월 입력\n(최근 3개월)')
    Text.pack()
    Text.place(x=15,y=150)
    MonthLabel = Entry(window, font=TempFont, width=8, borderwidth=12, relief='ridge')
    MonthLabel.pack()
    MonthLabel.place(x=150, y=150)

    Text = Label(window, font=TempFont, text='출력 방법\n(시,일,월)')
    Text.pack()
    Text.place(x=15,y=200)
    TypeLabel = Entry(window, font=TempFont, width=8, borderwidth=12, relief='ridge')
    TypeLabel.pack()
    TypeLabel.place(x=150, y=200)

def InitSearchButton():
    TempFont = font.Font(window, size=12, weight='bold', family = 'Consolas')
    SearchButton = Button(window, font = TempFont, text="검색",command = SearchButtonAction)
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
    TempFont = font.Font(window, size=10, family='Consolas')
    RenderText = Text(window, width=49, height=20, borderwidth=12, relief='ridge', yscrollcommand=RenderTextScrollbar.set)
    RenderText.pack()
    RenderText.place(x=10, y=300)
    RenderTextScrollbar.config(command=RenderText.yview)
    RenderTextScrollbar.pack(side=RIGHT, fill=BOTH)
    RenderText.configure(state='disabled')

def InitSearchListBox():
    global SearchListBox

    ListBoxScrollbar = Scrollbar(window)
    ListBoxScrollbar.pack()
    ListBoxScrollbar.place(x=255, y=50)

    TempFont = font.Font(window, size=15, weight='bold', family='Consolas')
    SearchListBox = Listbox(window, font=TempFont, activestyle='none', width=20, height=1, borderwidth=12, relief='ridge', yscrollcommand=ListBoxScrollbar.set)

    SearchListBox.insert(END, "실시간 검색")
    SearchListBox.insert(END, "월별 검색")
    SearchListBox.insert(END, "대기상태 나쁨 조회")
    SearchListBox.pack()
    SearchListBox.place(x=10, y=50)
    ListBoxScrollbar.config(command=SearchListBox.yview)

def SearchButtonAction():
    global SearchListBox

    RenderText.configure(state='normal')
    RenderText.delete(0.0, END)
    Index = SearchListBox.curselection()[0]
    if Index == 0:
        realtime_search.realtime_search(service_key,NameLabel.get(),database)
        RenderReady_realtime(database)
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

InitTopText()
InitInputLabel()
InitSearchButton()
InitRenderText()
InitSearchListBox()

window.mainloop()