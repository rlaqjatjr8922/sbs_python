
import time as a 



while True:

    
    path = '파이썬/파이썬/애습/'
    file = open (path + '현재시간.txt','wt',encoding='UTF-8')
    a.sleep(1)
    s = a.strftime('%y/%m/%d (%a) %H:%M:%S')
    file.write(str(s) )
    print ('q')
    