
# 반복문
# :만족할때까지반복
#while 조건식:
#       실행문장

#   for 변수 in (반복가능한객체):
#           반복 실행할 문장


i = 1
while i <= 10:
        print(i,end=' , ' )
        i = i + 1
        
        #1+2+3+...........+10


print('\n')#앤터
        
a=1
sum = 0
while a <= 10:
    sum += a
    print(a, end= ' ')
    if(a != 10):
        print( "+", end=' ' )
    a = a+1
print('sum = {}'.format(sum))