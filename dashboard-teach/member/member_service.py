from utils import util_time
from member import config
import os
import json
import session


class MemberService:

    def __init__(self):
        self.members = {}
        self.initDatabase()

    def signUp(self):
        id = input("input id: ")

        if self.members.get(id):
            print("duplicated id")
            return

        pw = input("input pw: ")
        mail = input("input mail: ")
        phone = input("input phone: ")

        newMember = {
            "id": id,
            "pw": pw,
            "mail": mail,
            "phone": phone,
            "regDate": util_time.getCurrentDateTime(),
            "modDate": util_time.getCurrentDateTime(),
        }

        self.members[id] = newMember
        self.saveMembers(self.members)

        print("sign-up success")

    def signOut(self):
        session.setSignInedMemberId()
        print("sign-out success")

    def signIn(self):
        id = input("input id: ")
        pw = input("input pw: ")

        member = self.members.get(id)

        if not member or member.get("pw") != pw:
            print("sign-in failed")
            return

        session.setSignInedMemberId(id)
        print("sign-in success")

    def modify(self):
        pw = input("input pw: ")
        mail = input("input mail: ")
        phone = input("input phone: ")

        member = self.members[session.getSignInedMemberId()]
        member["pw"] = pw
        member["mail"] = mail
        member["phone"] = phone
        member["modDate"] = util_time.getCurrentDateTime()

        self.saveMembers(self.members)

    def delete(self):
        confirm = input("\nare you sure of delete your account?(Y/N)\n: ")

        if confirm == "N":
            print("step back to menu")
            return

        del self.members[session.getSignInedMemberId()]
        self.saveMembers(self.members)

        session.setSignInedMemberId()
        print("member deleted")

    def run(self):
        onRunning = True
        while onRunning:
            if not session.getSignInedMemberId():
                selected = input("\n1. sign-up | 2. sign-in | 0. back\n: ")

                match selected:
                    case config.SIGN_UP:
                        self.signUp()
                    case config.SIGN_IN:
                        self.signIn()
                    case config.STEP_BACK:
                        onRunning = False
                    case "admin":
                        if __debug__:
                            for key in self.members:
                                print(self.members[key])
                    case _:
                        print("option out of bounds")

            else:
                selected = input("\n3. sign-out | 4. modify | 5. delete | 0. back\n: ")

                match selected:
                    case config.SIGN_OUT:
                        self.signOut()
                    case config.MODIFY:
                        self.modify()
                    case config.DELETE:
                        self.delete()
                    case config.STEP_BACK:
                        onRunning = False
                    case "admin":
                        if __debug__:
                            for key in self.members:
                                print(self.members[key])
                    case _:
                        print("option out of bounds")

    def initDatabase(self):
        BASE_PATH = os.path.dirname(os.path.abspath(__file__))
        ROOT_DIR_PATH = os.path.dirname(BASE_PATH)

        self.dbFile = os.path.join(ROOT_DIR_PATH, "db", "members.json")

        if not os.path.exists(self.dbFile):
            self.saveMembers(self.members)
            return

        self.members = self.loadMembers()

    def saveMembers(self, members):
        with open(self.dbFile, "w", encoding="utf-8") as f:
            json.dump(members, f, ensure_ascii=False, indent=2)

    def loadMembers(self):
        with open(self.dbFile, "r", encoding="utf-8") as f:
            return json.load(f)


if __name__ == "__main__":

    ms = MemberService()
    ms.run()
