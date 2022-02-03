'''
    파일복사
    
    원본 파일 -->변수 --> 복사본
     (읽기)              (쓰기)
    1.원본 파일 읽기
    2.1024Byte(1KB) 씩 읽어온다
    3.1024Byte(1KB) 씩 저장어온다
    4.저장 왈료
    
    #파일(20GB) --복사--> [버퍼](1KB) -->  생성
    #버퍼 : 임시저장공간
    
    1000MB          :1GB
    20 * 1000MB     :20GB (20000MB)
    20GB 처리하는 시간 :200초 (3분20초)
    
    #1초 10억 bit이상 (100MB~300MB)

    
    
    with
    :파일 입출력 시,자동으로 close() 함수를 호출한다.
    
    with open(파일경로,모드) as 파일 개체:
        처리 코드
    
'''


from shutil import copyfile


p = 'C:/c언어&파이썬/파이썬/sbs_python/파이썬/파이썬/'
f = p + 'helo.txt'
c = p + 'helo(복사).txt'

buffer_size = 1024      # 버퍼용량 : 1KB

#f 원본 파일객 채체
#c 복사 파일객 채체
with open (f,'rb')as s:
    with open (c,'wb')as c:
        while True:
            #원본파일을 버퍼용량 만큼 일어와서 buffer 에저장
            buffer = s.read(buffer_size)
            if not buffer:
                break
            c.write(buffer)
print(c)
print('복사성공')
            
