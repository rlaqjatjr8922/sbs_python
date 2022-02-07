'''
    csv 파일 일기
'''


import csv



i = 0
q = 0
qi = 0
p=1

# reader (파일객채,delimiter=구분기호,quotechar= 문자열기호)
with open('새 텍스트 문서.csv','r',newline='',encoding='korean') as file:
    csv_r = csv.reader(file,delimiter=',',quotechar=' ')
    
    #줄수새기
    for qweqwewqewqewqewqe in csv_r:
        
        print(p)
        print(qweqwewqewqewqewqe)
        p+=1
    
    #name = [[[]*20]*7]*(p+1)
    
    
    #일기
    for line in csv_r:
        q = q + 1
        i = 0
        print(q,"번째줄")
        
        #print(line,"번째줄")
        for qw in line:
            
            
                
            if i != 0:
                #print(qw)
                for qaz in range(0,(len(qw))):
                    #print( qaz)
                    name[q][i][qaz] = qw[qaz]
            
            i = i + 1 
            
            
            print(i,"       :",qw)
            
'''
x = 1

while True:
    for qwert in range(0,3):
        print(name[z][x][qwert])
    z = z+1
    '''