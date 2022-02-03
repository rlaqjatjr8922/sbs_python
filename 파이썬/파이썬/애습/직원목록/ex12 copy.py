'''
    csv 파일 일기
'''


import csv


i = 0
q = 0
qi = 0

aq = ''

# reader (파일객채,delimiter=구분기호,quotechar= 문자열기호)
with open('직원목록.csv','r',newline='',encoding='UTF-8') as file:
    csv_r = csv.reader(file,delimiter=',',quotechar='"')
    for line in csv_r:
        q = q + 1
        i = 0
        print(q,"번째줄",end="")
        for str in line:
            
            for aqw in range(0,len(str)):
                aq[q][i][aqw] = str[aqw]
            




            i = i + 1 
            print(i,"       :",str)
            
#한문장씩 일기     

for qwer in range(0,format(q)):
    print('')
    for qwe in range(0,format(i)) :
            for aqw in range(0,len(str)):
                print(format(aq[qwer][qwe][aqw]),end='')