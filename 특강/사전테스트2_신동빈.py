im = int(input("투입 금액 : "))
C = 350
change = im - C

w5000 = change // 5000
change = change % 5000
w1000 = change // 1000
change = change % 1000
w500 = change // 500
change = change % 500
w100 = change // 100
change = change % 100
w50 = change // 50
change = change % 50

print("5000원 권은 {}장이며, 1000원 권은 {}장, 500원은 {}개, 100원은 {}개, 50원은 {}개 입니다." 
      .format(w5000, w1000, w500, w100, w50))