SIGN_UP = 1
SIGN_IN = 2
PRINT_MY_INFO = 3
PRINT_ALL_MEMBER_INFO = 4
SYSTEM_SHUTDOWN = 99

DEV_MOD = True

members = {}  # Database


if DEV_MOD:
    uids = ["gildong", "chanho", "saeri"]
    uPws = ["1234", "5678", "9012"]
    uMails = ["gildong@gmail.com", "chanho@naver.com", "saeri@daum.net"]
    uPhones = ["010-1234-5678", "010-1234-5678", "010-1234-5678"]

    for i in range(len(uids)):
        members[uids[i]] = {
            "uId": uids[i],
            "uPw": uPws[i],
            "uMail": uMails[i],
            "uPhone": uPhones[i],
        }


def getSelectedMenuNum():
    selectedMenuNum = int(
        input(
            "1.회원가입    2.로그인    3.나의 정보 출력     4.모든 회원 정보 출력    99.종료"
        )
    )

    return selectedMenuNum


def setNewMember(uId, uPw, uMail, uPhone):
    members[uId] = {"uId": uId, "uPw": uPw, "uMail": uMail, "uPhone": uPhone}


def isMember(uId):
    if uId in members:
        print(f"{uId}는 이미 사용중입니다. 다시 확인해주세요.")
        return True

    return False


def printAllMemberInfo():
    for value in members.values():
        print(f'{value["uId"]}님의 정보---------------')
        for key, value in value.items():
            print(f"{key}: {value}")

        print("-" * 30)


flag = True

while flag:

    userSelect = getSelectedMenuNum()

    if userSelect == SIGN_UP:
        uId = input("Input member ID: ")

        if not isMember(uId):
            uPw = input("Input member PW: ")
            uMail = input("Input member EMAIL: ")
            while True:
                if "@" not in uMail:
                    print("입력한 이메일 주소가 형식에 맞지 않습니다.")
                    uMail = input("Input member EMAIL: ")
                else:
                    break

            uPhone = input("Input member PHONE: ")

            setNewMember(uId, uPw, uMail, uPhone)
            print("SIGN-UP SUCCESS!!")

            if DEV_MOD:
                print(f"members: {members}")

    elif userSelect == SIGN_IN:
        tryCnt = 0

        while tryCnt < 3:
            uId = input("Input member ID: ")
            uPw = input("Input member PW: ")

            if uId in members:
                uInfo = members[uId]
                if uInfo["uPw"] == uPw:
                    print("SIGN-IN SUCCESS!!")
                    break
                else:
                    print("SIGN-IN FAIL!!")
            else:
                print("존재 하지 않은 ID입니다. 다시 확인하세요.")

            tryCnt += 1

    elif userSelect == PRINT_MY_INFO:
        uId = input("Input member ID: ")
        uPw = input("Input member PW: ")

        if uId in members:
            uInfo = members[uId]
            if uInfo["uPw"] == uPw:
                print("SIGN-IN SUCCESS!!")

                print("-" * 30)
                for key, value in uInfo.items():
                    print(f"{key}: {value}")
                print("-" * 30)

            else:
                print("SIGN-IN FAIL!!")
        else:
            print("존재 하지 않은 ID입니다. 다시 확인하세요.")

    elif userSelect == PRINT_ALL_MEMBER_INFO:
        printAllMemberInfo()

    elif userSelect == SYSTEM_SHUTDOWN:
        flag = False
        print("Good bye~")
