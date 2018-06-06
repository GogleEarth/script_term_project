#import telepot
#from urllib.request import urlopen
#bot = telepot.Bot('607591452:AAGZfZpQ8H0GpHNI6vDA9cg6uY5uQDA7brU')
#bot.sendMessage('525600178','안녕하슈')

#url = 'http://openapi.molit.go.kr:8081/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcRHTrade?serviceKey=sea100UMmw23Xycs33F1EQnumONR%2F9ElxBLzkilU9Yr1oT4TrCot8Y2p0jyuJP72x9rG9D8CN5yuEs6AS2sAiw%3D%3D&LAWD_CD=11110&DEAL_YMD=201712'
#response = urlopen(url).read()
#print(response)

def f():
    data = listbox.curselection()

    print(data)

import tkinter

window=tkinter.Tk()
window.title("YUN DAE HEE")
window.geometry("640x480+100+100")
window.resizable(False, False)

listbox = tkinter.Listbox(window, selectmode='extended', height=0)
listbox.insert(0, "1번")
listbox.insert(1, "2번")
listbox.insert(2, "2번")
listbox.insert(3, "2번")
listbox.insert(4, "3번")
listbox.delete(1, 2)
listbox.pack()





window.mainloop()