
import time  
import os

path = 'C:/Users/pc/Desktop/새 폴더 (5)/'
#s = time.strftime('%Y년 %m월 %d일 %a요일 %H시 %M분 %S초')
q = 'a(ㄴ:ㅁㅇ)sd' 
#file = open (path + '현재시간 '+ s +').txt','wt',encoding='UTF-8')
#print(s)

while True:
    s = time.strftime('%Y년 %m월 %d일 %a요일 %H시 %M분 %S초')
    file = open (path + '현재시간 '+ s +').txt','wt',encoding='UTF-8')
    
    file.close()

    time.sleep(0.1)

    os.remove( path + '현재시간 '+ s +').txt')
    print('파일이 삭재됌.')

    
    
    
    
    print ('q')
    

    file.close()