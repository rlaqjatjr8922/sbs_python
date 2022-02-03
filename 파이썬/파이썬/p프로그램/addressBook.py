'''
    주소록 프로그램 만들기
    [기능]
    1. 새로운 주소 등록하기
    2. 기존 주소 삭제하기
    3. 기존 주소 수정하기
    4. 특정 주소 검색하기
    5. 전체 주소 출력하기
    6. 주소록 정보를 파일로 관리하기
    
    * 객체
    - Person 객체
    - AddressBook 객체
    
    * 주소록 정보
    - addressBook.csv 파일로 관리
    - 이름, 전화번호, 주소 정보를 저장
    ex)
    홍길동,010-1234-4321,서울시 노원구
    홍길동,010-1234-4321,서울시 노원구
    홍길동,010-1234-4321,서울시 노원구
    홍길동,010-1234-4321,서울시 노원구
    
    * 메소드(함수)
    file_reader()           : addressBook.csv 파일 읽기
    file_generator()        : addressBook.csv 파일 생성
    menu()                  : 수행 메뉴 소개 및 입력
    exit()                  : 프로그램 종료
    run()                   : 프로그램 실행
    insert()                : 추가
    delete()                : 삭제
    update()                : 수정
    search()                : 검색
    print_all()             : 전체 출력
    
    __init__()              : 생성자 - 주소록 리스트, 파일개체 초기화
    
'''

# 클래스 정의
'''
    객체 (속성, 기능)
    ex) 자동차 (바퀴?, 연료?  / 주행(), 기능1() )
    
    클래스
    : 객체를 정의하는 설계도
'''
# 사람
class Person:
    # 이름, 전화번호, 주소
    # 생성자 : 객체가 생성될 때, 실행되는 메소드
    def __init__(self, name, phone, addr):
        self.name = name
        self.phone = phone
        self.addr = addr
        
    def info(self):
        print('{}, {}, {}'.format(self.name, self.phone, self.addr))
        

# 주소록
class addressBook:
    # 주소 정보 리스트, 파일객체
    # 생성자
    def __init__(self):
        self.address_list = []
        self.file_reader()
        
    def file_reader(self):
        # 예외 처리
        # 에러 ? 프로그램 코드의 문법적인 문제   
        # 예외 ? 프로그램 실행 이후에 발생하는 문제
        #       - 숫자를 0 으로 나누는 경우 ( 10 / 0 )
        #       - 파일이 존재하지 않는 경우
        try:
            # 예외가 발생할 가능성이 있는 코드
            file = open('addressBook.csv', 'rt')
            
        except:
            # 예외 발생 시, 실행할 코드
            print('addressBook.csv 파일이 없습니다.')
        else:
            while True:
                buffer = file.readline()  # 한 줄씩 데이터를 읽어온다.
                if not buffer:
                    break
                # 홍길동,010-1234-4321,서울시 노원구\n
                # split() -->  ['홍길동', '010-1234-4321', '서울시 노원구\n']
                name = buffer.split(',')[0]
                phone = buffer.split(',')[1]
                # rstrip(문자) : 전달된 문자를 문자열의 오른쪽에서 제거
                addr = buffer.split(',')[2].rstrip('\n')
                # 주소 정보 리스트에 Person 객체 추가
                self.address_list.append(Person(name, phone, addr))
                
            print('addressBook.csv 파일을 읽어왔습니다.')
            file.close()
            
    # 파일 생성
    def file_generator(self):
        try:
            file = open('addressBook.csv', 'wt')
        except:
            print('addressBook.csv 파일을 생성할 수 없습니다.')
        else:
            for person in self.address_list:
                file.write('{},{},{}\n'.format( person.name, person.phone, person.addr) )
            file.close()
            
    # 메뉴 
    def menu():
        print('-' * 30)
        print('1. 주소 등록하기')
        print('2. 주소 삭제하기')
        print('3. 주소 수정하기')
        print('4. 주소 검색하기')
        print('5. 모든 주소 출력하기')
        print('0. 프로그램 종료')
        print('-' * 30)
        choice = int( input('메뉴 번호 : ') )
        return choice
        
    
              
              

        



