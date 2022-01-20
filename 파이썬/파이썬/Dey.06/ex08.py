
#단을입력밧아서 구구단응 출력하시오
dan = input("단 :")
dan = int(dan)
for n in range(1,10):
    print('{} x {} = {}'.format(dan, n, dan*n))


#이중반복
#2~9
print()
for i in range(2,10):
    for j in range(1,10):
        print('{} x {} = {}'.format(i,j,i*j))
    print()
    
    