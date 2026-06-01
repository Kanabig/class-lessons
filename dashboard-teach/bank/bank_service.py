import os
import json
from bank import config
import session
import uuid


class BankService:
    def __init__(self):
        self.accounts = {}
        self.initDatabase()

    def isMyAccountExists(self):
        if session.getSignInedMemberId() in self.accounts:
            return True

        return False

    def createAccount(self):
        if not self.isMyAccountExists():
            self.accounts[session.getSignInedMemberId()] = {}

        myAccount = self.accounts[session.getSignInedMemberId()]
        myAccount[str(uuid.uuid4())] = {"balance": 0, "histories": []}

        self.saveAccounts(self.accounts)
        print("create account success")

    def run(self):
        if not session.getSignInedMemberId():
            print("this service needs sign-in")
            return

        onRunning = True
        while onRunning:
            if not self.isMyAccountExists():
                selected = input("\n2. create account | 0. back\n: ")

                match selected:
                    case config.CREATE_ACCOUNT:
                        self.createAccount()
                    case _:
                        print("option out of bounds")
            else:
                selected = input(
                    "\n1. account list | 2. create account | 3. deposit | 4. withdrawal | 0. back\n: "
                )

                match selected:
                    case config.ACCOUNT_LIST:
                        self.createAccount()
                    case config.DEPOSIT:
                        pass
                    case config.WITHDRAWAL:
                        pass
                    case config.STEP_BACK:
                        onRunning = False
                    case "admin":
                        if __debug__:
                            for key in self.accounts:
                                print(self.accounts[key])
                    case _:
                        print("option out of bounds")

    def initDatabase(self):
        BASE_PATH = os.path.dirname(os.path.abspath(__file__))
        ROOT_DIR_PATH = os.path.dirname(BASE_PATH)

        self.dbFile = os.path.join(ROOT_DIR_PATH, "db", "accounts.json")

        if not os.path.exists(self.dbFile):
            self.saveAccounts(self.accounts)
            return

        self.accounts = self.loadAccounts()

    def saveAccounts(self, accounts):
        with open(self.dbFile, "w", encoding="utf-8") as f:
            json.dump(accounts, f, ensure_ascii=False, indent=2)

    def loadAccounts(self):
        with open(self.dbFile, "r", encoding="utf-8") as f:
            return json.load(f)


if __name__ == "__main__":
    session.setSignInedMemberId("1")
    bs = BankService()
    bs.run()
