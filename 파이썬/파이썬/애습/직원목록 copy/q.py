#append, insert
import csv
import sys
import time
    
    
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
                        #print(q0)
                    if q0 == 1:
                        self.tod.append(q2)
                        #print(q0)
                    if q0 == 2:
                        self.wjs.append(q2)
                        #print(q0)
                    if q0 == 3:
                        self.wn.append(q2)
                        #print(q0)
                    if q0 == 4:
                        self.dlq.append(q2)
                        #print(q0)
                    
                        
                    q0 = q0+1
                
                
        #self.q = self.q - 1        
        self.run()
    
    def run(self):
        #print(self.q) 
        print("******************************")
        print("                              ")
        print("0.종료                        ")
        print("1.추가                        ")#0
        print("2.삭재                        ") #&퇘사      1
        print("3.수정                        ")#1
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
        if eoekq == 5: self.wjdfl()  # 전체출력5
        if eoekq == 6: self.wjdfl()  # 전체출력5
        if eoekq < 0:
            if eoekq > 5:
                print('매뉴번호 박임 장난ㄴㄴㄴ')
                
    
    def whdfy(self):
            
        q1 = []
        q2 = []
        q3 = []
        q4 = []
        q5 = []
        a = []
        i3 = 0
        d = 0
        #i123 = 0
        for z in range(0,self.q):
            for z1 in range(0,self.q):
                x  = self.name[z]
                x1 = self.name[z1]
                if x > x1:
                    i3 = i3 + 1
            a.append(i3)
            i3 = 0
        for z10 in range(self.q):
            q1.append('')
            q2.append('')
            q3.append('')
            q4.append('')
            q5.append('')
            #print(a[z10])
        for i in range(self.q):
            #print(a[i],"qwdas")
            q1[a[i]] = self.name[i]
            q2[a[i]] = self.tod[i]
            q3[a[i]] = self.wjs[i]
            q4[a[i]] = self.wn[i]
            q5[a[i]] = self.dlq[i]
            #print(i)
            #print(q1[a[i]])
            #print(q2[a[i]])
            #print(q3[a[i]])
            #print(q4[a[i]])
            #print(q5[a[i]])
            #print(a[i])
        for i in range(0,self.q):
            
            #print(i,"번째줄     :",q1[i],q2[i],q3[i],q4[i],q5[i])
            with open('명단.csv','w',newline='') as file:
                csv.writer(file,delimiter=',')
                #csv_r = csv.reader(file,delimiter=',',quotechar='"')
                csv_r = csv.writer(file,delimiter=',')
            
                for w in range(0,self.q):
                    
                    csv_r.writerow([    q1[w],   q2[w], q3[w],  q4[w],  q5[w],])            
        print("종료")
        
    
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
        else:
            aq = []
            z = 0
            q3 = input("주소:")
            #   len
            with open('검색결과.csv','w',newline='') as file:
                csv.writer(file,delimiter=',')
                #csv_r = csv.reader(file,delimiter=',',quotechar='"')
                csv_r = csv.writer(file,delimiter=',')
                for a in range(0,self.q):
                    #print("                            ",a)
                    for a1 in range(0,len(self.wn)-len(q3)+1):
                        #print(self.wn[a][a1:a1+len(q3)])
                        if self.wn[a][a1:a1+len(q3)] == q3:
                            print(a,"줄\n")
                            print(self.name[a])
                            print(self.tod[a])
                            print(self.wjs[a])
                            print(self.wn[a])
                            print(self.dlq[a])
                            print("\n\n\n\n")
                            csv_r.writerow([    self.name[a],   self.tod[a],    self.wjs[a],  self.wn[a],  self.dlq[a],])
                            z = z+1
        print("총 {}개의 검색결과가 있슴니다.".format(z))
        self.run()    
        return

            
    def wjdfl(self):
        
        print("*********************************")
        print("                                 ")
        print("1.이름                           ")
        print("2.생일                           ")
        print("3.전화번호                       ")
        print("4.주소                           ")
        print("5.입사일                         ")
        print("                                 ")
        print("*********************************")
        
        aq = input("정수")
        aq = int(aq)
        if aq == 1:
            print(self.q,"개의 이름이있슴니다")
            for w in range(0,self.q):
                print(self.name)
                self.run()
        if aq == 2:
            print(self.q,"개의 생일이있슴니다")
            for w in range(0,self.q):
                print(self.tod)
                self.run()
        if aq == 3:
            print(self.q,"개의 전화번호이있슴니다")
            for w in range(0,self.q):
                print(self.wjs)
                self.run()
        if aq == 4:
            print(self.q,"개의 주소이있슴니다")
            for w in range(0,self.q):
                print(self.wn)
                self.run()
        if aq == 5:
            print(self.q,"개의 입사일이있슴니다")
            for w in range(0,self.q):
                print(self.dlq)
                self.run()
    




        
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
    
    
    
    
    
    
class dy:
    def __init__(self):
        
        
        #이름
        self.dl = []
        #성별
        self.tjd = []
        #생일
        self.tod = []
        #전화
        self.wjs = []
        #주소
        self.wn = []
        #비고
        self.ql = []
        #전화온 날자
        self.wjs1 = []
        #평가
        self.vud = []
        
        self.q = 0
        self.Pvmfhrmfoa = 0
        q0 = 0
        with open('요양사 리스트.csv','r',encoding='korean',newline='') as file:
            csv_r = csv.reader(file,delimiter=',',quotechar='"')
            for q1 in csv_r:
                self.q = self.q + 1
                q0 =0
                for q2 in q1:
                    #if not q2:
                    if "비어있음" ==  q2:
                        q2 = ""
                    if q0 == 0:
                    
                        self.dl.append(q2)
                        
                        #print(q0)
                    if q0 == 1:
                        self.tjd.append(q2)
                        #print(q0)
                    if q0 == 2:
                        self.tod.append(q2)
                        #print(q0)
                    if q0 == 3:
                        self.wjs.append(q2)
                        #print(q0)
                    if q0 == 4:
                        self.wn.append(q2)
                        #print(q0)                    if q0 == 1:

                    if q0 == 5:
                        self.ql.append(q2)
                        #print(q0)
                    if q0 == 6:
                        self.wjs1.append(q2)
                        #print(q0)
                    if q0 == 7:
                        self.vud.append(q2)
                        #print(q0)
                    #print(q0)
            
                        
                    q0 = q0+1
                
                
        #self.q = self.q - 1 
        #print(self.vud)       
        self.run()
    def run(self):
        print("******************************")
        print("                              ")
        print("0.죵료                        ")
        print("1.검색                        ")  
        print("2.수정                        ")      
        print("3.삭제                        ")      
        print("4.추가                        ")      
        print("5.전채출력                    ")      
        print("                              ")      
        print("******************************")
        i = int(input(""))
        if i ==  0: self.Awhd()
        if i ==  1: self.Arja()
        if i ==  2: self.Atn()
        if i ==  3: self.Atkr()
        if i ==  4: self.Acn()
        if i ==  5: self.Awjs()

        
        if i > 5:
            if i < 0 :
                print("ㅁㄴㅂㅎㅈㄴ ㄴㄴㄴㄴㄴㄴㄴㄴㄴㄴㄴㄴㄴㄴㄴㄴㄴㄴㄴㄴㄴ")
        
        
        
        
    def Awhd(self):
