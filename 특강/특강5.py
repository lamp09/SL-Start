num = int(input("정수 입력 : "))

if num < 0 :
    num = num - 2 * num
    if num // 10 == 0 :
        print("한 자리 수 입니다.")
    elif num // 100 == 0 :
        print("두 자리 수 입니다.")
    elif num // 1000 == 0 :
        print("세 자리 수 입니다.")
else :
    print("네 자리 수 이상입니다.")