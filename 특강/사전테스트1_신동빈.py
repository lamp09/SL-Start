kid = int(input("아이 수(13세 미만) : "))
adult = int(input("어른 수(13세~64세) : "))
old = int(input("노인 수(65세 이상) : "))
group = kid + adult + old
price = kid * 5000 + adult * 10000 + old * 7000

if group >= 10 :
    total = int(price - (price * 0.2))
else :
    total = price 
    
print("총 놀이공원 요금은 {}원 입니다." .format(total))