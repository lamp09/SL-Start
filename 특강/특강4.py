com = int(input("컴퓨터 점수 : "))
eng = int(input("영어 점수 : "))

if ((com or eng) >= 95) or (com + eng >= 170) :
    print("합격입니다.")
else :
    print("불합격입니다.")