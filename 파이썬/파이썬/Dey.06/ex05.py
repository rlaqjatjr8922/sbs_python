
#for 변수 in (리스트,튜플 등 컬랙션):




li = [1,2,3,4,5]

for n in li:
    print(n, end=' ')


# 비번만들기
#비번조건 숫자와 문자가 있어야됌

pwd = input('비번:')

문자 = 0
숫자 = 0

for ch in pwd:
    
    if ch.isalpha():
        문자 += 1
    if ch.isdigit():
        숫자 += 1
    
if 문자 > 0 and 숫자 > 0:
    print('사용가능')
else:
    print('사용불가능')