'''

    #가변 매개면수
    :가변 = 변화가 가능하다
    -매개변수압에 * 을 붓임
    dif 함변수명 (*매개변수)
    
    #디폴트 매개변수(기본매개변수)
    :'디폴트' -기본값
    인수가 없는경우에 ,기본갑을가짐

'''





def add( *args):
    print(' {} 의 합계는 {} 입니다'.format(args,sum(args) ))

add(1,2)
add(1,2,3)
add(1,2,3,4)

def greet(name,msg='안녕'):
    print('{} 님, {}'.format(name,msg))

greet('범석')
greet('범석','하이')