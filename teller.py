import telepot
import time
import sqlite3
import telepot
from pprint import pprint
from datetime import date, datetime
import noti

def replyrealData(user, station):
    print(user, station)
    res_list = noti.getData(station)
    msg = ''
    for data in res_list:
        print( str(datetime.now()).split('.')[0], data )
        msg = data.__str__()+'\n'

    if msg:
        noti.sendMessage( user, msg )
    else:
        noti.sendMessage( user, '%s라는 이름의 측정소는 없습니다..'%station )

def replybadData(user):
    print(user)
    res_list = noti.getbadData()
    msg = ''
    for data in res_list:
        print(str(datetime.now()).split('.')[0], data )
        msg += data + '\n'

    if msg:
        noti.sendMessage( user, msg )
    else:
        noti.sendMessage( user, '대기상태가 나쁜 측정소가 없습니다..')

def replyMonthlyData(user, month, station, method):
    print(user)
    res_list = noti.getmonthlyData(month, station, method)
    msg = ''

    if len(res_list) > 0:
        for data in res_list:
            print(str(datetime.now()).split('.')[0], data )
            msg = data.__str__() + '\n'
            if msg:
                noti.sendMessage(user, msg)

    else:
        noti.sendMessage( user, '입력을 잘못한것 같습니다..')


def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    if content_type != 'text':
        noti.sendMessage(chat_id, '난 텍스트 이외의 메시지는 처리하지 못해요.')
        return

    text = msg['text']
    args = text.split(' ')

    if text.startswith('실시간') and len(args)>1:
        print('try to 실시간', args[1])
        replyrealData(chat_id, args[1])
    elif text.startswith('월별') and len(args)>1:
        noti.sendMessage(chat_id, '시간이 좀 걸려요~')
        print(' try to 월별', args)
        replyMonthlyData(chat_id,args[1],args[2],args[3])
    elif text.startswith('나쁨') and len(args)>1:
        print('try to 나쁨', args[1])
        replybadData(chat_id)
    elif text.startswith('헬프') or text.startswith('help'):
        noti.sendMessage(chat_id, '실시간 검색은 "실시간 "측정소이름""을\n'
                                  '대기 상태가 나쁜 측정소 조회는 "나쁨 조회"를 입력하세요.')
        noti.sendMessage(chat_id, '월별 검색은 "월별 "월(01~12)" "측정소이름" "방법"을 입력하세요.\n'
                                  '방법은 "시간대별", "일평균", "월평균" 중 하나를 입력하세요.')
    else:
        noti.sendMessage(chat_id, '모르는 명령어입니다.\n'
                                  '실시간 검색은 "실시간 "측정소이름""을\n'
                                  '대기 상태가 나쁜 측정소 조회는 "나쁨 조회"를 입력하세요.')
        noti.sendMessage(chat_id, '월별 검색은 "월별 "월(01~12)" "측정소이름" "방법"을 입력하세요.\n'
                                  '방법은 "시간대별", "일평균", "월평균" 중 하나를 입력하세요.')


today = date.today()
current_month = today.strftime('%Y%m')

print( '[',today,']received token :', noti.TOKEN )

bot = telepot.Bot(noti.TOKEN)
pprint( bot.getMe() )

bot.message_loop(handle)

print('Listening...')

while 1:
  time.sleep(10)