
import time
#저장경로
path = 'C:/수업/SBS-py/sbs_python/파이썬/파이썬/Dey10/'
    
today =time.strftime('%y-%m-%d')

#파일 렬기 :open
file = open (path + '할일('+ today +').txt','wt',encoding='UTF-8')

no = 1
while True:
    todo =input('오늘 할 일 :')
    #아무갑도입력하지안을시종료
    if not todo:
        break
    file.write(str(no) + '. ' + todo + '\n')
    no = no + 1





