
import os
import sys
import urllib.request
import urllib.parse
from xml.dom.minidom import parseString


def monthly_search(service_key):
    station_name = str(input('측정소 이름 : '))
    #city_name = str(input('도시이름 : '))

    url = "http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getMsrstnAcctoRltmMesureDnsty?serviceKey="+service_key+"&numOfRows=24&pageSize=24&pageNo=1&startPage=1&stationName="+urllib.parse.quote(station_name)+"&dataTerm=MONTH&ver=1.3"
    #url2 = "http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey="+service_key+"&numOfRows=10&pageSize=10&pageNo=1&startPage=1&sidoName="+urllib.parse.quote(city_name)+"&ver=1.3"
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
        for item in ele:
            for data in item.childNodes:
                if data.nodeName == 'dataTime':
                    time = data.firstChild.data
                    print('시간대 :', time)
                if data.nodeName == 'so2Value':
                    so2 = data.firstChild.data
                    print('이산화황 : ',so2,'ppm')
                if data.nodeName == 'coValue':
                    co = data.firstChild.data
                    print('일산화탄소 : ',co,'ppm')
                if data.nodeName == 'no2Value':
                    no2 = data.firstChild.data
                    print('이산화질소 : ', no2, 'ppm')
                if data.nodeName == 'o3Value':
                    o3 = data.firstChild.data
                    print('오존 : ',o3,'ppm')
                if data.nodeName == 'pm10Value':
                    pm10 = data.firstChild.data
                    print('미세먼지 : ',pm10,'㎍/㎥')
                if data.nodeName == 'pm25Value':
                    pm25 = data.firstChild.data
                    print('초미세먼지 : ',pm25,'㎍/㎥\n')
    else:
        print("에러 코드 : " + str(rescode))
