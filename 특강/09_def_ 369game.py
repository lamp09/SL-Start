'''
사용자로부터 정수를 입력 받아 1부터 입력 받은 수 까지369 게임을 진행합니다.
3,6,9 가 들어가는 수에서는 짝을,
10,20,30.. 10의 배수 자리에서는 '만세'를 출력하는 부분을 함수로 작성하시오.

[실행결과]
<<< 369게임 >>>

정수 입력 : 50

1,2,짝,4,5,짝,7,8,짝,만세,11,12,짝,14,15,짝,17,18,짝,
만세,21,22,짝,24,25,짝,27,28,짝,만세,
'''
def game(num): # () => 지역 변수 즉, 이 game 이라는 지역안에서 쓸수있는 변수
    for i in range(1, num+1) :
        if i % 10 == 3 or i % 10 == 6 or i % 10 == 9 :
            print('짝', end=', ')
        elif i % 10 == 0 :
            print('만세', end=', ')
        else :
            print(i, end=', ')
        

print('<<< 369 게임 >>>')
num = int(input('정수 입력 : '))

game(num)