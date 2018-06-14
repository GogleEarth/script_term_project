#!/usr/bin/python
# coding=utf-8

import sys
import time
import sqlite3
import telepot
from pprint import pprint
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
from datetime import date, datetime, timedelta
import traceback
import realtime_search
import monthly_search
import data
import badair_search
from divide import *

service_key = 'fD%2FcMGFxBktwTG9%2BdUNuSZG%2FCnhfGOUAeEXyQUz6woSWm3JNpQazLAdKEmDuuYd7XZAmOnf6kWcWt49MrbnqcQ%3D%3D'
TOKEN = '607591452:AAGZfZpQ8H0GpHNI6vDA9cg6uY5uQDA7brU'
bot = telepot.Bot(TOKEN)
MAX_MSG_LENGTH = 9999

def getData(station):
    res_list = []
    data = realtime_search.realtime_search(service_key,station)
    res_list.append(data)
    return res_list

def getbadData():
    res_list = []
    datalist = []
    badair_search.badair_search(service_key,datalist)

    for data in datalist:
        res_list.append(data)

    return res_list

def getmonthlyData(month, station, method):
    res_list = []
    datalist = []

    monthly_search.monthly_search(service_key, station, datalist)
    if len(datalist) > 1:
        if method == '시간대별':
            for data in datalist:
                if data.month == month:
                    data.set_print_method(1)
                    res_list.append(data)
        elif method == '일평균':
            newlist = day_devide(datalist, month)
            for data in newlist:
                data.set_print_method(2)
                res_list.append(data)
        elif method == '월평균':
            data = month_devide(datalist, month)
            data.set_print_method(3)
            res_list.append(data)

    return res_list

def sendMessage(user, msg):
    try:
        bot.sendMessage(user, msg)
    except:
        traceback.print_exc(file=sys.stdout)

def run(date_param, param='11710'):
    conn = sqlite3.connect('logs.db')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS logs( user TEXT, log TEXT, PRIMARY KEY(user, log) )')
    conn.commit()

    user_cursor = sqlite3.connect('users.db').cursor()
    user_cursor.execute('CREATE TABLE IF NOT EXISTS users( user TEXT, location TEXT, PRIMARY KEY(user, location) )')
    user_cursor.execute('SELECT * from users')

    for data in user_cursor.fetchall():
        user, param = data[0], data[1]
        print(user, date_param, param)
        res_list = getData( param, date_param )
        msg = ''
        for r in res_list:
            try:
                cursor.execute('INSERT INTO logs (user,log) VALUES ("%s", "%s")'%(user,r))
            except sqlite3.IntegrityError:
                # 이미 해당 데이터가 있다는 것을 의미합니다.
                pass
            else:
                print( str(datetime.now()).split('.')[0], r )
                if len(r+msg)+1>MAX_MSG_LENGTH:
                    sendMessage( user, msg )
                    msg = r+'\n'
                else:
                    msg += r+'\n'
        if msg:
            sendMessage( user, msg )
    conn.commit()

if __name__=='__main__':
    today = date.today()
    current_month = today.strftime('%Y%m')

    print( '[',today,']received token :', TOKEN )

    pprint( bot.getMe() )

    run(current_month)
