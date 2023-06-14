'''
숫자 추측 게임 만들기

[문제분석]
사용자가 입력한 값과 컴퓨터가 생성한 랜덤 값을 비교한다.
몇번만에 맞혔는지 알려준다.

사용자에게 힌트를 준다.
사용자가 입력한 값이 랜덤 생성한 값보다 크면 숫자는 작다라고 한다.
사용자가 입력한 값이 랜덤 생성한 값도다 작으면 숫자는 크다라고 한다.

사용자가 값을 입력하여 힌트를 받을 때마다 count 1씩 증가한다.
게임은 사용자가 더 할지 안할지 정하여 종료하고 싲가한다.
'''
# 알고리즘
# 1. import random 사용
# 2. 무한 반복
#   1) 게임 실행 여부 확인
#   2) 만약 실행한다면
#       a. 랜덤 수 생성
#       b. 카운트 초기화
#       c. 게임실행합니다 출력
#       d. 수 맞추는 게임입니다 출력
#   3) 아니고 실행을 원하지 않으면
#       a. 게임을 종료합니다 출력
#       b. 게임 종료
#   
#   4) 무한반복
#       a. 정답 입력 받기
#       b. 만약 입력한 수보다 작다면
#           a) 입력한 수보다 작습니다. 출력
#           b) count에 1증갖
#       c. 아니고 만약 입력한 수보다 크다면
#           a) 입력한 수보다 큽니다. 출력
#           b) count 에 1 증가
#       d. 아니고 만약 정답과 같다면 
#           a) 정답입니다! 출력
#           b) count 만에 맞추셨습니다!
#           c) 종료
import random

while True :
    S = input('게임을 실행할까요? (y/n로 입력) : ')
    if S == 'y' :
        random1 = random.randint(1,30)
        count = 1
        print('게임을 실행합니다.')
        print('게임은 랜덤 수를 맞추는 게임입니다.')
    elif S == 'n' :
        print('게임을 종료합니다.')
        break
    while True :
        num = int(input('정답 : '))
        if num > random1 :
            print('입력한 수보다 작습니다.')
            count +=1
            continue
        elif num < random1 :
            print('입력한 수보다 큽니다.')
            count +=1
            continue
        elif num == random1 :
            print(f'축하합니다!\n{count}번만에 맞추셨습니다!')
            break
        
