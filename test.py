from tkinter import *
from tkinter import font
from data import *
import urllib.request
import urllib.parse
from xml.dom.minidom import parseString

service_key = 'fD%2FcMGFxBktwTG9%2BdUNuSZG%2FCnhfGOUAeEXyQUz6woSWm3JNpQazLAdKEmDuuYd7XZAmOnf6kWcWt49MrbnqcQ%3D%3D'
window = Tk()
window.geometry("400x600+750+200")

def InitTopText():
    TempFont = font.Font(window, size=20, weight='bold', family='consolas')
    MainText = Label(window, font=TempFont, text='[대기 현황 검색 APP]')
    MainText.pack()
    MainText.place(x=60)

def InitInputLabel():
    global InputLabel
    TempFont = font.Font(window, size=15, weight='bold', family = 'Consolas')
    InputLabel = Entry(window, font = TempFont, width = 26, borderwidth = 12, relief = 'ridge')
    InputLabel.pack()
    InputLabel.place(x=15, y=100)

def InitSearchButton():
    TempFont = font.Font(window, size=12, weight='bold', family = 'Consolas')
    SearchButton = Button(window, font = TempFont, text="검색",command = SearchButtonAction)
    SearchButton.pack()
    SearchButton.place(x=330, y=110)

def SearchButtonAction():
    global SearchListBox
    RenderText.configure(state='normal')
    RenderText.delete(0.0, END)
    search()
    RenderText.configure(state='disabled')

def search():
        url = "http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getMsrstnAcctoRltmMesureDnsty?serviceKey=" + service_key + "&numOfRows=1&pageSize=1&pageNo=1&startPage=1&stationName=" + urllib.parse.quote(
            InputLabel.get()) + "&dataTerm=DAILY&ver=1.3"
        req = urllib.request.Request(url)
        resp = urllib.request.urlopen(req)
        rescode = resp.getcode()

        # 항목	SO2	CO	O3	NO2	PM10	PM2.5
        # 단위	ppm	ppm	ppm	ppm	㎍/㎥	㎍/㎥
        # PM10 : 미세먼지 PM25 : 초미세먼지 O3 : 오존
        if rescode == 200:
            resp_body = resp.read()
            doc = parseString(resp_body.decode('utf-8'))
            ele = doc.getElementsByTagName('item')
            time = ''
            so2 = ''
            co = ''
            no2 = ''
            o3 = ''
            pm10 = ''
            pm25 = ''
            if len(ele) > 0:
                for item in ele:
                    for info in item.childNodes:
                        if info.nodeName == 'dataTime':
                            time = str(info.firstChild.data)
                        if info.nodeName == 'so2Value':
                            if info.firstChild.data == '-':
                                so2 = 0
                            else:
                                so2 = str(info.firstChild.data)
                        if info.nodeName == 'coValue':
                            if info.firstChild.data == '-':
                                co = 0
                            else:
                                co = str(info.firstChild.data)
                        if info.nodeName == 'no2Value':
                            if info.firstChild.data == '-':
                                no2 = 0
                            else:
                                no2 = str(info.firstChild.data)
                        if info.nodeName == 'o3Value':
                            if info.firstChild.data == '-':
                                o3 = 0
                            else:
                                o3 = str(info.firstChild.data)
                        if info.nodeName == 'pm10Value':
                            if info.firstChild.data == '-':
                                pm10 = 0
                            else:
                                pm10 = str(info.firstChild.data)
                        if info.nodeName == 'pm25Value':
                            if info.firstChild.data == '-':
                                pm25 = 0
                            else:
                                pm25 = str(info.firstChild.data)
                    newdata = data(InputLabel.get(), time, so2, co, o3, no2, pm10, pm25)
                    RenderText.insert(INSERT,newdata.year)
                    RenderText.insert(INSERT,'년 ')
                    RenderText.insert(INSERT,newdata.month)
                    RenderText.insert(INSERT,'월 ')
                    RenderText.insert(INSERT,newdata.date)
                    RenderText.insert(INSERT,'일 ')
                    RenderText.insert(INSERT,newdata.hour)
                    RenderText.insert(INSERT,'시 ')
                    RenderText.insert(INSERT,newdata.station)
                    RenderText.insert(INSERT,'의 대기현황\n')
                    RenderText.insert(INSERT,'이산화황 : ')
                    RenderText.insert(INSERT,newdata.so2)
                    RenderText.insert(INSERT,'ppm\n')
                    RenderText.insert(INSERT,'일산화탄소 : ')
                    RenderText.insert(INSERT,newdata.co)
                    RenderText.insert(INSERT,'ppm\n')
                    RenderText.insert(INSERT,'오존 : ')
                    RenderText.insert(INSERT,newdata.o3)
                    RenderText.insert(INSERT,'ppm\n')
                    RenderText.insert(INSERT,'이산화질소 : ')
                    RenderText.insert(INSERT,newdata.no2)
                    RenderText.insert(INSERT,'ppm\n')
                    RenderText.insert(INSERT,'미세먼지 : ')
                    RenderText.insert(INSERT,newdata.pm10)
                    RenderText.insert(INSERT,'㎍/㎥\n')
                    RenderText.insert(INSERT,'초미세먼지 : ')
                    RenderText.insert(INSERT,newdata.pm25)
                    RenderText.insert(INSERT,'㎍/㎥\n')

                    return
            else:
                RenderText.insert(INSERT, "데이터가 없습니다.")
        else:
            print("에러 코드 : " + str(rescode))

def InitRenderText():
    global RenderText

    RenderTextScrollbar = Scrollbar(window)
    RenderTextScrollbar.pack()
    RenderTextScrollbar.place(x=375, y=200)
    TempFont = font.Font(window, size=10, family='Consolas')
    RenderText = Text(window, width=49, height=27, borderwidth=12, relief='ridge', yscrollcommand=RenderTextScrollbar.set)
    RenderText.pack()
    RenderText.place(x=10, y=215)
    RenderTextScrollbar.config(command=RenderText.yview)
    RenderTextScrollbar.pack(side=RIGHT, fill=BOTH)
    RenderText.configure(state='disabled')

InitTopText()
InitInputLabel()
InitSearchButton()
InitRenderText()

window.mainloop()