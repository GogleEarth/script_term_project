import realtime_search
import monthly_search

service_key = 'fD%2FcMGFxBktwTG9%2BdUNuSZG%2FCnhfGOUAeEXyQUz6woSWm3JNpQazLAdKEmDuuYd7XZAmOnf6kWcWt49MrbnqcQ%3D%3D'

def printmenu():
    print("--------------------------------------------")
    print("1. 실시간 조회")
    print("2. 월별 측정 정보 조회")
    print("3. 대기상태가 나쁨인 지역 조회")
    print("--------------------------------------------")

def selectmenu():
    num = str(input("메뉴선택 : "))
    if(num == '1'):
        realtime_search.realtime_search(service_key)
    elif(num == '2'):
        pass
    elif(num == '3'):
        pass
    else:
        print("잘못 된 입력입니다.")

def main():
    printmenu()
    selectmenu()

while(True):
    main()