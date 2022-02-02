from shutil import copyfile

#file = open('C:/Users/pc/Desktop/코딩명단/' + '통합 문서1.csv','rb',encoding='UTF-8')

path = 'C:/Users/pc/Desktop/코딩명단/'

def new_func(path):
    file = open(path + '통합 문서1.csv','rb',encoding='UTF-8')
    return file

file = new_func(path)

fil = path + '통합 문서1.csv'

while True:
    str = file.read()
    print('#{}',str)


with open (fil,'rb')as s:
    str = s.read(550)
    print(str)




name = [] * 100



for i in range(0 ,100  ):
    name[i] = input('asd')
 
        


    if i < 2:
        print(i)





    print('q')

new_func()