'''1~n까지더한수'''
n = int(input("정수"))
q = 0
for i in range(0,n+1,1):
    q = q + i
print(q)