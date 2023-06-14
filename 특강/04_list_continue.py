'''
continue
'''
# 리스트의 값 10개 중에서 10보다 큰 수를 출력하시오.
numbers = [1,10,30,20,50,29,30,38,18,60]

print('리스트 값 중 10보다 큰 수 - 반복문 사용')

for i in numbers :
    if i >= 10 :
        print(i, end=', ')
    
print()

print('리스트 값 중 10보다 큰 수 - 반복문 사용')
for i in numbers :
    if i < 10 :
        continue
    print(i,end=', ')
    
print()

# 1 ~ 30 사이의 수 중에서 7의 배수만 출력하시오. - continue 사용
print('=====continue사용======')
for j in range(1,31) :
    if j % 7 != 0  :
        continue
    print(j, end=', ')