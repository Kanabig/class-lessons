# scores = {
#     "c/c++": "A",
#     "Java": "B+",
#     "네트워킹": "C",
#     "보안": "A+",
#     "해킹": "F",
#     "시스템": "C+",
# }

# print(scores)

# listVar1 = [1, 2, 3]
# listVar2 = [1, 2, 3, listVar1]
# print(listVar2[3][1])


# -----------------------------------------------------------------


# CRUD: Create, Read, Update, Delete

# container = {
#     "name": "고길동",
#     "age": 20,
#     "addr": "대전 중구",
#     "hobby": ["축구", "농구", "배구"],
#     "weight": 87.5,
# }

# print(container.keys())
# print(container.values())
# print(type(container.items()))
# print(len(container))


# print(container)
# container["연락처"] = "010-1111-2222"
# print(container)

# container["연락처"] = "010-3333-4444"
# print(container)

# del container["weight"]
# container.pop("연락처")
# item = container.popitem()

# print(container)
# print(item)


# -----------------------------------------------------------------


# 중간고사 성적 관리 프로그램 만들기
"""
아래 시나리오를 기반으로 딕셔너리를 이용해서 중간고사 성적 관리 프로그램을 만들어봅시다.
 -1 : 중간고사의 성적(C/C++은 A, Java는 B+, 모바일은 C, 보안은 A+, 해킹은 F, 시스템은 C+)을 저장하는
      딕셔너리를 만든다.
 -2 : 'Java'와 '시스템' 과목의 성적을 조회한다.
 -3 : 추가로 2과목의 성적(파이썬은 A, OS는 A+)을 삽입한다.
 -4 : 'Java'와 '시스템'의 성적을 각각 'F'와 'A'로 수정한다.
 -5 : 전체 과목과 성적을 조회하여 최종 성적표를 출력한다.
"""

# scores = {
#     "c/c++": "A",
#     "Java": "B+",
#     "네트워킹": "C",
#     "보안": "A+",
#     "해킹": "F",
#     "시스템": "C+",
# }

# print(scores["Java"], scores["시스템"], "\n")
# scores["파이썬"] = "A"
# scores["OS"] = "A++"
# scores["Java"] = "F"
# scores["시스템"] = "F"
# for subject, score in scores.items():
#     print(f"{subject}: {score}")


# subjectAndScores = {
#     "c/c++": "A",  # 4.0
#     "Java": "B+",  # 3.5
#     "네트워킹": "C",  # 2.0
#     "보안": "A+",  # 4.5
#     "해킹": "F",  # 0
#     "시스템": "C+",  # 2.5
# }

# creditsForScore = {
#     "A+": 4.5,
#     "A": 4.0,
#     "B+": 3.5,
#     "B": 3.0,
#     "C+": 2.5,
#     "C": 2.0,
#     "F": 0.0,
# }

# totalScore = 0
# for score in subjectAndScores.values():
#     print(creditsForScore[score])
#     totalScore += creditsForScore[score]

# print(totalScore, totalScore / len(subjectAndScores))
