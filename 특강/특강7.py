id = input("아이디 입력 : ")
pw = input("비밀번호 입력 : ")


if id == "admin" and pw == 'pw1234' :
    print("로그인 성공")
elif id != 'admin' and pw =='pw1234' :
    print('아이디가 틀렸습니다.')
elif pw != 'pw1234' and id == 'admin':
    print('비밀번호가 틀렸습니다.')
else :
    print('아이디와 비밀번호가 틀렸습니다.')
    