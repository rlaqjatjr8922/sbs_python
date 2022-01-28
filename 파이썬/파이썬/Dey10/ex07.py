'''
    CSV (Comma Separated Value)
    : (,)로 불리한 값들


    ex)
        학번,이름,주소,전화번호
        101,김철수,서울노원구,010-1111-2222
        102,김철수,서울노원구,010-1111-2222
        103,김철수,서울노원구,010-1111-2222
        104,김철수,서울노원구,010-1111-2222


'''

import csv

with open('test.csv','w') as file:
    #delimiter : 구분기호
    csv_maker = csv.writer(file,delimiter=',')
    csv_maker.writerow(['학번', '이름','주소','전화번호'])
    csv_maker.writerow(['101', '김범석','번동','01048598922'])
    csv_maker.writerow(['101', '김범석','번동','01048598922'])
    csv_maker.writerow(['101', '김범석','번동','01048598922'])

print('파일생성됌')