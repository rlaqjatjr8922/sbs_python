'''
문재 :제어문(조건문,반복문) 을 이용하여,
    아래와가치 *로이루진도형을출력
    1단개)
    숫자n을 입력바다
    이거출력
    
    *
    **
    ***
    ****
    *****
    
    
    2단개)
    *    
   ***
  *****
 *******
*********
    
'''
u = input("정수")
u = int(u)
for i in range(0,u+1,1):
    print('*' * i)
    

print(end = '')
u = input("정수")
u = int(u)
y = 0
for i in range(0,u+1,1):    #  for 변수 in range(변수초기갑 , 종료갑 , 증감갑):
    y = int( (u - 1) -i )   
    for rt in range(0,y+1,1):
        print (' ',end='')
    
    print('*',end = '')
    print('*' * i * 2)
    