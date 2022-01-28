


#파일삿재
#os 모듈

import os

p = 'C:/수업/SBS-py/sbs_python/파이썬/파이썬/Dey10/'

file = input('삭제할 파일명 : ')

file = p + file

#파일의 존재확인
if os.path.exists(file):
    os.remove(file)
    print('파일이 삭재됌.')