# members = {}

# isRuntime = True

# while isRuntime:
#     option = int(input("\n1.회원가입, 2.프로그램 종료: "))
#     if option == 1:
#         id = input("아이디: ")

#         if id in members:
#             print("사용 중인 아이디입니다.")
#             continue

#         pwd = input("비번: ")
#         members[id] = pwd
#     else:
#         isRuntime = False

# for id, pw in members.items():
#     print(f"ID: {id}, PW: {pw}")


# classes = {
#     "python": "5학점",
#     "C/C++": "5학점",
#     "HTML5": "3학점",
#     "Java": "5학점",
#     "Javascript": "3학점",
# }

# for subject, credit in classes.items():
#     if credit == "3학점":
#         classes[subject] = "5학점"

# print(classes)


# members = {
#     "2019-052001": ["박찬호", 25, "남", "010-1234-5678", "헬스, 수영", 0],
#     "2019-052004": ["박용택", 65, "남", "010-9012-3456", "수영", 50],
#     "2019-052003": ["박세리", 65, "여", "010-7890-1234", "아쿠아로빅", 50],
# }

# for key, value in members.items():
#     print(f"회원번호: {key}, 회원정보:{value}")

# print("-" * 100)
# NAME_IDX = 0
# GENDER_IDX = 2

# for key, value in members.items():
#     print(f"회원번호: {key}, 회원정보:{value[NAME_IDX]}, {value[GENDER_IDX]}")


# members = {
#     "2019-052001": {
#         "이름": "박찬호",
#         "나이": 25,
#         "성별": "남",
#         "연락처": "010-1234-5678",
#         "취미": ["헬스", "수영"],
#         "할인율": 0,
#     },
#     "2019-052004": {
#         "이름": "박용택",
#         "나이": 65,
#         "성별": "남",
#         "연락처": "010-9012-3456",
#         "취미": ["수영"],
#         "할인율": 50,
#     },
#     "2019-052003": {
#         "이름": "박세리",
#         "나이": 65,
#         "성별": "여",
#         "연락처": "010-7890-1234",
#         "취미": ["아쿠아로빅"],
#         "할인율": 50,
#     },
# }

# NAME = "이름"
# GENDER = "성별"
# HOBBY = "취미"

# for id, info in members.items():
#     print(f"회원번호: {id}, 회원정보: {info}")

# print("-" * 100)

# for id, info in members.items():
#     print(
#         f"회원번호: {id}, 회원정보: {info[NAME]}, {info[GENDER]}, "
#         f"{info[HOBBY]}, {len(info[HOBBY])}"
#     )


# refridgerator = {}

# while True:
#     name = input("야채 이름: ")
#     count = int(input("개수: "))
#     costOption = input("소비 혹은 입고: ")

#     if name not in refridgerator:
#         refridgerator[name] = 0

#     if costOption == "소비":
#         if refridgerator[name] - count >= 0:
#             refridgerator[name] -= count
#     else:
#         refridgerator[name] += count

#     print(refridgerator)
