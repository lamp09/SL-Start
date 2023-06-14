'''
"학생관리" 프로그램을 작성학시오.
이 프로그램은 종료 시킬 때까지 무한 반복된다.
- '작업 선택 : ' 에서 0 입력 시 프로그램이 종료된다.
- '작업 선택 : ' 에서 1 입력 시 관리하는 학생 목록이 조회된다.
- '작업 선택 : ' 에서 2 입력 시 학생을 추가할 수 있다.
- '작업 선택 : ' 에서 3 입력 시 학생을 삭제할 수 있다.
이때 입력한 학생은 관리하는 학생 목록에 있는 데이터만 삭제 가능하도록 하며,
목록에 없는 학생을 삭제하고자 할 때는 
'삭제할 학생이 없습니다. 다시 입력하세요!'를 화면에 출력한다.
'''

list_student = []
while True :
    print('- 작업 선택 :  에서 0 입력 시 프로그램이 종료된다.',end='\n')
    print('- 작업 선택 :  에서 1 입력 시 관리하는 학생 목록이 조회된다.', end='\n')
    print('- 작업 선택 :  에서 2 입력 시 학생을 추가할 수 있다.', end='\n') 
    print('- 작업 선택 :  에서 3 입력 시 학생을 삭제할 수 있다.', end='\n')
    work = int(input('작업 선택 : '))
    if work == 0 :
        break
    if work == 1 :
        print('======학생 목록======')
        print(list_student)
    if work == 2 :
        print('=====학생 이름 입력======', end='\n')
        name = str(input('추가 할 학생 이름 : '))
        list_student.append(str(name))
    if work == 3 :
        print('======학생 이름 삭제======', end='\n')
        del_name = str(input('삭제 할 학생 이름 : '))
        if list_student.count(del_name) == 0 :
            print('삭제 할 학생이 없습니다.')
            continue
        else :
            list_student.remove(del_name)