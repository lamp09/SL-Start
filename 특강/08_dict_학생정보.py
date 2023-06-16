'''
학과 : 컴퓨터공학부
학번 :  202395019
이름 : 신동빈

학생 정볼르 사전에 저장하고, (학번, 이름)
특정 학생의 정보(학번)를 입력하여 학생을 찾아주세요.

[알고리즘]
1. 학생 정보 저장 사전 만들기 (빈 사전)
2. 학생 정보 입력 - 사전에 저장(z 키를 누르면 종료 - 무한 반복)
3. 학번으로 검색하여 학생 찾기 (학번이 빈칸이면 검색 종료 - 무한 반복)

'''

student = {}
print('======학생 정보 입력======')
while True :
    student_num  = input('학생 학번(z 입력시 종료) : ')
    if student_num == 'z' :
        break
    student_name = input('학생 이름 : ')    
    student[student_num] = student_name
    print(f'학생정보 : {student}')
    
print('======학생 정보 검색======') 
while True :
    student_find = input('찾고자 하는 학생의 학번(enter 입력 시 종료) : ')
    if student_find == "" :
        print('프로그램을 종료합니다.')
        break
    elif student_find in student :
        print(f'학번 : {student_find} | 이름 : {student.get(student_find)}')
    elif not student_find in student :
        print('존재 하지 않는 학번입니다.')
   
    