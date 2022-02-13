import csv


with open('새 텍스트 문서.csv','r',newline='',encoding='korean') as file:
    csv_r = csv.reader(file,delimiter=',',quotechar='"')
    
    #줄수새기
    for line in csv_r:
        q = q + 1
        
        print("")
        print(q,"번째줄")
    