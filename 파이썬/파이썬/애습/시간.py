
import time as a 


for i in range(9999999999999):
    
    s = a.strftime('%y/%m/%d (%a) %H:%M:%S')
    print('str() : {}'.format(s) )
    i = i+100
    if i == -100:
        break