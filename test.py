import telepot
from urllib.request import urlopen
bot = telepot.Bot('607591452:AAGZfZpQ8H0GpHNI6vDA9cg6uY5uQDA7brU')
#bot.sendMessage('525600178','안녕하슈')

url = 'http://openapi.molit.go.kr:8081/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcRHTrade?serviceKey=sea100UMmw23Xycs33F1EQnumONR%2F9ElxBLzkilU9Yr1oT4TrCot8Y2p0jyuJP72x9rG9D8CN5yuEs6AS2sAiw%3D%3D&LAWD_CD=11110&DEAL_YMD=201712'
response = urlopen(url).read()
print(response)

