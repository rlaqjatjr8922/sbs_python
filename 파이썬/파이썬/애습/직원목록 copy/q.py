#append, insert
import csv
import sys

    
    
class pi:
    def __init__(self):
        
        self.name = []
        self.wjs = []
        self.wn = []
        self.dlq = []
        self.q = 0
        q0 = 0
        with open('새 텍스트 문서 - 복사본.csv','r',newline='') as file:
            csv_r = csv.reader(file,delimiter=',',quotechar='"')
            for q1 in csv_r:
                self.q = self.q + 1
                q0 =0
                for q2 in q1:
                    if q0 == 0:
                        self.name.append(q2)
                        print(q0)
                    if q0 == 1:
                        self.wjs.append(q2)
                        print(q0)
                    if q0 == 2:
                        self.wn.append(q2)
                        print(q0)
                    if q0 == 3:
                        self.dlq.append(q2)
                        print(q0)
                        
                    q0 = q0+1
                
                
                
        self.run()
    
    def run(self):
         
        print("******************************")
        print("                              ")
        print("0.종료                        ")
        print("1.추가                        ")
        print("2.수정                        ")
        print("3.검색                        ")
        print("                              ")
        print("******************************")
        eoekq = input("")   
        eoekq = int(eoekq)   

        if eoekq == 0: self.whdfy()         # 종료 1
        if eoekq == 1: self.insert()     # 추가 1
        if eoekq == 2: self.update()     # 수정
        if eoekq == 3: self.search()     # 검색
        if eoekq == 4: self.print_all()  # 전체출력5
        if eoekq < 0:
            if eoekq > 5:
                print('매뉴번호 박임 장난ㄴㄴㄴ')
        
    def whdfy(self):
        
        # reader (파일객채,delimiter=구분기호,quotechar= 문자열기호)
        with open('명단','w',newline='') as file:
            csv_r = csv.reader(file,delimiter=',',quotechar='"')
            
            for q1 in range(0,self.q):
                    
                csv_maker.writerow([self.name[self.q]   , self.wjs[self.q]  ,self.wn[self.q]    ,self.dlq[self.q]   ])
                    
        print("종료")
        sys.exit()
    
    def insert(self):
        q1 = input("이름:")
        q2 = input("전화번호:")
        q3 = input("주소:")
        q4 = input("입사날자:")
        if q1:
            if q2:
                if q3:
                    if q4:
                        self.name.append(q1)
                        self.wjs.append(q2)
                        self.wn.append(q3)
                        self.dlq.append(q4)
                        print("\n")
                        print("이름:{}".format(self.name[self.q]))
                        print("전화번호:{}".format(self.wjs[self.q]))
                        print("주소:{}".format(self.wn[self.q]))
                        print("입사일:{}".format(self.dlq[self.q]))
                        self.q = self.q + 1
                        return
                        
        print("불완전함")
        
        
    def delete(self):
        print("******************************")
        print("                              ")
        print("1.이름                        ")
        print("2.주소                        ")
        print("                              ")
        print("******************************")
        
        q1 =input("검색:")
        with open('새 텍스트 문서 - 복사본.csv','r',newline='') as file:
            csv_r = csv.reader(file,delimiter=',',quotechar='"')
            for q2 in csv_r:
                i = i + 1
                if q1 == q2:
                    print(i,"번째줄임니다")

            
            
            
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