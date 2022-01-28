
import time as a 



while True:

    
    path = 'C:/Users/admin/Desktop/새 폴더/'
    s = a.strftime('%y/%m/%d (%a) %H:%M:%S')
    file = open ( path + '현재시간'+ s +'.txt','wt',encoding='UTF-8')
    a.sleep(1)
    
    file.write(str(s) )
    file.close()
    print ('q')
    