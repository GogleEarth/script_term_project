# 항목	SO2	CO	O3	NO2	PM10	PM2.5
# 단위	ppm	ppm	ppm	ppm	㎍/㎥	㎍/㎥
# PM10 : 미세먼지 PM25 : 초미세먼지 O3 : 오존

class data:
    def __init__(self,station,time,so2,co,o3,no2,pm10,pm25):
        self.station = station
        self.so2 = so2
        self.co = co
        self.o3 = o3
        self.no2 = no2
        self.pm10 = pm10
        self.pm25 = pm25
        self.year = str(time[0]+time[1]+time[2]+time[3])
        self.month = str(time[5]+time[6])
        self.date = str(time[8]+time[9])
        self.hour = str(time[11]+time[12])

    def print_data(self):
        print(self.station,'의 ',self.year,'-',self.month,'-',self.date,' ',self.hour,'시 대기 현황')
        print('이산화황 : ', self.so2, 'ppm')
        print('일산화탄소 : ', self.co, 'ppm')
        print('이산화질소 : ', self.no2, 'ppm')
        print('오존 : ', self.o3, 'ppm')
        print('미세먼지 : ', self.pm10, '㎍/㎥')
        print('초미세먼지 : ', self.pm25, '㎍/㎥\n')

