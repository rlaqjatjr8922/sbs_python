import random
i = input('풀문재수')
i = int(i)
q = 1

for qwqwqwq in range(1):
    
    u = input('+ 를추가할까요?[o],[x]')   # +  =  2
    
    if u == 'o':
        q = q * 2
    

    u = input('- 를추가할까요?[o],[x]')   # -  =  3

    if u == 'o':
        q = q * 3
    
    
    u = input('x 를추가할까요?[o],[x]')
    if u == 'o':
        q = q * 5
    
    
    u = input('÷ 를추가할까요?[o],[x]')
    if u == 'o':
        q = q * 7
    
    print('풀문재수{}')
    if (q / 2) == int:
        print('+ 킴')
    else:
        print('+ 끔')
    if (q / 3) == int:
        print('- 킴')
    else:
        print('- 끔')
    if (q / 5) == int:
        print('x 킴')
    else:
        print('x 끔')
        
    if (q / 7) == int:
        print('÷ 킴')
    else:
        print('+ 끔')#더하기는 2, 마이너스는3,곱하기는5,나누기는7
                    #질문 풀문제수 더하기 빼기 곱하기 나누기
                    #설정확인
                    #계산문제
    u = input('당신이 원하는 설정이맛슴니까?[o],[x]')



for q in range(0,i,1):
    
    
    
    
    print(' ',end=" " )