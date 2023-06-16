'''
컴퓨터공학부 202395019 신동빈 

사이렌 오더를 통해 음료를 미리 예약하는 프로그램을 만드시오.
메뉴는 
1. 아메리카노 2500원
2. 카페라떼 3000원
3. 바닐라 라떼 3000원
메뉴 번호를 선택하면 해당 메뉴와 가격을 출력해 주는 부분을 함수로 작성하시오.
선택한 메뉴는 인수로 전달되어 가격이 결과 값으로 반환되는 함수로 작성하시오.

사용자가 음료를 선택하면 음료의 가격을 알려주는 프로그램.
'''
def coffee_type(choose) :
    if choose == 1 :
        return(f'선택하신 음료의 종류와 가격은 {coffee.get(choose)}입니다.')
    if choose == 2 :
        return(f'선택하신 음료의 종류와 가격은 {coffee.get(choose)}입니다.')
    if choose == 3 :
        return(f'선택하신 음료의 종류와 가격은 {coffee.get(choose)}입니다.')
    else :
        return('선택하신 메뉴 번호는 없습니다.')
    
coffee = {1 : '아메리카노 2500원', 2 : '카페라떼 3000원', 3 : '바닐라 라떼 3000원'}

print(f'메뉴 종류 : {coffee}')
while True :
    choose = int(input('메뉴 번호 선택(0 입력시 종료) : '))
    if choose == 0 :
        print('프로그램을 종료합니다.')
        break
    print(coffee_type(choose))
    