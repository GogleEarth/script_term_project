from tkinter import *

# 항목	SO2	CO	O3	NO2	PM10	PM2.5
# 단위	ppm	ppm	ppm	ppm	㎍/㎥	㎍/㎥
# PM10 : 미세먼지 PM25 : 초미세먼지 O3 : 오존

class data:
    def __init__(self,station,time,so2,co,o3,no2,pm10,pm25):
        self.station = station
        self.so2 = float(so2)
        self.co = float(co)
        self.o3 = float(o3)
        self.no2 = float(no2)
        self.pm10 = int(pm10)
        self.pm25 = int(pm25)
        self.year = str(time[0]+time[1]+time[2]+time[3])
        self.month = str(time[5]+time[6])
        self.date = str(time[8]+time[9])
        self.hour = str(time[11]+time[12])

    def print_data(self, RenderText):
        RenderText.insert(INSERT,self.year + '년 ' + self.month + '월 ' + self.date + '일 ' + self.hour + '시 ' +  self.station + '의 대기 현황\n')
        RenderText.insert(INSERT,'아황산 : ' + str(self.so2) + 'ppm\n')
        RenderText.insert(INSERT,'일산화탄소 : ' + str(self.co) + 'ppm\n')
        RenderText.insert(INSERT,'오존 : ' + str(self.o3) + 'ppm\n')
        RenderText.insert(INSERT,'이산화질소 : ' + str(self.no2) + 'ppm\n')
        RenderText.insert(INSERT,'미세먼지 : ' + str(self.pm10) + '㎍/㎥\n')
        RenderText.insert(INSERT,'초미세먼지 : ' + str(self.pm25) + '㎍/㎥\n\n')

    def print_data_dayaver(self,RenderText):
        RenderText.insert(INSERT, self.year + '년 ' + self.month + '월 ' + self.date + '일 ' + self.station + '의 일 평균 대기 현황\n')
        RenderText.insert(INSERT, '아황산 : {0:.3f} ppm\n'.format(self.so2))
        RenderText.insert(INSERT, '일산화탄소 : {0:.3f} ppm\n'.format(self.co))
        RenderText.insert(INSERT, '오존 : {0:.3f} ppm\n'.format(self.o3))
        RenderText.insert(INSERT, '이산화질소 : {0:.3f} ppm\n'.format(self.no2))
        RenderText.insert(INSERT, '미세먼지 : ' + str(self.pm10) + '㎍/㎥\n')
        RenderText.insert(INSERT, '초미세먼지 : ' + str(self.pm25) + '㎍/㎥\n\n')

    def print_data_monthaver(self,RenderText):
        RenderText.insert(INSERT, self.year + '년 ' + self.month + '월 ' + self.station + '의 월 평균 대기 현황\n')
        RenderText.insert(INSERT, '아황산 : {0:.3f} ppm\n'.format(self.so2))
        RenderText.insert(INSERT, '일산화탄소 : {0:.3f} ppm\n'.format(self.co))
        RenderText.insert(INSERT, '오존 : {0:.3f} ppm\n'.format(self.o3))
        RenderText.insert(INSERT, '이산화질소 : {0:.3f} ppm\n'.format(self.no2))
        RenderText.insert(INSERT, '미세먼지 : ' + str(self.pm10) + '㎍/㎥\n')
        RenderText.insert(INSERT, '초미세먼지 : ' + str(self.pm25) + '㎍/㎥\n\n')

    def __str__(self):
        topic = self.year + '년 ' + self.month + '월 ' + self.date + '일 ' + self.hour + '시 ' + self.station + '의 대기 현황\n'
        topic += '아황산 : ' + str(self.so2) + 'ppm\n'
        topic += '일산화탄소 : ' + str(self.co) + 'ppm\n'
        topic += '오존 : ' + str(self.o3) + 'ppm\n'
        topic += '이산화질소 : ' + str(self.no2) + 'ppm\n'
        topic += '미세먼지 : ' + str(self.pm10) + '㎍/㎥\n'
        topic += '초미세먼지 : ' + str(self.pm25) + '㎍/㎥\n\n'
        return topic