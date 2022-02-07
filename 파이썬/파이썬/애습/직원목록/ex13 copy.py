
def dhfb(qi,qi1):

    import csv

    tnwjd1 = ['']*qi
    tnwjd2 = ['']*qi1
    tnwjd3 = ['']*50
    
    #수정한문서
    anstj[q][i]

    i = 0
    q = 0
    pi = 0
    tls = 0
    sin = 0
    



    with open('새 텍스트 문서.csv','r',newline='',encoding='korean') as file:
        csv_r = csv.reader(file,delimiter=',',quotechar='"')
        for line in csv_r:
            q = q + 1
            i = 0
        
            for str1 in line:
                i = i + 1
                print(i)
                for qaz in range(0,(len(str1))):
                
                    if str1[qaz] == ",":
                        
                        print(q,"번째줄 ",end='')
                        tnwjd1 [pi] = q
                        print(i,"칸 ",end='')
                        tnwjd2 [pi] = i
                        print(qaz,"번째글자 ",end='')
                        tnwjd3 [pi] = qaz
                        print("애러")
                        
                        pi = pi + 1
                        sin = sin + 1
                        
    with open('새 텍스트 문서.csv','r',newline='',encoding='korean') as file:
        csv_r = csv.reader(file,delimiter=',',quotechar='"')
        for line in csv_r:
            q = q + 1
            i = 0
        
            for str1 in line:
                i = i + 1
                print(q,"`:",i)
                    #수정해서일기
                if str == type(str1):
                    i = i - 2
                
                    if sin == 0:
                        print(q,"1:",i)
                        anstj[q][i] = str1
                        i = i + 2
                    else:
                        print(q,"2:",i,"         애러남")
                        str1[tnwjd3 [pi]] = "/"
                        anstj[q][i] = str1
                        i = i + 2
                        sin = 0
                        
    return(anstj[1][1])

        
q,w,e =dhfb(73,10)

for a in range(0,100):
    for s in range(0,100):
        print(q[a][s])
        print(w[a][s])
        print(e[a][s])

    
                
            