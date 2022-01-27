
import time as a 

#1970년 1월 1일 0시 0분 0.00000000초기준으로 경괴한시간 반환
print('time() : {}'.format(a.time()) )

t = a.time()
print('ctime() : {}'.format(a.ctime(t)))

'''
    날짜 지시자
    %y  :2자리연도(22)
    %Y  :4자리냔도(2022)
    %m  :2자리 월(01~12)
    %b  :3자리 영문요 월(Jan~Dec)
    %B  :전채 영문 월()
    %d  :2자리 일
    %a  :3자리 요일
    %A  :전채영문요일
    %i  :12시 시간(00~12)
    %H  :24시 시간(00~23)
    %M  :분(00~59)
    %S  :초(00~59)

'''



s = a.strftime('%y/%m/%d (%a) %H:%M:%S')
print('str() : {}'.format(s) )


#지정 한초만큼 일시중지
a.sleep(5)  #5초정지


import datetime 

niw = datetime.datetime.now ()
print('날자시간:{}'.format(niw))

to = datetime.date(2022,1,13)
print('날시 시간:{}'.format)

sp = datetime


#사진1