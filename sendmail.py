import smtplib
from email.mime.base import MIMEBase
from email.mime.text import MIMEText

def sendmail(senderAddr, password, add, datalist,flag):
    topic = ''

    msg = MIMEBase("multipart", "alternative")

    msg['Subject'] = '대기현황'
    msg['From'] = senderAddr
    msg['To'] = add

    for data in datalist:
        if flag == 0 or flag == 1 or flag == 4:
            topic = data.year + '년 ' + data.month + '월 ' + data.date + '일 ' + data.hour + '시 ' +  data.station + '의 대기 현황\n'
        elif flag == 2:
            topic = data.station + '의' + data.year + '년 ' + data.month + '월 ' + data.date + '일 평균 대기 현황\n'
        elif flag == 3:
            topic = data.station + '의' + data.year + '년 ' + data.month + '월 평균 대기 현황\n'

        part = MIMEText(topic, 'html', _charset='UTF-8')
        msg.attach(part)
        topic = '아황산 : {0:.3f} ppm\n'.format(data.so2)
        part = MIMEText(topic, 'html', _charset='UTF-8')
        msg.attach(part)
        topic = '일산화탄소 : {0:.3f} ppm\n'.format(data.co)
        part = MIMEText(topic, 'html', _charset='UTF-8')
        msg.attach(part)
        topic = '오존 : {0:.3f} ppm\n'.format(data.o3)
        part = MIMEText(topic, 'html', _charset='UTF-8')
        msg.attach(part)
        topic = '이산화질소 : {0:.3f} ppm\n'.format(data.no2)
        part = MIMEText(topic, 'html', _charset='UTF-8')
        msg.attach(part)
        topic = '미세먼지 : ' + str(data.pm10) + '㎍/㎥\n'
        part = MIMEText(topic, 'html', _charset='UTF-8')
        msg.attach(part)
        topic = '초미세먼지 : ' + str(data.pm25) + '㎍/㎥\n\n'
        part = MIMEText(topic, 'html', _charset='UTF-8')
        msg.attach(part)
        topic = ''
        part = MIMEText(topic, 'html', _charset='UTF-8')
        msg.attach(part)


    s = smtplib.SMTP("smtp.gmail.com",587)
    s.starttls()
    s.login(senderAddr,password)
    s.sendmail(senderAddr,[add],msg.as_string())
    s.close()

