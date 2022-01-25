'''
    사용자함수
    :사용자가직접정이한 함수
    
    함수 정의 키워드 :def
    
    def 함수명(매개변수1,매개변수2,.....):
        실행할 문장;
        실행할 문장;
        실행할 문장;
        return(내보낼갑)
        
    #return 합수종료
    
    #용어
    1.함수의저의 : dif 키워드로 사용자 함수를 새로 만드는 것
    2.함수 호출  :정의됀 함수가 실해돼도록 명령을 작성하는 겄
    3. 인수      :함수호출할때(입력)하는 갑(argument)
    4.배개변수   :인수를전달밨는 변수 (parameter)
    5.변환갑     :함수가 반환하는 값,return 다음애작성
    
    #함수호출
    함수명(인수1,2, ....)
    
    # 함수의 형태
    1.인수x 반환값 x    :함수명()
    2.인수o 반환값 x    :함수명(인수)
    3.인수x 반환값 o    :변수 = 함수명()
    4.인수o 반환값 o    :함수명= 함수명(인수)



'''


a=10
b=2
def plus(a,b):
    return a + b

def mi(a,b):
    return a - b

def mul(a,b):
    return a * b

def div(a,b):
    return a / b

print('a + b = {}'.format( plus(a,b)))
print('a - b = {}'.format( mi(a,b)))
print('a * b = {}'.format( mul(a,b)))
print('a / b = {}'.format( div(a,b)))
