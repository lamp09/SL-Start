# 1. 연도를 입력받기
year = int(input("년도를 입력하세요: "))

# 2. 만약 4로 나누어 떨어지면
if year % 4 == 0 :
    if year % 100 == 0 :
        if year % 400 == 0 :
            print("윤년입니다.")
        else :
            print("윤년이 아닙니다.")
    else :
        print("윤년 입니다.")
else :
    print("윤년이 아닙니다.")