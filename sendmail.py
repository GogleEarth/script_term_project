import smtplib
import mimetypes
from email.mime.base import MIMEBase
from email.mime.text import MIMEText


def send_mail(senderAddr, password, recipientAddr, maildatalist, mailflag):

    s = smtplib.SMTP("smtp.gmail.com", 587)  # SMTP 서버 설정
    s.ehlo()
    s.starttls()  # STARTTLS 시작
    s.ehlo()
    s.login(senderAddr, password)

    msg = MIMEBase("multipart", "alternative")

    msg['Subject'] = '대기현황'
    msg['From'] = senderAddr
    msg['To'] = recipientAddr

    topic = ''

    for data in maildatalist:
        if mailflag == 0 or mailflag == 1 or mailflag == 4:
            topic = data.year + '년 ' + data.month + '월 ' + data.date + '일 ' + data.hour + '시 ' + data.station + '의 대기 현황'
        elif mailflag == 2:
            topic = data.station + '의' + data.year + '년 ' + data.month + '월 ' + data.date + '일 평균 대기 현황'
        elif mailflag == 3:
            topic = data.station + '의' + data.year + '년 ' + data.month + '월 평균 대기 현황'
        part1 = MIMEText(topic, 'html', _charset='UTF-8')
        msg.attach(part1)

        topic = '아황산 : {0:.3f} ppm'.format(data.so2)
        part2 = MIMEText(topic, 'html', _charset='UTF-8')
        msg.attach(part2)

        topic = '일산화탄소 : {0:.3f} ppm'.format(data.co)
        part3 = MIMEText(topic, 'html', _charset='UTF-8')
        msg.attach(part3)

        topic = '오존 : {0:.3f} ppm'.format(data.o3)
        part4 = MIMEText(topic, 'html', _charset='UTF-8')
        msg.attach(part4)

        topic = '이산화질소 : {0:.3f} ppm'.format(data.no2)
        part5 = MIMEText(topic, 'html', _charset='UTF-8')
        msg.attach(part5)

        topic = '미세먼지 : ' + str(data.pm10) + '㎍/㎥'
        part6 = MIMEText(topic, 'html', _charset='UTF-8')
        msg.attach(part6)

        topic = '초미세먼지 : ' + str(data.pm25) + '㎍/㎥'
        part7 = MIMEText(topic, 'html', _charset='UTF-8')
        msg.attach(part7)

        topic = ''
        part8 = MIMEText(topic, 'html', _charset='UTF-8')
        msg.attach(part8)

    s.sendmail(senderAddr, [recipientAddr], msg.as_string())
    s.close()

