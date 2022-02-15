#append, insert
import csv
import sys

    
    
class pi:
    def __init__(self):
        
        self.name = []
        self.tod = []
        self.wjs = []
        self.wn = []
        self.dlq = []
        self.q = 0
        q0 = 0
        with open('명단.csv','r',encoding='korean',newline='') as file:
            csv_r = csv.reader(file,delimiter=',',quotechar='"')
            for q1 in csv_r:
                self.q = self.q + 1
                q0 =0
                for q2 in q1:
                    if q0 == 0:
                        self.name.append(q2)
                        print(q0)
                    if q0 == 4:
                        self.tod.append(q2)
                        print(q0)
                    if q0 == 1:
                        self.wjs.append(q2)
                        print(q0)
                    if q0 == 3:
                        self.wn.append(q2)
                        print(q0)
                    if q0 == 4:
                        self.dlq.append(q2)
                        print(q0)
                    
                        
                    q0 = q0+1
                
                
                
        self.run()
    
    def run(self):
         
        print("******************************")
        print("                              ")
        print("0.종료                        ")
        print("1.추가                        ")
        print("2.삭재                        ") #&퇘사
        print("3.수정                        ")
        print("4.검색                        ")
        print("5.전채출력                    ")
        print("                              ")
        print("******************************")
        eoekq = input("")   
        eoekq = int(eoekq)   

        if eoekq == 0: self.whdfy()      # 종료 1
        if eoekq == 1: self.insert()     # 추가 1
        if eoekq == 2: self.delete()     # 삭재 1
        if eoekq == 3: self.update()     # 수정
        if eoekq == 4: self.search()     # 검색
        if eoekq == 5: self.print_all()  # 전체출력5
        if eoekq < 0:
            if eoekq > 5:
                print('매뉴번호 박임 장난ㄴㄴㄴ')
        
    def whdfy(self):
        
        # reader (파일객채,delimiter=구분기호,quotechar= 문자열기호)
        with open('명단.csv','w',newline='') as file:
            csv.writer(file,delimiter=',')
            #csv_r = csv.reader(file,delimiter=',',quotechar='"')
            csv_r = csv.writer(file,delimiter=',')
            
            for q1 in range(0,self.q):
                    
                csv_r.writerow([self.name[q1]   ,self.tod[q1]   , self.wjs[q1]  ,self.wn[q1]    ,self.dlq[q1]   ])
                    
        print("종료")
        sys.exit()
    
    def insert(self):
        print("추가할 정보")
        q1 = input("이름:")
        q2 = input("생년월일:")
        q3 = input("전화번호:")
        q4 = input("주소:")
        q5 = input("입사날자:")
        if q1:
            if q2:
                if q3:
                    if q4:
                        if q5:
                            self.name.append(q1)
                            self.tod.append(q2)
                            self.wjs.append(q3)
                            self.wn.append(q4)
                            self.dlq.append(q5)
                            print("\n")
                            print("이름:{}".format(self.name[self.q]))
                            print("생년월일:{}".format(self.tod[self.q]))
                            print("전화번호:{}".format(self.wjs[self.q]))
                            print("주소:{}".format(self.wn[self.q]))
                            print("입사일:{}".format(self.dlq[self.q]))
                            self.q = self.q + 1
                            self.run()
                            return
                        
        print("불완전함")
        self.run()
        return
    
    def delete(self):
        q1 =input("삭재할이름:")
        print(q1,end='')
        q2 = input("을 삭재할까요?(o/x)")
        if q2 == "o":
            q=0
            for i in self.name:
                
                if i == q1:
                    
                    
                    self.name.pop(q)
                    self.tod.pop(q)
                    self.wjs.pop(q)
                    self.wn.pop(q)
                    self.dlq.pop(q)
                    
                    self.q = self.q - 1
                    self.run()
                    return
                q = q + 1
            print("찻는 선생님의 이름이 없음")
            self.run()
        
            return
        else:
            print("삭재를 치소함")
            self.run()
            
            
            
        
    
    def update(self):

        q=0
        q3 = input("수정할 이름:")
        for i in self.name:
            print("a")
            if i == q3:
                
                q4 = input("이름:")
                if q4:
                    self.name[q] = q4
                    print("qw")
                
                q4 = input("생년월일:")
                if q4:   
                    self.wjs[q] = q4
                    print("qw")
                q4 = input("연락처:")
                if q4:   
                    self.wn[q] = q4
                    print("qw")
                q4 = input("주소:")
                if q4:
                    self.dlq[q] = q4
                    print("qw")
                    print(q)
                
                self.run()
                return
            q = q + 1
        print("찻는 선생님의 이름이 없음")
        self.run()
                
    
    def search(self):
        print("*********************************")
        print("                                 ")
        print("1.이름                           ")
        print("2.주소                           ")
        print("                                 ")
        print("*********************************")
        q1 =input("")
        
        if q1 == "1":
            q=0
            q3 = input("이름:")
            for i in self.name:
                
                if i == q3:
                    
                    print(self.name[q])
                    print(self.tod[q])
                    print(self.wjs[q])
                    print(self.wn[q])
                    print(self.dlq[q])
                        
                    
                    self.run()
                    return
                q = q + 1
            print("찻는 선생님의 이름이 없음")
            self.run()
        
            return

            
    def print_all(self):
        
        aq = input("정수")
        aq = int(aq)
        if aq == 1:
            
            for w in range(0,self.q):
                print(self.name)
                self.run()
        if aq == 2:
            
            for w in range(0,self.q):
                print(self.tod)
                self.run()
        if aq == 3:
            
            for w in range(0,self.q):
                print(self.wjs)
                self.run()
        if aq == 4:
            
            for w in range(0,self.q):
                print(self.wn)
                self.run()
        if aq == 5:
            
            for w in range(0,self.q):
                print(self.dlq)
                self.run()
            
            
            
applrqw = pi()

        
'''
/*
   
# reader (파일객채,delimiter=구분기호,quotechar= 문자열기호)
    with open('새 텍스트 문서 - 복사본.csv','r',newline='') as file:
        csv_r = csv.reader(file,delimiter=',',quotechar='"')
        q1=0
        print(type(csv_r))
        for q2 in csv_r:
            
            q1 = q1 + 1
    return(q1+1)
#q2 = red() 
i =[[]*7]*red()




    if eoekq == 0: whdfy()         # 종료
    elif eoekq == 1: self.insert()     # 추가
    elif eoekq == 2: self.delete()     # 삭제
    elif eoekq == 3: self.update()     # 수정
    elif eoekq == 4: self.search()     # 검색
    elif eoekq == 5: self.print_all()  # 전체출력5
    else: print('매뉴번호 박임 장난ㄴㄴㄴ')

def whdfy():
    





















        
#for str in line:
#한문장씩 일기     
            
                
           
        
#for str in line:
#한문장씩 일기     
    print("1")
    */'''