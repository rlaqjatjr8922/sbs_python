
import time as a 
import os

p = 'C:/Users/user/Desktop/시간/'



    
    
while True:

    s = a.strftime('%y/%m/%d (%a) %H:%M:%S')
    
    file = open (p + '현재시간.txt','wt',encoding='UTF-8')
    a.sleep(1)
    
    file.write(str(s) )
    
    
    if os.path.exists(file):
        os.remove(file)
    print('파일이 삭재됌.')
    