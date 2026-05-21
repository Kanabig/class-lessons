from db import member_db

ids = ["gildong", "chanho"]
pws = ["1234", "0000"]
mails = ["gildong@gmail.com", "chanho@naver.com"]
phones = ["010-1234-5678", "010-9012-3456"]


def memberDumyInit():
    for idx in range(len(ids)):
        member_db.memberDb[ids[idx]] = {
            "id": ids[idx],
            "pw": pws[idx],
            "mail": mails[idx],
            "phone": phones[idx],
        }
