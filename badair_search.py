import os
import sys
import urllib.request
import urllib.parse
from xml.dom.minidom import parseString

def badair_search(service_key,database):
    url = "http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getUnityAirEnvrnIdexSnstiveAboveMsrstnList?serviceKey=" + service_key + "&numOfRows=10&pageSize=10&pageNo=1&startPage=1"

    req = urllib.request.Request(url)
    resp = urllib.request.urlopen(req)
    rescode = resp.getcode()

    if rescode == 200:
        resp_body = resp.read()
        doc = parseString(resp_body.decode('utf-8'))
        ele = doc.getElementsByTagName('item')
        station_name = ''
        for item in ele:
            for data in item.childNodes:
                if data.nodeName == 'stationName':
                    station_name = data.firstChild.data
                    database.append(station_name)
    else:
        print("에러 코드 : " + str(rescode))
