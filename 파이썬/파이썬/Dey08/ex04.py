'''
    지역변수 
    :함수 내부애서 선언한 변수
    함수내부애서만 접근이 능하다 
    
    
    전역변수
    :모든영역애서 접근가능
'''



def func():
    a = 10  #지역변수
    print("f() 내부-a : {}".format(a))

func()      #함수호출
#print("f() 내부-a : {}".format(a))
#애러발생
#   a 가 선언돼어있지 안슴니다

b = 10

def test():
     print("f() 내부-b : {}".format(b))
test()      #함수호출
print("f() 왜부-b : {}".format(b))