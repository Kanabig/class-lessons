from db import member_db
from db import diary_db

ids = ["gildong", "chanho"]
pws = ["1234", "0000"]
mails = ["gildong@gmail.com", "chanho@naver.com"]
phones = ["010-1234-5678", "010-9012-3456"]


def dummyInit():
    for n in range(len(ids)):
        member_db.memberDb[ids[n]] = {
            "id": ids[n],
            "pw": pws[n],
            "mail": mails[n],
            "phone": phones[n],
        }

        diary_db.diaryDb[ids[n]] = []
