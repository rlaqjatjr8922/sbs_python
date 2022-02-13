
def dhfb(w1):

    import csv



    i = [0]*10
    q = 0
    e = 0



    with open('새 텍스트 문서.csv','r',newline='',encoding='korean') as file:
                csv_r = csv.reader(file,delimiter=',',quotechar='"')
        
                for qaz in range(0,(len(w1))):
                
                    if w1[qaz] == ",":
                        
                        
                        print(qaz,"번째글자 ",end='')
                        i[q] = int(qaz)
                        print("애러")
                        q = q+1
                        

                        
    while True :
        
        if q != 0:
            
            q1 = len(w1)
            
            print(i[e])
            
            w1 = w1[0:(i[e])] + "/" + w1[(i[e])+1:q1]
            
            print(w1)
            
            e = e + 1
            q = q - 1
        else:
            break
            
    

    return(w1)


def qwe():
    
    import csv
    q = 0
    
    with open('새 텍스트 문서.csv','r',newline='',encoding='korean') as file:
        csv_r = csv.reader(file,delimiter=',',quotechar='"')
    
        #줄수새기
        for line in csv_r:
            q = q + 1

            print("")
            print(q,"번째줄")
    return (q +1)




    
                
            