import realtime_search
import monthly_search
import badair_search

service_key = 'fD%2FcMGFxBktwTG9%2BdUNuSZG%2FCnhfGOUAeEXyQUz6woSWm3JNpQazLAdKEmDuuYd7XZAmOnf6kWcWt49MrbnqcQ%3D%3D'
databaseformonth = []
databaseforstation = []
databaseforbaddata = []


def printmenu():
    print("--------------------------------------------")
    print("1. 실시간 조회")
    print("2. 월별 측정 정보 조회")
    print("3. 통합 대기 상태가 나쁨인 지역 조회")
    print("4. 프로그램 종료")
    print("--------------------------------------------")

def selectmenu():
    global service_key,database,databaseformonth,monthly_search_flag,databaseforstation

    num = str(input("메뉴선택 : "))
    if(num == '1'):
        station_name = str(input('측정소 이름 : '))
        realtime_search.realtime_search(service_key, station_name)
    elif(num == '2'):
        station_name = str(input('측정소 이름 : '))
        month = str(input("월 입력(최근 3개월까지)(5월이면 05) : "))
        monthly_search.monthly_search(service_key,databaseformonth,station_name)
        printdatabasemonth(databaseformonth,month,station_name)
        databaseformonth.clear()
    elif(num == '3'):
        badair_search.badair_search(service_key,databaseforstation)
        for name in databaseforstation:
            realtime_search.realtime_search(service_key,name)
    elif(num == '4'):
        print("프로그램을 종료합니다.")
        exit(1)
    else:
        print("잘못 된 입력입니다.")

def printdatabasemonth(database,month,station_name):
    for data in database:
        if data.station == station_name:
            if data.month == month:
                data.print_data()

def main():
    printmenu()
    selectmenu()

while(True):
    main()