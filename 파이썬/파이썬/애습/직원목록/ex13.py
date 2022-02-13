'''
    csv 파일 일기
'''


import csv

from ex13copy2 import *


i = 0
q = 0
qi = 0
p=1

# reader (파일객채,delimiter=구분기호,quotechar= 문자열기호)
with open('새 텍스트 문서.csv','r',newline='',encoding='korean') as file:
    csv_r = csv.reader(file,delimiter=',',quotechar='"')
    
    #줄수새기
    
    
    name = [['']*7]*(qwe()+1)
    
    
    #일기
    for line in csv_r:
        
        q = q + 1
        i = 0
        print("q,i,1",q,i)
        #print("")
        #print(q,"번째줄")
        
        #print(line,"번째줄")
        for qw in line:
            print("q,i,2",q,i)
            #print(i,"번째칸:",end='')
            
                
            if i != 0:
                print("q,i,3",q,i)
                name[q][i] = dhfb(qw)
                for i in range(0,70):
                    for a in range(0,7):
                        print("s",name[i][a])
                #print(name[q][i],end='')
            #print(name[71][i],end='q\n')
            i = i + 1 
        
        #print(name[q][i-1],end='    qw')
    '''
    e = 0 
    #크기비교
    for a1 in range(6,q):
        for a2 in range(6,q):
            if name[a1][1] > name[a2][1]:
                e = 1
        
        name[a1][0] = str(e)
        
'''

'''
    for i in range(0,70):
        for a in range(0,7):
            print("s",name[i][a])
'''

with open('test1.csv','w',newline='',encoding='korean') as file:
    
    csv_maker = csv.writer(file,delimiter=',')
    for i in range(0,q):
        
                
        csv_maker.writerow(name[i])
print("성공")
    
        
                
            
            
            
            
            
            

