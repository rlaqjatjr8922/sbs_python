# format () 매쏘드
#{}괄호 기호로 변수나 값이 표시될 위치(형식)을 지정하여 출력하는 메소드


print('이름{}'.format('김범석'))
a = 10
b = 20
print('a : {},b : {}'.format(a,b))

print('a : {0},b : {1}'.format(a,b))

print('{0}하새요,저는 ㅇㅇㅇ : {1}'.format('안녕','임니다'))

tell1,tell2,tell3 = '02','222','3333'
print('연락처 : {0}-{1}-{2}'.format(tell1,tell2,tell3))