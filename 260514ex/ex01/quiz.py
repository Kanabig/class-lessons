"""
-PC방 자리 관리 프로그램

너는 PC방 사장이다.
손님이 자리에 앉으면 "사용중" 으로 바뀌고, 비어있으면 예약할 수 있다.

seats = {
    1: "빈자리",
    2: "사용중",
    3: "빈자리",
    4: "사용중",
    5: "빈자리"
}

프로그램 요구사항
1.현재 자리 상태를 전부 출력하기
2.사용자에게 원하는 자리 번호 입력받기
3.예약할 자리 번호 :
4.빈자리라면 "예약 완료" 출력 해당 자리 상태를 "사용중" 으로 변경 이미 사용중이라면 이미 사용중인 자리입니다 출력
5.예약 후 전체 자리 상태 다시 출력하기
"""

# # FIXME: 문자열 리터럴 상수로 변환
# OCCUPIED = "사용중"
# FREE = "빈자리"

# seats = {1: "빈자리", 2: "사용중", 3: "빈자리", 4: "사용중", 5: "빈자리"}

# for cnt, status in seats.items():
#     print(f"[{cnt}번 자리]: {status}")

# bookNum = int(input("예약할 자리 번호: "))

# if bookNum not in seats:
#     print("사용중인 자리입니다.")
# elif seats[bookNum] == FREE:
#     seats[bookNum] = OCCUPIED
#     print("예약 완료.")
# else:
#     print("사용중인 자리입니다.")

# for cnt, status in seats.items():
#     print(f"[{cnt}번 자리]: {status}")

"""
- 배달 주문 통계 프로그램
배달 앱에서 하루 주문 데이터를 분석하려고 한다.
주어진 주문 목록
orders = [
    "치킨",
    "피자",
    "치킨",
    "햄버거",
    "피자",
    "치킨"
]
프로그램 요구사
1. 각 음식이 몇 번 주문됐는지 딕셔너리에 저장하기
2. 가장 많이 주문된 음식 찾기
3. 총 주문 개수 출력하기
4. 사용자가 음식 이름 입력하면
몇 번 주문됐는지 출력하기
"""

# orders = ["치킨", "피자", "치킨", "햄버거", "피자", "치킨"]
# analysis = {}

# for item in orders:
#     cnt = orders.count(item)
#     analysis[item] = cnt

# print(analysis)

"""
-시험 결과 분석 프로그램
학원에서 시험 결과를 분석하려고 한다.
주어진 데이터
scores = {
    "민수": 88,
    "지훈": 72,
    "수아": 95,
    "유진": 64,
    "서연": 100
}
프로그램 요구사항
1.전체 학생 점수 출력하기
2.평균 점수 계산하기
3.최고 점수 학생 찾기
4.60점 이상은 합격, 미만은 불합격 출력하기
5.90점 이상 학생 수 출력하기
6.점수 높은 순으로 학생 출력 도전하기
"""

students = {"민수": 88, "지훈": 72, "수아": 95, "유진": 64, "서연": 100}
reverseStudent = {}

maxScore = 0
moreThan90Cnt = 0
highestStudent = ""

for name, score in students.items():
    reverseStudent[score] = name
    result = "합격" if score >= 60 else "불합격"
    print(f"{name}: {score}점, {result}")

    if score >= 90:
        moreThan90Cnt += 1

# sorted_students = sorted(student.items(), key=lambda x: x[1], reverse=True)
# for name, score in sorted_students:
#     print(f"{name}: {score}점")
# 중복되는 value가 있을 경우, 값이 소실될 가능성이 있다.
scoreList = list(reverseStudent.keys())
scoreList.sort(reverse=True)


print(f"\n평균: {sum(students.values()) / len(students)}")
print(f"최고 점수 학생: {max(students, key=students.get)}")
print(f"90점 이상인 학생 수: {moreThan90Cnt}")
print("\n성적 높은 학생 순")
for score in scoreList:
    print(reverseStudent[score])
