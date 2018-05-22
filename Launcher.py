import realtime_search
import monthly_search
import badair_search
from data import *

service_key = 'fD%2FcMGFxBktwTG9%2BdUNuSZG%2FCnhfGOUAeEXyQUz6woSWm3JNpQazLAdKEmDuuYd7XZAmOnf6kWcWt49MrbnqcQ%3D%3D'
databaseformonth = []
databaseforstation = []
Days = ['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31']

def printmenu():
    print("--------------------------------------------")
    print("1. 실시간 조회")
    print("2. 월별 측정 정보 조회")
    print("3. 통합 대기 상태가 나쁨인 지역 조회")
    print("4. 프로그램 종료")
    print("--------------------------------------------")

def printmenuformonth():
    print("--------------------------------------------")
    print("1. 시간대 별 조회")
    print("2. 일 평균 조회")
    print("3. 월 평균 조회")
    print("--------------------------------------------")

def selectmenu():
    global service_key,database,databaseformonth,databaseforstation

    num = str(input("메뉴선택 : "))
    if(num == '1'):
        station_name = str(input('측정소 이름 : '))
        realtime_search.realtime_search(service_key, station_name)
    elif(num == '2'):
        station_name = str(input('측정소 이름 : '))
        month = str(input("월 입력(최근 3개월까지)(5월이면 05) : "))
        monthly_search.monthly_search(service_key,databaseformonth,station_name)
        if len(databaseformonth) > 0:
            printmenuformonth()
            selectmenuformonth(databaseformonth,month)
            databaseformonth.clear()
        else:
            print("데이터가 없습니다.")
    elif(num == '3'):
        badair_search.badair_search(service_key,databaseforstation)
        for name in databaseforstation:
            realtime_search.realtime_search(service_key,name)
        databaseforstation.clear()
    elif(num == '4'):
        print("프로그램을 종료합니다.")
        exit(1)
    else:
        print("잘못 된 입력입니다.")

def selectmenuformonth(database,month):
    num = str(input("메뉴선택 : "))
    while(True):
        if(num == '1'):
            printdatabasemonth(database,month)
            break
        elif(num == '2'):
            dayaver = day_devide(database,month)
            for data in dayaver:
                data.print_data_dayaver()
            break
        elif(num == '3'):
            monthaver = month_devide(database,month)
            monthaver.print_data_monthaver()
            break
        else:
            print("잘못 된 입력입니다.")

def printdatabasemonth(database,month):
    for data in database:
            if data.month == month:
                data.print_data()

def month_devide(database,month):
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

def main():
    printmenu()
    selectmenu()

while(True):
    main()