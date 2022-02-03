
'''
    csv 파일 일기
'''


import csv



# reader (파일객채,delimiter=구분기호,quotechar= 문자열기호)
with open('test.csv','r',newline='') as file:
    csv_r = csv.reader(file,delimiter=',',quotechar='"')
    for line in csv_r:
        print(line)
        
#for str in line:
#한문장씩 일기    