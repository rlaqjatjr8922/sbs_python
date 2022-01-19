# 재어문
#1. 조건문

#2. 반복문

#조건문
#if
#   if 조건식:
#   (들여쓰기) 결과 = 참

# * 들였기
#1. 같은 영력의 들여쓰기는 같아야한다


# input 무조껀 문자열로가저온다

age = input("당신은 몃살임니까")
age = int (age)
#연상하기위해서는 형변황이필요함
if age >= 20:
    print("성인")
    print("나이 : {}".format(age))
else:
    print("청소년")
    print("나이 : {}".format(age))
