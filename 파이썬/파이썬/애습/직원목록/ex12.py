'''
    csv 파일 일기
'''


import csv


i = 0
q = 0
qi = 0
# reader (파일객채,delimiter=구분기호,quotechar= 문자열기호)
with open('새 텍스트 문서.csv','r',newline='',encoding='korean') as file:
    csv_r = csv.reader(file,delimiter=',',quotechar='"')
    for line in csv_r:
        q = q + 1
        i = 0
        print(q,"번째줄")
        for str in line:
            
            
            print(i,"       :",str)
            i = i + 1 
#한문장씩 일기     