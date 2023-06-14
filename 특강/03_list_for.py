'''
리스트를 만들고, 반복무으로 출력하시오.
'''
num1 = list(range(1,10))
print(f'num1 : {num1}')

for i in num1 :
    print(i, end=', ')
    
print()
'''
1 ~ 100 사이의 정수 중 랜덤으로 10개의 수를 뽑아서 리스트에 저장하시오.
'''

import random
num2 = []

for i in range(1,11) :
    num2.append(random.randint(1,100))
print(f'생성된 리스트 : {num2}')
    