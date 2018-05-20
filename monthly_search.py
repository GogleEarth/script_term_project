from data import *
import urllib.request
import urllib.parse
from xml.dom.minidom import parseString


def monthly_search(service_key,databaseformonth,station_name):
    url = "http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getMsrstnAcctoRltmMesureDnsty?serviceKey="+service_key+"&numOfRows=2136&pageSize=2136&pageNo=1&startPage=1&stationName="+urllib.parse.quote(station_name)+"&dataTerm=3MONTH&ver=1.3"
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
        for item in ele:
            for info in item.childNodes:
                if info.nodeName == 'dataTime':
                    time = str(info.firstChild.data)
                if info.nodeName == 'so2Value':
                    so2 = str(info.firstChild.data)
                if info.nodeName == 'coValue':
                    co = str(info.firstChild.data)
                if info.nodeName == 'no2Value':
                    no2 = str(info.firstChild.data)
                if info.nodeName == 'o3Value':
                    o3 = str(info.firstChild.data)
                if info.nodeName == 'pm10Value':
                    pm10 = str(info.firstChild.data)
                if info.nodeName == 'pm25Value':
                    pm25 = str(info.firstChild.data)
                    newdata = data(station_name, time, so2, co, o3, no2, pm10, pm25)
                    databaseformonth.append(newdata)

    else:
        print("에러 코드 : " + str(rescode))