#        for i in range(0,self.q):
            
            #print(i,"번째줄     :",q1[i],q2[i],q3[i],q4[i],q5[i])
            with open('요양사 리스트.csv','w',newline="") as file:
                csv.writer(file,delimiter=',')
                #csv_r = csv.reader(file,delimiter=',',quotechar='"')
                csv_r = csv.writer(file,delimiter=',')
            
                for w in range(0,self.q):
                    
                    csv_r.writerow([    self.dl[w],   self.tjd[w],   self.tod[w],  self.wjs[w],  self.wn[w],   self.ql[w]     ,self.wjs1[w],    self.vud[w]])
            print("종료")
        
    def Arja(self):
        
        print("******************************")
        print("                              ")
        print("1.이름                        ")
        print("2.성별                        ")
        print("3.전화번호                    ")
        print("4.주소                        ")
        print("5.평점 8                      ")
#        print("6.입주                       ")
        print("                              ")
        print("******************************")

        i = input("")
        i = int (i)
        with open('검색결과.csv','w',newline='') as file:
            csv.writer(file,delimiter=',')
            #csv_r = csv.reader(file,delimiter=',',quotechar='"')
            csv_r = csv.writer(file,delimiter=',')            
            if i ==  1:

                q=0
                q3 = input("검색할 이름:")
                for a in self.dl:
                    print("a")
                    if a == q3:
                        print("******************************")
                        print("이름",self.dl[q])
                        print("성별",self.tjd[q])
                        print("생일",self.tod[q])
                        print("전화번호",self.wjs[q])
                        print("주소",self.wn[q])
                        print("비고",self.ql[q])
                        print("전화온날자",self.wjs1[q])
                        print("평가",self.vud[q])
                        print("******************************")
                        csv_r.writerow([   self.dl[q],   self.tjd[q],   self.tod[q],  self.wjs[q],  self.wn[q],   self.ql[q]     ,self.wjs1[q],    self.vud[q]])
                        self.Pvmfhrmfoa = q
                        self.run()
                        return
                    
                
                    q = q + 1
                print("찻는 선생님의 이름이 없음")
                self.run()
            
            if i ==  2: 
                print("******************************")
                print("                              ")
                print("1.여                          ")
                print("2.남                          ")
                print("                              ")
                print("******************************")
                i = int(input(""))
                if i == 2:
                    q=0
                    q1=0
                    q3 = "남"
                    for v in self.tjd:
                        #print("a")
                        if v == q3:
                            print("******************************")
                            print("이름",self.dl[q1])
                            print("성별",self.tjd[q1])
                            print("생일",self.tod[q1])
                            print("전화번호",self.wjs[q1])
                            print("주소",self.wn[q1])
                            print("비고",self.ql[q1])
                            print("전화온날자",self.wjs1[q1])
                            print("평가",self.vud[q1])
                            print("******************************")
                            csv_r.writerow([   self.dl[q1],   self.tjd[q1],   self.tod[q1],  self.wjs[q1],  self.wn[q1],   self.ql[q1]     ,self.wjs1[q1],    self.vud[q1]])
                            q = q+1
                        q1 = q1 +1
                    print(q,"개의 검색결과가 있슴니다.")
                    self.run()
                    return
                else:
                    q=0
                    q1=0
                    q3 = "여"
                    for v in self.tjd:
                        #print("a")
                        if v == q3:
                            print("******************************")
                            print("이름",self.dl[q1])
                            print("성별",self.tjd[q1])
                            print("생일",self.tod[q1])
                            print("전화번호",self.wjs[q1])
                            print("주소",self.wn[q1])
                            print("비고",self.ql[q1])
                            print("전화온날자",self.wjs1[q1])
                            print("평가",self.vud[q1])
                            print("******************************")
                            csv_r.writerow([   self.dl[q1],   self.tjd[q1],   self.tod[q1],  self.wjs[q1],  self.wn[q1],   self.ql[q1]     ,self.wjs1[q1],    self.vud[q1]])
                            q = q+1
                        q1 = q1 +1
                    print(q,"개의 검색결과가 있슴니다.")
                    self.run()
                    return
                
                

                
            
            if i ==  3: 

                q=0
                q3 = input("검색할 전화번호:")
                for i in self.wjs:
                    print("a")
                    if i == q3:
                        q = q + 1
                        print("******************************")
                        print("이름",self.dl[q])
                        print("성별",self.tjd[q])
                        print("생일",self.tod[q])
                        print("전화번호",self.wjs[q])
                        print("주소",self.wn[q])
                        print("비고",self.ql[q])
                        print("전화온날자",self.wjs1[q])
                        print("평가",self.vud[q])
                        print("******************************")
                        self.Pvmfhrmfoa = q
                        csv_r.writerow([   self.dl[q],   self.tjd[q],   self.tod[q],  self.wjs[q],  self.wn[q],   self.ql[q]     ,self.wjs1[q],    self.vud[q]])
                        self.run()
                        return
                q = q + 1
                print("등록 돼지 안은전 화번호 임니다")        
                self.run()
                return    
            #print("찻는 선생님의 이름이 없음")
        
            if i ==  4: 
                aq = []
                z = 0
                q3 = input("주소:")
            #   len
            
                for q1 in range(0,self.q):
                    #print("                            ",a)
                    for a1 in range(0,len(self.wn)-len(q3)+1):
                    #print(self.wn[a][a1:a1+len(q3)])
                        if self.wn[q1][a1:a1+len(q3)] == q3:
                            print(q1+1,"줄\n")
                            print("이름",self.dl[q1])
                            print("성별",self.tjd[q1])
                            print("생일",self.tod[q1])
                            print("전화번호",self.wjs[q1])
                            print("주소",self.wn[q1])
                            print("비고",self.ql[q1])
                            print("전화온날자",self.wjs1[q1])
                            #print("평가",self.vud[q1])
                            print("\n\n\n\n")
                            csv_r.writerow([   self.dl[q1],   self.tjd[q1],   self.tod[q1],  self.wjs[q1],  self.wn[q1],   self.ql[q1]     ,self.wjs1[q1],    self.vud[q1]])#
                            z = z+1
                print(z,"권의 검색 결과가 있슴니다")
                self.run()
            if i ==  5:
                print("5")
            
            if i ==  6: 
                print("6")
                print("s")       
            if i > 5 or i <= 0:
                print("a")
            
                print("ㅁㄴㅂㅎㅈㄴ ㄴㄴㄴㄴㄴㄴㄴㄴㄴㄴㄴㄴㄴㄴㄴㄴㄴㄴㄴㄴㄴ")
                self.run()
                return
                

    def Awjs(self):
        print("******************************")
        print("                              ")
        print("1.이름                        ")
        print("2.성별                        ")
        print("3.생일                        ")
        print("4.전화번호                    ")
        print("5.평점                        ")
        print("6.주소                        ")
