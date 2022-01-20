
# 커피 = 300원
#금액입력 
# 잔수애타라서남은금액을 출력

money = input('금액:')
money = int(money)
i = 0
while money > 300:
    money = money - 300
    i = i + 1
    print('커피 {} 잔, 잔돈 {}'.format(i, money))