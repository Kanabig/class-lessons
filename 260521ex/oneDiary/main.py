from config import config
from member import session
from db import member_db
from member import member_dummy


def mainDisplay():
    print(
        f"\n{config.OPT_SIGN_UP}. Sign-up | "
        f"{config.OPT_SIGN_IN}. Sign-in | "
        f"{config.OPT_CLOSE}. close"
    )


def loginDisplay():
    print(
        f"\n{config.OPT_SIGN_OUT}. sign-out | "
        f"{config.OPT_MODIFY}. modify | "
        f"{config.OPT_DELETE}. delete | "
        f"{config.OPT_CLOSE}. close"
    )


# session.signInedMemberId = "park"

member_dummy.memberDumyInit()
print(f"memberDB: {member_db.memberDb}")

onRunning = True
while onRunning:

    # on sign-out
    if session.signInedMemberId == "":
        mainDisplay()
        selected = input("옵션을 선택하세요: ")

        if config.OPT_SIGN_UP == selected:
            id = input("new member id: ")
            pw = input("new member pw: ")
            mail = input("new member mail: ")
            phone = input("new member phone: ")

            member_db.memberDb[id] = {"id": id, "pw": pw, "mail": mail, "phone": phone}
            print(f"wellcome!! {id}")

            if config.DEBUG_MODE:
                print(f"memberDB: {member_db.memberDb}")

        elif config.OPT_SIGN_IN == selected:
            id = input("member id: ")
            pw = input("member pw: ")

            if id in member_db.memberDb:
                if member_db.memberDb[id]["pw"] == pw:
                    session.signInedMemberId = id
                    print("sign-in success!!")

                else:
                    print("sign-in fail!! -- pw error")

            else:
                print("sign-in fail!! -- id error")

        elif config.OPT_CLOSE == selected:
            onRunning = False

        else:
            print("out of bounds")

    # on sign-in
    else:
        loginDisplay()
        selected = input("옵션을 선택하세요: ")

        if config.OPT_SIGN_OUT == selected:
            session.signInedMemberId = ""

        elif config.OPT_MODIFY == selected:
            pass
        elif config.OPT_DELETE == selected:
            pass
        elif config.OPT_CLOSE == selected:
            onRunning = False
        else:
            print("out of bounds")
