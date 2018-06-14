from data import *

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