import config
from member import member_service
from bank import bank_service


def main():

    ms = member_service.MemberService()
    bs = bank_service.BankService()

    onRunning = True
    while onRunning:
        selected = input("\n1. member | 2. bank | 3. memo | 4. todo | 0. exit\n: ")

        match selected:
            case config.MEMBER_SERVICE:
                ms.run()
            case config.BANK_SERVICE:
                bs.run()
            case config.MEMO_SERVICE:
                pass
            case config.TODO_SERVICE:
                pass
            case config.EXIT:
                onRunning = False
                print("close")
            case _:
                print("option out of bounds")


if __name__ == "__main__":
    main()
