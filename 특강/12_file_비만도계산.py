'''
컴퓨터공학부 202395019 신동빈 

키와 몸무게로 비만도 계산하기
'''
with open('info.txt', 'r') as file :
    for line in file :
        (name, weight, height) = line.strip().split(',') # strip() 공백제거, split() ','를 사용하여 구분함
        if (not name) or (not weight) or (not height) :
            continue
        # 비만도 계산하기
        bmi = int(weight) / ((int(height) / 100 ) ** 2)     # 파일에 있는것을 읽어오기에 문자열로 인식되기 떄문에 다시 문자열로 변경
        if bmi >= 25 :
            result = '과체중'
        elif bmi >= 18 :
            result = '정상체중'
        else :
            result = '저체중'
            
        print('\n'.join([f'이름 : {name} | 몸무게 : {weight} | 키 : {height} | bmi : {bmi:.2f} | 결과 : {result}']))