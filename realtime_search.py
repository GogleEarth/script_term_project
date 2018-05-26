from data import *
import urllib.request
import urllib.parse
from xml.dom.minidom import parseString

def realtime_search(service_key,station_name,database):
    url = "http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getMsrstnAcctoRltmMesureDnsty?serviceKey="+service_key+"&numOfRows=1&pageSize=1&pageNo=1&startPage=1&stationName="+urllib.parse.quote(station_name)+"&dataTerm=DAILY&ver=1.3"
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
                newdata = data(station_name, time, so2, co, o3, no2, pm10, pm25)
                database.append(newdata)
                return
    else:
        print("에러 코드 : " + str(rescode))
