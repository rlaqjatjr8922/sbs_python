'''
시퀀스 내장 함수
1. enumerate()함수
 :리스
 
 
    
      len()함수
    함수의길이반환
    
     sorted() 함수
    : 반복가능한 개채를 오름차순으로 정렬
    ex) li = [10,3,9,2,5]
        sorted(li) -->[2,3,5,9,10]
    
    zip() 함수
    :여려 개의 반복가는한 객체들을 튜푸로묵어서 반환
    ex)names = ['c언어','파이썬','lava']
        scores = [100,90,80]
        zip( names, scores)
        -->('c언어',100),    
           ('파이썬',90),    
           ('lava',80), 
'''




from unicodedata import name


prog = ['c언어','파이썬','lava']
for item in enumerate(prog):
    print(item)
    
    
for i in range(10):
    print (i, end=' ')
    
print()

for i in range(1,20,2):
    print(i,end=" ")

print()
    
for i in range(2,21,2):
    print(i,end=" ")
    
print()

li = ['월','화','수', '목','금','토','일']
print(li)
print('li요소갰수 :{}'.format( len(li) ))


scores = [100,90,65,80,70]
print(scores)
print( sorted(scores))

nam = ['s1','s2','s3','s4','s5']

for student in zip(nam,scores):
    print(student)