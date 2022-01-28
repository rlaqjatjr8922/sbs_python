
p = 'sbs_python/파이썬/파이썬/Dey10/'


#일기모드 : r
#파일유형 : t

file = open(p + 'helo.txt','rt',encoding='UTF-8')

while True:
    str = file.read(10)     #10씩읽는다
    
    str = file.read()       #한줄씩읽는다
    #아무갑도입력하지안을시종료
    if not str:
        break
    
    print(str,end='')
    
file.close()