'''
숫자 내장 함수
'''

print ('#1')
print( abs(-10))

print("#2")
mo = 10000
pr = 3000
re = divmod(mo,pr)
print ('커피{}개 사고 {}원남음'.format(re[0],re[1]))

print('#4')
b = '15'
print('#5')

x,y,z, = input ('정수3:').split()
x=int(x)
y=int(y)
z=int(z)
print ('쵀대갑 : {}'.format( max(x,y,z) ))

print('#6')
print('쵀소갑 : {}'.format( min(x,y,z) ))

print('#7')
print('2^2 : {}'.format( pow(2,2)))
print('2^3 : {}'.format( pow(2,3)))
print('2^4 : {}'.format( pow(2,4)))

print('#8')
print('round(1.5): {}'.format( round(1.5) ))
print('round(1.4): {}'.format( round(1.5) ))
print('round(1.55,1): {}'.format( round(1.55,1) ))
print('round(2.675): {}'.format( round(2.675,2) ))

print('#9')
li = [1,2,3,4,5]
print ('sum(li) = {}'.format(sum (li)))

t = (10,20,30,40,50)
print ('sum(t) = {}'.format( sum (t)))