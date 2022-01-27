'''
    파일입출력
    
    -택스트파일생성
'''
path = 'C:/수업/SBS-py/sbs_python/파이썬/파이썬/Dey10/'
    
#파일 렬기 :open
file = open (path + 'helo.txt','wt',encoding='UTF-8')
#파일내부애출력
file.write('안녕하새요')
file.write('\n')
file.write('파일입출력 내용 학습')
print ('파일이 생성됌')

file.close()

