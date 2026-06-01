from config import config
from member import session
from db import member_db
from db import diary_db
from member import member_dummy


def mainDisplay():
    print(
        f"\n{config.OPT_SIGN_UP}. sign-up | "
        f"{config.OPT_SIGN_IN}. sign-in | "
        f"{config.OPT_WRITE}. diary write | "
        f"{config.OPT_READ}. diary read | "
        f"{config.OPT_CLOSE}. close"
    )


def signInDisplay():
    print(
        f"\n{config.OPT_SIGN_OUT}. sign-out | "
        f"{config.OPT_MODIFY}. modify | "
        f"{config.OPT_DELETE}. delete | "
        f"{config.OPT_WRITE}. diary write | "
        f"{config.OPT_READ}. diary read | "
        f"{config.OPT_CLOSE}. close "
    )


def signUp():
    id = input("new member id: ")

    if id in member_db.memberDb:
        print("이미 존재하는 id입니다.")
        return

    pw = input("new member pw: ")
    mail = input("new member mail: ")
    phone = input("new member phone: ")

    member_db.memberDb[id] = {
        config.KEY_ID: id,
        config.KEY_PW: pw,
        config.KEY_MAIL: mail,
        config.KEY_PHONE: phone,
    }
    diary_db.diaryDb[id] = []

    print(f"wellcome!! {id}")

    if config.DEBUG_MODE:
        print(f"memberDb[{id}]: {member_db.memberDb[id]}")
        print(f"diaryDb[{id}]: {diary_db.diaryDb[id]}")


def signIn():
    id = input("member id: ")
    pw = input("member pw: ")

    if id in member_db.memberDb:
        if member_db.memberDb[id][config.KEY_PW] == pw:
            session.signInedMemberId = id
            print("sign-in success!!")

        else:
            print("sign-in fail!! -- pw error")

    else:
        print("sign-in fail!! -- id error")


def signOut():
    session.signInedMemberId = ""
    print("sign-out success!!")


def delete():
    del member_db.memberDb[session.signInedMemberId]
    print("member deleted!!")
    signOut()

    if config.DEBUG_MODE:
        print(f"{member_db.memberDb}")


def modify():
    pw = input("new member pw: ")
    mail = input("new member mail: ")
    phone = input("new member phone: ")

    member = member_db.memberDb[session.signInedMemberId]

    member[config.KEY_PW] = pw
    member[config.KEY_MAIL] = mail
    member[config.KEY_PHONE] = phone

    if config.DEBUG_MODE:
        print(f"memberInfo: {member} ")


def diaryWrite():
    if session.signInedMemberId == "":
        print("please sign-in!!")
        return

    onLoop = True
    while onLoop:
        print(f"{config.DIARY_TEXT_LIMIT}글자 이하의 짧은 일기를 작성하세요.")
        text = input(": ")

        if len(text) > config.DIARY_TEXT_LIMIT:
            print(
                f"{config.DIARY_TEXT_LIMIT}글자를 초과했습니다.\n"
                f"입력한 글자 수: {len(text)}"
            )
        else:
            onLoop = False

            diary_db.diaryDb[session.signInedMemberId].append(text)
            print("일기가 기록되었습니다.")

            if config.DEBUG_MODE:
                print(diary_db.diaryDb)


def diaryRead():
    if session.signInedMemberId == "":
        print("please sign-in!!")
        return

    myDiaries = diary_db.diaryDb[session.signInedMemberId]

    for idx, text in enumerate(myDiaries[::-1]):
        print(f"({idx + 1}): {text}")


def close():
    global onRunning
    onRunning = False
    print("closed!!")


signOutActions = {}
signInActions = {}


def addAction(actions, opt, func):
    actions[opt] = func
    pass


def matchOptActions():
    addAction(signOutActions, config.OPT_SIGN_UP, signUp)
    addAction(signOutActions, config.OPT_SIGN_IN, signIn)
    addAction(signOutActions, config.OPT_WRITE, diaryWrite)
    addAction(signOutActions, config.OPT_READ, diaryRead)
    addAction(signOutActions, config.OPT_CLOSE, close)

    addAction(signInActions, config.OPT_SIGN_OUT, signOut)
    addAction(signInActions, config.OPT_MODIFY, modify)
    addAction(signInActions, config.OPT_DELETE, delete)
    addAction(signInActions, config.OPT_WRITE, diaryWrite)
    addAction(signInActions, config.OPT_READ, diaryRead)
    addAction(signInActions, config.OPT_CLOSE, close)


def selectAction(actions, selected):
    action = actions.get(selected, None)
    action() if action else print("out of bounds")


# session.signInedMemberId = "park
member_dummy.dummyInit()
matchOptActions()

onRunning = True
while onRunning:

    # on sign-out
    if session.signInedMemberId == "":
        mainDisplay()
        selected = input("옵션을 선택하세요: ")
        selectAction(signOutActions, selected)

    # on sign-in
    else:
        signInDisplay()
        selected = input("옵션을 선택하세요: ")
        selectAction(signInActions, selected)
