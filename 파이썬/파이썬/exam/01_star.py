'''
���� :���(���ǹ�,�ݺ���) �� �̿��Ͽ�,
    �Ʒ��Ͱ�ġ *���̷������������
    1�ܰ�)
    ����n�� �Է¹ٴ�
    �̰����
    
    *
    **
    ***
    ****
    *****
    
    
    2�ܰ�)
    *    
   ***
  *****
 *******
*********
    
'''
u = input("����")
u = int(u)
for i in range(0,u+1,1):
    print('*' * i)
    

print(end = '')
u = input("����")
u = int(u)
y = 0
for i in range(0,u+1,1):    #  for ���� in range(�����ʱⰩ , ���ᰩ , ������):
    y = int( (u - 1) -i )   
    for rt in range(0,y+1,1):
        print (' ',end='')
    
    print('*',end = '')
    print('*' * i * 2)
    