#        print("7.입주                        ")
        print("                              ")
        print("******************************")
        i = int(input(""))
        
            
        if i ==  1:
            for i in range(0,self.q):
                print(self.dl[i])
            
        if i ==  2: 
            for i in range(0,self.q):
                print(self.tjd[i])
            
        if i ==  3: 
            for i in range(0,self.q):
                print(self.tod[i])
            
        if i ==  4: 
            for i in range(0,self.q):
                print(self.wjs[i])
            
        if i ==  5:
            #for i in range(0,self.q):
                print(self.vud)
            
        if i ==  6: 
            for i in range(0,self.q):
                print(self.wn[i])
        
            
               
        
        
        #print("ㅁㄴㅂㅎㅈㄴ ㄴㄴㄴㄴㄴㄴㄴㄴㄴㄴㄴㄴㄴㄴㄴㄴㄴㄴㄴㄴㄴ")        
        self.run()
        return
    
    def Atkr(self):
        q1 =input("삭재할이름:")
        print(q1,end='')
        q2 = input("을 삭재할까요?(o/x)")
        if q2 == "o":
            q=0
            for i in self.dl:
                
                if i == q1:
                    
                    
                    self.dl.pop(q)
                    self.tjd.pop(q)
                    self.tod.pop(q)
                    self.wjs.pop(q)
                    self.wn.pop(q)
                    self.ql.pop(q)
                    self.wjs1.pop(q)
                    
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
    
    def Atn(self):

        q=0
        q3 = input("수정할 이름:")
        if  not q3:
                q3 = self.Pvmfhrmfoa
                q4 = input("이름:")
                if q4:
                    self.dl[q] = q4
                    print("qw")
                
                q4 = input("성별:")
                if q4:   
                    self.tjd[q] = q4
                    print("qw")
                q4 = input("생년월일:")
                if q4:   
                    self.tod[q] = q4
                    print("qw")
                q4 = input("전화번호:")
                if q4:
                    self.wjs[q] = q4
                    print("qw")
                    print(q)
                q4 = input("주소:")
                if q4:
                    self.wn[q] = q4
                    print("qw")
                    print(q)
                q4 = input("비고:")
                if q4:
                    self.ql[q] = q4
                    print("qw")
                    print(q)
                q4 = input("평가:")
                if q4:
                    self.vud[q] = q4
                    print("qw")
                    print(q)
                
                self.run()
                return
            
            
        for i in self.dl:
            print("a")
            if i == q3:
                
                q4 = input("이름:")
                if q4:
                    self.dl[q] = q4
                    print("qw")
                
                q4 = input("성별:")
                if q4:   
                    self.tjd[q] = q4
                    print("qw")
                q4 = input("생년월일:")
                if q4:   
                    self.tod[q] = q4
                    print("qw")
                q4 = input("전화번호:")
                if q4:
                    self.wjs[q] = q4
                    print("qw")
                    print(q)
                q4 = input("주소:")
                if q4:
                    self.wn[q] = q4
                    print("qw")
                    print(q)
                q4 = input("비고:")
                if q4:
                    self.ql[q] = q4
                    print("qw")
                    print(q)
                q4 = input("평가:")
                if q4:
                    self.vud[q] = q4
                    print("qw")
                    print(q)
                
                self.run()
                return
            q = q + 1
        print("찻는 선생님의 이름이 없음")
        self.run()
        
    


    def Acn(self):
        print("추가할 정보")
        q1 = input("이름:")
        self.dl.append(q1)
        q2 = input("성별:")
        self.tjd.append(q2)
        q3 = input("생년월일:")
        self.tod.append(q3)
        q4 = input("전화번호:")
        self.wjs.append(q4)
        q5 = input("주소:")                           
        self.wn.append(q5)
        q6 = input("비고:")
        self.ql.append(q6)
        q7 = input("입사날자:")
        self.vud.append(q7)
        q8 = input("평가:")
        self.vud.append(q8)
        print("\n\n\n\n추가돼었슴니다.")
        
        
        self.run()
        return    
    
    
    
    
        
if "1" == input("qqe"):
    applrqw = pi()
else:
    applrqw = dy()        