# 모듈
'''
    모듈이란?
    :변수나 함수 또는 클래스로 모아노은 파이썬파일
        -하나의 파이썬파일(.py)
        
    패키지?
    :모듈이 여러 개 모여 있는 폴더
    
    모듈의 사용
    :import 무듈
'''

import wqadsa
from wqadsa import *
e = input('km')
e = int(e)
miles = kilom(e)
print('{}km = {} miles'.format(e,miles))

e = input('gram')
e = int(e)
pound = gram(e)
print('{} = {} pound'.format(e,pound))