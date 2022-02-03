'''
    주소록프로그램만들기
    [기능]
    1.새로웅주 소등록
    2.지존주소 삭새
    3.기존주소 수정
    4.특정주소 검색
    5.전채수소 출력
    6.주소록괄리
    
    *객채
    -person 개체
    -AddressBook 개체
    
    *주소록 정보
    - AddressBook.csv 파일로괄리
    -이름,전화번호,주소 정보를 저장
    ex)
    홍갈동,010-1234-5678,서울 노원구
    홍갈동,010-1234-5678,서울 노원구
    홍갈동,010-1234-5678,서울 노원구
    홍갈동,010-1234-5678,서울 노원구
    
    *메소드(함수)
    fill_reader()       :AddressBook.csv  파일읽기
    fill_reader()       :AddressBook.csv  파일생성
    meun()              :수행 매뉴 소개 및 밉력
    exit()              :프로그램종료
    run()               :프로그램실행
    insert()            :추가
    delete()            :삭재
    update()            :수정
    search()            :검색
    print_all()         :검색
    
    __init__()          :생성자 - 주소록 리스트,파일객채 초기화
    
'''

#클래스정의
'''
    객채 (속성,기능)
    ex) 자동차(바퀴? ,연료? / 주행(),기능1())
    
    클래스
    :개채를정의한는 설개도
    
'''
#사람

from distutils.command.build import build
from os import name


class person:
    
    #생정자 : 겍채가생성됄때 ,실행돼는 매쏘드
    def __init__(self,name,phone,addr):
        self.name = name
        self.ph = phone
        self.ad = addr
    
    def info(self):
        print("{},{},{},".format(self.name , self.ph , self.ad))


#주소록
class addressBook:
    #주소 정보 리스트,파일객체
    #생성자
    def __init__(self):
        #예왜 처리
        #에러 ? 포로그램코드의 문법 적문재
        #에러 ? 실행이후애 생기는문재
        #   ex) /0   파일이존재X
        
        try:
            #애요ㅐ가발생하는 코드
            file = open('addressBook.csv', 'rt')
        except:
            #애왜 발생 시,실행할 코드
            print('파일 X')
            
        else:
            while True:
                buffer = fill.readline()    #한줄씩 데이터를 가저온다.
                if not buffer:
                    break
                
                name = buffer.split(',')[0]
                phone = buffer.split(',')[1]
                #rstrip(문자) : 전달됀문자를 문자열의 오른쪽애서 재거
                addr = buffer.split(',')[2].rstrip('\n')
                #주소 정보 리스트애 Person 객채추가
                self.address_list.append(person(nam,))
                
                
                
                #매뉴
    def menu():
        print('_'*30)
        print('1.주소등록')
        print('2.주소삭재')
        print('3.주소삭재하기')
        print('2.')
        print('2.')
        choice = int(input("매뉴번호"))
                
