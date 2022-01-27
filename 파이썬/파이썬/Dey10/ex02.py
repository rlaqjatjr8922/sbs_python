'''
    파일입출력
    
    -택스트파일생성
'''
path = 'C:/수업/SBS-py/sbs_python/파이썬/파이썬/Dey10/'
    
#파일 렬기 :open
file = open (path + 'helo.txt','at',encoding='UTF-8')

#추가할내용
file.write('\n')
file.write('이어서내용추가')
file.write('\n')
file.write('텍스트 파일내용 추가모드: at')
print ('파일에 내용추가함')

file.close()

