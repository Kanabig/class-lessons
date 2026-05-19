# Toy 프로젝트 진행
"""
처음 프로그램이 실행되면 다음과 같은 메뉴를 출력한다.
메뉴: 1.회원가입    2.로그인     3.특정 회원 정보 출력     4.모든 회원 정보 출력     99.종료
사용자가
'1.회원가입'을 선택하면 회원ID, 회원PW, 회원Email, 회원Phone 정보를 입력받아 회원가입 진행한다.
'2.로그인'을 선책하면 회원ID, 회원PW를 입력받아 로그인 '성공' 또는 '실패'를 출력한다.
'3.특정 회원 정보 출력'를 선택하면 회원ID와 회원PW를 입력받아 일치하는 회원 정보를 모두 출력한다.
'4.모든 회원 정보 출력'를 선택하면 가입되어 있는 모든 회원 정보를 출력한다.
'99.종료'를 선택하면 프로그램 종료 시킨다.

심심하면> 특정 회원의 회원ID와 회원PW를 입력받아 인증되면 회원 정보를 수정하는 기능을 구현해 보자!

"""

DEV_MODE = True

ADD_ACCOUNT = 1
LOGIN = 2
PRINT_SPECIFIC_ACCOUNT = 3
PRINT_ALL_ACCOUNT = 4
EXIT_PROGRAM = 99

NEED_ACCOUNT_OPTIONS = (
    ADD_ACCOUNT,
    LOGIN,
    PRINT_SPECIFIC_ACCOUNT,
)

KEY_PWD = "USER_PWD"
KEY_EMAIL = "USER_EMAIL"
KEY_PHONE = "USER_PHONE"

accounts = {}


def addAccount(id, pw, email, phone):
    accounts[id] = {
        KEY_PWD: pw,
        KEY_EMAIL: email,
        KEY_PHONE: phone,
    }


def getAccountVerification(id):
    return (id) in accounts.keys()


def printAllAccounts():
    for key, value in accounts.items():
        print(key, value)


def makePromptText():
    text = []

    text.append(f"{ADD_ACCOUNT}.회원가입")
    text.append(f"{LOGIN}.로그인")
    text.append(f"{PRINT_SPECIFIC_ACCOUNT}.특정 회원 정보 출력")
    text.append(f"{PRINT_ALL_ACCOUNT}.모든 회원 정보 출력")
    text.append(f"{EXIT_PROGRAM}. 종료")

    prompt = " | ".join(text) + "\n옵션 입력: "

    return prompt


if DEV_MODE:
    addAccount("parkjungho", "1111", "apd@ansdna", "01012334556")
    addAccount("Leeyoonho", "2222", "asdas@ggooa", "01012334556")
    addAccount("LeeGyuchan", "3333", "nnaop@dasd", "01012334556")
    addAccount("KimTaeJoon", "4444", "taejoon@gmail.com", "01012334556")
    addAccount("jangdongun", "5555", "dongun@naver.com", "01012334556")


isRunning = True
prompt = makePromptText()

# while isRunning:
#     selected_opt = int(input(prompt))

#     if selected_opt == EXIT_PROGRAM:
#         isRunning = False

#     elif selected_opt == PRINT_ALL_ACCOUNT:
#         printAllAccounts()

#     elif selected_opt in NEED_ACCOUNT_OPTIONS:
#         id = input("아이디: ")

#         if selected_opt == PRINT_SPECIFIC_ACCOUNT:
#             if getAccountVerification(id):
#                 print(id, accounts[id])
#             else:
#                 print("이 계정은 없는 계정입니다.")
#                 continue

#         pw = input("비밀번호: ")

#         if selected_opt == ADD_ACCOUNT:
#             if getAccountVerification(id):
#                 print("이미 있는 계정입니다.")
#                 continue

#             email = input("Email: ")
#             phone = input("Phone Number(-제외): ")
#             addAccount(id, pw, email, phone)

#         elif selected_opt == LOGIN:
#             if getAccountVerification(id):
#                 print("성공")
#             else:
#                 print("실패")

while isRunning:
    selected_opt = int(input(prompt))
    if selected_opt == EXIT_PROGRAM:
        isRunning = False

    elif selected_opt == PRINT_ALL_ACCOUNT:
        printAllAccounts()

    else:
        id = input("아이디: ")
        pw = input("비밀번호: ")

        if selected_opt == ADD_ACCOUNT:
            email = input("Email: ")
            phone = input("Phone Number(-제외): ")
            addAccount(id, pw, email, phone)

        elif selected_opt == LOGIN:
            if getAccountVerification(id, pw):
                print("성공")
            else:
                print("실패")

        elif selected_opt == PRINT_SPECIFIC_ACCOUNT:
            print(id, pw, accounts[(id, pw)])
