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

import subprocess

DEV_MODE = True

# ENUM
OPT_SIGN_UP = "1"
OPT_LOGIN = "2"
OPT_UPDATE_USER_INFO = "3"
OPT_PRINT_USER = "4"
OPT_PRINT_ALL_USER = "5"
OPT_EXIT = "99"

KEY_PW = "USER_PW"
KEY_EMAIL = "USER_EMAIL"
KEY_PHONE = "USER_PHONE"

TXT_MENU = (
    f"{'-' * 110}\n"
    f" | {OPT_SIGN_UP}. 회원가입"
    f" | {OPT_LOGIN}. 로그인"
    f" | {OPT_UPDATE_USER_INFO}. 계정 정보 수정"
    f" | {OPT_PRINT_USER}. 특정 회원 정보 출력"
    f" | {OPT_PRINT_ALL_USER}. 모든 회원 정보 출력"
    f" | {OPT_EXIT}. 종료 |\n"
    f"{'-' * 110}\n"
)

# 아오힘들어

accounts = {}


def isAlreadyExists(id):
    return id in accounts


def isValidAccount(id, pw):
    return isAlreadyExists(id) and (pw == accounts[id][KEY_PW])


def createAccount(id, pw, email, phone):
    accounts[id] = {
        KEY_PW: pw,
        KEY_EMAIL: email,
        KEY_PHONE: phone,
    }


def updateAccount(id, pw, email, phone):
    accounts[id][KEY_PW] = pw
    accounts[id][KEY_EMAIL] = email
    accounts[id][KEY_PHONE] = phone


def getIdInput():
    id = input("아이디: ")
    return id


def getPwInput():
    pw = input("비밀번호: ")
    return pw


def getEmailInput():
    email = input("이메일: ")
    return email


def getPhoneNumberInput():
    phoneNumber = input("전화번호: ")
    return phoneNumber


def handleSignUp():
    id = getIdInput()
    pw = getPwInput()

    if isAlreadyExists(id):
        printText("이미 존재하는 계정입니다.")
        return

    email = getEmailInput()
    phone = getPhoneNumberInput()
    createAccount(id, pw, email, phone)
    printText("계정 생성이 완료되었습니다.")


def handleLogin():
    id = getIdInput()
    pw = getPwInput()
    if not isValidAccount(id, pw):
        printText("로그인에 실패했습니다.")
        return

    printText("로그인에 성공했습니다.")


def handlePrintUser():
    id = getIdInput()
    pw = getPwInput()

    if not isValidAccount(id, pw):
        printText("계정 정보 획득에 실패하셨습니다.")
        return

    print(id, accounts[id])
    printText("계정 정보 획득에 성공했습니다.")


def handlePrintAllUser():
    for key, value in accounts.items():
        print(key, value)

    printText("모든 계정 정보가 출력되었습니다.")


def handleUpdateUser():
    id = getIdInput()
    pw = getPwInput()

    if not isValidAccount(id, pw):
        printText("계정 정보가 틀렸습니다.")
        return

    print("계정 정보를 변경합니다.")
    pw = getPwInput()
    email = getEmailInput()
    phone = getPhoneNumberInput()

    updateAccount(id, pw, email, phone)
    printText("변경이 완료되었습니다.")


if DEV_MODE:
    createAccount("1", "1", "parkjungho@gmail.com", "010-1111-1111")
    createAccount("2", "2", "parkjungho@gmail.com", "010-2222-2222")
    # createAccount("parkjungho", "1111", "parkjungho@gmail.com", "01012334556")
    # createAccount("Leeyoonho", "2222", "yunho@kakao.com", "01012334556")
    # createAccount("LeeGyuchan", "3333", "gyuchan@dasd@daum.net", "01012334556")
    # createAccount("KimTaeJoon", "4444", "taejoon@naver.com", "01012334556")
    # createAccount("jangdongeun", "5555", "dongeun@nate.com", "01012334556")


def printText(text):
    print(text, end="")


isRunning = True

while isRunning:
    subprocess.run("clear")
    printText(TXT_MENU)
    selected = input("옵션 입력: ")

    if OPT_SIGN_UP == selected:
        handleSignUp()

    elif OPT_LOGIN == selected:
        handleLogin()

    elif OPT_UPDATE_USER_INFO == selected:
        handleUpdateUser()

    elif OPT_PRINT_USER == selected:
        handlePrintUser()

    elif OPT_PRINT_ALL_USER == selected:
        handlePrintAllUser()

    elif OPT_EXIT == selected:
        isRunning = False
        continue

    else:
        printText("정해진 옵션을 선택해 주십시오.")

    input()

printText("프로그램이 종료되었습니다.")
